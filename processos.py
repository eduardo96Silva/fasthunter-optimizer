import os
import shutil
import subprocess
from tkinter import *
import ctypes
import sys
import os

def clear_temp(output):
    """Limpa os arquivos temporários."""
    try:
        # Obtém o caminho da pasta temporária do usuário
        temp_dir = os.getenv("TEMP")
        
        if not temp_dir or not os.path.exists(temp_dir):
            print("A pasta de arquivos temporários não foi encontrada.")
            return
        
        print(f"Limpando arquivos temporários em: {temp_dir}")
        
        # Lista todos os arquivos e diretórios na pasta temporária
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)
            
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)  # Remove arquivos ou links
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)  # Remove pastas e subpastas
                    
                print(f"Removido: {item_path}")
            except Exception as e:
                print(f"Não foi possível excluir {item_path}: {e}")
                
        output.insert(END, "\n✔ Limpeza de arquivos temporários concluída !")
        output.yview(END)
        print("Limpeza concluída com sucesso.")
    except Exception as e:
        output.insert(END, f"\n✗ Ocorreu um erro durante a limpeza")
        output.yview(END)
        print(f"Ocorreu um erro durante a limpeza: {e}")

def dns_optmizer(output):
    """ Resolve, Limpa e Atualiza DNS"""
    try:
        subprocess.run([
                "ipconfig", 
                "/flushdns"
            ], check=True, text=True)
        
        output.insert(END, f"\n✔ Liberação de cache e busca de informações DNS atualizadas com sucesso!")
        output.yview(END)
        
    except Exception as e:
        output.insert(END, f"\n✗ Ocorreu um erro durante a liberação de cache e busca de informações DNS")
        output.yview(END)
        print(f"Ocorreu um erro durante a otimização de DNS: {e}")
        
def set_power_plan(output):
    try:
        # Identificador do plano de energia desempenho máximo
        plan_guid = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
        
        # Verifica o plano de energia ativo
        result = subprocess.run(["powercfg", "-query"], capture_output=True, text=True)
        
        if plan_guid in result.stdout:
            output.insert(END, f"\n● Não foi necessário ativar o plano de energia de desempenho máximo, pois ele já está ativado.")
            output.yview(END)
            print("O plano de energia de desempenho máximo já está ativo.")
        else:
            subprocess.run(["powercfg", "-setactive", plan_guid], check=True)
            output.insert(END, f"\n✔ Plano de energia alterado para desempenho máximo com sucesso!")
            output.yview(END)
            print("Plano de energia alterado com sucesso.")
    
    except Exception as e:
        output.insert(END, f"\n✗ Erro ao alterar plano de energia para o desempenho máximo")
        output.yview(END)
        print(f"Erro ao alterar plano de energia")

def clear_trash(output):
    try:
        # Executa o comando no terminal
        subprocess.run(['rd', '/s', '/q', r'C:\$Recycle.Bin'], check=True, shell=True)
        output.insert(END, f"\n✔ Lixeira esvaziada com sucesso!")
        output.yview(END)
        print("Lixeira esvaziada com sucesso!")
    except subprocess.CalledProcessError as e:
        output.insert(END, f"\n✗ Erro ao tentar esvaziar a lixeira")
        output.yview(END)
        print(f"Erro ao esvaziar a lixeira")

def check_and_enable_ctcp(output):
    # Comando para verificar o provedor de congestionamento atual
    try:
        result = subprocess.run(['netsh', 'int', 'tcp', 'show', 'global'], capture_output=True, text=True, shell=True)
        
        # Verifica se o CTCP está habilitado
        if 'Provedor de Controle de Congestão de Complementos  : ctcp' or 'Provedor de Controle de Congestão  : ctcp' in result.stdout:
            output.insert(END, f"\n● Não foi necessário ativar o CTCP, pois ele já está ativado.")
            output.yview(END)
            print("CTCP já está habilitado.")
        else:
            # Habilita o CTCP
            subprocess.run(['netsh', 'int', 'tcp', 'set', 'global', 'congestionprovider=ctcp'], shell=True)
            output.insert(END, f"\n✔ CTCP habilitado com sucesso!")
            output.yview(END)
            print("CTCP habilitado com sucesso!")
    except:
        output.insert(END, f"\n✗ Erro ao tentar ativar o CTCP")
        output.yview(END)

def check_and_enable_dca(output):
    # Verifica o estado atual do DCA e habilita se necessário
    try:
        result = subprocess.run('netsh int tcp show global', capture_output=True, text=True)
        
        if 'DCA' in result.stdout and 'enabled' in result.stdout:
            output.insert(END, f"\n● Não foi necessário ativar o DCA, pois ele já está ativado.")
            output.yview(END)
            print("DCA já está habilitado.")
        else:
            subprocess.run('netsh int tcp set global dca=enabled', shell=True)
            output.insert(END, f"\n✔ DCA habilitado com sucesso!")
            output.yview(END)
    except:
        output.insert(END, f"\n✗ Erro ao tentar ativar o DCA")
        output.yview(END)
        


def check_winget():
    """Verifica se o Winget está instalado."""
    if shutil.which("winget"):
        return True
    else:
        print("Winget não encontrado.")
        return False

def install_winget():
    """Tenta instalar o Winget usando o comando de atualização do sistema."""
    try:
        print("Tentando instalar o Winget...")
        # Comando para tentar instalar ou atualizar o Winget via PowerShell
        subprocess.run(["powershell", "-Command", "Get-AppxPackage Microsoft.DesktopAppInstaller | Foreach {Add-AppxPackage -Path $_.InstallLocation + '\\AppXManifest.xml' }"], check=True)
        print("Winget instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao tentar instalar o Winget: {e}")
        
def update_packages(output):
    """Verifica se possui atualizações nos softwares instalados"""
    try:
        if not check_winget():
            install_winget()
            
        subprocess.run([
            "winget", 
            "upgrade", 
            "--all", 
            "--accept-package-agreements", 
            "--accept-source-agreements"
            ], check=True)
        
        output.insert(END, f"\n✔ Todos os pacotes atualizados com sucesso!")
        output.yview(END)
        print("Todos os pacotes atualizados.")
    except Exception as e:
        output.insert(END, f"\n✗ Erro ao atualizar pacotes: {e}")
        output.yview(END)
        print(f"Erro ao atualizar pacotes: {e}")