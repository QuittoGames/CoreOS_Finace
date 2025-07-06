from PySide6.QtWidgets import *
from PySide6.QtWidgets import QGraphicsOpacityEffect, QPushButton, QFrame, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer

from UI.UI import UI


class SideBar(QFrame):
    def __init__(self, parent, UI_local: UI):
        super().__init__(parent)
        self.UI_local = UI_local
        self.expanded = True
        self.animating = False

        self.setMinimumWidth(60)
        self.setMaximumWidth(260)
        self.setObjectName("Sidebar")
        self.setStyleSheet(f"""
            QFrame#Sidebar {{
                background-color: {UI_local.getColors()["black_third"]};
                border: none;
            }}
            QPushButton {{
                background-color: transparent;
                color: white;
                border: none;
                padding: 12px 16px;
                font-size: 14px;
                text-align: left;
                border-radius: 6px;
            }}
            QPushButton:hover {{
                background-color: rgba(255, 255, 255, 0.08);
            }}
            QPushButton:pressed {{
                background-color: rgba(255, 255, 255, 0.12);
            }}
        """)
        self.animations = []
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # Toggle button
        self.toggle_btn = QPushButton("☰")
        self.toggle_btn.setFixedHeight(40)
        self.toggle_btn.setStyleSheet("font-size: 18px; color: white; padding: 8px 12px;")
        self.toggle_btn.clicked.connect(self.toggle)
        self.layout.addWidget(self.toggle_btn)

        # Logo
        self.logo = QLabel("Core OS")
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setFont(QFont("Segoe UI", 18, QFont.Bold))
        self.logo.setStyleSheet("color: white; padding: 20px;")
        self.logo_opacity = QGraphicsOpacityEffect(self.logo)
        self.logo.setGraphicsEffect(self.logo_opacity)
        self.layout.addWidget(self.logo)

        # Separator
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet("background-color: rgba(255,255,255,0.1); height: 1px;")
        self.layout.addWidget(sep)

        # Botões do menu
        self.menu_buttons = []
        self.button_data = [
            ("", "Dashboard"),
            ("", "Transações"),
            ("", "Investimentos"),
            ("", "Relatórios"),
            ("", "Configurações")
        ]
        for icon, text in self.button_data:
            btn = QPushButton(f"{icon}  {text}")
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

            opacity = QGraphicsOpacityEffect(btn)
            btn.setGraphicsEffect(opacity)

            self.layout.addWidget(btn)
            self.menu_buttons.append((btn, icon, text, opacity))

        self.layout.addStretch()

    def toggle(self):
        if self.animating:
            return
        self.animating = True

        target_width = 260 if not self.expanded else 60

        self.anim = QPropertyAnimation(self, b"minimumWidth")
        self.anim.setDuration(300)
        self.anim.setStartValue(self.width())
        self.anim.setEndValue(target_width)
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.start()

        logo_anim = QPropertyAnimation(self.logo_opacity, b"opacity")
        logo_anim.setDuration(200)
        logo_anim.setStartValue(1 if self.expanded else 0)
        logo_anim.setEndValue(0 if self.expanded else 1)
        logo_anim.start()

        self.animations = []
        for i, (btn, icon, text, effect) in enumerate(self.menu_buttons):
            delay = i * 50  # delay de 50ms entre cada fade para efeito cascata
            QTimer.singleShot(delay, lambda e=effect, ex=self.expanded: self.start_fade_animation(e, ex))

        QTimer.singleShot(200, self.update_button_texts)
        QTimer.singleShot(700, lambda: setattr(self, "animating", False))

        self.expanded = not self.expanded


    def start_fade_animation(self, effect, expanded):
        fade = QPropertyAnimation(effect, b"opacity")
        fade.setDuration(200)
        fade.setStartValue(1 if expanded else 0)
        fade.setEndValue(0 if expanded else 1)
        fade.setEasingCurve(QEasingCurve.InOutQuad)
        fade.start()
        self.animations.append(fade)

    def update_button_texts(self):
        for btn, icon, text, effect in self.menu_buttons:
            btn.setText(f"{icon}" if not self.expanded else f"{icon}  {text}")

            fade_in = QPropertyAnimation(effect, b"opacity")
            fade_in.setDuration(200)
            fade_in.setStartValue(0)
            fade_in.setEndValue(1)
            fade_in.setEasingCurve(QEasingCurve.InOutQuad)
            fade_in.start()
            self.animations.append(fade_in)

        self.logo.setVisible(self.expanded)
