



'''

#******************SOURCE******************
pythonFilePath = 'D:/mcantat_BDD/projects/code/maya/' 
import sys
sys.path.append( pythonFilePath )
#******************SOURCE******************



import maya.cmds as mc
import python
from python.plugIn.utilsMayaNodesBuild import *



cPlusPlusVersion = 1


path     = 'D:/mcantat_BDD/projects/code/maya/python/plugIn/dynamicSkin.py'
nodeType = 'dynamicSkin'

if( cPlusPlusVersion == 1 ):
    path = 'D:\mcantat_BDD\Travail\code\maya\\node\c++\mayaNode\dynamicSkin\Build\Debug\dynamicSkin.mll'
    nodeType = 'dynamicSkin'  
    fileName = 'dynamicSkin'


#NEW SCENE    
clean( path , nodeType)    
mc.loadPlugin( path  )
#BUILD LOCATORS
print('=== BUILD TEST ===')
inputGrp = mc.createNode( 'transform' , n = 'input' )
inBase = createPlaneTest( [ -5 , 0 , 2 ] , parent = inputGrp )
outMesh = createPlaneTest( [ 0 , 0 , 0 ] , parent = inputGrp )
#NEW SCENE    
mc.select( outMesh )
mc.cluster()
mc.select( outMesh )
newNode = mc.deformer(  type = nodeType )[0]     
#INPUT  
print('=== INPUT CONNECTIONS ===')   
mc.connectAttr( ( inBase + '.outMesh' ) , ( newNode + '.inBaseMesh' ) )
#mc.connectAttr( ( newNode + '.outputGeometry[0]' ) , ( outMesh + '.inMesh' ) , f = True )
#BUILD LOCATORS 

mc.deformerWeights('clusterTestWeight.xml', im=True, deformer='cluster1', path = 'D:/mcantat_BDD/projects/test/dynamics/')



mc.setAttr( newNode + '.envelope', 1 );
mc.setAttr( newNode + '.cache', 0 );
mc.setAttr( newNode + '.momentumPastSample', 1 );
mc.setAttr( newNode + '.momentumAverageSize', 1 );
mc.setAttr( newNode + '.friction', 1 );
mc.setAttr( newNode + '.mass', 0 );
mc.setAttr( newNode + '.bindElasticity', 1 );
mc.setAttr( newNode + '.pressure', 0 );
mc.setAttr( newNode + '.topoType', 0 );
mc.setAttr( newNode + '.nbrLinkEval', 1 );
mc.setAttr( newNode + '.linkElasticity', 1 );
mc.setAttr( newNode + '.linkRepulsion', 1 );
mc.setAttr( newNode + '.modeTopo', 3 );



'''






pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'dynamicSkin'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/dynamicSkin/Build/{}/dynamicSkin.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/dynamicSkinBuildTest{}.ma'.format(lodSuffixs[highPoly])

#__________________________ NODE DRAW INFO
nodeTypeDraw     = 'glDraw'  
pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'.format( releaseFolder[releaseMode] )





print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("mesh_GEO") ):
	clean( [pathNode , pathNodeCppDraw  ] , [nodeType , nodeTypeDraw ] )
	mc.error("****CLEAN FOR RECOMPILING NODE*****")

    
print( 'BUILD TEST __________________________ PREPARE SCENE')
#mc.file( pathBuildTest , i = True )

print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
inputGrp = mc.createNode( 'transform' , n = 'input' )
inBase = createPlaneTest( [ -5 , 0 , 2 ] , parent = inputGrp )
outMesh = createPlaneTest( [ 0 , 0 , 0 ] , parent = inputGrp )
#NEW SCENE    
mc.select( outMesh )
mc.cluster()
mc.select( outMesh )
newNode = mc.deformer(  type = nodeType )[0]   

print( 'BUILD TEST __________________________ CONNECT IN')
mc.connectAttr( ( inBase + '.outMesh' ) , ( newNode + '.inBaseMesh' ) )
mc.deformerWeights('clusterTestWeight.xml', im=True, deformer='cluster1', path = 'D:/mcantat_BDD/projects/test/dynamics/')


print( 'BUILD TEST __________________________ CONNECT OUT')

print( 'BUILD TEST __________________________ SET ATTR')


mc.setAttr( newNode + '.envelope', 1 );
mc.setAttr( newNode + '.cache', 0 );
mc.setAttr( newNode + '.momentumPastSample', 1 );
mc.setAttr( newNode + '.momentumAverageSize', 1 );
mc.setAttr( newNode + '.friction', 1 );
mc.setAttr( newNode + '.mass', 0 );
mc.setAttr( newNode + '.bindElasticity', 1 );
mc.setAttr( newNode + '.pressure', 0 );
mc.setAttr( newNode + '.topoType', 0 );
mc.setAttr( newNode + '.nbrLinkEval', 1 );
mc.setAttr( newNode + '.linkElasticity', 1 );
mc.setAttr( newNode + '.linkRepulsion', 1 );
mc.setAttr( newNode + '.modeTopo', 3 );


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

