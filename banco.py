import sqlite3
from funcs import Funcs
from tkinter import *
from tkinter import ttk
from tkinter import  messagebox


class Banco(Funcs):


    def conectaDb(self):
        self.conn = sqlite3.connect('ejex.db')
        self.cursor = self.conn.cursor()

    def desconectaDb(self):
        self.conn.close()

    def montandoTabelas(self):
        self.conectaDb(); print('conectando')
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tabela_produtos ( 
                id INTEGER PRIMARY KEY,
                cod VARCHAR(20),
                nome_do_produto VARCHAR(40) ,
                fornecedor VARCHAR(40),
                qtde VARCHAR(20),
                valor VARCHAR(20)
              );
        """)
        self.conn.commit()

        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS clientes ( 
                        id INTEGER PRIMARY KEY,
                        nome VARCHAR(40),
                        cpf VARCHAR(11) UNIQUE,
                        rg VARCHAR(20),
                        sexo VARCHAR(1),
                        dt_nascimento VARCHAR(10),
                        convenio VARCHAR(20),
                        endereco VARCHAR(20),
                        n_casa VARCHAR(10),
                        complemento VARCHAR(20),
                        cep VARCHAR(20),
                        bairro VARCHAR(20),
                        uf VARCHAR(20),
                        municipio VARCHAR(20),
                        email VARCHAR(20),
                        ddd VARCHAR(2),
                        celular VARCHAR(20),
                        plano_desconto VARCHAR(20),
                        info_gerais VARCHAR(100)
                      );
                """)
        self.conn.commit()
        self.desconectaDb()

    def variaveis(self):
        self.codigo = self.entryCod2.get()
        self.nome = self.entryNomePro.get()
        self.fornecedor = self.entryFornecedor.get()
        self.qtde = self.entryQtd2.get()
        self.valor = self.entryValor2.get()

    def adicionarProdutos(self):
        self.variaveis()
        self.conectaDb()

        self.cursor.execute(""" INSERT INTO tabela_produtos (cod,nome_do_produto,fornecedor,qtde,valor)
          VALUES (?, ?, ?, ?, ?)""",(self.codigo,self.nome,self.fornecedor,self.qtde,self.valor))

        self.conn.commit()
        self.desconectaDb()
        self.selectTabela()
        self.limparTelaEstoque()

    def deletaProdutos(self):
        self.variaveis()
        self.conectaDb()

        self.cursor.execute(""" DELETE FROM tabela_produtos WHERE  cod = ? """, (self.codigo,))

        self.conn.commit()
        self.selectTabela()
        self.limparTelaEstoque()
        self.desconectaDb()

    def clickDuplo(self,event):
        self.limparTelaEstoque()
        self.tabela2.selection()

        for n in self.tabela2.selection():
            codigo,nome,fornecedor,valor,qtd = self.tabela2.item(n, 'values')
            self.entryCod2.insert(END, codigo)
            self.entryNomePro.insert(END, nome)
            self.entryFornecedor.insert(END, fornecedor)
            self.entryQtd2.insert(END, qtd)
            self.entryValor2.insert(END, valor)


    def selectTabela(self):
       self.tabela2.delete(*self.tabela2.get_children())
       self.conectaDb()
       lista = self.cursor.execute(""" SELECT cod, nome_do_produto, fornecedor, qtde, valor FROM tabela_produtos
       ORDER BY nome_do_produto ASC; """)

       for i in lista:
            self.tabela2.insert("", END, values = i)
       self.desconectaDb()


    def selectTabelaFrente(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conectaDb()
        consultaFinal = self.cursor.execute(""" SELECT cod, nome_do_produto,qtde,valor,desc,total FROM tabela_frente_loja
                ; """, )
        for i in consultaFinal:
            self.tabela.insert("", END, values = i)
        self.desconectaDb()



    def contas(self):

        self.CodProduto = self.entryCodProduto.get()
        self.Quantidade = self.entryQuantidade.get()



        self.conectaDb()
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tabela_frente_loja ( 
                        id INTEGER PRIMARY KEY,
                        cod INTEGER(20),
                        nome_do_produto VARCHAR(40) ,
                        qtde INTEGER(20),
                        valor FLOAT(40),
                        desc FLOAT(20),
                        total FLOAT(40)
                      );
                """)

        self.conn.commit()


        lista1 = self.cursor.execute(""" SELECT cod, nome_do_produto, valor FROM tabela_produtos WHERE cod = ?; """, (self.CodProduto,))

        lista2 = lista1.fetchall()
        print(lista2)

        codigo = lista2[0][0]
        nome = lista2[0][1]
        valor = lista2[0][2]
        desc = 2
        total = valor * float(self.Quantidade)
        print(total)
        self.soma = 0
        self.soma =self.soma + total


        self.cursor.execute(""" INSERT INTO tabela_frente_loja (cod,nome_do_produto,qtde,valor,desc,total)
                 VALUES (?, ?, ?, ?, ?, ?)""", (int(codigo), nome,int(self.Quantidade),float(valor),float(desc),float(total)))
        self.conn.commit()

        self.lbValorSubTotal['text'] = total
        self.lbValorTotal['text'] = self.soma

        self.selectTabelaFrente()
        self.desconectaDb()

    def consultaCliente(self):
        self.conectaDb()
        self.codigoCliente = self.lbCodCliente.get()

        if (not self.codigoCliente):
            return messagebox.showwarning("", "Informe o CPF!")

        busca = self.cursor.execute('''  SELECT nome,convenio,email,info_gerais FROM clientes WHERE cod = ?; ''',(self.codigoCliente,))

        nomeCliente = busca.fetchone()

        if (not nomeCliente):
            return messagebox.showinfo("", "Cliente não encontrado!")

        #self.['text'] = f'SEJA BEM VINDO, {nomeCliente[0]}'


        self.desconectaDb()

    def finalizaCompra(self):
        self.dinheiro = self.entryDinheiro.get()

        troco = float(self.dinheiro) - self.soma
        self.lbValorTroco['text'] = f'R${troco:.2f}'

        self.entryCodProduto.delete(0, END)
        self.entryQuantidade.delete(0, END)

    def limpaTabela(self):
        self.conectaDb()
        drop = self.cursor.execute(''' DROP TABLE tabela_frente_loja ''')
        self.conn.commit()
        self.desconectaDb()
        self.selectTabelaFrente()
        self.entryDinheiro.delete(0, END)

    def consultaCliente(self):
        self.conectaDb()
        self.codigoCliente = self.entryCpfCli.get()

        if (not self.codigoCliente):
            return messagebox.showwarning("", "Informe o CPF!")

        busca = self.cursor.execute(''' SELECT nome, convenio, email, info_gerais FROM clientes WHERE cpf = ?; ''',
                                    (self.codigoCliente,))

        dados = busca.fetchall()

        if (not dados):
            return messagebox.showinfo("", "Cliente não encontrado!")

        for i in dados:
            self.tabela3.insert("", END, values=i)

        self.desconectaDb()

    def cadastrar_cliente(self):

        if (not self.entryNomeCli.get()):
            return messagebox.showwarning("", "Campo Nome obrigatório!")

        if (not self.entryCpfCli.get()):
            return messagebox.showwarning("", "Campo CPF obrigatório!")

        if (not self.entryEmail.get()):
            return messagebox.showwarning("", "Campo Email obrigatório!")

        self.conectaDb()

        # Inserir dados na tabela:
        self.cursor.execute(
            """ INSERT INTO clientes (nome,cpf,rg,sexo,dt_nascimento,convenio,endereco,n_casa,complemento,cep,bairro,uf,municipio,email,ddd,celular,plano_desconto,info_gerais) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                self.entryNomeCli.get(),
                self.entryCpfCli.get(),
                self.entryRgCli.get(),
                self.vSexo.get(),
                self.entryDataNa.get(),
                self.entryConvenio.get(),
                self.entryEndereco.get(),
                self.entryNum.get(),
                self.entryComp.get(),
                self.entryCep.get(),
                self.entryBairro.get(),
                self.entryUf.get(),
                self.entryMunicipio.get(),
                self.entryEmail.get(),
                self.entryDdd.get(),
                self.entryNume.get(),
                self.vdesc.get(),
                self.txtInfo.get("1.0", 'end-1c')
            )
            )

        # Commit as mudanças:
        self.conn.commit()

        self.limparTelaClientes()

        # Fechar o banco de dados:
        self.desconectaDb()

        return messagebox.showinfo("", "Cliente cadastrado!")




