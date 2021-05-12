
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'meshMirrorIndexes'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/meshMirrorIndexes/Build/{}/meshMirrorIndexes.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/meshMirrorIndexesBuildTest{}.ma'.format(lodSuffixs[highPoly])

#__________________________ NODE DRAW INFO
nodeTypeDraw     = 'glDraw'  
pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'.format( releaseFolder[releaseMode] )

print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("pSphere1") ):
	clean( [pathNode , pathNodeCppDraw   ] , [nodeType , nodeTypeDraw ] )
	mc.error("****CLEAN FOR RECOMPILING NODE*****")

    
print( 'BUILD TEST __________________________ PREPARE SCENE')
mc.file( pathBuildTest , i = True )


mesh          = 'pSphere1'
meshShape     = mc.listRelatives( mesh     , c = True , s = True )[0]

print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
mc.select(mesh)
newNode = mc.deformer( type = nodeType)[0]



print( 'BUILD TEST __________________________ CONNECT IN')

#mc.connectAttr( meshShape     + '.outMesh' , newNode + '.mesh'     )
mc.setAttr( newNode + '.middleEdgeIndex' , 629)
mc.setAttr( newNode + '.recompute' , 0)

print( 'BUILD TEST __________________________ CONNECT OUT')

print( 'BUILD TEST __________________________ SET ATTR')

print( 'BUILD TEST __________________________ DONE')
mc.select(newNode)



#TEST INIT
array      = [ int(i) for i in mc.getAttr( newNode + '.mirroredIndexes' )[0] ]
array_size = [ int(i) for i in mc.getAttr( newNode + '.mirroredIndexesSizes' )[0] ]

# GET SIDES
sides = [[],[]]
last_size = 0
for i in range(0,2):
    iStart = last_size
    iEnd   = last_size + array_size[i]
    
    for j in range(iStart,iEnd):
        sides[i].append( array[j] )
        
    last_size = iEnd

# TEST SIDES
mc.select(cl = True )
iSide = 0
for i in range(0,len(sides[iSide])):
    mc.select( '{}.vtx[{}]'.format(mesh, sides[iSide][i] ) , add = True )

mc.select(cl = True )
iSide = 1
for i in range(0,len(sides[iSide])):
    mc.select( '{}.vtx[{}]'.format(mesh, sides[iSide][i] ) , add = True )
    


# GET mirrored vtx 

mirroredVtxIndexe = []

vtxNbr = mc.polyEvaluate( mesh , v = True )
for i in range(0,vtxNbr):
    if( i in sides[0] ):
        mirroredVtxIndexe.append( sides[1][ sides[0].index(i) ] )
    elif( i in sides[1] ):
        mirroredVtxIndexe.append( sides[0][ sides[1].index(i) ] )
    else:
        mirroredVtxIndexe.append( i )
        
        
       
i =0
#TEST mirrored vtx 
mc.select( '{}.vtx[{}]'.format(mesh,i) )
mc.select( '{}.vtx[{}]'.format(mesh,mirroredVtxIndexe[i]) , add = True )
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



