
import maya.cmds as mc

def mirrorSkin( middleEdge , debug = False ):

	mesh            = middleEdge.split('.e[')[0]
	middleEdgeIndex = int( middleEdge.split('.e[')[1][:-1] )

	pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/meshMirrorIndexes/Build/Release/meshMirrorIndexes.mll'
	nodeType       = 'meshMirrorIndexes' 


	mc.loadPlugin( pathNodeCpp  )

	mc.select(mesh)
	newNode = mc.deformer( type = nodeType)[0]

	mc.setAttr( newNode + '.middleEdgeIndex' , middleEdgeIndex)
	mc.setAttr( newNode + '.recompute' , 0)

	array = mc.getAttr( newNode + '.mirroredIndexes' )

	if( debug ):
		nodeTypeDraw     = 'glDraw'  
		pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'

		camera = "persp"
		mc.loadPlugin( pathNodeCppDraw  )
		drawNode = mc.createNode( nodeTypeDraw ) 

		mc.connectAttr( ( camera + '.worldMatrix[0]' )  , '{}.camMatrix'.format( drawNode )  )
		mc.connectAttr( ( newNode + '.outDraw' )  , '{}.inDraw'.format( drawNode )  )
	else:
		mc.delete( newNode )

	array[0][i]

i =0
#TEST
mc.select( '{}.vtx[{}]'.format(mesh,i) )
mc.select( '{}.vtx[{}]'.format(mesh,int(array[0][i])) , add = True )
i+=1




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



