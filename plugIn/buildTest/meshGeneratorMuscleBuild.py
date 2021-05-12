
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'meshGeneratorMuscle'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/meshGeneratorMuscle/Build/{}/meshGeneratorMuscle.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/meshGeneratorMuscleBuildTest{}.ma'.format(lodSuffixs[highPoly])

#__________________________ NODE DRAW INFO
nodeTypeDraw     = 'glDraw'  
pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'.format( releaseFolder[releaseMode] )



print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("muscle_GEO") ):
	clean( [pathNode , pathNodeCppDraw  ] , [nodeType , nodeTypeDraw ] )
	mc.error("****CLEAN FOR RECOMPILING NODE*****")

    
print( 'BUILD TEST __________________________ PREPARE SCENE')
mc.file( pathBuildTest , i = True )


sheet            = 'sheet_GEO'
sheetShape       = mc.listRelatives( sheet     , c = True , s = True )[0]
sheetBase        = 'sheetBase_GEO'
sheetBaseShape   = mc.listRelatives( sheetBase     , c = True , s = True )[0]
polyCube         = 'polyCube1'
muscle           = 'muscle_GEO'
muscleShape      = mc.listRelatives( muscle     , c = True , s = True )[0]

print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
newNode = mc.createNode( nodeType)


print( 'BUILD TEST __________________________ CONNECT IN')

mc.connectAttr( sheetShape       + '.worldMesh[0]'  , newNode + '.mesh' )
#mc.connectAttr( sheetBaseShape   + '.worldMesh[0]'  , newNode + '.cageBase' )
mc.connectAttr( polyCube         + '.output'  , newNode + '.inMesh' )

print( 'BUILD TEST __________________________ CONNECT OUT')
mc.connectAttr(  newNode + '.uSampleNbr' , polyCube + '.subdivisionsWidth' )
mc.connectAttr(  newNode + '.vSampleNbr' , polyCube + '.subdivisionsHeight' )
mc.connectAttr(  newNode + '.outMesh'   , muscleShape + '.inMesh' ,f = True )

print( 'BUILD TEST __________________________ SET ATTR')

print( 'BUILD TEST __________________________ DONE')
mc.select(newNode)



#LOAD DRAW

print( 'BUILD TEST __________________________ PREPARE SCENE')
camera = "persp"
print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNodeCppDraw  )
print( 'BUILD TEST __________________________ CREATE NODE')
drawNode = mc.createNode( nodeTypeDraw ) 

print( 'BUILD TEST __________________________ CONNECT IN')
mc.connectAttr( ( camera + '.worldMatrix[0]' )  , '{}.camMatrix'.format( drawNode )  )
mc.connectAttr( ( newNode + '.outDraw' )  , '{}.inDraw'.format( drawNode )  )

print( 'BUILD TEST __________________________ CONNECT OUT')

print( 'BUILD TEST __________________________ SET ATTR')


print( 'BUILD TEST __________________________ DONE')
mc.select(newNode)

