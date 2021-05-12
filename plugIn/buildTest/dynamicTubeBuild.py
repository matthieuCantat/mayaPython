


pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE INFO
nodeType       = 'dynamicTube'  
useNodeCpp    = 1
highPoly      = 1
releaseMode   = 0
pathNodePython = 'NONE'
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:\mcantat_BDD\projects\code\maya\c++\mayaNode\\dynamicTube\Build\{}\\dynamicTube.mll'.format( releaseFolder[releaseMode] )
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/dynamicTubeBuildTest.ma'

print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("pCube1") ):
    mc.file( new = True, f= True  )
    clean( pathNode , nodeType)
    clean( pathNodeB , nodeTypeB)
    mc.error("****CLEAN FOR RECOMPILING NODE*****")
    
print( 'BUILD TEST __________________________ PREPARE SCENE')
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
clean( pathNode , nodeType)
#mc.file( pathBuildTest , i = True )

print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
newNode = mc.createNode( nodeType ) 
  
print( 'BUILD TEST __________________________ PREPARE SCENE')
nbrTest = 10
inputMatrixObjsA = createCubeTest( [ 0 , 0 , 0 ] , returnTransform = True  )
inputMatrixObjsB = createCubeTest( [ nbrTest , 0 , 0 ] , returnTransform = True  )
planeCollision   = createPlaneTest( [ 5 , -1 , 5 ] , returnTransform = True )
sphereCollision  = createSphereTest( [ 7 , 0 , 7 ] , returnTransform = True )

outputMatrixObjs = []
for i in range( 0 , nbrTest ):
    outputMatrixObjs.append( createSphereTest( [ 0 , 0 , 0 ] , returnTransform = True ) )


print( 'BUILD TEST __________________________ CONNECT IN')  

mc.connectAttr( ( inputMatrixObjsA + '.translate' ) , ( newNode + '.inputPointA' ) )
mc.connectAttr( ( inputMatrixObjsB + '.translate' ) , ( newNode + '.inputPointB' ) )
mc.connectAttr( ( planeCollision + '.translate' )   , ( newNode + '.pointPlaneCollision' ) )
mc.connectAttr( ( sphereCollision + '.translate' ) , ( newNode + '.pointSphereCollision' ) )
mc.connectAttr( ( sphereCollision + '.scaleX' ) , ( newNode + '.raySphereCollision' ) )


print( 'BUILD TEST __________________________ CONNECT OUT')

mc.setAttr( 'dynamicTube1.nbrSamples', nbrTest)
for i in range( 0 , len(outputMatrixObjs) ):
    mc.connectAttr( ( newNode + '.outPoints['+str(i)+']' ) , ( outputMatrixObjs[i] + '.translate' ) )  

print( 'BUILD TEST __________________________ SET ATTR') 

mc.setAttr( newNode + '.nbrLinkEval', 5)
mc.setAttr( newNode + '.momentumPastSample', 7)
mc.setAttr( newNode + '.momentumAverageSize', 7)
mc.setAttr( newNode + '.friction', 0.1)
mc.setAttr( newNode + '.mass', 0.01)
mc.setAttr( newNode + '.length', 1)
mc.setAttr( newNode + '.elasticity', 1)
mc.setAttr( newNode + '.repulsion', 1)
mc.setAttr( newNode + '.init', 1)
mc.setAttr( newNode + '.edgeLengthPower', 0)
mc.setAttr( newNode + '.addPower', 0)
mc.setAttr( newNode + '.smoothPower', 0)
mc.setAttr( newNode + '.relaxPower', 1)

print( 'BUILD TEST __________________________ DONE')
mc.select(newNode)

