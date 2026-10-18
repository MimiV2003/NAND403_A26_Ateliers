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

        #Nombre d element---------------------------------------------
        count_layout = QHBoxLayout()
        count_layout.addWidget(QLabel("Number of Objects"))
        self.input_count = QLineEdit("10")
        count_layout.addWidget(self.input_count)
        layout.addLayout(count_layout)

        # Minimum ---------------------------------------------------------
        pos_min_layout = QHBoxLayout()
        pos_min_layout.addWidget(QLabel("Minimum"))

        self.input_min_x = QLineEdit("-10.0")
        pos_min_layout.addWidget(self.input_min_x)

        self.input_min_y = QLineEdit("0.0")
        pos_min_layout.addWidget(self.input_min_y)

        self.input_min_z = QLineEdit("-10.0")
        pos_min_layout.addWidget(self.input_min_z)

        layout.addLayout(pos_min_layout)

        # Y ----------------------------------------------------------

        dim_layout.addWidget(QLabel("Y:"))
        self.spin_y = QDoubleSpinBox()
        self.spin_y.setRange(0.01, 100.0)
        self.spin_y.setValue(1.0)
        dim_layout.addWidget(self.spin_y)

        # Z ----------------------------------------------------------

        dim_layout.addWidget(QLabel("Z:"))
        self.spin_z = QDoubleSpinBox()
        self.spin_z.setRange(0.01, 100.0)
        self.spin_z.setValue(1.0)
        dim_layout.addWidget(self.spin_z)

        layout.addLayout(dim_layout)

        #Creation du bouton-------------------------------------------

        self.create_button = QPushButton("Create Objects")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):
        forme = random.choice(["cube", "cylindre", "sphere"])

        if forme == "cube":
            objet = cmds.polyCube()[0]
        elif forme == "cylindre":
            objet = cmds.polyCylinder()[0]
        else:
            objet = cmds.polySphere()[0]

        random_value = random.uniform(-10, 10)
        cmds.move(random_value, random_value, random_value, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()