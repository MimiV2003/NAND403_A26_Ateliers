#Atelier7 ===> Atelier 8

from maya import cmds

cmds.playbackOptions(min=0, max=100)


nom = "monCube"

if not cmds.objExists(nom):
    objet = cmds.polyCube(name=nom)[0]
    print("Objet cree :", objet)
else:
    objet = nom
    print("L'objet existe deja :", nom)

cmds.cutKey(objet, clear=True)

cmds.setKeyframe(objet, attribute="translateX", value= 20, time=0) 

cmds.setKeyframe(objet, attribute="translateX", value= 1, time=50)

cmds.setKeyframe(objet, attribute="translateX", value= 10, time=100)