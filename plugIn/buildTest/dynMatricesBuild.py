
import maya.cmds as mc

def getlinksIndexes( links , linksSearch ):
    indexes = []
    for i in range( 0 , len(linksSearch) ):
        for j in range( 0 , len(links) ):
            linksearch = linksSearch[i]
            edge       = links[j]
            linksearch.sort()
            edge.sort()
            if( edge == linksearch ):
                indexes.append(j)
                break
                
    return indexes    

def getAttatchlinks( links , attachPoints , skipAttachPointsEdge = True ):
    attachlinks = []
    for edge in links:
        if(   edge[0] in attachPoints ) and ( edge[1] in attachPoints ):
            if(skipAttachPointsEdge == False):
                attachlinks.append(edge)             
        elif( edge[0] in attachPoints ) or  ( edge[1] in attachPoints ):
            attachlinks.append(edge)
    return attachlinks

#####################################################################################

pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE DISPLAY
useNodeCpp    = 1
highPoly      = 0
releaseMode   = 1 # tbb doesnt have a debug mode
pathNodePython = 'NONE'
#__________________________ NODE INFO
nodeType       = 'dynMatrices'  
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/dynMatrices/Build/{}/dynMatrices.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/dynMatricesBuildTest{}.ma'.format(lodSuffixs[highPoly])

#__________________________ NODE DRAW INFO
nodeTypeDraw     = 'glDraw'  
pathNodeCppDraw  = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/Release/glDraw.mll'.format( releaseFolder[releaseMode] )



print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("loc0") ):
    clean( [pathNode , pathNodeCppDraw  ] , [nodeType , nodeTypeDraw ] )
    mc.error("****CLEAN FOR RECOMPILING NODE*****")

    
print( 'BUILD TEST __________________________ PREPARE SCENE')
mc.file( pathBuildTest , i = True )

inLocs      = [ 'loc{}'.format(i)      for i in range(0,59) ]
inBaseLocs  = [ 'locBase{}'.format(i)  for i in range(0,59) ]
outLocs     = [ 'locOut{}'.format(i)   for i in range(0,59) ]










#INIT MAPS




# ORIGIN ATTRACT
#for i in [0,2,6,7    ]: pointsOriginAttract[i]  = 1.0

# MASS 







print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
newNode = mc.createNode( nodeType)


print( 'BUILD TEST __________________________ CONNECT IN')


mc.connectAttr( 'time1.outTime'  , newNode + '.currentFrame' )

print( 'BUILD TEST __________________________ CONNECT OUT')

for i in range(0,len(outLocs)):
    connectMatrix( '{}.outMatrices[{}]'.format( newNode , i) , outLocs[i] )



print( 'BUILD TEST __________________________ SET ATTR - MATRICES INFO')

# GET INFO
matricesShapes    = [ 'sphere' for i in range(0,len(inLocs)) ]
matricesRay       = [ 0.1      for i in range(0,len(inLocs)) ]
matricesMass      = [ 1.0      for i in range(0,len(inLocs)) ]
matricesFriction  = [ 0.1      for i in range(0,len(inLocs)) ]
matricesAttract   = [ 0.0      for i in range(0,len(inLocs)) ]
matricesCaches    = [ 0.0      for i in range(0,len(inLocs)) ]


for i in [22,23,25,26,28]:
    matricesMass[i] = 50.0

for i in [56,57,58]:
    matricesShapes[i]   = 'sphere'    
    matricesRay[i]      = 2.0
    matricesFriction[i] = 1.0    
    matricesAttract[i]  = 1.0
    matricesCaches[i]   = 0.0

# SET INFO
for i in range(0,len(inLocs)):
    mc.connectAttr( '{}.worldMatrix[0]'.format(inLocs[i]    ) , newNode + '.matrices_anim[{}]'.format(i)     )
    mc.connectAttr( '{}.worldMatrix[0]'.format(inBaseLocs[i]) , newNode + '.matrices_base[{}]'.format(i) )

    mc.setAttr(     '{}.matrices_shapes[{}]'.format(             newNode,i)    , matricesShapes[i] , type = 'string')
    mc.setAttr(     '{}.matrices_rays[{}]'.format(               newNode,i)    , matricesRay[i]                     )
    mc.setAttr(     '{}.matrices_masses[{}]'.format(             newNode,i)    , matricesMass[i]                    )    
    mc.setAttr(     '{}.matrices_frictions[{}]'.format(          newNode,i)    , matricesFriction[i]                )
    mc.setAttr(     '{}.matrices_animPointAttracts[{}]'.format(  newNode,i)    , matricesAttract[i]                 )
    mc.setAttr(     '{}.matrices_animOrientAttracts[{}]'.format( newNode,i)    , matricesAttract[i]                 )
    mc.setAttr(     '{}.matrices_caches[{}]'.format(             newNode,i)    , matricesCaches[i]                  )


