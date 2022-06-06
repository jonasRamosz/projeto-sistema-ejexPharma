from tkinter import *
from tkinter import ttk


from banco import Banco
import sqlite3

import os


root = Tk()




class Venda(Banco):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.widgetsFrame1()
        self.widgetsFrame2()
        self.widgetsFrame3()
        self.widgetsFrame4()
        self.widgetsFrame5()
        self.widgetsFrame6()
        self.widgetsFrame7()
        self.menu()
        self.elementosSoltos()
        self.montandoTabelas()

        root.mainloop()



    def tela(self):
        self.root.title('EJ3X PHARMA')
        self.root.configure(background = '#40E0D0')
        self.root.geometry('1000x650')
        self.root.resizable(True,True)

        self.root.minsize(width=600, height=325)

    def frame(self):
        self.frame1 = Frame(self.root , bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frame1.place(relx = 0.02, rely = 0.02, relwidth = 0.55, relheight = 0.93)

        self.frame2 = Frame(self.root, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frame2.place(relx=0.60, rely=0.15, relwidth=0.38, relheight=0.08)

        self.frame3 = Frame(self.root, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frame3.place(relx=0.60, rely=0.3, relwidth=0.38, relheight=0.25)

        self.frame4 = Frame(self.root, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frame4.place(relx=0.60, rely=0.57, relwidth=0.38, relheight=0.08)

        self.frame5 = Frame(self.root, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frame5.place(relx=0.60, rely=0.67, relwidth=0.38, relheight=0.08)

        self.frame6 = Frame(self.root, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frame6.place(relx=0.60, rely=0.77, relwidth=0.38, relheight=0.08)

        self.frame7 = Frame(self.root, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frame7.place(relx=0.60, rely=0.87, relwidth=0.38, relheight=0.08)

    def menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)

        def quit():
            self.root.destroy()

        menubar.add_cascade(label = 'CADASTROS' , menu = filemenu )
        menubar.add_cascade(label = 'ESTOQUE', menu = filemenu2)
        menubar.add_checkbutton(label = 'SAIR' ,command =quit)

        filemenu.add_command(label = 'CLIENTES', command = self.cadCliente)


        filemenu2.add_command(label='CADASTRO',command = self.telaEstoque)



    def elementosSoltos(self):
        self.lbBVindo = Label(self.root, text='SEJA BEM VINDO,', bg='#40E0D0',fg='#008B8B', font=('verdana', 12, 'bold'))
        self.lbBVindo.place(relx=0.6, rely=0.25)

        self.btFinaliza = Button(self.root, text='FINALIZAR COMPRA', font=('verdana', 10, 'bold'),command = self.finalizaCompra)
        self.btFinaliza.place(relx=0.83, rely=0.955, relwidth=0.15, relheight=0.04)

        pasta = 'ejexlogo3.png'
        self.imgLogo = PhotoImage(file=pasta)
        self.lbLogo = Label(self.root, image = self.imgLogo,anchor = 'w')
        self.lbLogo.place(relx=0.58,rely=0.019,relwidth=0.45,relheight=0.13)

    def widgetsFrame1(self):
        self.tabela = ttk.Treeview(self.frame1, height=100,
                                   columns=( 'id', 'nome', 'qtd', 'valor', 'desconto', 'total'),show='headings')

        self.tabela.column('id', width=55)
        self.tabela.column('nome', width=247)
        self.tabela.column('qtd', width=45)
        self.tabela.column('valor', width=65)
        self.tabela.column('desconto', width=50)
        self.tabela.column('total', width=60)

        self.tabela.heading('id', text='CÓDIGO', anchor='w')
        self.tabela.heading('nome', text='NOME', anchor='w')
        self.tabela.heading('qtd', text='QNTD', anchor='w')
        self.tabela.heading('valor', text='PREÇO', anchor='w')
        self.tabela.heading('desconto', text='DESC', anchor='w')
        self.tabela.heading('total', text='TOTAL', anchor='w')

        self.tabela.place(relx=0.01, rely=0.01, relwidth=0.99, relheight=0.95)

    def widgetsFrame2(self):

        self.lbCodCliente = Label(self.frame2, text='CÓD. DO CLIENTE', bg='#008B8B',fg='white', font=('verdana', 12, 'bold'))
        self.lbCodCliente.place(relx=0.02, rely=0.15)
        self.entryCodCliente = Entry(self.frame2, font=('verdana', 10, 'bold'),fg='#FF4500')
        self.entryCodCliente.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.8)

        self.btOk = Button(self.frame2, text='OK', font=('verdana', 10, 'bold'),command=self.limpaTabela)
        self.btOk.place(relx=0.85, rely=0.1, relwidth=0.15, relheight=0.8)

    def widgetsFrame3(self):

        self.lbCodProduto = Label(self.frame3, text='CÓDIGO DO PRODUTO', bg='#008B8B', fg='white',font=('verdana', 12, 'bold'))
        self.lbCodProduto.place(relx=0.02, rely=0.01)
        self.entryCodProduto = Entry(self.frame3, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryCodProduto.place(relx=0.02, rely=0.18, relwidth=0.5, relheight=0.18)
        


        self.lbQuantidade = Label(self.frame3, text='QUANTIDADE', bg='#008B8B', fg='white',font=('verdana', 12, 'bold'))
        self.lbQuantidade.place(relx=0.02, rely=0.75)
        self.entryQuantidade = Entry(self.frame3, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryQuantidade.place(relx=0.4, rely=0.75, relwidth=0.4, relheight=0.18)

        self.btOk = Button(self.frame3,text='OK', font=('verdana', 10, 'bold'),command = self.contas)
        self.btOk.place(relx=0.85,rely=0.75,relwidth=0.15,relheight=0.18)

    def widgetsFrame4(self):
        self.lbSubTotal = Label(self.frame4, text='SUBTOTAL', bg='#008B8B',fg = 'white', font=('verdana', 14, 'bold'))
        self.lbSubTotal.place(relx=0.02, rely=0.1)
        self.lbValorSubTotal = Label(self.frame4, text=f'R$ 00,00', bg='#008B8B',fg = 'white', font=('verdana', 14, 'bold'))
        self.lbValorSubTotal.place(relx=0.6, rely=0.1)

    def widgetsFrame5(self):
        self.lbTotal = Label(self.frame5, text='TOTAL', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbTotal.place(relx=0.02, rely=0.1)
        self.lbValorTotal = Label(self.frame5, text=f'R$ 00,00', bg='#008B8B', fg='white',font=('verdana', 14, 'bold'))
        self.lbValorTotal.place(relx=0.6, rely=0.1)

    def widgetsFrame6(self):
        self.lbDinheiro = Label(self.frame6, text='DINHEIRO', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbDinheiro.place(relx=0.02, rely=0.1)
        self.entryDinheiro = Entry(self.frame6, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryDinheiro.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.7)

    def widgetsFrame7(self):
        self.lbTroco = Label(self.frame7, text='TROCO', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbTroco.place(relx=0.02, rely=0.1)
        self.lbValorTroco = Label(self.frame7, text=f'R$ 00,00', bg='#008B8B', fg='#FF4500',font=('verdana', 14, 'bold'))
        self.lbValorTroco.place(relx=0.6, rely=0.1)

    def cadCliente(self):
        self.root2 = Toplevel()
        self.root2.title('GERENCIAMENTO DE CLIENTES')
        self.root2.configure(background='#40E0D0')
        self.root2.geometry('1000x650')
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

        self.framePri = Frame(self.root2, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.framePri.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.08)

        self.frameQua = Frame(self.root2, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frameQua.place(relx=0.02, rely=0.12, relwidth=0.80, relheight=0.34)
        self.tabela3 = ttk.Treeview(self.frameQua, height=100,
                                    columns=('nome', 'convenio', 'email', 'informacoes',),
                                    show='headings')

        self.tabela3.column('nome', width=150)
        self.tabela3.column('convenio', width=50)
        self.tabela3.column('email', width=150)
        self.tabela3.column('informacoes', width=50)

        self.tabela3.heading('nome', text='NOME', anchor='w')
        self.tabela3.heading('convenio', text='CONVENIO', anchor='w')
        self.tabela3.heading('email', text='EMAIL', anchor='w')
        self.tabela3.heading('informacoes', text='INFORMAÇÕES', anchor='w')

        self.tabela3.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        self.frameSeg = Frame(self.root2, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frameSeg.place(relx=0.02, rely=0.48, relwidth=0.96, relheight=0.28)

        self.frameTer = Frame(self.root2, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frameTer.place(relx=0.02, rely=0.78, relwidth=0.66, relheight=0.2)

        self.lbNomeCli = Label(self.framePri, text='NOME', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbNomeCli.place(relx=0.02, rely=0.1)
        self.entryNomeCli = Entry(self.framePri, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryNomeCli.place(relx=0.1, rely=0.18, relwidth=0.5, relheight=0.7)

        self.lbCpfCli = Label(self.framePri, text='CPF', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbCpfCli.place(relx=0.63, rely=0.1)
        self.entryCpfCli = Entry(self.framePri, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryCpfCli.place(relx=0.7, rely=0.18, relwidth=0.28, relheight=0.7)

        self.lbRgCli = Label(self.frameSeg, text='RG', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbRgCli.place(relx=0.01, rely=0.02)
        self.entryRgCli = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryRgCli.place(relx=0.01, rely=0.18, relwidth=0.18, relheight=0.15)

        self.vSexo = StringVar()

        self.lbSexo = Label(self.frameSeg, text='SEXO', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbSexo.place(relx=0.21, rely=0.02)
        self.radioMasculino = Radiobutton(self.frameSeg, text='MASCULINO', bg='#008B8B', value='MASCULINO',
                                          variable=self.vSexo)
        self.radioMasculino.place(relx=0.21, rely=0.18)
        self.radioFeminino = Radiobutton(self.frameSeg, text='FEMININO', bg='#008B8B', value='FEMININO',
                                         variable=self.vSexo)
        self.radioFeminino.place(relx=0.31, rely=0.18)

        self.lbDataNaCli = Label(self.frameSeg, text='DATA DE NASCIMENTO', bg='#008B8B', fg='white',
                                 font=('verdana', 14, 'bold'))
        self.lbDataNaCli.place(relx=0.41, rely=0.02)
        self.entryDataNa = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryDataNa.place(relx=0.41, rely=0.18, relwidth=0.18, relheight=0.15)

        self.lbConvenio = Label(self.frameSeg, text='CONVENIO', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbConvenio.place(relx=0.69, rely=0.02)
        self.entryConvenio = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryConvenio.place(relx=0.69, rely=0.18, relwidth=0.18, relheight=0.15)

        self.lbEndereco = Label(self.frameSeg, text='ENDEREÇO', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbEndereco.place(relx=0.01, rely=0.325)
        self.entryEndereco = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryEndereco.place(relx=0.01, rely=0.485, relwidth=0.28, relheight=0.15)

        self.lbNum = Label(self.frameSeg, text='N°', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbNum.place(relx=0.3, rely=0.325)
        self.entryNum = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryNum.place(relx=0.3, rely=0.485, relwidth=0.06, relheight=0.15)

        self.lbComp = Label(self.frameSeg, text='COMP.', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbComp.place(relx=0.37, rely=0.325)
        self.entryComp = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryComp.place(relx=0.37, rely=0.485, relwidth=0.08, relheight=0.15)

        self.lbCep = Label(self.frameSeg, text='CEP', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbCep.place(relx=0.46, rely=0.325)
        self.entryCep = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryCep.place(relx=0.46, rely=0.485, relwidth=0.11, relheight=0.15)

        self.lbBairro = Label(self.frameSeg, text='BAIRRO', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbBairro.place(relx=0.58, rely=0.325)
        self.entryBairro = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryBairro.place(relx=0.58, rely=0.485, relwidth=0.14, relheight=0.15)

        self.lbUf = Label(self.frameSeg, text='UF', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbUf.place(relx=0.73, rely=0.325)
        self.entryUf = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryUf.place(relx=0.73, rely=0.485, relwidth=0.04, relheight=0.15)

        self.lbMunicipio = Label(self.frameSeg, text='MUNICIPIO', bg='#008B8B', fg='white',
                                 font=('verdana', 14, 'bold'))
        self.lbMunicipio.place(relx=0.79, rely=0.325)
        self.entryMunicipio = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryMunicipio.place(relx=0.79, rely=0.485, relwidth=0.14, relheight=0.15)

        self.lbEmail = Label(self.frameSeg, text='E-MAIL', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbEmail.place(relx=0.01, rely=0.645)
        self.entryEmail = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryEmail.place(relx=0.01, rely=0.805, relwidth=0.28, relheight=0.15)

        self.lbCelular = Label(self.frameSeg, text='CELULAR', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbCelular.place(relx=0.3, rely=0.645)
        self.entryDdd = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryDdd.place(relx=0.3, rely=0.805, relwidth=0.04, relheight=0.15)
        self.entryNume = Entry(self.frameSeg, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryNume.place(relx=0.345, rely=0.805, relwidth=0.2, relheight=0.15)

        self.vdesc = StringVar()
        self.lbDesconto = Label(self.frameSeg, text='SUA IDADE, SEU DESCONTO?', bg='#008B8B', fg='white',
                                font=('verdana', 14, 'bold'))
        self.lbDesconto.place(relx=0.6, rely=0.645, )
        self.radioSim = Radiobutton(self.frameSeg, text='SIM', bg='#008B8B', value='S', variable=self.vdesc)
        self.radioSim.place(relx=0.6, rely=0.805)
        self.radioNao = Radiobutton(self.frameSeg, text='NÃO', bg='#008B8B', value='N', variable=self.vdesc)
        self.radioNao.place(relx=0.68, rely=0.805)

        self.lbInfo = Label(self.frameTer, text='INFORMAÇOES GERAIS', bg='#008B8B', fg='white',
                            font=('verdana', 14, 'bold'))
        self.lbInfo.place(relx=0.01, rely=0.01)

        self.txtInfo = Text(self.frameTer, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.txtInfo.place(relx=0.01, rely=0.25, relwidth=0.6, relheight=0.7)

        self.btConsultar = Button(self.root2, text='CONSULTAR', font=('verdana', 10, 'bold'),
                                  command=self.consultaCliente)
        self.btConsultar.place(relx=0.88, rely=0.12, relwidth=0.1, relheight=0.08)

        # self.btLimpaCampo = Button(self.root2, text='LIMPAR CAMPOS', font=('verdana', 10, 'bold'))
        # self.btLimpaCampo.place(relx=0.84, rely=0.1, relwidth=0.14, relheight=0.08)

        self.btGravar = Button(self.root2, text='GRAVAR', font=('verdana', 10, 'bold'), command=self.cadastrar_cliente)
        self.btGravar.place(relx=0.76, rely=0.90, relwidth=0.1, relheight=0.08)

        self.btExcluir = Button(self.root2, text='EXCLUIR', font=('verdana', 10, 'bold'))
        self.btExcluir.place(relx=0.88, rely=0.90, relwidth=0.1, relheight=0.08)

        # self.lbLogo = Label(self.root2, image=self.imgLogo)
        # self.lbLogo.place(relx=0.02, rely=0.02, relwidth=0.1, relheight=0.1)


    def telaEstoque(self):
        self.root3 = Toplevel()
        self.root3.title('ESTOQUE')
        self.root3.configure(background='#40E0D0')
        self.root3.geometry('1000x650')
        self.root3.resizable(False, False)
        self.root3.transient(self.root)
        self.root3.focus_force()
        self.root3.grab_set()

        self.lbLogo = Label(self.root3, image=self.imgLogo)
        self.lbLogo.place(relx=0.02, rely=0.01, relwidth=0.4, relheight=0.15)

        self.framePri = Frame(self.root3, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.framePri.place(relx=0.02, rely=0.15, relwidth=0.96, relheight=0.15)

        self.frameSeg = Frame(self.root3, bd=4, bg='#008B8B', highlightbackground='#696969', highlightthickness=3)
        self.frameSeg.place(relx=0.02, rely=0.35, relwidth=0.96, relheight=0.4)



        self.lbCod = Label(self.framePri, text='CÓD.', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbCod.place(relx=0.01, rely=0.02)
        self.entryCod2 = Entry(self.framePri, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryCod2.place(relx=0.07, rely=0.04, relwidth=0.15, relheight=0.26)

        self.lbNomePro = Label(self.framePri, text='NOME', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbNomePro.place(relx=0.23, rely=0.02)
        self.entryNomePro = Entry(self.framePri, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryNomePro.place(relx=0.31, rely=0.04, relwidth=0.35, relheight=0.26)

        self.lbFornecedor = Label(self.framePri, text='FORNECEDOR', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbFornecedor.place(relx=0.67, rely=0.02)
        self.entryFornecedor = Entry(self.framePri, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryFornecedor.place(relx=0.84, rely=0.04, relwidth=0.16, relheight=0.26)

        self.lbQtd2 = Label(self.framePri, text='QTDE.', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbQtd2.place(relx=0.01, rely=0.55)
        self.entryQtd2 = Entry(self.framePri, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryQtd2.place(relx=0.09, rely=0.55, relwidth=0.06, relheight=0.26)

        self.lbValor2 = Label(self.framePri, text='VALOR', bg='#008B8B', fg='white', font=('verdana', 14, 'bold'))
        self.lbValor2.place(relx=0.16, rely=0.55)
        self.entryValor2 = Entry(self.framePri, font=('verdana', 10, 'bold'), fg='#FF4500')
        self.entryValor2.place(relx=0.25, rely=0.55, relwidth=0.07, relheight=0.26)

        self.tabela2 = ttk.Treeview(self.frameSeg, height=100,
                                    columns=('codigo', 'nome', 'fornecedor', 'qtd', 'valor',),
                                    show='headings')

        self.tabela2.column('codigo', width=30)
        self.tabela2.column('nome', width=150)
        self.tabela2.column('fornecedor', width=150)
        self.tabela2.column('qtd', width=50)
        self.tabela2.column('valor', width=70)

        self.tabela2.heading('codigo', text='CÓDIGO', anchor='w')
        self.tabela2.heading('nome', text='NOME', anchor='w')
        self.tabela2.heading('fornecedor', text='FORNECEDOR', anchor='w')
        self.tabela2.heading('qtd', text='QNTD', anchor='w')
        self.tabela2.heading('valor', text='PREÇO', anchor='w')

        self.tabela2.place(relx=0.01, rely=0.01, relwidth=0.8, relheight=0.95)

        self.tabela2.bind('<Double-1>',self.clickDuplo)
        self.selectTabela()



        self.btAdicionar = Button(self.framePri, text='ADICIONAR', font=('verdana', 10, 'bold'), command = self.adicionarProdutos)
        self.btAdicionar.place(relx=0.84, rely=0.55, relwidth=0.14, relheight=0.35)



        self.btConsultar2 = Button(self.frameSeg, text='CONSULTAR', font=('verdana', 10, 'bold'))
        self.btConsultar2.place(relx=0.84, rely=0.01, relwidth=0.14, relheight=0.2)

        self.btExcluir2 = Button(self.frameSeg, text='EXCLUIR', font=('verdana', 10, 'bold'),command = self.deletaProdutos)
        self.btExcluir2.place(relx=0.84, rely=0.3, relwidth=0.14, relheight=0.2)

        self.btLimparTelaEs = Button(self.root3, text='LIMPAR TELA', font=('verdana', 10, 'bold'),command=self.limparTelaEstoque)
        self.btLimparTelaEs.place(relx=0.82, rely=0.8, relwidth=0.14, relheight=0.07)



Venda()