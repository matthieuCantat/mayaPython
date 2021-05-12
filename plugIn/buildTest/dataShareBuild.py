
pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE INFO
nodeType       = ['dataShareA','dataShareB']  
useNodeCpp    = 1
highPoly      = 1
releaseMode   = 0
pathNodePython = 'NONE'
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/dataShare/Build/{}/dataShare.mll'.format( releaseFolder[releaseMode] )
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/aimBuildTest.ma'

print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("dataShareA1") ):
    mc.file( new = True, f= True  )
    clean( pathNode , nodeType[0])
    clean( pathNode , nodeType[1])

    mc.error("****CLEAN FOR RECOMPILING NODE*****")
    
print( 'BUILD TEST __________________________ PREPARE SCENE')
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
clean( pathNode , nodeType[0])
clean( pathNode , nodeType[1])
#mc.file( pathBuildTest , i = True )
mc.file(new=True)

print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
newNodeA = mc.createNode( nodeType[0] ) 
newNodeB = mc.createNode( nodeType[1] ) 
print( 'BUILD TEST __________________________ CONNECT IN')
mc.connectAttr( newNodeA + '.dataOut' , newNodeB + '.dataIn' )

mc.select( [newNodeA,newNodeB] )


