from processos import *
from ativacaoSoftware import *
from configuracao import *;
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from returnPathAbsolute import *

logo_ico_path = get_resource_path("assets/logo1.ico")
logo_path = get_resource_path("assets/logo1.png")
logo_letreiro_path = get_resource_path("assets/logo-letreiro1.png")
chipset_path = get_resource_path("assets/chipset16x16.png")


def abrir_tela_principal():
    """
    Abre a tela principal da aplicação.
    """
    
    bg_color = "#e3e3e3"
    color_btn_inactive = "#F5F5DC"
    color_btn_active = "#FFE77B"
    
    def exibir_page1():
        page2_labelResultado.configure(text="")
        page2.pack_forget() # Oculta a página
        page3.pack_forget() # Oculta a página  
        page1_output_status.grid_forget()
        page1.pack_propagate(False) # Evita redimensionamento automático
        page1.pack(side="right", fill="both", expand=True) # Exibe a página
        
        menu_button1.config(bg=color_btn_active)
        menu_button2.config(bg=color_btn_inactive)
        menu_button3.config(bg=color_btn_inactive)


    def exibir_page2():
        page2_labelResultado.configure(text="")
        page1_output_status.grid_forget()
        page1.pack_forget() # Oculta a página
        page3.pack_forget() # Oculta a página
        page2.pack_propagate(False)  # Evita redimensionamento automático
        page2.pack(side="right", fill="both", expand=True) # Exibe a página        
        
        menu_button1.config(bg=color_btn_inactive)
        menu_button2.config(bg=color_btn_active)
        menu_button3.config(bg=color_btn_inactive)


    def exibir_page3():
        page2_labelResultado.configure(text="")
        page1_output_status.grid_forget()
        page1.pack_forget() # Oculta a página
        page2.pack_forget() # Oculta a página
        page3.pack_propagate(False)  # Evita redimensionamento automático
        page3.pack(side="right", fill="both", expand=True) # Exibe a página
        
        menu_button1.config(bg=color_btn_inactive)
        menu_button2.config(bg=color_btn_inactive)
        menu_button3.config(bg=color_btn_active)

    def salvar():
        config = {option: var.get() for option, var in options.items()}
        resultado = salvar_configuracoes(config)
        page2_labelResultado.configure(text=resultado)

    def iniciar_otimizacao():
        # request_admin(page1_output_status)
        page1_output_status.grid(column=1, row=2, pady=20)
        page1_output_status.delete("1.0", END)
        
        # Carregar as configurações salvas
        configuracoes = carregar_configuracoes()
    
        # Verificar se todas as opções estão desabilitadas
        if all(value == False for value in configuracoes.values()):
            page1_output_status.insert(END, "Nenhum processo está habilitado. Por favor, ative pelo menos um processo nas configurações.\n")
            page1_output_status.yview(END)
            return
        
        if configuracoes.get("Remover arquivos tempor\u00e1rios do sistema", False):
            clear_temp(page1_output_status)
            
        if configuracoes.get("Libera\u00e7\u00e3o de cache e busca de informa\u00e7\u00f5es DNS atualizadas", False):
            dns_optmizer(page1_output_status)
        
        if configuracoes.get("Habilitar o desempenho m\u00e1ximo do seu plano de energia", False):
            set_power_plan(page1_output_status)
             
        if configuracoes.get("Esvaziar lixeira", False):
            clear_trash(page1_output_status)
        
        if configuracoes.get("Configurar o provedor de controle de congestionamento como Compound TCP", False):
            check_and_enable_ctcp(page1_output_status)
        
        if configuracoes.get("Configurar o DCA para o protocolo TCP", False):
            check_and_enable_dca(page1_output_status)
            
        messagebox.showinfo("Fasthunter Optimizer", "Otimização concluída!")

    # Execução da tela principal
    root = Tk()
    root.geometry("900x500")
    root.resizable(False, False)
    root.iconbitmap(logo_ico_path)
    root.title("FastHunter Optimizer")

    # Carregando as imagens
    root.logo = PhotoImage(file=logo_path)
    root.logo_letreiro = PhotoImage(file=logo_letreiro_path)
    root.chipset_image = PhotoImage(file=chipset_path)

    # Redimensionando as imagens
    root.logo = root.logo.subsample(7, 7)
    root.logo_letreiro = root.logo_letreiro.subsample(3,3)
    root.logo_letreiro_carimbo = root.logo_letreiro.subsample(2,2)

    # Criando um Frame "PAI" para receber todo o conteúdo da aplicação
    frame = Frame(root, width=900, height=500, bg="#000")
    frame.pack_propagate(False)  # Evita redimensionamento automático
    frame.pack(fill="both", expand=True)

    ########### Menu
    menu = Frame(frame, width=200, height=500, bg="#373737")
    menu.pack_propagate(False)  # Evita redimensionamento automático
    menu.pack(side="left", fill="y")

    menu_img_logo = Label(menu, image=root.logo, bg="#373737")
    menu_img_logo.grid(column=0, row=0, padx=62, pady=20)

    menu_button1 = Button(menu, text="Otimizar", width=15, padx=10, pady=5, bg=color_btn_active, cursor="hand2", command=exibir_page1)
    menu_button1.grid(column=0, row=1, pady=20)

    menu_button2 = Button(menu, text="Configurações", width=15, padx=10, pady=5, bg=color_btn_inactive, cursor="hand2", command=exibir_page2)
    menu_button2.grid(column=0, row=2, pady=20)

    menu_button3 = Button(menu, text="Sobre", width=15, padx=10, pady=5, bg=color_btn_inactive, cursor="hand2", command=exibir_page3)
    menu_button3.grid(column=0, row=3, pady=20)

    ######### Conteúdo Pagina 1
    page1 = Frame(frame, width=700, height=500, bg=bg_color)
    page1.pack_propagate(False)  # Evita redimensionamento automático
    page1.pack(side="right", fill="both", expand=True)

    # Configura o grid para centralizar conteudos
    page1.columnconfigure(0, weight=1)
    page1.columnconfigure(1, weight=1)
    page1.columnconfigure(2, weight=1)

    page1_image = Label(page1, image=root.logo_letreiro, bg=bg_color)
    page1_image.grid(column=1, row=0, pady=40)

    page1_buttonStart = Button(
        page1, 
        text="Iniciar Otimização", 
        padx=20, pady=10, 
        bg=color_btn_active, fg='#000', 
        cursor="hand2",
        font=(12),
        image=root.chipset_image, 
        compound="left",
        command=iniciar_otimizacao
    )
    page1_buttonStart.grid(column=1, row=1, pady=0)

    page1_output_status = scrolledtext.ScrolledText(page1, wrap=WORD, width=70, height=6, bg="#454545", fg="#5fff46", font=("Arial", 13))


    ######### Conteúdo Pagina 2
    page2 = Frame(frame, width=700, height=500, bg=bg_color)

    # Configura o grid para centralizar conteudos
    page2.columnconfigure(0, weight=1)
    page2.columnconfigure(1, weight=1)
    page2.columnconfigure(2, weight=1)

    page2_texto1 = Label(
        page2, 
        bg=bg_color,
        justify="left",
        pady=20, padx=20,
        font=("Arial", 10),
        text=f"Esta é uma página destinada a pessoas que sabem o que cada processo significa e que desejam\nhabilitar ou desativar alguma das opções para o processo de otimização do seu computador.\nCiente o que cada opção faz, caso você alterar alguma delas, certifique-se de salvar antes de sair da página\npara o sistema reconhecer as configurações na hora da otimização.",
    )
    page2_texto1.grid(sticky="w")


    config = carregar_configuracoes()
    options = {}
    for name_option in [
        "Remover arquivos temporários do sistema",
        "Liberação de cache e busca de informações DNS atualizadas",
        "Habilitar o desempenho máximo do seu plano de energia",
        "Esvaziar lixeira",
        "Configurar o provedor de controle de congestionamento como Compound TCP",
        "Configurar o DCA para o protocolo TCP"]:
        var = BooleanVar(value=config.get(name_option, False))
        chk = Checkbutton(
            page2,
            bg=bg_color,
            pady=9, padx=10,
            font=("Arial", 10),
            cursor="hand2",
            text=name_option,
            variable=var,
            anchor="w"
        )
        chk.grid(sticky="w")
        options[name_option] = var


    page2_labelResultado = Label(page2,bg=bg_color,font=("Arial", 10),fg="green",text="")
    page2_labelResultado.grid(pady=10)

    page2_buttonSave = Button(
        page2,
        bg=color_btn_active,
        text="Salvar",
        anchor="w",
        cursor="hand2",
        pady=3, padx=50,
        command=salvar,
    )
    page2_buttonSave.grid(pady=20, padx=20)


    ######### Conteúdo Pagina 3
    page3 = Frame(frame, width=700, height=500, bg=bg_color)

    # Configura o grid para centralizar conteudos
    page3.columnconfigure(0, weight=1)
    page3.columnconfigure(1, weight=1)
    page3.columnconfigure(2, weight=1)
    page3.rowconfigure(0, weight=1)
    page3.rowconfigure(1, weight=1)
    page3.rowconfigure(2, weight=1)

    page3_texto1 = Label(
        page3, 
        bg=bg_color,
        justify="left",
        pady=10,
        font=("Arial", 12),
        text=f"Olá, este é o Fasthunter Optimizer, um sistema que otimiza\nseu computador de forma segura, usando técnicas de limpeza e otimização\nde hardware/rede de forma nativa do windows.\n\nEsse sistema foi criado pensando em automatizar essas técnicas para otimizar\nseu computador em apenas 1 clique.\n\n"
    )
    page3_texto1.grid(column=1,row=0)

    page3_carimbo = Label(page3, image=root.logo_letreiro_carimbo, bg=bg_color)
    page3_carimbo.grid(column=2, row=2)

    root.mainloop()