print( 'BUILD TEST __________________________ SET ATTR - LINKS')

# GET INFO
objLinkIndexes_edges  = [[0, 1], [0, 3], [0, 9], [1, 2], [1, 4], [1, 10], [2, 5], [2, 11], [3, 4], [3, 6], [3, 12], [4, 5], [4, 7], [4, 13], [5, 8], [5, 14], [6, 7], [6, 15], [7, 8], [7, 16], [8, 17] ]
objLinkIndexes_edges += [[9, 10], [9, 12], [9, 18], [10, 11], [10, 13], [10, 19], [11, 14], [11, 20], [12, 13], [12, 15], [12, 21], [13, 14], [13, 16], [13, 22], [14, 17], [14, 23], [15, 16], [15, 24], [16, 17], [16, 25], [17, 26] ] 
objLinkIndexes_edges += [[18, 19], [18, 21], [19, 20], [19, 22], [20, 23], [21, 22], [21, 24], [22, 23], [22, 25], [23, 26], [24, 25], [25, 26]] # 

objLinkIndexes_faceDiag    = [[0,4],[1,3],[1,5],[2,4],[3,7],[4,6],[4,8],[5,7],[9,13],[10,12],[10,14],[11,13],[12,16],[13,15],[13,17],[14,16],[18,22],[19,21],[19,23],[20,22],[21,25],[22,24],[22,26],[23,25]]
objLinkIndexes_faceDiag   += [[20,14],[23,11],[23,17],[26,14],[11,5],[14,2],[14,8],[17,5],[19,13],[22,10],[22,16],[25,13],[10,4],[13,1],[13,7],[16,4],[18,12],[21,9],[21,15],[24,12],[9,3],[12,0],[12,6],[15,3]] 
objLinkIndexes_faceDiag   += [[18,10],[19,9],[19,11],[20,10],[9,1],[10,0] ,[10,2] ,[11,1] ,[21,13],[22,12],[22,14],[23,13],[12,4],[13,3],[13,5],[14,4],[24,16],[25,15],[25,17],[26,16],[15,7] ,[16,6],[16,8],[17,7]] 

objLinkIndexes_volumeDiag  = [[9 ,4 ],[13,0 ],[10,3 ],[12,1 ],[10,5 ],[14,1 ],[4 ,11],[13,2 ],[12,7 ],[16,3 ],[13,6 ],[4 ,15],[13,8 ],[17,4 ],[14,7 ],[16,5]]
objLinkIndexes_volumeDiag += [[18,13],[22,9 ],[19,12],[21,10],[19,14],[23,10],[20,13],[22,11],[22,15],[24,13],[21,16],[25,12],[22,17],[26,13],[23,16],[14,25]]

objLinkIndexes_A = objLinkIndexes_edges + objLinkIndexes_faceDiag + objLinkIndexes_volumeDiag

iShift = 29
objLinkIndexes_B = []
for i in range(0,len(objLinkIndexes_A)):
    objLinkIndexes_B.append( [ objLinkIndexes_A[i][0]+iShift , objLinkIndexes_A[i][1]+iShift ] )

links = objLinkIndexes_A + objLinkIndexes_B
links_flatten = [ i for link in links for i in link]


linksShapePreserve  = [ 1.0 for i in range(0,len(links))  ]
linksLengthPreserve = [ 1.0 for i in range(0,len(links))  ]

btwMatlinks        = getAttatchlinks( links , [22,23,25,26,28] , skipAttachPointsEdge = True)
btwMatlinksIndexes = getlinksIndexes( links ,btwMatlinks )

for i in btwMatlinksIndexes: linksShapePreserve[i] = 0.1
for i in btwMatlinksIndexes: linksLengthPreserve[i] = 1.0



#SET INFO

