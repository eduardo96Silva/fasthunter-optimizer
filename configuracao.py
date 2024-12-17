# Funções para salvar e carregar configurações
import json
from returnPathAbsolute import *
import os

def get_config_path():
    """
    Retorna o caminho do arquivo de configuração na pasta AppData/Roaming.
    """
    app_name = "FasthunterOptimizer"  # Nome da sua aplicação
    config_dir = os.path.join(os.getenv("APPDATA"), app_name)  # Diretório persistente
    os.makedirs(config_dir, exist_ok=True)  # Cria o diretório se não existir
    return os.path.join(config_dir, "config.json")


def salvar_configuracoes(config):
    try:
        """
        Salva a configuração no arquivo config.json.
        """
        config_path = get_config_path()
        with open(config_path, "w") as file:
            json.dump(config, file, indent=4)
        return "Configurações salva com sucesso!"
    except:
        return "Não foi possível salvar as configurações."
    
    
def carregar_configuracoes():
    try:
        """
        Carrega a configuração do arquivo config.json.
        """
        config_path = get_config_path()
        if os.path.exists(config_path):
            with open(config_path, "r") as file:
                return json.load(file)
        else:
            return {
                "Remover arquivos tempor\u00e1rios do sistema": True, 
                "Libera\u00e7\u00e3o de cache e busca de informa\u00e7\u00f5es DNS atualizadas": True, 
                "Habilitar o desempenho m\u00e1ximo do seu plano de energia": True, 
                "Esvaziar lixeira": False, 
                "Configurar o provedor de controle de congestionamento como Compound TCP": False, 
                "Configurar o DCA para o protocolo TCP": False
            }
    except FileNotFoundError:
        return {}