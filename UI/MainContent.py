from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from UI.UI import UI
from modules.User import User
from data import data

class MainContent(QFrame):
    def __init__(self, parent, UI_local: UI, user: User, data_local: data):
        super().__init__(parent)
        self.UI_local = UI_local
        self.user = user
        self.data_local = data_local

        self.setStyleSheet(f"""
            QFrame {{
                background-color: {self.UI_local.getColors()["black"]};
                border: none;
            }}
        """)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)

        layout.addWidget(self.create_top_bar())
        layout.addLayout(self.create_widget_rows())
        layout.addStretch()

    def create_top_bar(self):
        top = QFrame()
        lyt = QVBoxLayout(top)
        lyt.setSpacing(6)

        welcome = QLabel(f"Bem-vindo, {self.user.name}")
        welcome.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        lyt.addWidget(welcome)

        saldo = QLabel(f"Saldo: R$ {self.user.getSaldo(self.data_local)}")
        saldo.setStyleSheet("color: #888888; font-size: 16px;")
        lyt.addWidget(saldo)

        return top

    def create_widget_rows(self):
        layout = QVBoxLayout()

        row1 = QHBoxLayout()
        row1.addWidget(self.create_card("Lucro", f"R$ {self.user.lucro}", gradient=True))
        row1.addStretch()

        row2 = QHBoxLayout()
        row2.addWidget(self.create_info_box("Resumo Financeiro", "Gráficos\nMetas\nEvolução"))
        row2.addWidget(self.create_info_box("Transações Recentes", "Compra X\nVenda Y\nPIX Z"))
        
        row3 = QHBoxLayout()
        row3.addWidget(self.create_info_box("Extrato Completo", f"{len(self.user.extrato)} transações registradas"))

        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addLayout(row3)

        return layout

    def create_card(self, title, value, gradient=False):
        card = QFrame()
        card.setFixedSize(240, 70)
        card.setStyleSheet(f"""
            QFrame {{
                background: {'qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0655FF, stop:1 #1438E9)' if gradient else self.UI_local.getColors()['black_second']};
                border-radius: 10px;
            }}
            QLabel {{
                color: white;
                background: transparent;
            }}
        """)
        layout = QVBoxLayout(card)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.addWidget(QLabel(title))
        val = QLabel(value)
        val.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(val)
        return card

    def create_info_box(self, title, content):
        box = QFrame()
        box.setMinimumSize(300, 200)
        box.setStyleSheet(f"""
            QFrame {{
                background-color: {self.UI_local.getColors()["black_second"]};
                border-radius: 10px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            QLabel {{
                color: white;
                background-color: transparent;
            }}
        """)
        layout = QVBoxLayout(box)
        layout.setContentsMargins(20, 20, 20, 20)

        title_lbl = QLabel(title)
        title_lbl.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 8px;")
        layout.addWidget(title_lbl)

        content_lbl = QLabel(content)
        content_lbl.setStyleSheet("color: #999999;")
        layout.addWidget(content_lbl)
        layout.addStretch()
        return box
