from PySide6.QtWidgets import(QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit)

#--------------------------------------------------------------------------------
#class MyClass(QWidget):
#    def __init__(self):
#        super().__init__()
#       self.variable =42
#
#    def print_variable(self):
#        print(self.variable)
#------------------------------------------------------------------------------
class MessageBoard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message board")
        self.setMinimumWidth(400)
        self.build_ui()
    def build_ui(self):
            layout = QVBoxLayout(self)
            label = QLabel("Message board")
            layout.addWidget(label)

            self.message = QTextEdit()
            self.message.setPlaceholderText("Entrez message...")
            layout.addWidget(self.message)
            
            
            button = QPushButton("Afficher")
            layout.addWidget(button)
            
            button.clicked.connect(self.on_click)
            
            print("create UI")








class RandomAnimationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random animation")
        self.setMinimumWidth(400)



        
    