
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'variationDetectorMesh'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/variationDetectorMesh/Build/{}/variationDetectorMesh.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/variationDetectorMeshBuildTest{}.ma'.format(lodSuffixs[highPoly])

#__________________________ NODE DRAW INFO
nodeTypeDraw     = 'glDraw'  
pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'.format( releaseFolder[releaseMode] )

#__________________________ NODE DRAW INFO
nodeTypeWeightMap     = 'weightMap'  
pathNodeCppWeightMap  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/weightMap/Build/Release/weightMap.mll'.format( releaseFolder[releaseMode] )

print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("mesh") ):
	clean( [pathNode , pathNodeCppDraw , pathNodeCppWeightMap  ] , [nodeType , nodeTypeDraw , nodeTypeWeightMap] )
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
newNode = mc.createNode( nodeType)


print( 'BUILD TEST __________________________ CONNECT IN')

mc.connectAttr( meshShape     + '.outMesh' , newNode + '.mesh'     )
mc.connectAttr( meshBaseShape + '.outMesh' , newNode + '.meshBase' )

mc.connectAttr( 'time1.outTime'  , newNode + '.currentFrame_v' )
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








print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNodeCppWeightMap  )
print( 'BUILD TEST __________________________ CREATE NODE')
mc.select(mesh)
newNodeWM = mc.deformer( type = nodeTypeWeightMap)[0]
mc.makePaintable(  clearAll = True )
mc.makePaintable(  "weightMap" , "inWeightsDouble" ,attrType = "multiDouble" , sm ="deformer" )
mc.makePaintable(  "weightMap" , "inWeightsFloat" ,attrType = "multiFloat" , sm ="deformer" )
mc.makePaintable(  "weightMap" , "weights" ,attrType = "multiFloat" , sm ="deformer" )
mc.makePaintable(  "weightMap" , "outWeights" ,attrType = "multiFloat" , sm ="deformer" )

print( 'BUILD TEST __________________________ CONNECT IN')
mc.connectAttr( ( newNode      + '.outValuesList' )  , ( newNodeWM + '.inWeightsList'     ) )
print( 'BUILD TEST __________________________ CONNECT OUT')

print( 'BUILD TEST __________________________ SET ATTR')
mc.setAttr( newNode + '.envelope', 1)
mc.setAttr( newNode + '.cache', 0)
mc.refresh()
mc.setAttr( newNode + '.cache', 1)

print( 'BUILD TEST __________________________ DONE')
mc.select(newNode)

