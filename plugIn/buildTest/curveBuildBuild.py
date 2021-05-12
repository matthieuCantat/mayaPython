
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'curveBuild'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/curveBuild/Build/{}/curveBuild.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/curveBuildBuildTest.ma'

#__________________________ NODE DRAW INFO
nodeTypeDraw     = 'glDraw'  
pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'.format( releaseFolder[releaseMode] )



print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("locator1") ):
	clean( [pathNode , pathNodeCppDraw  ] , [nodeType , nodeTypeDraw ] )
	mc.error("****CLEAN FOR RECOMPILING NODE*****")




print( 'BUILD TEST __________________________ PREPARE SCENE')
mc.file( pathBuildTest , i = True )

drivers    = mc.ls( "locator*" , type = "transform" )
curve      = mc.curve( n = "curveOut" , d = 3 , p=[(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0)] , k=[ 0 , 0 , 0 , 1 , 1 , 1 ] ) ;
curveShape = mc.listRelatives( curve , s = True , c = True )[0]

print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
newNode = mc.createNode( nodeType ) 

print( 'BUILD TEST __________________________ CONNECT IN')
for i in range( 0 , len( drivers ) ) :
	mc.connectAttr( ( drivers[i] + '.worldMatrix[0]' )  , '{}.matrices[{}]'.format( newNode , i)  )

print( 'BUILD TEST __________________________ CONNECT OUT')
mc.connectAttr( ( newNode + '.curve' ) , ( curveShape + '.create' ) )  

print( 'BUILD TEST __________________________ SET ATTR')
mc.setAttr( newNode + '.mode'     , 0)
mc.setAttr( newNode + '.degree'   , 3)
mc.setAttr( newNode + '.isClose'  , 0)
mc.setAttr( newNode + '.offsetAxe', 1)
mc.setAttr( newNode + '.offset'   , 0)

print( 'BUILD TEST __________________________ DONE')
mc.select(newNode)



mc.setAttr( "curveShape1.lineWidth" , 5)




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

