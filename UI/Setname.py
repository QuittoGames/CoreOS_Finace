from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class NameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Digite seu nome")
        self.setFixedSize(300, 120)

        layout = QVBoxLayout(self)

        self.label = QLabel("Bem Vindo! Digite seu nome:")
        layout.addWidget(self.label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Seu nome aqui")
        layout.addWidget(self.name_input)

        self.ok_btn = QPushButton("OK")
        self.ok_btn.clicked.connect(self.accept)
        layout.addWidget(self.ok_btn)

    def getName(self) -> str:
        return self.name_input.text().strip()
