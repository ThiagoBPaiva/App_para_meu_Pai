import sqlite3
from tkinter import *
from tkinter import messagebox
import requests


class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.rg_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.idade_entry.delete(0, END)
        self.sexo_entry.delete(0, END)
        self.estado_civil_entry.delete(0, END)
        self.profição_entry.delete(0, END)
        self.uf_entry.delete(0, END)
        self.naturalidade_entry.delete(0, END)
        self.cep_entry.delete(0, END)
        self.rua_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.complemento_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.rede_social_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("dadosdosclienter.txt")
        self.cursor = self.conn.cursor();
        print('Conectando ao banco de dados')

    def desconectar_bd(self):
        self.conn.close();
        print('Desconectando ao banco de dados')

    def mantatabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dadosdosclienter (
                codigo INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
                rg CHAR(20),
                cpf CHAR(20),
                idade CHAR(20),
                sexo CHAR(20),
                estado_civil CHAR(20),
                profição CHAR(30),
                uf CHAR(20),
                naturalidade CHAR(30),
                cep CHAR(20),
                rua CHAR(20),
                bairro CHAR(20),
                complemento CHAR(40),
                telefone CHAR(20),
                email CHAR(20),
                rede_social CHAR(20)
                
            );
        """)

        self.conn.commit();
        print('Banco de dados criado')
        self.desconectar_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.rg = self.rg_entry.get()
        self.cpf = self.cpf_entry.get()
        self.idade = self.idade_entry.get()
        self.sexo = self.sexo_entry.get()
        self.estado_civil = self.estado_civil_entry.get()
        self.profição = self.profição_entry.get()
        self.uf = self.uf_entry.get()
        self.naturalidade = self.naturalidade_entry.get()
        self.cep = self.cep_entry.get()
        self.rua = self.rua_entry.get()
        self.bairro = self.bairro_entry.get()
        self.complemento = self.complemento_entry.get()
        self.telefone = self.telefone_entry.get()
        self.email = self.email_entry.get()
        self.rede_social = self.rede_social_entry.get()

    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.validação_de_cep()

        self.cursor.execute(""" INSERT INTO dadosdosclienter (nome, rg, cpf, idade, sexo, estado_civil, profição, cep, naturalidade,
        uf, rua, bairro, complemento, email, telefone, rede_social)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.nome,
                                                                     self.rg,
                                                                     self.cpf,
                                                                     self.idade,
                                                                     self.sexo,
                                                                     self.estado_civil,
                                                                     self.profição,
                                                                     self.cep,
                                                                     self.naturalidade2,
                                                                     self.uf2,
                                                                     self.rua2,
                                                                     self.bairro2,
                                                                     self.complemento,
                                                                     self.email,
                                                                     self.telefone,
                                                                     self.rede_social
                                                                     )
                            )
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listacli.delete(*self.listacli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT codigo, nome, rg, cpf, idade, sexo, estado_civil, profição, cep,
         naturalidade, uf, rua, bairro, complemento, email, telefone, rede_social FROM dadosdosclienter ORDER BY codigo""")
        for i in lista:
            self.listacli.insert('', END, values=i)
        self.desconectar_bd()

    def ondoubleclick(self, event):
        self.limpa_tela()
        self.listacli.selection()

        for i in self.listacli.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17 \
                = self.listacli.item(i, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.rg_entry.insert(END, col3)
            self.cpf_entry.insert(END, col4)
            self.idade_entry.insert(END, col5)
            self.sexo_entry.insert(END, col6)
            self.estado_civil_entry.insert(END, col7)
            self.profição_entry.insert(END, col8)
            self.uf_entry.insert(END, col11)
            self.naturalidade_entry.insert(END, col10)
            self.cep_entry.insert(END, col9)
            self.rua_entry.insert(END, col12)
            self.bairro_entry.insert(END, col13)
            self.complemento_entry.insert(END, col14)
            self.email_entry.insert(END, col15)
            self.telefone_entry.insert(END, col16)
            self.rede_social_entry.insert(END, col17)

    def delata_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM dadosdosclienter WHERE codigo = ? """, (self.codigo))
        self.conn.commit()
        self.desconectar_bd()
        self.limpa_tela()
        self.select_lista()

    def alterar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE dadosdosclienter SET nome = ?, rg = ?, cpf = ?, idade = ?, sexo = ?, estado_civil = ?,
         profição = ?, cep = ?, naturalidade = ?, uf = ?, rua = ?, bairro = ?, complemento = ?, telefone = ?, email = ?,
         rede_social = ?
         WHERE codigo = ?""", (self.nome, self.rg, self.cpf, self.idade, self.sexo, self.estado_civil, self.profição,
                               self.cep, self.naturalidade, self.uf, self.rua, self.bairro, self.complemento,
                               self.telefone, self.email, self.rede_social, self.codigo
                               )
                            )
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpa_tela()

    def buscar_cliente(self):
        self.conecta_bd()
        self.listacli.delete(*self.listacli.get_children())
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute(
            f"""SELECT codigo, nome, rg, cpf, idade, sexo, estado_civil, profição, cep, naturalidade, uf, rua,
            bairro, complemento, telefone, email, rede_social FROM dadosdosclienter
            WHERE nome LIKE '{nome}' ORDER BY nome ASC""")
        buscanomecls = self.cursor.fetchall()
        for i in buscanomecls:
            self.listacli.insert('', END, values=i)
        self.limpa_tela()
        self.desconectar_bd()

    def validação_de_cep(self):
        self.cep = self.cep_entry.get()

        if len(self.cep) == 8:
            self.link = f'https://viacep.com.br/ws/{self.cep}/json/'

            self.requisicao = requests.get(self.link)

            self.dic_requisicao = self.requisicao.json()

            self.uf2 = self.dic_requisicao['uf']
            self.naturalidade2 = self.dic_requisicao['localidade']
            self.rua2 = self.dic_requisicao['logradouro']
            self.bairro2 = self.dic_requisicao['bairro']
            print(f'UF: {self.uf2}\n'
                  f'Naturalidade: {self.naturalidade2}\n'
                  f'Rua: {self.rua2}\n'
                  f'Bairro: {self.bairro2}')

        else:
            msg = 'CEP invalido'
            messagebox.showinfo('ERRO', msg)
