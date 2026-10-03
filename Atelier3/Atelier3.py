from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QLineEdit


#Information--------------------------------------------------------------------------------------------------
#Allo, il n'y avait plus les enoncers pour l'atelier 3, j'ai fais ce que je me suis rappeler
#---------------------------------------------------------------------------------------------------------------
#Le resultat c'est barre de recherche et notification "allo" //Note de cours
#--------------------------------------------------------------------------------------------------------

#Note de cours

 #snake case
 #this_is_a_snake_case_syntax

 #Camel case
 #thisIsACamelCaseSyntax

 #Pascal case
 #ThisIsAPascalCase


class MessageBoard(QWidget):#definir la classe | QWidget = affiche dans lecran

    def __init__(self): #Constructeur (self = this) (nous meme)

        super().__init__() #Initialisation | Constructeur a quelqu'un d'autre ====> De notre parent (QWidget)

        self.setWindowTitle("Message board") #(Titre)----Parametre
        self.create_ui()#fonction defeni a l'interieur d'une class | instance (c'est quel instance) (Sassure de prendre le bon)
    
    def create_ui(self):
        layout = QVBoxLayout(self)
        label = QLabel("Message board")
        layout.addWidget(label)

        #TEST (essaie-erreur)--------------------------------------------------------------------
        #QTextEdit
        #text_edit = QTextEdit()
        #layout.addWidget(text_edit)
        #QLineEdit pour barre de recherche
        #------------------------------------------------------------------------
        #Bonne version

        self.message = QTextEdit()
        self.message.setPlaceholderText("Entrez message...")
        layout.addWidget(self.message)


        button = QPushButton("Afficher")
        layout.addWidget(button)

        button.clicked.connect(self.on_click)

        print("create UI")

    

    def on_click(self):
        #print("on click called")
        message_afficher = self.message.toPlainText()
        #add QMessageBox
        QMessageBox.information(self, "Notification", message_afficher) #C'est cool, j'ai appris que QMessageBox peut avoir plusieur icones different
        #Information c'est i en bleu
        #Il y a aussi le warning, le critical et question.

def main():

    global widget #arrete dexister apres 

    try:

        widget.close()

    except Exception:

        pass

    widget = MessageBoard()#premiere creation class

    widget.show()

 

main()

