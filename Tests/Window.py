import maya.cmds as mc
cmds.file(f=True, new=True) #permet de vider la scène à chaque exécution

if mc.window("zds_window", query=True, exists=True):
    mc.deleteUI("zds_window", window=True)

window = mc.window("zds_window", title="Ma fenetre", widthHeight=(200, 55), backgroundColor=(0.925, 0.467, 0.047))
mc.columnLayout(adjustableColumn=True)
mc.button(label='Do Nothing')
mc.button(label='Close', command=('mc.deleteUI(\"'+window+'\", window=True)') )
mc.setParent('..')
mc.showWindow(window)
