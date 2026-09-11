#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gi
from modelo import Conta

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

pasta = os.path.dirname(os.path.abspath(__file__))
gladeLeon = os.path.join(pasta, 'view.glade')

class App:
    def __init__(self):
        self.constructor = constr = Gtk.Builder()
        constr.add_from_file(gladeLeon)
        constr.connect_signals(self)
        self.janela = constr.get_object("jan_principal")
        self.txtPessoa = constr.get_object("txt_pessoa")
        self.txtConsumo = constr.get_object("txt_consumo")
        self.btnNovaConta = constr.get_object("btn_pessoa")
        self.btnAdicionar = constr.get_object("btn_adicionar")
        self.lblLista = constr.get_object("lbl_lista")
        self.lblResultado = constr.get_object("lbl_resultado")
        self.lblRodape = constr.get_object("lbl_rodape")

        self.janela.show_all()
        self.conta = Conta()

    def atualizar(self):
        lista = self.conta.listar()
        aEscrever = ""
        for pessoa in lista:
            aEscrever += pessoa[0] + " - R$" + pessoa[1].format(":.2f") + "\n"
        self.lblLista.set_text(aEscrever)

        if self.conta.total() == 0:
            self.lblResultado.set_text("Nenhuma pessoa adicionada à conta")
        else:
            resultados = f"Subtotal: RS${self.conta.subtotal():.2f}\n"
            resultados +=f"Serviço: RS${self.conta.valor_servico():.2f}\n"
            resultados +=f"Total: RS${self.conta.total():.2f}\n"
            resultados +=f"Cada um paga: RS${self.conta.por_pessoa():.2f}\n"
            self.lblResultado.set_text(resultados)

        self.lblRodape.set_text(f"{self.conta.total_pessoas()} coisa(s) na conta")

    def ao_nova_conta(self,comp=None,arg=None):
        self.conta.esvaziar_conta()
        self.atualizar()

    def ao_adicionar(self,comp=None,arg=None):
        self.conta.adicionar(self.txtPessoa.get_text(), self.txtConsumo.get_text())
        self.atualizar()

    def ao_destruir(self,comp=None,arg=None):
        pass

App()
Gtk.main()
