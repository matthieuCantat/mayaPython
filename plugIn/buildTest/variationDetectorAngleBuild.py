
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'variationDetectorAngle'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/variationDetectorAngle/Build/{}/variationDetectorAngle.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/variationDetectorAngleBuildTest{}.ma'.format(lodSuffixs[highPoly])

#__________________________ NODE DRAW INFO
nodeTypeDraw     = 'glDraw'  
pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'.format( releaseFolder[releaseMode] )



print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("pCone1") ):
	clean( [pathNode , pathNodeCppDraw  ] , [nodeType , nodeTypeDraw ] )
	mc.error("****CLEAN FOR RECOMPILING NODE*****")

    
print( 'BUILD TEST __________________________ PREPARE SCENE')
mc.file( pathBuildTest , i = True )
mc.playbackOptions( min =0 , max = 400 )

inputObjs        = ['joint2', 'joint3' ]
outputObj        = 'pCone1'

print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
newNode = mc.createNode( nodeType)


print( 'BUILD TEST __________________________ CONNECT IN')

mc.connectAttr( inputObjs[0] + '.worldMatrix[0]'  , newNode + '.matrixA' )
mc.connectAttr( inputObjs[1] + '.worldMatrix[0]'  , newNode + '.matrixB' )

mc.connectAttr( 'time1.outTime'  , newNode + '.currentFrame_v' )
#mc.connectAttr( inputObjs[0] + '.worldMatrix[0]', newNode + '.drawMatrix' )
print( 'BUILD TEST __________________________ CONNECT OUT')
mc.connectAttr(  newNode + '.outValue' , outputObj + '.translateY' )

print( 'BUILD TEST __________________________ SET ATTR')
mc.setAttr( newNode + '.offsetA' , 1 , 0 , 0 , type = 'float3' )
mc.setAttr( newNode + '.offsetB' , 1 , 0 , 0 , type = 'float3' )

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

