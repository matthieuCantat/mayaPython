
############################################################################ BUILD RIG PUPPET

import maya.cmds as mc

attr = 'pCube1.ty'
anm = mc.listConnections(attr , s = True , d = False )[0]

breakdown    = mc.keyframe(anm, q=1, breakdown=1)
eval         = mc.keyframe(anm, q=1, eval=1)
floatChange  = mc.keyframe(anm, q=1, floatChange=1) # NONE TIME INPUT
valueChange  = mc.keyframe(anm, q=1, valueChange=1)
timeChange   = mc.keyframe(anm, q=1, timeChange =1)




inTangentType  = mc.keyTangent(anm, q=1, inTangentType =1)
outTangentType = mc.keyTangent(anm, q=1, outTangentType=1)
weightedTangents = mc.keyTangent(anm, q=1, weightedTangents=1)
mc.keyTangent(anm, e=1, weightedTangents=1)
ix = mc.keyTangent(anm, q=1, ix=1)
iy = mc.keyTangent(anm, q=1, iy=1)
ox = mc.keyTangent(anm, q=1, ox=1)
oy = mc.keyTangent(anm, q=1, oy=1)
#mc.keyTangent(anm, e=1, weightedTangents=weightedTangents)


inAngle        = mc.keyTangent(anm, q=1, inAngle=1)
inWeight       = mc.keyTangent(anm, q=1, inWeight=1)
lock           = mc.keyTangent(anm, q=1, lock=1)
outAngle       = mc.keyTangent(anm, q=1, outAngle=1)
outWeight      = mc.keyTangent(anm, q=1, outWeight=1)

weightLock = mc.keyTangent(anm, q=1, weightLock=1)

for i in range(0,len(inTangentType)):
    print('_____________ {}'.format(i) )
    print('IN')
    print('type : {}'.format( inTangentType[i] ) )
    print('x    : {}'.format( ix[i] ) )
    print('y    : {}'.format( iy[i] ) )
    print('a    : {}'.format( inAngle[i] ) )
    print('w    : {}'.format( inWeight[i] ) )
    print('_____________ {}'.format(i) )
    print('OUT')
    print('type : {}'.format( outTangentType[i] ) )
    print('x    : {}'.format( ox[i] ) )
    print('y    : {}'.format( oy[i] ) )
    print('a    : {}'.format( outAngle[i] ) )
    print('w    : {}'.format( outWeight[i] ) )