import maya.cmds as cmds
from random import *
cmds.file(f=True, new=True) #permet de vider la scène à chaque exécution

def temple():    
    # Variables dynamiques
    longueur = cmds.intSliderGrp(slider1, q=True, value=True) #10
    largeur = cmds.intSliderGrp(slider2, q=True, value=True) #8
    hauteur_colonne = cmds.floatSliderGrp(slider3, q=True, value=True) #5
    espace = cmds.floatSliderGrp(slider4, q=True, value=True) #3

    nb_marches = cmds.intSliderGrp(slider5, q=True, value=True) #10
    hauteur_marche = cmds.floatSliderGrp(slider6, q=True, value=True) #0.3
   
    nb_etages_toit = cmds.intSliderGrp(slider7, q=True, value=True) #20
    hauteur_toit = cmds.intSliderGrp(slider8, q=True, value=True) #6
    
    random = randint(0,200) #seed d'un temple
    # Algorithme permettant à la largeur de toujours être plus petite que la longueur
    if (largeur>longueur):
        largeur, longueur = longueur, largeur

    # Génération du sol  
    cmds.polyCube(width=(largeur)*espace, height=hauteur_marche, depth=(longueur)*espace, name="sol_1_"+str(random))
    cmds.move(espace*(largeur-1)/2,nb_marches*hauteur_marche,espace*(longueur-1)/2, "sol_1_"+str(random))
    
    for a in range (nb_marches-1):
        nom_tmp = "sol_"+str(a+2)+"_"+str(random)
        cmds.instance("sol_1_"+str(random), name=nom_tmp)
        cmds.scale(1+0.1*(a+1),1,1+0.1*(a+1), nom_tmp)
        cmds.move(espace*(largeur-1)/2,(nb_marches-a-1)*hauteur_marche, espace*(longueur-1)/2, nom_tmp)
    
    #Génération des colonnes
    for i in range(longueur):
        for j in range(largeur):
            if (j==largeur-1) or (j==0) or (i==0) or (i==longueur-1):
                
                # VARIABLES
                cube_bas = "cube_bas_"+str(i)+str(j)+"_"+str(random)      # Rangée de cubes au sol
                cube_bas2 = "cube_bas2_"+str(i)+str(j)+"_"+str(random)    # Rangée de cubes au dessus de la précédente
                cylindre = "cylindre_"+str(i)+str(j)+"_"+str(random)      # Colonne
                cylindre2 = "cylindre2_"+str(i)+str(j)+"_"+str(random)    # Ornements
                cube_haut = "cube_haut_"+str(i)+str(j)+"_"+str(random)    # Rangée de cubes au dessus des colonnes
                cube_haut2 = "cube_haut2_"+str(i)+str(j)+"_"+str(random)  # Rangée de cubes au plafond
                
                # MODELS
                cmds.polyCube(width=1.3, height=.3, depth=1.3, name=cube_bas+str(random))
                cmds.polyCube(width=1.1, height=.1, depth=1.1, name=cube_bas2+str(random))
                cmds.polyCylinder(height=hauteur_colonne, radius=.4, sx=7, name=cylindre+str(random))
                cmds.polyCylinder(height=hauteur_colonne, radius=.4, sx=9, name=cylindre2+str(random))
                cmds.polyCube(width=1.1, height=.1, depth=1.1, name=cube_haut+str(random))
                cmds.polyCube(width=1.3, height=.3, depth=1.3, name=cube_haut2+str(random))
                
                # ACTIONS
                cmds.move(j*espace,(nb_marches+1)*hauteur_marche,i*espace, cube_bas+str(random))
                cmds.move(j*espace,(nb_marches+1)*hauteur_marche+0.2,i*espace, cube_bas2+str(random))
                cmds.move(j*espace,(nb_marches+1)*hauteur_marche+0.2+(hauteur_colonne/2.0),i*espace, cylindre+str(random))
                cmds.move(j*espace,(nb_marches+1)*hauteur_marche+0.2+(hauteur_colonne/2.0),i*espace, cylindre2+str(random))
                cmds.move(j*espace,(nb_marches+1)*hauteur_marche+0.2+hauteur_colonne,i*espace, cube_haut+str(random))
                cmds.move(j*espace,(nb_marches+1)*hauteur_marche+0.4+hauteur_colonne,i*espace, cube_haut2+str(random))
            
    #Génération du plafond
    cmds.polyCube(width=(largeur-1+0.7)*espace, height=.4, depth=(longueur-1+0.7)*espace, name="plafond_1_"+str(random))
    cmds.polyCube(width=(largeur-1+0.6)*espace, height=.3, depth=(longueur-1+0.6)*espace, name="plafond_2_"+str(random))
    cmds.polyCube(width=(largeur-1+0.8)*espace, height=.6, depth=(longueur-1+0.8)*espace, name="plafond_3_"+str(random))
    cmds.polyCube(width=(largeur-1+0.6)*espace, height=.6, depth=(longueur-1+0.6)*espace, name="plafond_4_"+str(random))
    
    cmds.move(espace*(largeur-1)/2,(nb_marches+1)*hauteur_marche+0.6+hauteur_colonne,espace*(longueur-1)/2, "plafond_1_"+str(random))
    cmds.move(espace*(largeur-1)/2,(nb_marches+1)*hauteur_marche+0.75+hauteur_colonne,espace*(longueur-1)/2, "plafond_2_"+str(random))
    cmds.move(espace*(largeur-1)/2,(nb_marches+1)*hauteur_marche+1.05+hauteur_colonne,espace*(longueur-1)/2, "plafond_3_"+str(random))
    cmds.move(espace*(largeur-1)/2,(nb_marches+1)*hauteur_marche+1.35+hauteur_colonne,espace*(longueur-1)/2, "plafond_4_"+str(random))
    
    #Génération du toit
    float_h = float(hauteur_toit)
    float_n = float(nb_etages_toit)
    hauteur_etage = float_h/float_n
    
    for n in range (1, nb_etages_toit+1):
        nom_tmp = "toit_"+str(n)+"_"+str(random)
        cmds.polyCube(width=(largeur*espace+1)*(1-(float(n)/nb_etages_toit)), height=hauteur_etage, depth=(longueur*espace)*(1-(float(n-1)/(2*nb_etages_toit-2))), name=nom_tmp)
        cmds.move(espace*(largeur-1)/2,(nb_marches+1)*hauteur_marche+1.55+hauteur_colonne+(hauteur_etage/2.0)+hauteur_etage*(n-1),espace*(longueur-1)/2, nom_tmp)

