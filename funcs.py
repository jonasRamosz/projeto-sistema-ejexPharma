from tkinter import *
from tkinter import ttk

class Funcs():

    def limparTelaEstoque(self):
        self.entryCod2.delete(0, END)
        self.entryNomePro.delete(0, END)
        self.entryFornecedor.delete(0, END)
        self.entryQtd2.delete(0, END)
        self.entryValor2.delete(0, END)

    def limparTelaClientes(self):
        self.entryNomeCli.delete(0, END),
        self.entryCpfCli.delete(0, END),
        self.entryRgCli.delete(0, END),
        self.vSexo.set(''),
        self.entryDataNa.delete(0, END)
        self.entryConvenio.delete(0, END),
        self.entryEndereco.delete(0, END),
        self.entryNum.delete(0, END),
        self.entryComp.delete(0, END),
        self.entryCep.delete(0, END),
        self.entryBairro.delete(0, END),
        self.entryUf.delete(0, END),
        self.entryMunicipio.delete(0, END),
        self.entryEmail.delete(0, END),
        self.entryDdd.delete(0, END),
        self.entryNume.delete(0, END),
        self.vdesc.set(''),
        self.txtInfo.delete('1.0', END)