def abrir_tela_ativacao():
    """
    Abre a tela de ativação do produto.
    """
    janela_ativacao = Tk()
    janela_ativacao.title("Fasthunter Optimizer - Ativação do Produto")
    janela_ativacao.geometry("900x300")
    janela_ativacao.resizable(False, False)
    janela_ativacao.iconbitmap(logo_ico_path)
    
    # Carregando as imagens
    background_tela_ativacao_path = get_resource_path("assets/background_tela_ativacao.png")
    key_black_icon_path = get_resource_path("assets/key_black.png")
    key_white_icon_path = get_resource_path("assets/key_white.png")
    janela_ativacao.bg_image = PhotoImage(file=background_tela_ativacao_path)
    janela_ativacao.icon_key_black = PhotoImage(file=key_black_icon_path)
    janela_ativacao.icon_key_white = PhotoImage(file=key_white_icon_path)
    
    # Cria um label para a imagem de fundo
    label_fundo = Label(janela_ativacao, image=janela_ativacao.bg_image)
    label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    # Label e Entry para inserir a chave de ativação
    lbl_instrucoes = Label(janela_ativacao, text="Esse é o software Oficial do Fasthunter Optimizer.\nPara ter acesso, Insira a chave de ativação do produto:", font=("Arial", 13))
    lbl_instrucoes.pack(pady=10)
    entrada_chave = Entry(janela_ativacao, width=50, font=("Arial", 14), fg="#1b6300", bg="#d9d9d9", border=3)
    entrada_chave.pack(pady=10)

    def ativar_produto():
        chave_licenca = entrada_chave.get()
        if not chave_licenca.strip():
            messagebox.showerror("Fasthunter Optimizer - Ativação do Produto", "Por favor, insira uma chave de ativação.")
            return

        resultado = verificar_chave(chave_licenca)

        if resultado == "SUCCESSFUL PRODUCT REGISTRATION" or resultado == "ACTIVATED PRODUCT":
            messagebox.showinfo("Fasthunter Optimizer - Ativação do Produto", "Produto ativado com sucesso!")
            janela_ativacao.destroy()  # Fecha a janela de ativação
            abrir_tela_principal()    # Abre a tela principal
        else:
            messagebox.showerror("Fasthunter Optimizer - Ativação do Produto", resultado)

    # Botão de ativar
    btn_ativar = Button(
        janela_ativacao, 
        padx=30, pady=10,
        bg="#e3df43",
        text="Ativar Produto",
        image=janela_ativacao.icon_key_black, 
        cursor="hand2",
        compound="left", 
        command=ativar_produto
    )
    btn_ativar.pack(pady=20)

    janela_ativacao.mainloop()


def iniciar_aplicacao():
    """       
        Função principal para iniciar a aplicação.
        Verifica se o produto já está ativado.
    """
    resultado = verificar_chave("")
    if resultado == "ACTIVATED PRODUCT":
        abrir_tela_principal()
    else:
        abrir_tela_ativacao()



# Inicializa a aplicação
if __name__ == "__main__":
    iniciar_aplicacao()
