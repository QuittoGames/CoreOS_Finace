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
                border-radius: 5px;
            }}
        """)

        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Top bar com saudação e saldo
        top_bar = self.create_top_bar()
        layout.addWidget(top_bar)
        
        # Widgets principais
        widgets_area = self.create_widgets_area()
        layout.addWidget(widgets_area)
        
        layout.addStretch()
    
    def create_top_bar(self):
        top_bar = QFrame()
        top_layout = QVBoxLayout(top_bar)
        top_layout.setSpacing(5)
        top_layout.setContentsMargins(0, 0, 0, 0)
        
        welcome_title = QLabel(f"Bem Vindo, {self.user.name}")
        welcome_title.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        top_layout.addWidget(welcome_title)
        
        saldo_show = QLabel(f"Saldo: {self.user.getSaldo(self.data_local)}")
        saldo_show.setStyleSheet("color: #888; font-size: 16px;")
        top_layout.addWidget(saldo_show)
        
        return top_bar
    
    def create_widgets_area(self):
        widgets_frame = QFrame()
        widgets_layout = QVBoxLayout(widgets_frame)
        widgets_layout.setSpacing(20)
        widgets_layout.setContentsMargins(0, 0, 0, 0)
        
        # Primeira linha - Widget de lucro
        first_row = QHBoxLayout()
        
        # Widget de lucro
        lucro_widget = self.create_lucro_widget()
        first_row.addWidget(lucro_widget)
        first_row.addStretch()
        
        widgets_layout.addLayout(first_row)
        
        # Segunda linha - Widgets grandes
        second_row = QHBoxLayout()
        second_row.setSpacing(20)
        
        # Widget esquerdo - Gráfico/Resumo
        left_widget = self.create_summary_widget()
        second_row.addWidget(left_widget)
        
        # Widget direito - Transações recentes
        right_widget = self.create_transactions_widget()
        second_row.addWidget(right_widget)
        
        widgets_layout.addLayout(second_row)
        
        # Terceira linha - Widget de extrato
        extrato_widget = self.create_extrato_widget()
        widgets_layout.addWidget(extrato_widget)
        
        return widgets_frame
    
    def create_lucro_widget(self):
        lucro_widget = QFrame()
        lucro_widget.setFixedSize(220, 65)
        lucro_widget.setStyleSheet("""
            QFrame {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 1, y2: 0,
                    stop: 0 #0655FF,
                    stop: 1 #1438E9
                );
                border-radius: 8px;
            }
            QLabel {
                color: white;
                background-color: transparent;
            }
        """)
        
        layout = QVBoxLayout(lucro_widget)
        layout.setContentsMargins(16, 12, 16, 12)
        
        lucro_label = QLabel(f"Lucro: R${self.user.lucro}")
        lucro_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(lucro_label)
        
        return lucro_widget
    
    def create_summary_widget(self):
        widget = QFrame()
        widget.setFixedSize(350, 250)
        widget.setStyleSheet(f"""
            QFrame {{
                background-color: {self.UI_local.getColors()["black_second"]};
                border-radius: 8px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            QLabel {{
                color: white;
                background-color: s;
            }}
        """)
        
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(20, 20, 20, 20)
        
        title = QLabel("Resumo Financeiro")
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)
        
        # Adicionar mais conteúdo aqui (gráficos, estatísticas, etc.)
        content = QLabel("Gráfico de evolução\nPatrimônio mensal\nMetas de investimento")
        content.setStyleSheet("color: #888; line-height: 1.5;")
        layout.addWidget(content)
        
        layout.addStretch()
        
        return widget
    
    def create_transactions_widget(self):
        widget = QFrame()
        widget.setFixedSize(350, 250)
        widget.setStyleSheet(f"""
            QFrame {{
                background-color: {self.UI_local.getColors()["black_second"]};
                border-radius: 8px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            QLabel {{
                color: white;
                background-color: transparent;
            }}
        """)
        
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(20, 20, 20, 20)
        
        title = QLabel("Transações Recentes")
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)
        
        # Lista de transações (exemplo)
        transactions_list = QScrollArea()
        transactions_list.setStyleSheet("border: none; background-color: transparent;")
        transactions_widget = QWidget()
        transactions_layout = QVBoxLayout(transactions_widget)
        
        # Adicionar algumas transações de exemplo
        for i in range(3):
            trans_item = QFrame()
            trans_item.setStyleSheet("background-color: rgba(255, 255, 255, 0.05); border-radius: 4px; padding: 8px; margin: 2px;")
            trans_layout = QHBoxLayout(trans_item)
            
            trans_label = QLabel(f"Transação {i+1}")
            trans_label.setStyleSheet("color: white; font-size: 12px;")
            value_label = QLabel(f"R$ {100 * (i+1)}")
            value_label.setStyleSheet("color: #0655FF; font-size: 12px; font-weight: bold;")
            
            trans_layout.addWidget(trans_label)
            trans_layout.addStretch()
            trans_layout.addWidget(value_label)
            
            transactions_layout.addWidget(trans_item)
        
        transactions_list.setWidget(transactions_widget)
        layout.addWidget(transactions_list)
        
        return widget
    
    def create_extrato_widget(self):
        widget = QFrame()
        widget.setFixedHeight(150)
        widget.setStyleSheet(f"""
            QFrame {{
                background-color: {self.UI_local.getColors()["black_second"]};
                border-radius: 8px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            QLabel {{
                color: white;
                background-color: transparent;
            }}
        """)
        
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(20, 20, 20, 20)
        
        title = QLabel("Extrato Completo")
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)
        
        extrato_info = QLabel(f"Total de transações: {len(self.user.extrato)}")
        extrato_info.setStyleSheet("color: #888;")
        layout.addWidget(extrato_info)
        
        layout.addStretch()
        
        return widget
