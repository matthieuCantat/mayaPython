
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'meshSampler'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/meshSampler/Build/{}/meshSampler.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/meshSamplerBuildTest{}.ma'.format(lodSuffixs[highPoly])

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
	clean( [pathNode , pathNodeCppDraw  ] , [nodeType , nodeTypeDraw ] )
	mc.error("****CLEAN FOR RECOMPILING NODE*****")

    
print( 'BUILD TEST __________________________ PREPARE SCENE')
mc.file( pathBuildTest , i = True )


mesh          = 'mesh'
meshShape     = mc.listRelatives( mesh     , c = True , s = True )[0]

meshBase      = 'meshBase'
meshBaseShape = mc.listRelatives( meshBase     , c = True , s = True )[0]


print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
newNode = mc.createNode( nodeType)


print( 'BUILD TEST __________________________ CONNECT IN')

mc.connectAttr( meshShape     + '.outMesh' , newNode + '.mesh'     )
mc.connectAttr( meshBaseShape + '.outMesh' , newNode + '.meshBase' )
mc.connectAttr( 'inUV1.translateZ'     , newNode + '.inCoords[0]' )
mc.connectAttr( 'inUV1.translateX'     , newNode + '.inCoords[1]' )
mc.connectAttr( 'inUV2.translateZ'     , newNode + '.inCoords[2]' )
mc.connectAttr( 'inUV2.translateX'     , newNode + '.inCoords[3]' )
mc.connectAttr( 'inUV3.translateZ'     , newNode + '.inCoords[4]' )
mc.connectAttr( 'inUV3.translateX'     , newNode + '.inCoords[5]' )

mc.connectAttr( 'inMatrix1.worldMatrix[0]'    , newNode + '.inMatrices[0]' )
mc.connectAttr( 'inMatrix2.worldMatrix[0]'    , newNode + '.inMatrices[1]' )
mc.connectAttr( 'inMatrix3.worldMatrix[0]'    , newNode + '.inMatrices[2]' )

mc.connectAttr( 'inMatrix1.paramU'    , newNode + '.inMatricesParam[0]' )
mc.connectAttr( 'inMatrix1.paramV'    , newNode + '.inMatricesParam[1]' )
mc.connectAttr( 'inMatrix2.paramU'    , newNode + '.inMatricesParam[2]' )
mc.connectAttr( 'inMatrix2.paramV'    , newNode + '.inMatricesParam[3]' )
mc.connectAttr( 'inMatrix3.paramU'    , newNode + '.inMatricesParam[4]' )
mc.connectAttr( 'inMatrix3.paramV'    , newNode + '.inMatricesParam[5]' )

mc.connectAttr( 'inMatrix1.falloff'    , newNode + '.inMatricesFalloff[0]' )
mc.connectAttr( 'inMatrix2.falloff'    , newNode + '.inMatricesFalloff[1]' )
mc.connectAttr( 'inMatrix3.falloff'    , newNode + '.inMatricesFalloff[2]' )

print( 'BUILD TEST __________________________ CONNECT OUT')

#connectMatrix( newNode + '.outMatrices[0]' , 'outPoint1' )
#connectMatrix( newNode + '.outMatrices[1]' , 'outPoint2' )
#connectMatrix( newNode + '.outMatrices[2]' , 'outPoint3' )

print( 'BUILD TEST __________________________ SET ATTR')

mc.setAttr( newNode + '.distibutionMode' ,5);
mc.setAttr( newNode + '.meshAxeTarget'   ,1);
mc.setAttr( newNode + '.upAxeTarget'     ,1);

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