for i in range(0,len(links_flatten)):
    mc.setAttr( '{}.links_matricesIndexes[{}]'.format(newNode,i)    , links_flatten[i] )

for i in range(0,len(links)):
    mc.setAttr( '{}.links_keepAnglePoints[{}]'.format(newNode,i)    , linksShapePreserve[i] )
    mc.setAttr( '{}.links_keepLengthPoints[{}]'.format(newNode,i)   , linksLengthPreserve[i] )    




print( 'BUILD TEST __________________________ SET ATTR FACE')
# FACE
faces_center = 13

faces  = [0 ,1,4 ,0 ,3 ,4 ,1 ,2 ,5 ,1 ,4 ,5 ,3 ,4 ,7 ,3 ,6 ,7 ,4 ,5 ,8 ,4 ,7 ,8 ]## TOP
faces += [24,25,22,24,21,22,25,26,23,25,22,23,21,22,19,21,18,19,22,23,20,22,19,20 ]## BOTOM
faces += [18,19,10,18,9 ,10,19,20,11,19,10,11,9 ,10,1 ,9 ,0 ,1 ,10,11,2 ,10,1 ,2 ]## FACE
faces += [26,25,16,26,17,16,17,8 ,7 ,17,16,7 ,25,24,15,25,16,15,16,7 ,6 ,16,15,6 ]## BACK
faces += [20,23,14,20,11,14,23,26,17,23,14,17,11,2 ,5 ,11,14,5 ,14,5 ,8 ,14,17,8 ]## LEFT
faces += [24,21,12,24,15,12,21,18,9 ,21,12,9 ,15,12,3 ,15,6 ,3 ,12,3 ,0 ,12,9 ,0 ]## RIGHT

facesBuildIndexes = []
for i in range(0,len(faces),3):
    facesBuildIndexes += [ faces[i],faces[i+1],faces[i+2]]

faceNormalsBuildIndexes = []
for i in range(0,len(faces),3):
    faceNormalsBuildIndexes.append(13)


faces_B = [ face+iShift for face in facesBuildIndexes]
facesBuildIndexes += faces_B

facesNormal_B = [ face+iShift for face in faceNormalsBuildIndexes]
faceNormalsBuildIndexes += facesNormal_B




for i in range(0,len(facesBuildIndexes)):
    mc.setAttr( '{}.faces_matricesIndexes[{}]'.format(newNode,i)    , facesBuildIndexes[i] )
for i in range(0,len(faceNormalsBuildIndexes)):    
    mc.setAttr( '{}.facesNormals_matricesIndexes[{}]'.format(newNode,i)    , faceNormalsBuildIndexes[i] )




print( 'BUILD TEST __________________________ SET ATTR OBJS')

# OBJ

objsIndexes_objA = range(0,27)
objsIndexes_objB = [ i+iShift for i in objsIndexes_objA]

objsBuildIndexes = objsIndexes_objA + objsIndexes_objB    
objsBuildIndexesSize = [ len(objsIndexes_objA) , len(objsIndexes_objB)] 

objsFrictions = [ 0.1 , 0.1 ]

for i in range(0,len(objsBuildIndexes)):
    mc.setAttr( '{}.objs_matricesIndexes[{}]'.format(newNode,i)    , objsBuildIndexes[i] )
for i in range(0,len(objsBuildIndexesSize)):    
    mc.setAttr( '{}.objs_matricesIndexesSize[{}]'.format(newNode,i)    , objsBuildIndexesSize[i] )
for i in range(0,len(objsFrictions)):    
    mc.setAttr( '{}.objs_frictions[{}]'.format(newNode,i)    , objsFrictions[i] )    






mc.setAttr( newNode + '.cache' ,0)
mc.refresh()
mc.setAttr( newNode + '.cache', 1)


mc.setAttr( newNode + '.startFrame' ,3);
mc.setAttr( newNode + '.gravity'    ,0.1);




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




#COLLISION TEST


#COLLISION TEST
mc.setAttr( "dynMatrices1.drawCollide" ,1)

mc.setAttr( "dynMatrices1.lengthPreserveAttract" ,0)
mc.setAttr( "dynMatrices1.originAttract" ,0)
mc.setAttr( "dynMatrices1.shapePreserveAttract" ,0)
mc.setAttr( "dynMatrices1.lengthPreserveLimits" ,0)




