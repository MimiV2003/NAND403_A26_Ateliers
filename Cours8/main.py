#import de librairie de base/classique
import os
import sys

#-------------------------------------------------------------------------------------------------
#on a obtenu le folder dans lequel il y a notre fichier courant
#__file__ = le fichier courant
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)
print(absolute_folder_path) #Repos/NAND
#ici on vient ajouter absolute_folder_path au path de python pour qu'il puisse trouver ui.py
sys.path.append(absolute_folder_path)



#from ui import MyClass

#def my_function():
#    absolute_path = os.path.abspath(os.path.curdir)
#   print(absolute_path)

#my_class = MyClass()
#my_class.print.print_variable()

#---------------------------------------------------------------------------------------------


import ui
import importlib
importlib.reload(ui)

def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    random_animation_ui = ui.RandomAnimationUI()
    random_animation_ui.show()

main()
    