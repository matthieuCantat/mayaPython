
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE INFO
nodeType       = 'glDraw'  
useNodeCpp    = 1
highPoly      = 1
releaseMode   = 1
pathNodePython = 'NONE'
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/{}/glDraw.mll'.format( releaseFolder[releaseMode] )
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/glDrawBuildTest.ma'

print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("vector1") ):
    clean( [pathNode  ] , [nodeType  ] )
    mc.error("****CLEAN FOR RECOMPILING NODE*****")
    
print( 'BUILD TEST __________________________ PREPARE SCENE')
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
mc.file( pathBuildTest , i = True )

camera = "persp"
visTrigGeo = "pCube1"
VectorDrivers    = mc.ls( "vector*" , type = "transform" )

print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
newNode = mc.createNode( nodeType ) 

print( 'BUILD TEST __________________________ CONNECT IN')
mc.connectAttr( ( camera + '.worldMatrix[0]' )  , '{}.camMatrix'.format( newNode )  )

for i in range( 0 , len( VectorDrivers ) ) :
	mc.connectAttr( ( VectorDrivers[i] + '.translate' )  , '{}.coords[{}]'.format( newNode , i)  )

mc.connectAttr( ('pCube1.worldMatrix[0]' )      , '{}.attributesMatrix'.format( newNode )  )
mc.connectAttr( ('pCube1.translateX' )      , '{}.attributes[0]'.format( newNode )  )
mc.connectAttr( ('pCube1.rotateX' )      , '{}.attributes[1]'.format( newNode )  )
mc.connectAttr( ( 'pCube1.colors' )      , '{}.attributes[2]'.format( newNode )  )

print( 'BUILD TEST __________________________ CONNECT OUT')

print( 'BUILD TEST __________________________ SET ATTR')
mc.setAttr( newNode + '.shapes[0]'     , 2)
mc.setAttr( newNode + '.sizes[0]'      , 1)
mc.setAttr( newNode + '.colors[0]'     , 0,1,0 , type = "double3" )
mc.setAttr( newNode + '.names[0]'      , "test" , type = "string" )
mc.setAttr( newNode + '.fills[0]'      , True )
mc.setAttr( newNode + '.spaces[0]'      , 1 )
mc.setAttr( newNode + '.projPlanes[0]'      , 1 )
mc.setAttr( newNode + '.maxMemories[0]'   , 0 )

mc.setAttr( newNode + '.shapes[1]'     , 3)
mc.setAttr( newNode + '.sizes[1]'      , 1)
mc.setAttr( newNode + '.colors[1]'     , 0,1,0 , type = "double3" )
mc.setAttr( newNode + '.names[1]'      , "test" , type = "string" )
mc.setAttr( newNode + '.fills[1]'      , True )
mc.setAttr( newNode + '.spaces[1]'      , 1 )
mc.setAttr( newNode + '.projPlanes[1]'      , 1 )
mc.setAttr( newNode + '.maxMemories[1]'   , 0 )


mc.setAttr( newNode + '.shapes[2]'     , 10)
mc.setAttr( newNode + '.sizes[2]'      , 1)
mc.setAttr( newNode + '.colors[2]'     , 0,1,0 , type = "double3" )
mc.setAttr( newNode + '.names[2]'      , "test" , type = "string" )
mc.setAttr( newNode + '.fills[2]'      , True )
mc.setAttr( newNode + '.spaces[2]'      , 1 )
mc.setAttr( newNode + '.projPlanes[2]'      , 1 )
mc.setAttr( newNode + '.maxMemories[2]'   , 0 )

print( 'BUILD TEST __________________________ DONE')
mc.select(newNode)


