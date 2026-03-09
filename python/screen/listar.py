from modules.mysql import MySQL
from modules.aluno import Aluno

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem
)

class Listar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.configurar_janela()
        self.criar_componentes()
        self.carregar_dados()

    def configurar_janela(self):
        self.janela.setWindowTitle("Listagem de Alunos")

        screen = self.app.primaryScreen().geometry()
        largura = int(screen.width() * 0.8)
        altura = int(screen.height() * 0.8)

        self.janela.resize(largura, altura)
        self.janela.setLayout(self.layout)
        
        # Fundo moderno
        self.janela.setStyleSheet("""
            QWidget {
                background: lineargradient(x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #667eea, stop:1 #764ba2);
            }
        """)

    def criar_componentes(self):

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(
            ["ID", "Nome", "Email", "CPF", "Telefone","Matricula"]
        )
        
        # Estilo da tabela
        self.tabela.setStyleSheet("""
            QTableWidget { 
                background-color: white; 
                gridline-color: #e0e0e0;
                alternate-background-color: #f5f5f5;
                selection-background-color: #4fc3f7;
                border: 1px solid #ccc;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QHeaderView::section {
                background-color: #42a5f5;
                color: white;
                padding: 10px;
                border: none;
                font-weight: bold;
            }
        """)
        
        self.tabela.setAlternatingRowColors(True)
        self.layout.addWidget(self.tabela)

        botao_atualizar = QPushButton("🔄 Atualizar")
        botao_atualizar.setStyleSheet("""
            QPushButton {
                background-color: #26c6da;
                color: white;
                border: none;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #00acc1;
            }
            QPushButton:pressed {
                background-color: #00838f;
            }
        """)
        
        self.layout.addWidget(botao_atualizar)
        botao_atualizar.clicked.connect(self.carregar_dados)

    def carregar_dados(self):

        self.banco.connect()
        alunos = Aluno.listar(self.banco)
        self.banco.disconnect()

        self.tabela.setRowCount(len(alunos))

        for linha, aluno in enumerate(alunos):
            self.tabela.setItem(linha, 0, QTableWidgetItem(str(aluno["id"])))
            self.tabela.setItem(linha, 1, QTableWidgetItem(aluno["nome"]))
            self.tabela.setItem(linha, 2, QTableWidgetItem(aluno["email"]))
            self.tabela.setItem(linha, 3, QTableWidgetItem(aluno["cpf"]))
            self.tabela.setItem(linha, 4, QTableWidgetItem(aluno["telefone"]))
            if aluno["matricula"] == True:
                self.tabela.setItem(linha, 5, QTableWidgetItem("✅ Sim"))
            else:
                self.tabela.setItem(linha, 5, QTableWidgetItem("❌ Não"))
