import maya.cmds as cmds
cmds.file(f=True, new=True) #permet de vider la scène à chaque exécution


#Variables dynamiques
espace = 3
largeur = 4
longueur = 6
hauteur = 3.5


#Algorithme permettant à la largeur de toujours être plus petite que la longueur
if (largeur>longueur):
    cst=largeur
    largeur=longueur
    longueur=cst


#Génération du sol
cmds.polyCube(width=(largeur+1)*espace, height=.3, depth=(longueur+1)*espace, name="sol_1")
cmds.polyCube(width=(largeur+1.5)*espace, height=.3, depth=(longueur+1.5)*espace, name="sol_2")
cmds.polyCube(width=(largeur+2)*espace, height=.3, depth=(longueur+2)*espace, name="sol_3")

cmds.move(espace*largeur/2,-.2,espace*longueur/2, "sol_1")
cmds.move(espace*largeur/2,-.6,espace*longueur/2, "sol_2")
cmds.move(espace*largeur/2,-1,espace*longueur/2, "sol_3")


#Génération des colonnes
for i in range(longueur+1):
    for j in range(largeur+1):
        if (j==largeur) or (j==0) or (i==0) or (i==longueur):
            #Si le nombre de colonnes est impair, on efface celle du milieu
            if (j==largeur/2) and (largeur%2 == 0):
                j=j+1
            
            # Rangée de cubes au sol
            cmds.polyCube(width=1.3, height=.3, depth=1.3)
            cmds.move((j+1)*espace,0,0)
            cmds.move((j)*espace,0,i*espace)
            
            #Rangée de cubes au dessus de la précédente
            cmds.polyCube(width=1.1, height=.1, depth=1.1)
            cmds.move((j+1)*espace,.2,0)
            cmds.move((j)*espace,.2,i*espace)
            
            #Colonnes
            cmds.polyCylinder(height=hauteur, radius=.4, sx=7)
            cmds.move((j+1)*espace,1.9,0)
            cmds.move((j)*espace,1.9,i*espace)
            cmds.polyCylinder(height=hauteur, radius=.4, sx=9)
            cmds.move((j+1)*espace,1.9,0)
            cmds.move((j)*espace,1.9,i*espace)
            
            #Rangée de cubes au dessus des colonnes
            cmds.polyCube(width=1.1, height=.1, depth=1.1)
            cmds.move((j+1)*espace,3.7,0)
            cmds.move((j)*espace,3.7,i*espace)
            
            #Rangée de cubes au plafond
            cmds.polyCube(width=1.3, height=.3, depth=1.3)
            cmds.move((j+1)*espace,3.9,0)
            cmds.move((j)*espace,3.9,i*espace)
        

#Génération du plafond
cmds.polyCube(width=(largeur+0.7)*espace, height=.4, depth=(longueur+0.7)*espace, name="plafond_1")
cmds.polyCube(width=(largeur+0.6)*espace, height=.3, depth=(longueur+0.6)*espace, name="plafond_2")
cmds.polyCube(width=(largeur+0.8)*espace, height=.6, depth=(longueur+0.8)*espace, name="plafond_3")
cmds.polyCube(width=(largeur+0.6)*espace, height=.6, depth=(longueur+0.6)*espace, name="plafond_4")

cmds.move(espace*largeur/2,4.2,espace*longueur/2, "plafond_1")
cmds.move(espace*largeur/2,4.5,espace*longueur/2, "plafond_2")
cmds.move(espace*largeur/2,4.9,espace*longueur/2, "plafond_3")
cmds.move(espace*largeur/2,5.2,espace*longueur/2, "plafond_4")


#Génération du toit
cmds.polyPrism(length=(longueur+0.8)*espace, sideLength=(largeur+0.8)*espace, name="toit")
cmds.rotate(90,0,90, "toit")
cmds.move(espace*largeur/2,46+largeur,espace*longueur/2, "toit")
cmds.scale(0.12,1,1, "toit", centerPivot=True)