# INTERFACE 
window = cmds.window(title = "Temple Generator © Nathanaël ROVERE", tlc=[0,0], backgroundColor=(0.1, 0.4, 0.5))
cmds.columnLayout(adjustableColumn=True, columnAttach=["both", 20])

cmds.separator(style="none", h=20)

slider1= cmds.intSliderGrp( field=True, label='Longueur du Temple', minValue=3, maxValue=30, value=10)
slider2= cmds.intSliderGrp( field=True, label='Largeur du Temple', minValue=3, maxValue=30, value=8)
slider3= cmds.floatSliderGrp( field=True, label='Hauteur du Temple', minValue=2, maxValue=30, value=5)
slider4= cmds.floatSliderGrp( field=True, label='Espace entre les colonnes', minValue=1, maxValue=10, value=3)

cmds.separator(style="none", h=10)

slider5= cmds.intSliderGrp( field=True, label='Nombre de Marches', minValue=2, maxValue=30, value=5)
slider6= cmds.floatSliderGrp( field=True, label='Hauteur des marches', minValue=0.1, maxValue=5, value=0.3)
cmds.separator(style="none", h=10)

slider7= cmds.intSliderGrp( field=True, label='Nombre de couches du toit', minValue=4, maxValue=50, value=20)
slider8= cmds.intSliderGrp( field=True, label='Hauteur totale du toit', minValue=4, maxValue=20, value=6)

cmds.separator(style="none", h=20)

cmds.button(label = "Create Temple",c='temple()')
cmds.setParent('..')
cmds.showWindow()