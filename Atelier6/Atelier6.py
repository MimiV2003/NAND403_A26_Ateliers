
#Atelier 4-5
#Note---------------------------------------------------------------------------------------------------------
#Un peu plus difficile celui la
#jai eu des erreur avec le random mais jai fini par reussir l apparition aleatoire des objets, yyyeaahh!
#Jaime le resultat final
#-------------------------------------------------------------------------------------------------------------


import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit
)

class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 6")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)

        #La fenetre pour mettre le nbr de planches----------------------------------------------------------------------------------------------
        nbr_planche = QHBoxLayout()
        nbr_planche.addWidget(QLabel("Number of Objects")) #Affiche un titre sur le coter
        self.input_nbr_planche = QLineEdit("0")
        nbr_planche.addWidget(self.input_nbr_planche)
        layout.addLayout(nbr_planche)

        #Creation du bouton-----------------------------------------------------------------------------------------------------

        self.create_button = QPushButton("Create Objects")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    #creation d'une varaible pour transformer text en int----------------------------------------------------------------------
    def create_object(self):

        creation_maya = int(self.input_nbr_planche.text())

        offset_x = 0

        #MFor loop pour faire 3 planches par loop + creation des formes
        for _ in range(creation_maya):

                #Premiere apparition de la planche
                objet = cmds.polyCube()[0]
                cmds.move(0 + offset_x, 6, 0, objet)
                cmds.scale(1, 12, 1, objet)

                #Le deuxieme
                objet2 = cmds.polyCube()[0]
                cmds.move(6.5 + offset_x, 3, 0, objet2)
                cmds.scale(12, 1, 1, objet2)

                #le troisieme
                objet3 = cmds.polyCube()[0]
                cmds.move(6.5 + offset_x, 9, 0, objet3)
                cmds.scale(12, 1, 1, objet3)

                offset_x = offset_x + 13 #Grace a plus 13, les planches ne chevauche pas
                
        #---------------------------------------------------------------------------------------------------------------------


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()