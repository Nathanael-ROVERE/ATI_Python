import maya.cmds as cmds
cmds.file(f=True, new=True) #permet de vider la scène à chaque exécution

# Variables dynamiques
largeur = 5
longueur = 4
hauteur = 3.5
espace = 3
nb_marches = 4

# Algorithme permettant à la largeur de toujours être plus petite que la longueur
if (largeurlongueur)
    cst=largeur
    largeur=longueur
    longueur=cst

# Génération du sol  
cmds.polyCube(width=(largeur+1)espace, height=.3, depth=(longueur+1)espace, name=sol_1)
cmds.move(espacelargeur2,-.2,espacelongueur2, sol_1)

for a in range (nb_marches-1)
    nom_tmp = sol_%d%(a+2)
    cmds.instance(sol_1, name=nom_tmp)
    cmds.scale(1+0.1(a+1),1,1+0.1(a+1), nom_tmp)
    cmds.move(espacelargeur2,-0.2-0.4(a+1), espacelongueur2, nom_tmp)

#Génération des colonnes
for i in range(longueur+1)
    for j in range(largeur+1)
        if (j==largeur) or (j==0) or (i==0) or (i==longueur)
            #Si le nombre de colonnes est impair, on efface celle du milieu
            if (j==largeur2) and (largeur%2 == 0) and (i==0)
                j=j+1
            
            # VARIABLES
            cube_bas = cube_bas_+str(i)+str(j)      # Rangée de cubes au sol
            cube_bas2 = cube_bas2_+str(i)+str(j)    # Rangée de cubes au dessus de la précédente
            cylindre = cylindre_+str(i)+str(j)      # Colonne
            cylindre2 = cylindre2_+str(i)+str(j)    # Ornements
            cube_haut = cube_haut_+str(i)+str(j)    # Rangée de cubes au dessus des colonnes
            cube_haut2 = cube_haut2_+str(i)+str(j)  # Rangée de cubes au plafond
            
            # MODELS
            cmds.polyCube(width=1.3, height=.3, depth=1.3, name=cube_bas)
            cmds.polyCube(width=1.1, height=.1, depth=1.1, name=cube_bas2)
            cmds.polyCylinder(height=hauteur, radius=.4, sx=7, name=cylindre)
            cmds.polyCylinder(height=hauteur, radius=.4, sx=9, name=cylindre2)
            cmds.polyCube(width=1.1, height=.1, depth=1.1, name=cube_haut)
            cmds.polyCube(width=1.3, height=.3, depth=1.3, name=cube_haut2)
            
            # ACTIONS
            cmds.move((j)espace,0,iespace, cube_bas)
            cmds.move((j)espace,.2,iespace, cube_bas2)
            cmds.move((j)espace,1.9,iespace, cylindre)
            cmds.move((j)espace,1.9,iespace, cylindre2)
            cmds.move((j)espace,3.7,iespace, cube_haut)
            cmds.move((j)espace,3.9,iespace, cube_haut2)
        
#Génération du plafond
cmds.polyCube(width=(largeur+0.7)espace, height=.4, depth=(longueur+0.7)espace, name=plafond_1)
cmds.polyCube(width=(largeur+0.6)espace, height=.3, depth=(longueur+0.6)espace, name=plafond_2)
cmds.polyCube(width=(largeur+0.8)espace, height=.6, depth=(longueur+0.8)espace, name=plafond_3)
cmds.polyCube(width=(largeur+0.6)espace, height=.6, depth=(longueur+0.6)espace, name=plafond_4)

cmds.move(espacelargeur2,4.2,espacelongueur2, plafond_1)
cmds.move(espacelargeur2,4.5,espacelongueur2, plafond_2)
cmds.move(espacelargeur2,4.9,espacelongueur2, plafond_3)
cmds.move(espacelargeur2,5.2,espacelongueur2, plafond_4)

#Génération du toit
cmds.polyPrism(length=(longueur+0.8)espace, sideLength=(largeur+0.8)espace, name=toit)
cmds.rotate(90,0,90, toit)
cmds.move(espacelargeur2,46+largeur,espacelongueur2, toit)
cmds.scale(0.12,1,1, toit, centerPivot=True)