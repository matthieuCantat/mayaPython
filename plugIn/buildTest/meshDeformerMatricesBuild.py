
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'meshDeformerMatrices'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/meshDeformerMatrices/Build/{}/meshDeformerMatrices.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/meshDeformerMatricesBuildTest{}.ma'.format(lodSuffixs[highPoly])

#__________________________ NODE DRAW INFO
nodeTypeDraw     = 'glDraw'  
pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'.format( releaseFolder[releaseMode] )

print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("mesh") ):
	clean( [pathNode , pathNodeCppDraw   ] , [nodeType , nodeTypeDraw ] )
	mc.error("****CLEAN FOR RECOMPILING NODE*****")

    
print( 'BUILD TEST __________________________ PREPARE SCENE')
mc.file( pathBuildTest , i = True )
mc.playbackOptions( min =0 , max = 400 )

mesh          = 'mesh'
meshShape     = mc.listRelatives( mesh     , c = True , s = True )[0]

meshBase      = 'meshBase'
meshBaseShape = mc.listRelatives( meshBase , c = True , s = True )[0]


print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
mc.select(mesh)
newNode = mc.deformer( type = nodeType)[0]



print( 'BUILD TEST __________________________ CONNECT IN')

#mc.connectAttr( meshShape     + '.outMesh' , newNode + '.mesh'     )
mc.connectAttr( meshBaseShape + '.outMesh' , newNode + '.meshBase' )

mc.connectAttr( 'manip1' + '.worldMatrix[0]' , newNode + '.matrices[0]' )
mc.connectAttr( 'manip2' + '.worldMatrix[0]' , newNode + '.matrices[1]' )
mc.connectAttr( 'manip3' + '.worldMatrix[0]' , newNode + '.matrices[2]' )
mc.connectAttr( 'manip4' + '.worldMatrix[0]' , newNode + '.matrices[3]' )

mc.connectAttr( 'manip1_base' + '.worldMatrix[0]' , newNode + '.matricesBase[0]' )
mc.connectAttr( 'manip2_base' + '.worldMatrix[0]' , newNode + '.matricesBase[1]' )
mc.connectAttr( 'manip3_base' + '.worldMatrix[0]' , newNode + '.matricesBase[2]' )
mc.connectAttr( 'manip4_base' + '.worldMatrix[0]' , newNode + '.matricesBase[3]' )

print( 'BUILD TEST __________________________ CONNECT OUT')

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






