
#******************************************************** BUILD MODEL
import maya.cmds as mc
import python
from python.classe.model import *
reload( python.classe.model)
reload( python.classe.buildPosition)

#___________________________________________________________________________LOAD MODEL BASE
from python.classe.readWriteInfo import *
reload(python.classe.readWriteInfo)
rwi = readWriteInfo()
rwi.mayaScene_load( 'D:/mcantat_BDD/projects/flyAway/assets/howie/maya/scenes/howie_modelBase.ma'  , open = True )
#rwi.mayaScene_save( 'D:/mcantat_BDD/projects/flyAway/assets/howie/maya/scenes/howie_modelBase.ma' )
#___________________________________________________________________________LOAD MODEL BASE

import python.utils.utilsMaya as utilsMaya
utilsMaya.setSceneUnitToMeter()



mirrorX = {}
mirrorX['value']             = [0,0,0 , 0,1,0 , 0,0,1]
mirrorX['mode']              = 'mirror'
mirrorX['pivot']             = [0,0,0 , 0,0,0 , 1,1,1]
mirrorX['namePrefix']        = ['r','l']
mirrorX['nameReplace']       = ['','']
mirrorX['nameIncr']          = ''
mirrorX['nameAdd']           = []
mirrorX['noneMirrorAxe']     = -1


#BUILD
for lod in [ 'Hi' , 'Low' ]:  
    modelClass_duplicateAndBuild( ('head'+lod+'_GRP') , [                         mirrorX ] )


#REORDER HIERARCHY      




#CLEAN HIERARCHY
grps = mc.listRelatives("ALL_GRP", c = True )
for i in range(0,len(grps) ):
    childrens = mc.listRelatives( grps[i] , c = True )
    if( childrens == None )or( len(childrens) == 0 ): mc.delete(grps[i])


#REORDER HIERARCHY
mc.createNode( "transform" , n = "all_GRP" )
mc.createNode( "transform" , n = "hi_GRP"  , p = "all_GRP" )
mc.createNode( "transform" , n = "low_GRP" , p = "all_GRP" )
mc.parent(mc.ls("ALL_GRP|*Low_GRP"),"low_GRP")
mc.parent(mc.ls("ALL_GRP|*_GRP"),"hi_GRP")
mc.delete("ALL_GRP")



#___________________________________________________________________________SAVE TO MODEL
rwi.mayaScene_save( 'D:/mcantat_BDD/projects/flyAway/assets/howie/maya/scenes/howie_model.ma' )
#___________________________________________________________________________SAVE TO MODEL
