from modules.mysql import MySQL
from modules.aluno import Aluno

import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QFormLayout,
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
        self.form_layout = QFormLayout()

        self.banco = MySQL()
        self.campos = {}

        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):
        self.janela.setWindowTitle("Cadastro Aluno")
        self.janela.resize(600, 400)

        self.janela.setLayout(self.layout)

        # Estilo visual
        self.janela.setStyleSheet("""
            QWidget {
                background-color: #f4f6f9;
                font-size: 14px;
            }

            QLabel {
                font-weight: bold;
                color: #333;
            }

            QLineEdit {
                padding: 6px;
                border-radius: 6px;
                border: 1px solid #ccc;
                background-color: white;
            }

            QLineEdit:focus {
                border: 1px solid #0078d7;
            }

            QPushButton {
                background-color: #0078d7;
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #005fa3;
            }
        """)

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

            self.form_layout.addRow(label, campo)

            self.campos[chave] = campo

        self.layout.addLayout(self.form_layout)

        botao_cadastro = QPushButton("Cadastrar")
        botao_cadastro.setFixedHeight(40)

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
                "Sucesso",
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