import firebase_admin
from firebase_admin import credentials, firestore, auth
import uuid  # Para obter o MAC Address
import socket  # Para verificar conexão com a internet
from tkinter import messagebox  # Para exibir mensagens
from returnPathAbsolute import *

# Inicializar o Firebase
cred_path = get_resource_path("serviceAccountKey.json")
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

def adicionar_mac_no_token(uid):
    """
    Adiciona o MAC Address do dispositivo às custom claims do usuário no Firebase Authentication.
    """
    try:
        mac_address = obter_mac_address()
        auth.set_custom_user_claims(uid, {"mac": mac_address})
        print(f"MAC Address {mac_address} associado ao usuário {uid}.")
    except Exception as e:
        print(f"Erro ao adicionar MAC Address no token: {str(e)}")


def autenticar_usuario():
    """
    Autentica o usuário no Firebase Authentication e associa o MAC Address ao token.
    """
    try:
        # Criação de um usuário anônimo (ou ajuste para usar outro tipo de autenticação)
        user = auth.create_user()  # Essa linha cria um novo usuário
        uid = user.uid

        # Adicionar o MAC Address como custom claim
        adicionar_mac_no_token(uid)

        print("Usuário autenticado e MAC Address associado com sucesso!")
    except Exception as e:
        print(f"Erro ao autenticar usuário: {str(e)}")



def obter_mac_address():
    """
    Obtém o MAC Address do dispositivo como um identificador único.
    """
    
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]  # Gera o MAC Address
    mac_formatado = ":".join(mac[i:i+2] for i in range(0, 12, 2))  # Formata como XX:XX:XX:XX:XX:XX
    return mac_formatado

def verificar_conexao_internet(host="8.8.8.8", port=53, timeout=3):
    """
    Verifica se há conexão com a internet.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

def verificar_chave(key):
    if not verificar_conexao_internet():
        messagebox.showerror(
            "Fasthunter Optimizer - Erro de conexão", 
            "Sem conexão com a internet. Verifique sua rede e tente novamente."
        )
        return "É necessário conexão com a internet!"

    try:
        # Referência à coleção de licenças
        licencas_ref = db.collection("licencas")
        
        mac_address = obter_mac_address()
        
        # Consulta para verificar se o dispositivo já está registrado em alguma licença
        docs = licencas_ref.where("usuario", "==", mac_address).stream()
        for doc in docs:
            # Dispositivo já registrado
            return "ACTIVATED PRODUCT"

        # Se não estiver registrado, pedir licença ao usuário
        docs = licencas_ref.where("licenca", "==", key).stream()
        for doc in docs:
            licenca_id = doc.id
            licenca_data = doc.to_dict()

            # Verificar se a licença já está vinculada a outro dispositivo
            usuario_vinculado = licenca_data.get("usuario")
            if usuario_vinculado:
                if usuario_vinculado == mac_address:
                    return "ESSE PRODUTO JÁ FOI ATIVADO"
                else:
                    return f"ESSA CHAVE DE ATIVAÇÃO JÁ FOI USADA"

            # Atualizar o documento com o MAC Address
            licencas_ref.document(licenca_id).update({"usuario": mac_address})

            # Autenticar o usuário após ativação bem-sucedida
            autenticar_usuario()

            return "SUCCESSFUL PRODUCT REGISTRATION"

        return "CHAVE DE ATIVAÇÃO INVÁLIDA"  # Chave não encontrada

    except Exception as e:
        return f"ERROR ACTIVATING KEY: {str(e)}"



