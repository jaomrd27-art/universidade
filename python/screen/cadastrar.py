from modules.mysql import MySQL
from modules.aluno import Aluno

import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

class Cadastrar():
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.campos = {}

        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):
        self.janela.setWindowTitle("Cadastro Aluno")
        # Adaptar redimensionamentar para tamanho dinamico 
        self.janela.resize(1200, 600)
        self.janela.setLayout(self.layout)

    def criar_componentes(self):
        componentes = {
            "nome": "Digite seu nome:",
            "email": "Digite seu email:",
            "cpf": "Digite seu cpf:",
            "telefone": "Digite seu telefone:",
            "endereço": "Digite seu endereço:"
        }    

        for chave, valor in componentes.items():
            label = QLabel(valor)
            campo = QLineEdit()

            self.layout.addWidget(label)
            self.layout.addWidget(campo)

            self.campos[chave] = campo    

        botao_cadastro = QPushButton("Cadastrar")
        self.layout.addWidget(botao_cadastro)   

        botao_cadastro.clicked.connect(self.cadastrar)

    def cadastrar(self):
        aluno = Aluno(
            self.campos["nome"].text(), 
            self.campos["email"].text(),
            self.campos["cpf"].text(),
            self.campos["telefone"].text(),
            self.campos["endereço"].text()
        )  

        try:
            self.banco.connect()
            aluno.cadastrar(self.banco)
            QMessageBox.information(
                self.janela,
                "Sucesso"
                "Aluno Cadastrado!"
            )
            self.limpar_campos()

        except Exception as e:
            QMessageBox.critical(
                self.janela,
                "Erro",
                f"Erro ao Cadastrar: {e}"
            ) 
        finally:
                self.banco.disconnect() 

    def limpar_campos(self):
        for campo in self.campos.values(): 
            campo.clear()

