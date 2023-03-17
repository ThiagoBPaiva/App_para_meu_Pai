from tkinter import *
from tkinter import ttk
import os
import Comandos_do_app_de_pai
from Comandos_do_app_de_pai import Funcs
import Relatorio_do_cliente
from Relatorio_do_cliente import Relatorio

janela = Tk()


class AppDePAi(Funcs, Relatorio):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.freimes()
        self.labals()
        self.entradas()
        self.botoes()
        self.menu()
        self.lista_frame2()
        self.limpa_tela()
        self.mantatabelas()
        self.select_lista()
        self.ondoubleclick(1)
        self.alterar_cliente()
        janela.mainloop()

    def tela(self):
        self.janela.title('Tela de cadastro')
        self.janela.configure(background='#2F4F4F')
        self.janela.attributes('-fullscreen', True)

    def freimes(self):
        self.freime1 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#000000',
                        highlightthickness=3)
        self.freime1.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.99)
        # ----------------------------------------------------------------
        self.freime2 = Frame(self.freime1, bd=4, bg='#dfe3ee', highlightbackground='#000000',
                             highlightthickness=3)
        self.freime2.place(relx=0.02, rely=0.02, relwidth=0.85, relheight=0.6)
        # ----------------------------------------------------------------
        self.freime3 = Frame(self.freime1, bd=4, bg='#dfe3ee', highlightbackground='#000000',
                             highlightthickness=3)
        self.freime3.place(relx=0.02, rely=0.63, relwidth=0.981, relheight=0.35)


    def labals(self):
        self.lb_dados = Label(self.freime1, text='Dados', bg='#dfe3ee', font=('Verdana', 20, 'bold'))
        self.lb_dados.place(relx=0.01)

    def entradas(self):
        self.lb_codigo = Label(self.freime2, text='Código:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_codigo.place(relx=0.01, rely=0.1)

        self.codigo_entry = Entry(self.freime2)
        self.codigo_entry.place(relx=0.01, rely=0.17, relwidth=0.07)
        # ----------------------------------------------------------------
        self.lb_nome = Label(self.freime2, text='Nome:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_nome.place(relx=0.11, rely=0.1)

        self.nome_entry = Entry(self.freime2)
        self.nome_entry.place(relx=0.11, rely=0.17, relwidth=0.37)
        # ----------------------------------------------------------------
        self.lb_rg = Label(self.freime2, text='RG:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_rg.place(relx=0.51, rely=0.1)

        self.rg_entry = Entry(self.freime2)
        self.rg_entry.place(relx=0.51, rely=0.17, relwidth=0.07)
        # ----------------------------------------------------------------
        self.lb_cpf = Label(self.freime2, text='CPF:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_cpf.place(relx=0.61, rely=0.1)

        self.cpf_entry = Entry(self.freime2)
        self.cpf_entry.place(relx=0.61, rely=0.17, relwidth=0.125)
        # ----------------------------------------------------------------
        self.lb_idade = Label(self.freime2, text='Idade:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_idade.place(relx=0.765, rely=0.1)

        self.idade_entry = Entry(self.freime2)
        self.idade_entry.place(relx=0.765, rely=0.17, relwidth=0.065)
        # ----------------------------------------------------------------
        self.lb_sexo = Label(self.freime2, text='Sexo:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_sexo.place(relx=0.01, rely=0.25)

        self.sexo_entry = Entry(self.freime2)
        self.sexo_entry.place(relx=0.01, rely=0.32, relwidth=0.07)
        # ----------------------------------------------------------------
        self.lb_estado_civil = Label(self.freime2, text='Estado Civil:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_estado_civil.place(relx=0.11, rely=0.25)

        self.estado_civil_entry = Entry(self.freime2)
        self.estado_civil_entry.place(relx=0.11, rely=0.32, relwidth=0.12)
        # ----------------------------------------------------------------
        self.lb_profição = Label(self.freime2, text='Profição:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_profição.place(relx=0.26, rely=0.25)

        self.profição_entry = Entry(self.freime2)
        self.profição_entry.place(relx=0.26, rely=0.32, relwidth=0.22)
        # ----------------------------------------------------------------
        self.lb_cep = Label(self.freime2, text='CEP:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_cep.place(relx=0.51, rely=0.25)

        self.cep_entry = Entry(self.freime2)
        self.cep_entry.place(relx=0.51, rely=0.32, relwidth=0.07)
        # ----------------------------------------------------------------
        self.lb_naturalidade = Label(self.freime2, text='Naturalidade:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_naturalidade.place(relx=0.61, rely=0.25)

        self.naturalidade_entry = Entry(self.freime2)
        self.naturalidade_entry.place(relx=0.61, rely=0.32, relwidth=0.125)
        # ----------------------------------------------------------------
        self.lb_uf = Label(self.freime2, text='UF:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_uf.place(relx=0.765, rely=0.25)

        self.uf_entry = Entry(self.freime2)
        self.uf_entry.place(relx=0.765, rely=0.32, relwidth=0.065)
        # ----------------------------------------------------------------
        self.lb_rua = Label(self.freime2, text='Rua:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_rua.place(relx=0.01, rely=0.4)

        self.rua_entry = Entry(self.freime2)
        self.rua_entry.place(relx=0.01, rely=0.47, relwidth=0.22)
        # --------------------------------------------------------------
        self.lb_bairro = Label(self.freime2, text='Bairro', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_bairro.place(relx=0.26, rely=0.4)

        self.bairro_entry = Entry(self.freime2)
        self.bairro_entry.place(relx=0.26, rely=0.47, relwidth=0.22)
        # --------------------------------------------------------------
        self.lb_complemento = Label(self.freime2, text='Complemento:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_complemento.place(relx=0.51, rely=0.4)

        self.complemento_entry = Entry(self.freime2)
        self.complemento_entry.place(relx=0.51, rely=0.47, relwidth=0.32)
        # --------------------------------------------------------------
        self.lb_email = Label(self.freime2, text='Telefone:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_email.place(relx=0.01, rely=0.55)

        self.email_entry = Entry(self.freime2)
        self.email_entry.place(relx=0.01, rely=0.62, relwidth=0.22)
        # -------------------------------------------------------------
        self.lb_telefone = Label(self.freime2, text='E-mail:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_telefone.place(relx=0.26, rely=0.55)

        self.telefone_entry = Entry(self.freime2)
        self.telefone_entry.place(relx=0.26, rely=0.62, relwidth=0.22)
        # -------------------------------------------------------------
        self.lb_redi_social = Label(self.freime2, text='Social:', bg='#dfe3ee', font=('Verdana', 15))
        self.lb_redi_social.place(relx=0.51, rely=0.55)

        self.rede_social_entry = Entry(self.freime2)
        self.rede_social_entry.place(relx=0.51, rely=0.62, relwidth=0.32)

    def botoes(self):
        self.bt_novo = Button(self.freime1, text='Novo', bd=5, bg='#D3D3D3',
                                font=('verdana', 10, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.885, rely=0.07, relwidth=0.1, relheight=0.1)
        # -------------------------------------------------------------
        self.bt_apagar = Button(self.freime1, text='Apagar', bd=5, bg='#D3D3D3',
                                font=('Verdana', 10, 'bold'), command=self.limpa_tela)
        self.bt_apagar.place(relx=0.885, rely=0.17, relwidth=0.1, relheight=0.1)
        # -------------------------------------------------------------
        self.bt_alterar = Button(self.freime1, text='Alterar', bd=5, bg='#D3D3D3',
                                 font=('Verdana', 10, 'bold'), command=self.alterar_cliente)
        self.bt_alterar.place(relx=0.885, rely=0.27, relwidth=0.1, relheight=0.1)
        # -------------------------------------------------------------
        self.bt_pesquisa = Button(self.freime1, text='Pesquisar', bd=5, bg='#D3D3D3',
                                  font=('Verdana', 10, 'bold'), command=self.buscar_cliente)
        self.bt_pesquisa.place(relx=0.885, rely=0.37, relwidth=0.1, relheight=0.1)
        # -------------------------------------------------------------
        self.bt_remover = Button(self.freime1, text='Remover', bd=5, bg='#D3D3D3',
                                 font=('Verdana', 10, 'bold'), command=self.delata_cliente)
        self.bt_remover.place(relx=0.885, rely=0.47, relwidth=0.1, relheight=0.1)
        # -------------------------------------------------------------

    def menu(self):
        menubar = Menu(self.janela)
        self.janela.configure(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.janela.destroy()

        menubar.add_cascade(label='Opções', menu=filemenu)
        menubar.add_cascade(label='Relatorios', menu=filemenu2)

        filemenu.add_command(label='Sair', command=quit)
        filemenu.add_command(label='Limpar Cliente', command=self.limpa_tela)

        filemenu2.add_command(label='Ficha do Cliente', command=self.gera_relatorio_do_cliente)

    def lista_frame2(self):
        self.listacli = ttk.Treeview(self.freime3, height=3, columns=('col1', 'col2', 'col3', 'col4',
                                                                      'col5', 'col6', 'col7', 'col8',
                                                                      'col9', 'col10', 'col11', 'col12',
                                                                      'col13', 'col14', 'col15', 'col16',
                                                                      'col17'))
        self.listacli.heading('#1', text='Codigo')
        self.listacli.heading('#2', text='Nome')
        self.listacli.heading('#3', text='RG')
        self.listacli.heading('#4', text='CPF')
        self.listacli.heading('#5', text='Idade')
        self.listacli.heading('#6', text='Sexo')
        self.listacli.heading('#7', text='Estado Civil')
        self.listacli.heading('#8', text='Profição')
        self.listacli.heading('#9', text='CEP')
        self.listacli.heading('#10', text='Naturalidade')
        self.listacli.heading('#11', text='UF')
        self.listacli.heading('#12', text='RUA')
        self.listacli.heading('#13', text='Bairro')
        self.listacli.heading('#14', text='Complemento')
        self.listacli.heading('#15', text='Telefone')
        self.listacli.heading('#16', text='E-mail')
        self.listacli.heading('#17', text='Rede Social')

        self.listacli.column('#0', width=0)
        self.listacli.column('#1', width=50)
        self.listacli.column('#2', width=50)
        self.listacli.column('#3', width=50)
        self.listacli.column('#4', width=50)
        self.listacli.column('#5', width=50)
        self.listacli.column('#6', width=50)
        self.listacli.column('#7', width=50)
        self.listacli.column('#8', width=50)
        self.listacli.column('#9', width=50)
        self.listacli.column('#10', width=50)
        self.listacli.column('#11', width=50)
        self.listacli.column('#12', width=50)
        self.listacli.column('#13', width=50)
        self.listacli.column('#14', width=50)
        self.listacli.column('#15', width=50)
        self.listacli.column('#16', width=50)
        self.listacli.column('#17', width=50)


        self.listacli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroollista = Scrollbar(self.freime3, orient='vertical')
        self.listacli.configure(yscrollcommand=self.scroollista)
        self.scroollista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listacli.bind('<Double-1>', self.ondoubleclick)