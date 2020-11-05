import maya.cmds as cmds
cmds.file(f=True, new=True) #permet de vider la scène à chaque exécution

# Variables dynamiques
largeur = 10
longueur = 8
hauteur_colonne = 4.5
espace = 3

nb_marches = 10
hauteur_marche = .3

nb_etages_toit = 20
hauteur_toit = 6

# Algorithme permettant à la largeur de toujours être plus petite que la longueur
if (largeur>longueur):
    cst=largeur
    largeur=longueur
    longueur=cst

# Génération du sol  
cmds.polyCube(width=(largeur)*espace, height=hauteur_marche, depth=(longueur)*espace, name="sol_1")
cmds.move(espace*(largeur-1)/2,nb_marches*hauteur_marche,espace*(longueur-1)/2, "sol_1")

for a in range (nb_marches-1):
    nom_tmp = "sol_%d"%(a+2)
    cmds.instance("sol_1", name=nom_tmp)
    cmds.scale(1+0.1*(a+1),1,1+0.1*(a+1), nom_tmp)
    cmds.move(espace*(largeur-1)/2,(nb_marches-a-1)*hauteur_marche, espace*(longueur-1)/2, nom_tmp)

#Génération des colonnes
for i in range(longueur):
    for j in range(largeur):
        if (j==largeur-1) or (j==0) or (i==0) or (i==longueur-1):
            
            # VARIABLES
            cube_bas = "cube_bas_"+str(i)+str(j)      # Rangée de cubes au sol
            cube_bas2 = "cube_bas2_"+str(i)+str(j)    # Rangée de cubes au dessus de la précédente
            cylindre = "cylindre_"+str(i)+str(j)      # Colonne
            cylindre2 = "cylindre2_"+str(i)+str(j)    # Ornements
            cube_haut = "cube_haut_"+str(i)+str(j)    # Rangée de cubes au dessus des colonnes
            cube_haut2 = "cube_haut2_"+str(i)+str(j)  # Rangée de cubes au plafond
            
            # MODELS
            cmds.polyCube(width=1.3, height=.3, depth=1.3, name=cube_bas)
            cmds.polyCube(width=1.1, height=.1, depth=1.1, name=cube_bas2)
            cmds.polyCylinder(height=hauteur_colonne, radius=.4, sx=7, name=cylindre)
            cmds.polyCylinder(height=hauteur_colonne, radius=.4, sx=9, name=cylindre2)
            cmds.polyCube(width=1.1, height=.1, depth=1.1, name=cube_haut)
            cmds.polyCube(width=1.3, height=.3, depth=1.3, name=cube_haut2)
            
            # ACTIONS
            cmds.move(j*espace,(nb_marches+1)*hauteur_marche,i*espace, cube_bas)
            cmds.move(j*espace,(nb_marches+1)*hauteur_marche+0.2,i*espace, cube_bas2)
            cmds.move(j*espace,(nb_marches+1)*hauteur_marche+0.2+(hauteur_colonne/2.0),i*espace, cylindre)
            cmds.move(j*espace,(nb_marches+1)*hauteur_marche+0.2+(hauteur_colonne/2.0),i*espace, cylindre2)
            cmds.move(j*espace,(nb_marches+1)*hauteur_marche+0.2+hauteur_colonne,i*espace, cube_haut)
            cmds.move(j*espace,(nb_marches+1)*hauteur_marche+0.4+hauteur_colonne,i*espace, cube_haut2)
        
#Génération du plafond
cmds.polyCube(width=(largeur-1+0.7)*espace, height=.4, depth=(longueur-1+0.7)*espace, name="plafond_1")
cmds.polyCube(width=(largeur-1+0.6)*espace, height=.3, depth=(longueur-1+0.6)*espace, name="plafond_2")
cmds.polyCube(width=(largeur-1+0.8)*espace, height=.6, depth=(longueur-1+0.8)*espace, name="plafond_3")
cmds.polyCube(width=(largeur-1+0.6)*espace, height=.6, depth=(longueur-1+0.6)*espace, name="plafond_4")

cmds.move(espace*(largeur-1)/2,(nb_marches+1)*hauteur_marche+0.6+hauteur_colonne,espace*(longueur-1)/2, "plafond_1")
cmds.move(espace*(largeur-1)/2,(nb_marches+1)*hauteur_marche+0.75+hauteur_colonne,espace*(longueur-1)/2, "plafond_2")
cmds.move(espace*(largeur-1)/2,(nb_marches+1)*hauteur_marche+1.05+hauteur_colonne,espace*(longueur-1)/2, "plafond_3")
cmds.move(espace*(largeur-1)/2,(nb_marches+1)*hauteur_marche+1.35+hauteur_colonne,espace*(longueur-1)/2, "plafond_4")

#Génération du toit
float_h = float(hauteur_toit)
float_n = float(nb_etages_toit)
hauteur_etage = float_h/float_n
print(hauteur_etage)

for n in range (1, nb_etages_toit+1):
    nom_tmp = "toit_%d"%n
    cmds.polyCube(width=(largeur*espace+1)*(1-(float(n)/nb_etages_toit)), height=hauteur_etage, depth=(longueur*espace)*(1-(float(n-1)/(2*nb_etages_toit-2))), name=nom_tmp)
    cmds.move(espace*(largeur-1)/2,(nb_marches+1)*hauteur_marche+1.55+hauteur_colonne+(hauteur_etage/2.0)+hauteur_etage*(n-1),espace*(longueur-1)/2, nom_tmp)

