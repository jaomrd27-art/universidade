from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QApplication
)

from screen.cadastrar import Cadastrar
from screen.listar import Listar

import sys

class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.janela = QWidget()
        self.layout = QVBoxLayout()

        self.janela.setWindowTitle("🎓 Sistema Universidade")
        self.janela.resize(450, 350)
        self.janela.setLayout(self.layout)

        # Fundo escuro suave
        self.janela.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #1e3a8a, stop:1 #1e40af);
            }
        """)

        self.criar_botoes()
        self.janela.show()

    def criar_botoes(self):
        botao_listar = QPushButton("📋 Listar Alunos")   
        botao_listar.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #10b981, stop:1 #059669);
                color: white;
                border: none;
                padding: 20px 40px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 15px;
                margin: 20px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #34d399, stop:1 #10b981);
            }
            QPushButton:pressed {
                background: #059669;
            }
        """)
        self.layout.addWidget(botao_listar)
        botao_listar.clicked.connect(self.abrir_listagem)

        botao_cadastrar = QPushButton("➕ Cadastrar Aluno")
        botao_cadastrar.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #f59e0b, stop:1 #d97706);
                color: white;
                border: none;
                padding: 20px 40px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 15px;
                margin: 20px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #fbbf24, stop:1 #f59e0b);
            }
            QPushButton:pressed {
                background: #d97706;
            }
        """)
        self.layout.addWidget(botao_cadastrar)
        botao_cadastrar.clicked.connect(self.abrir_cadastro)

    def abrir_listagem(self):
        self.tela_listagem = Listar(self.app)     
        self.tela_listagem.janela.show()

    def abrir_cadastro(self):
        self.tela_cadastro = Cadastrar(self.app) 
        self.tela_cadastro.janela.show()   

if __name__ == "__main__":
    system = App()
    sys.exit(system.app.exec())