
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'curveSampler'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/curveSampler/Build/{}/curveSampler.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/curveSamplerBuildTest{}.ma'.format(lodSuffixs[highPoly])

#__________________________ NODE DRAW INFO
nodeTypeDraw     = 'glDraw'  
pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'.format( releaseFolder[releaseMode] )



print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("curve") ):
	clean( [pathNode , pathNodeCppDraw  ] , [nodeType , nodeTypeDraw ] )
	mc.error("****CLEAN FOR RECOMPILING NODE*****")

    
print( 'BUILD TEST __________________________ PREPARE SCENE')
mc.file( pathBuildTest , i = True )


curve            = 'curve'
curveShape       = mc.listRelatives( curve     , c = True , s = True )[0]
upCurve          = 'upCurve'
upCurveShape     = mc.listRelatives( upCurve     , c = True , s = True )[0]
curveBase        = 'curveBase'
curveBaseShape   = mc.listRelatives( curveBase     , c = True , s = True )[0]
upCurveBase      = 'upCurveBase'
upCurveBaseShape = mc.listRelatives( upCurveBase     , c = True , s = True )[0]

print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
newNode = mc.createNode( nodeType)


print( 'BUILD TEST __________________________ CONNECT IN')

mc.connectAttr( curveShape       + '.worldSpace[0]' , newNode + '.curve' )
mc.connectAttr( upCurveShape     + '.worldSpace[0]' , newNode + '.upCurve' )
mc.connectAttr( curveBaseShape   + '.worldSpace[0]' , newNode + '.curveBase' )
mc.connectAttr( upCurveBaseShape + '.worldSpace[0]' , newNode + '.upCurveBase' )

mc.connectAttr(  'locator1.worldMatrix[0]' , newNode + '.matrices[0]' )
mc.connectAttr(  'locator1.param'          , newNode + '.matricesParams[0]' )
mc.connectAttr(  'locator2.worldMatrix[0]' , newNode + '.matrices[1]' )
mc.connectAttr(  'locator2.param'          , newNode + '.matricesParams[1]' )
mc.connectAttr(  'locator3.worldMatrix[0]' , newNode + '.matrices[2]' )
mc.connectAttr(  'locator3.param'          , newNode + '.matricesParams[2]' )

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

