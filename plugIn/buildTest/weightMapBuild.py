
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'weightMap'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/weightMap/Build/{}/weightMap.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/weightMapBuildTest{}.ma'.format(lodSuffixs[highPoly])

#__________________________ NODE DRAW INFO
nodeTypeDraw     = 'glDraw'  
pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'.format( releaseFolder[releaseMode] )





print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("reciever") ):
	clean( [pathNode , pathNodeCppDraw  ] , [nodeType , nodeTypeDraw ] )
	mc.error("****CLEAN FOR RECOMPILING NODE*****")

    
print( 'BUILD TEST __________________________ PREPARE SCENE')
mc.file( pathBuildTest , i = True )
print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )
mc.makePaintable(  clearAll = True )
mc.makePaintable(  "weightMap" , "inWeights" ,attrType = "multiFloat" , sm ="deformer" )


meshs = ['A','B','C','reciever']
nodes = []

paintIndexes = []
paintIndexes.append( range(180,200) )
paintIndexes.append( [299,279,259,239,219,199,179,159,139,119,99,79] )
paintIndexes.append( [199,218,238,258,257,277,297,296,160,140,141,121,122,102,103] )

iEnd = len(meshs) - 1

for j , mesh in enumerate(meshs):
	meshShape     = mc.listRelatives( mesh     , c = True , s = True )[0]
	print( 'BUILD TEST __________________________ CREATE NODE')
	mc.select(mesh)
	node = mc.deformer( type = nodeType )[0]
	print( 'BUILD TEST __________________________ SET ATTR')
	if( j < iEnd ):
		vtxNbr = mc.polyEvaluate(mesh , v = True)
		for i in range( 0 , vtxNbr ):
			mc.setAttr( '{}.inWeightsList[0].inWeights[{}]'.format(node,i) , 0.0 )
		for iP in paintIndexes[j]:
			mc.setAttr( '{}.inWeightsList[0].inWeights[{}]'.format(node,iP) , 1.0 )			

	nodes.append(node)
	

for i in range(0,iEnd):
	mc.connectAttr( ( nodes[i]      + '.outWeightsList[0]' )  , ( nodes[iEnd]  + '.inWeightsList[{}]'.format(i)     ) )

#LOAD DRAW

print( 'BUILD TEST __________________________ PREPARE SCENE')
camera = "persp"
print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNodeCppDraw  )
print( 'BUILD TEST __________________________ CREATE NODE')
drawNode = mc.createNode( nodeTypeDraw ) 

print( 'BUILD TEST __________________________ CONNECT IN')
mc.connectAttr( ( camera + '.worldMatrix[0]' )  , '{}.camMatrix'.format( drawNode )  )
mc.connectAttr( ( nodes[-1] + '.outDraw' )  , '{}.inDraw'.format( drawNode )  )

print( 'BUILD TEST __________________________ CONNECT OUT')

print( 'BUILD TEST __________________________ SET ATTR')


print( 'BUILD TEST __________________________ DONE')
mc.select(newNode)

