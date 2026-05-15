from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QLineEdit,
    QLabel
)

from backend.rag import build_query_engine
from backend.ollama import stop_ollama

import sys


class MainWindow(QWidget):
    def __init__(self, port, proc):
        super().__init__()

        self.proc = proc
        self.query_engine = build_query_engine(port)

        self.setWindowTitle("EasyLocalLlm")
        self.resize(800, 600)

        layout = QVBoxLayout()

        self.label = QLabel("Question")
        layout.addWidget(self.label)

        self.input = QLineEdit()
        layout.addWidget(self.input)

        self.button = QPushButton("Envoyer")
        self.button.clicked.connect(self.ask_question)
        layout.addWidget(self.button)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.setLayout(layout)

    def ask_question(self):
        question = self.input.text()

        response = self.query_engine.query(question)

        self.output.append(f"\nQuestion:\n{question}\n")
        self.output.append(f"Réponse:\n{response}\n")

    def closeEvent(self, event):
        stop_ollama(self.proc)
        event.accept()


def start_ui(port, proc):
    app = QApplication(sys.argv)

    window = MainWindow(port, proc)
    window.show()

    sys.exit(app.exec())