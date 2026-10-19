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
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)

        #Nombre d element--------------------------------------------------------------------------------------------------
        #Mettre un titre et un rectangle pour mettre un text
        count_layout = QHBoxLayout()
        count_layout.addWidget(QLabel("Number of Objects")) #Affiche un titre sur le coter
        self.input_count = QLineEdit("20")
        count_layout.addWidget(self.input_count)
        layout.addLayout(count_layout)

        # X --------------------------------------------------------------------------------------------------------------
        #Pour cette partie, le x, y, z on a le meme code pour pouvoir controler leur minimum et max chacun
        #Aide a definir les limites de deplacement aleatoire
        pos_min_layout = QHBoxLayout()
        pos_min_layout.addWidget(QLabel("Min/Max X:")) #titre

        self.input_min_x = QLineEdit("-10.0")
        pos_min_layout.addWidget(self.input_min_x) #conteneur horizontal qui rassemble les elements / self.input_min_x = champs saisie de la valeur minimale

        self.input_max_x = QLineEdit("10.0")
        pos_min_layout.addWidget(self.input_max_x)

        layout.addLayout(pos_min_layout) #Apparaitre

        # Y ---------------------------------------------------------------------------------------------------------------
        pos_min_layout = QHBoxLayout()
        pos_min_layout.addWidget(QLabel("Min/Max Y:"))

        self.input_min_y = QLineEdit("-10.0")
        pos_min_layout.addWidget(self.input_min_y)

        self.input_max_y = QLineEdit("10.0")
        pos_min_layout.addWidget(self.input_max_y)

        layout.addLayout(pos_min_layout)

        # Z ---------------------------------------------------------------------------------------------------------------
        pos_min_layout = QHBoxLayout()
        pos_min_layout.addWidget(QLabel("Min/Max Z:"))

        self.input_min_z = QLineEdit("-10.0")
        pos_min_layout.addWidget(self.input_min_z)

        self.input_max_z = QLineEdit("10.0")
        pos_min_layout.addWidget(self.input_max_z)

        layout.addLayout(pos_min_layout)

        #Scale-----------------------------------------------------------------------------------------------------------------------------
        #Aide a definir la taille minimum et maximum des objets

        scale_layout = QHBoxLayout()
        scale_layout.addWidget(QLabel("Min/Max Scale:"))
        self.input_scale_min = QLineEdit("0.5")
        scale_layout.addWidget(self.input_scale_min)
        self.input_scale_max = QLineEdit("2.0")
        scale_layout.addWidget(self.input_scale_max)

        layout.addLayout(scale_layout)


        #Creation du bouton-----------------------------------------------------------------------------------------------------

        self.create_button = QPushButton("Create Objects")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

        #---------------------------------------------------------------------------------------------------------------------------
        #Recuperation et verification de donnee---------------------------------------------------------------------------------------
        #Sa repete beaucoup mais sa marche!
        #Protege le code contre les erreurs par exemple, accepte seulement les chiffres sinon = erreur
        #int = nombre, float pour nbr en virgule

    def create_object(self):
        try:
            count = int(self.input_count.text())
            min_x = float(self.input_min_x.text())
            max_x = float(self.input_max_x.text())
            min_y = float(self.input_min_y.text())
            max_y = float(self.input_max_y.text())
            min_z = float(self.input_min_z.text())
            max_z = float(self.input_max_z.text())
            scale_min = float(self.input_scale_min.text())
            scale_max = float(self.input_scale_max.text())
        except ValueError:
            cmds.warning("Invalide")#le warning va apparaitre dans maya, en bas de l ecran
            return

        #-------------------------------------------------------------------------------------------------------------------------
        #Random--------------------------------------------------------------------------------------------------------------------
        #random.choice va effectuer un choix au hasard parmi les choix d objet
        for _ in range(count):
            forme = random.choice(["cube", "cylindre", "sphere"])
            #creation objet
            if forme == "cube":
                objet = cmds.polyCube()[0] # le [0] sert a recuperer le nom de l objet
            elif forme == "cylindre":
                objet = cmds.polyCylinder()[0]
            else:
                objet = cmds.polySphere()[0]

            #Placement et resultat aleatoire------------------------------------------------------------------------------------
            cmds.move(random.uniform(min_x, max_x), random.uniform(min_y, max_y), random.uniform(min_z, max_z), objet) # prends information ecrit = creation

            s = random.uniform(scale_min, scale_max) # aide a ne PAS deformer la forme de l objet
            cmds.scale(s, s, s, objet)

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