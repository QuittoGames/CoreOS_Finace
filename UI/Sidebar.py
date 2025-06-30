from data import data
from tool import tool
import asyncio
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from decimal import Decimal
from modules.User import User
from UI.UI import UI
from time import sleep    

class SideBar(QFrame):
    def __init__(self, parent,UI_local:UI):
        super().__init__(parent)
        self.setFixedWidth(250)
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {UI_local.getColors()["black_third"]};
                border: none;
                border-radius: 5px;
            }}
            QPushButton {{
                background-color: transparent;
                color: white;
                border: none;
                padding: 12px 16px;
                text-align: left;
                font-size: 14px;
                border-radius: 5px;
                margin: 2px;
            }}
            QPushButton:hover {{
                background-color: rgba(255, 255, 255, 0.1);
            }}
            QPushButton:pressed {{
                background-color: rgba(255, 255, 255, 0.2);
            }}
        """)
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Logo área
        logo_frame = QFrame()
        logo_frame.setFixedHeight(60)
        logo_layout = QHBoxLayout(logo_frame)
        logo_layout.setContentsMargins(16, 12, 16, 12)
        
        # Logo placeholder (você pode substituir por uma imagem real)
        logo_label = QLabel("") # Icon App
        logo_label.setFixedSize(32, 32)
        logo_label.setStyleSheet("font-size: 24px; color: #0655FF;")
        logo_label.setAlignment(Qt.AlignCenter)
        
        app_name = QLabel("Core OS Finance")
        app_name.setStyleSheet("""
            color: white;
            font-weight: bold;
            font-size: 16px;
            padding: 4px 8px;
            border-radius: 4px;
            transition: background 0.3s ease;
        """)
        app_name.setAttribute(Qt.WA_Hover)

        # Para hover, você pode fazer assim:
        app_name.setStyleSheet("""
        QLabel {
            color: white;
            font-weight: bold;
            font-size: 16px;
            padding: 4px 8px;
            border-radius: 2px;
        }
        QLabel:hover {
            background: qlineargradient(
                x1: 0, y1: 1,
                x2: 0, y2: 0,
                stop: 0 rgba(6, 85, 255, 255),   /* azul totalmente opaco */
                stop: 1 rgba(6, 85, 255, 0)      /* azul totalmente transparente */
            );
        }
    """)
        logo_layout.addWidget(logo_label)
        logo_layout.addWidget(app_name)
        logo_layout.addStretch()
        
        layout.addWidget(logo_frame)
        
        # Linha separadora
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("background-color: rgba(255, 255, 255, 0.1); height: 1px;")
        layout.addWidget(separator)
        
        # Menu buttons
        menu_frame = QFrame()
        menu_layout = QVBoxLayout(menu_frame)
        menu_layout.setContentsMargins(8, 16, 8, 16)
        menu_layout.setSpacing(4)
        
        # Botões do menu
        buttons = [
            ("🏠", "Dashboard"),
            ("💰", "Transações"),
            ("📈", "Investimentos"),
            ("📊", "Relatórios"),
            ("⚙️", "Configurações")
        ]
        
        for icon, text in buttons:
            btn = QPushButton(f"{icon}  {text}")
            btn.setFixedHeight(40)
            menu_layout.addWidget(btn)
        
        layout.addWidget(menu_frame)
        layout.addStretch()