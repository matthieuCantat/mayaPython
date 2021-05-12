'''


pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE INFO
nodeType       = 'textOverlay'  
useNodeCpp    = 0
highPoly      = 1
releaseMode   = 1
pathNodePython = r'D:\mcantat_BDD\projects\code\maya\python\plugIn\nodes\textOverlay.py'
releaseFolder = ['Debug','Release']
pathNodeCpp    = 'D:/mcantat_BDD/projects/code/maya/c++/mayaNode/glDraw/Build/{}/glDraw.mll'.format( releaseFolder[releaseMode] )
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
#__________________________ BUILD TEST INFO
lodSuffixs = [ 'Low' , 'High' ]
pathBuildTest = 'D:/mcantat_BDD/projects/nodeTest/annotatePyBuildLow.ma'

print( 'BUILD TEST __________________________ SOURCE')
import sys
sys.path.append( pathPythonFiles )
import python
import maya.cmds as mc
from python.plugIn.utilsMayaNodesBuild import *


if( mc.objExists("locator1") ):
    clean( [pathNode  ] , [nodeType  ] )
    mc.error("****CLEAN FOR RECOMPILING NODE*****")
    
print( 'BUILD TEST __________________________ PREPARE SCENE')
pathNode   = [ pathNodePython , pathNodeCpp ][useNodeCpp]
mc.file( pathBuildTest , i = True )

camera = "persp"
visTrigGeo = "pCube1"
VectorDrivers    = mc.ls( "vector*" , type = "transform" )

print( 'BUILD TEST __________________________ LOAD NODE')
mc.loadPlugin( pathNode  )

print( 'BUILD TEST __________________________ CREATE NODE')
newNode = mc.createNode( nodeType ) 

mc.setAttr( "perspShape.nearClipPlane" , 10 )

size_letter = 20
size_inter  = 30
pos_h_up , pos_h_dn = 5  , 1070
pos_w_l  , pos_w_r  = 10 , 1910 

x = pos_w_r - 80
y = pos_h_up + size_inter*0.7
mc.setAttr( newNode + '.coords[0]'     ,   x, y      ,0 , type = "double3" )
mc.setAttr( newNode + '.sizes[0]'      , size_letter)
mc.setAttr( newNode + '.colors[0]'     , 1,1,1 , type = "double3" )
mc.setAttr( newNode + '.names[0]'      , "TANG"  , type = "string" )

x = pos_w_l
y = pos_h_up + size_inter*0.7
mc.setAttr( newNode + '.coords[1]'     , x, y      ,0 , type = "double3" )
mc.setAttr( newNode + '.sizes[1]'      , size_letter)
mc.setAttr( newNode + '.colors[1]'     , 1,1,1 , type = "double3" )
mc.setAttr( newNode + '.names[1]'      , "Extra - Student-girl-A"  , type = "string" )

x = pos_w_l
y = pos_h_up + size_inter*1.4
mc.setAttr( newNode + '.coords[2]'     , x, y      ,0, type = "double3" )
mc.setAttr( newNode + '.sizes[2]'      , size_letter*0.7)
mc.setAttr( newNode + '.colors[2]'     , 1,1,1 , type = "double3" )
mc.setAttr( newNode + '.names[2]'      , "Work 042 - Publish 120" , type = "string" )

x = pos_w_l
y = pos_h_dn - size_inter*0.8
mc.setAttr( newNode + '.coords[3]'     , x, y      ,0 , type = "double3" )
mc.setAttr( newNode + '.sizes[3]'      , size_letter)
mc.setAttr( newNode + '.colors[3]'     , 1,1,1 , type = "double3" )
mc.setAttr( newNode + '.names[3]'      , "Publish - check - comment" , type = "string" )

x = pos_w_l
y = pos_h_dn-size_inter*0 
mc.setAttr( newNode + '.coords[4]'     , x, y      ,0 , type = "double3" )
mc.setAttr( newNode + '.sizes[4]'      , size_letter*0.8)
mc.setAttr( newNode + '.colors[4]'     , 1,1,1 , type = "double3" )
mc.setAttr( newNode + '.names[4]'      , "//jad_server/projets/jade-armor/jad_tang/scenes/anim/characterisations/characterisations_jade-run/publish/jad_anim_characterisations_jade-run_v003.shot (ADJUSTED)" , type = "string" )




'''
import sys
sys.path.append('D:/mcantat_BDD/projects/code/maya')

import maya.api.OpenMaya as ompy
import maya.cmds as mc
import maya.api.OpenMayaRender as ompyr
import maya.api.OpenMayaUI as ompyui
import maya.OpenMayaMPx as ompx
import maya.OpenMaya as om
import maya.OpenMayaRender as omr
import time
import math
import copy


#import python.plugIn.utilsMayaNodes as utils

'''
glRenderer = ompyr.MHardwareRenderer.theRenderer()
glFT = glRenderer.glFunctionTable()
'''

shapesNames            = ["segment", "triangle", "pointTriangle" , "pointSquare", "pointCircle", "pointStar", "pointCross", "vector"  , "text" ]
shapeToNbrElemForBuild = [ 2       , 3         ,  1              , 1            , 1            , 1          , 1           , 2         , 1      ]


######################## WTF MAYA...
def maya_useNewAPI():
    pass
######################## WTF MAYA...


class textOverlay(ompyui.MPxLocatorNode):

    name = 'textOverlay'
    id = ompy.MTypeId(0x00033448)
    drawDbClassification = "drawdb/geometry/textOverlay"
    drawRegistrantId     = "textOverlayNodePlugin"

    def __init__(self):
        print('textOverlay.__init__')
        ompyui.MPxLocatorNode.__init__(self)  
  
    def compute( self, plug , dataBlock ):
        print('textOverlay.compute') 
        return 1
 
    @classmethod
    def creator(cls):
        print('creator')
        return cls()

    @classmethod
    def initialize(cls):
        print('initialize')
        nData = ompy.MFnNumericData()
        cData = ompy.MFnNurbsCurveData() 
        mData = ompy.MFnMeshData() 
        sData = ompy.MFnStringData()

        nAttr = ompy.MFnNumericAttribute()  
        eAttr = ompy.MFnEnumAttribute()
        mAttr = ompy.MFnMatrixAttribute()
        gAttr = ompy.MFnGenericAttribute()
        tAttr = ompy.MFnTypedAttribute()  
        sAttr = ompy.MFnTypedAttribute()

        cls.inAttrs = []
        # OUT ATTR    
        cls.inAttrs.append( nAttr.createPoint( 'coords' , 'coords' ) )    
        nAttr.array = True
        nAttr.usesArrayDataBuilder = True

        cls.inAttrs.append( nAttr.create( 'sizes', 'sizes', nData.kFloat, 1.0 ) )
        nAttr.array = True
        nAttr.usesArrayDataBuilder = True

        cls.inAttrs.append( nAttr.createPoint( 'colors' , 'colors' ) )    
        nAttr.array = True
        nAttr.usesArrayDataBuilder = True


        cls.inAttrs.append( tAttr.create( 'names' , 'names', sData.kString ) )    
        tAttr.array = True
        tAttr.usesArrayDataBuilder = True   

        for i in range( 0 , len( cls.inAttrs ) ):
            cls.addAttribute( cls.inAttrs[i] )
         

def initializePlugin(obj):  
    print('initializePlugin' , obj ) 
    plugin = ompy.MFnPlugin( obj )
    plugin.registerNode( textOverlay.name, textOverlay.id, textOverlay.creator, textOverlay.initialize, ompy.MPxNode.kLocatorNode , textOverlay.drawDbClassification )
    ompyr.MDrawRegistry.registerDrawOverrideCreator(textOverlay.drawDbClassification, textOverlay.drawRegistrantId, textOverlayDrawOverride.Creator)



def uninitializePlugin(obj):
    print('uninitializePlugin')  
    plugin = ompy.MFnPlugin(obj)
    try:
        ompyr.MDrawRegistry.deregisterDrawOverrideCreator(textOverlay.drawDbClassification, textOverlay.drawRegistrantId)
    except:
        raise Exception('Failed to unregister node: {0}'.format(textOverlay.name) )

    try:
        plugin.deregisterNode( textOverlay.id )
    except:
        raise Exception('Failed to unregister node: {0}'.format(textOverlay.name) )




###############################################################################################################   
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################



class textOverlayDrawOverride(ompyr.MPxDrawOverride):


    def __init__(self , obj ):
        ompyr.MPxDrawOverride.__init__( self , obj , None )  

    @classmethod
    def Creator(cls,obj):
        print('textOverlayDrawOverride.creator' )
        return cls(obj)

    '''
    def OnModelEditorChanged( self , clientData):
        print( clientData )
    '''

    def prepareForDraw( self , objPath, cameraPath, frameContext, oldData):
        DEBUG_C = 1
        if (DEBUG_C): print("glDrawDrawOverride________________________________________PREPARE - GET FROM MAYA")
        #DISPLAY
        coords             = dagPath_getAttrMFloatVectorArray( objPath, textOverlay.inAttrs[0] )
        sizes              = dagPath_getAttrFloatArray(        objPath, textOverlay.inAttrs[1] )
        colors             = dagPath_getAttrMFloatPointArray(  objPath, textOverlay.inAttrs[2] )
        names              = dagPath_getAttrMStringArray(      objPath, textOverlay.inAttrs[3] )

    
        if (DEBUG_C): print("glDrawDrawOverride________________________________________ CREATE DATA")
        data = oldData

        if( data == None ):
            data = textOverlayData()
        if (DEBUG_C): print("glDrawDrawOverride________________________________________PREPARE - FILL DATA ATTR")
    
        #FILL DATA ATTR
        data.coords             = coords
        data.sizes              = sizes
        data.colors             = colors
        data.names              = names
    
        data.cameraPath         = ompy.MDagPath(cameraPath)

        return data
    
    def hasUIDrawables( self ):
        return True
    
    def addUIDrawables( self , objPath, drawManager, frameContext, data):
        DEBUG_C = 1

        size_coef = 0.5

        if (DEBUG_C): print("glDrawDrawOverride________________________________________addUIDrawables - GET DATA");

        cameraFn             = ompy.MFnCamera(data.cameraPath)
        cameraTrsf           = ompy.MFnDagNode(cameraFn.parent(0))

        camMatrix            = cameraTrsf.transformationMatrix()

        # GET CAMERA WORLD MATRIX
        camParent = ompy.MFnDagNode(cameraTrsf.parent(0) )
        lap = 0

        while ( 0 < camParent.parentCount() ):
            camMatrix = camMatrix*camParent.transformationMatrix() 
            camParent = ompy.MFnDagNode(camParent.parent(0))
            lap += 1
            if( 500 < lap ):
                break

        camMatrix = MMatrixToMFloatMatrix( camMatrix )


        camPlaneNearDistance = cameraFn.nearClippingPlane

        focal_length         = cameraFn.focalLength
        h_film_aperture      = cameraFn.horizontalFilmAperture
        h_angle_of_view , v_angle_of_view = camera_get_angles_of_view( h_film_aperture , focal_length)


        cMatrix = camMatrix
        camVX = ompy.MFloatVector( camMatrix[0], camMatrix[1], camMatrix[2] )
        camVY = ompy.MFloatVector( camMatrix[4], camMatrix[5], camMatrix[6] )
        camVZ = ompy.MFloatVector( camMatrix[8], camMatrix[9], camMatrix[10] )

        vDepthOffset = camVZ * camPlaneNearDistance *-1
      
        upHalfDist   = camPlaneNearDistance * math.tan( math.radians(v_angle_of_view/2.0) )
        sideHalfDist = camPlaneNearDistance * math.tan( math.radians(h_angle_of_view/2.0) )

        vUpOffset   = camVY * upHalfDist
        vSideOffset = camVX * sideHalfDist *-1

        pScreenO = ompy.MFloatPoint( cMatrix[12], cMatrix[13], cMatrix[14] ) + vDepthOffset + vUpOffset + vSideOffset 
        vScreenX = camVX
        vScreenY = camVY *-1

        vScreenX.normalize()
        vScreenY.normalize()


        if (DEBUG_C): print("glDrawDrawOverride________________________________________addUIDrawables - DRAW");
        drawManager.beginDrawable()
    
        iCoords = 0
        exitDrawing = False

        vDist   = upHalfDist  *2
        hDist   = sideHalfDist*2
    
        distIncr        = 0.001
        foregroundDist  =  0.02

        ssOffsets = ompy.MFloatPoint(0.0,0.0,0.0)
        for i in range( 0 , len(data.coords) ):
            
            screenCoords = pScreenO + (data.coords[i][0]/ 1920.0 )*hDist * vScreenX + (data.coords[i][1] / 1080.0 )*vDist * vScreenY + camVZ * foregroundDist  *-1
            new_size = data.sizes[i] * size_coef 
            glDrawText( drawManager, camMatrix, [ screenCoords ] , [ssOffsets] , data.names[i] , data.colors[i], True, new_size , 1.0)     
            foregroundDist += distIncr  
        
        drawManager.endDrawable()



###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################



class textOverlayData( ompy.MUserData ):

    def __init__(self):
        ompy.MUserData.__init__(self , False) 
        self.setDeleteAfterUse(False)# don;t delete after draw
        self.shapes = [] #vector<int>
        self.coords = ompy.MFloatVectorArray() #MFloatVectorArray
        self.screenSpaceOffsets = ompy.MFloatVectorArray() #MFloatVectorArray
        self.sizes = [] #vector<float> 
        self.thicknesses = [] #vector<float> 
        self.colors = ompy.MFloatPointArray() #MFloatPointArray
        self.pColors = [] #vector<MFloatPointArray>
        self.names = [] #vector<MString>
        self.fills = [] #vector<bool>
        self.spaces = [] #vector<int>
        self.maxMemorys = [] #vector<int>
        self.projPlanes = [] #vector<int>
        self.drawPlaneMode = 0 #int
        self.cameraPath = ompy.MDagPath() #MDagPath
    
        self.attrMatrix = ompy.MFloatMatrix() #MFloatMatrix
        self.attrNames = []  #vector<MString>
        self.attrValueType = []  #vector<MString>
        self.attrValueInt = []  #vector<int>
        self.attrValueFloat = []  #vector<float>
        self.attrValueDouble = []  #vector<double>
        self.attrValueEnum = []  #vector<MString>

###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################


def dagPath_getAttrInt( objPath, Attr ):
    out_value = 0

    node = objPath.node()
    plug = ompy.MPlug(node, Attr)
    if ( plug.isNull == False ):
        out_value = plug.asInt()

    return out_value

def dagPath_getAttrMFloatMatrix( objPath, Attr ):
    out_value = ompy.MFloatMatrix()

    node = objPath.node()
    plug = ompy.MPlug(node, Attr)
    if ( plug.isNull == False ):
        dHandle = plug.asMDataHandle();
        out_value = dHandle.asFloatMatrix();
        plug.destructHandle(dHandle); 

    return out_value

def dagPath_getAttrIntArray( objPath, Attr ):
    out_value = []

    node = objPath.node()
    plug = ompy.MPlug(node, Attr)
    if ( plug.isNull == False ):
        if ( plug.isArray == True):
            for i in range(0,plug.numElements() ):
                out_value.append( plug.elementByLogicalIndex(i).asInt() )

    return out_value

def dagPath_getAttrFloatArray( objPath, Attr ):
    out_value = []

    node = objPath.node()
    plug = ompy.MPlug(node, Attr)
    if ( plug.isNull == False ):
        if ( plug.isArray == True):
            for i in range(0,plug.numElements() ):
                out_value.append( plug.elementByLogicalIndex(i).asFloat() )

    return out_value

def dagPath_getAttrMStringArray( objPath, Attr ):
    out_value = []

    node = objPath.node()
    plug = ompy.MPlug(node, Attr)
    if ( plug.isNull == False ):
        if ( plug.isArray == True):
            for i in range(0,plug.numElements() ):
                out_value.append( plug.elementByLogicalIndex(i).asString() )

    return out_value

def dagPath_getAttrMFloatVectorArray( objPath, Attr ):
    out_value = []

    node = objPath.node()
    plug = ompy.MPlug(node, Attr)
    if ( plug.isNull == False ):
        if ( plug.isArray == True):
            for i in range(0,plug.numElements() ):
                dHandle = plug.elementByLogicalIndex(i).asMDataHandle()
                out_value.append( dHandle.asFloatVector() )
                plug.destructHandle(dHandle)

    return out_value

def dagPath_getAttrMFloatPointArray( objPath, Attr ):
    out_value = []

    node = objPath.node()
    plug = ompy.MPlug(node, Attr)
    if ( plug.isNull == False ):
        if ( plug.isArray == True):
            for i in range(0,plug.numElements() ):
                dHandle = plug.elementByLogicalIndex(i).asMDataHandle()
                out_value.append( ompy.MFloatPoint(dHandle.asFloatVector()) )
                plug.destructHandle(dHandle)

    return out_value


###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################





def glDrawSegments(drawManager, camMatrix, coords, ssOffsets, color, closeShape, thickness):

    #PRE GL
    drawManager.setLineWidth(thickness)
    drawManager.setColor(ompy.MColor(color[0], color[1], color[2], color[3]))
    drawManager.setLineStyle(ompyr.MUIDrawManager.kSolid)

    #START BUILD
    for i in range(0 ,coords.length() ):
        coords[i] += utils_screenTo3dOffset(camMatrix, coords[i], ssOffsets[min(i, ssOffsets.length() - 1)])
    
    points = floatToMPointArray(coords)

    for i in range(0 ,coords.length() ,2 ):
        drawManager.line(points[i], points[i + 1])



def glDrawTriangles( drawManager, camMatrix, coords, ssOffsets, color, colors):
    colorsArray = ompy.MColorArray()
    for i in range(0 ,coords.length() ):
        if (colors.length() == 0): colorsArray.append(ompy.MColor([color[0], color[1], color[2], color[3] ]))
        else:                      colorsArray.append(ompy.MColor([colors[i][0], colors[i][1], colors[i][2], colors[i][3]]))

    for i in range(0 ,coords.length() ):
        coords[i] += utils_screenTo3dOffset(camMatrix, coords[i], ssOffsets[min(i, ssOffsets.length() - 1)]);

    drawManager.mesh(ompyr.MUIDrawManager.kTriangles, coords, None, colorsArray)


def glDrawText( drawManager, camMatrix, coords, ssOffsets, text ,color, fill, size, thickness):

    vOffset = utils_screenTo3dOffset(camMatrix, coords[0], ssOffsets[0])

    textPos = coords[0] + vOffset

    drawManager.setColor(ompy.MColor( [color[0], color[1], color[2] ] ))
    drawManager.setFontSize( max(1 , int(size)) )
    drawManager.text( ompy.MPoint(textPos), text, drawManager.kLeft)



###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################




def utils_screenTo3dOffset( camMatrix, coords, ssOffset ):
    coef = 0.1

    vTargetCam = coords - ompy.MFloatPoint( matrix_getRow(3, camMatrix) )
    vOffset = matrix_getRow(0, camMatrix) * ssOffset.x * -1.0 + matrix_getRow(1, camMatrix) * ssOffset.y * -1.0

    vOffset *= vTargetCam.length() * -0.015

    return vOffset




def matrix_getRow( row, m):
    return ompy.MFloatVector(m.getElement(row, 0), m.getElement(row, 1), m.getElement(row, 2))



def floatToMPointArray( array ):

    arrayConverted = MPointArray(array.length());
    for i in range(0,len(array)):
        arrayConverted[i].x = array[i].x
        arrayConverted[i].y = array[i].y
        arrayConverted[i].z = array[i].z
    
    return arrayConverted






def MMatrixToMFloatMatrix( matrixA ):

    outMatrix = ompy.MFloatMatrix() 

    for row in range(0,4):
        for col in range(0,4):
            outMatrix.setElement(row, col , float(matrixA.getElement(row, col)) )


    return outMatrix










def convertToPointsOnProjPlane( pointO , points , v2X ,  v2Y , distance ):
    iPoints = []
    for point in points:
        iPoints.append( convertToPointOnProjPlane( pointO , point , v2X ,  v2Y , distance ) )
    return iPoints





def convertToPointOnProjPlane( pointO , point , v2X ,  v2Y , distance ):

    vectorTmp = ompy.MFloatVector( point.x - pointO.x , point.y - pointO.y , point.z - pointO.z )
    vectorTmp.normalize()
    pointTmp = pointO + vectorTmp * distance

    planeCoords = [ pointTmp.x , pointTmp.y , pointTmp.z , pointTmp.x + v2X.x , pointTmp.y + v2X.y , pointTmp.z + v2X.z  , pointTmp.x + v2Y.x , pointTmp.y + v2Y.y , pointTmp.z + v2Y.z ]
    lineCoords  = [ pointO.x , pointO.y , pointO.z , point.x , point.y , point.z ]
    iPoint = utils_getLinePlaneIntersectionPoint( lineCoords , planeCoords )

    return ompy.MFloatVector( iPoint[0] , iPoint[1] , iPoint[2] )




def utils_getLinePlaneIntersectionPoint( lineCoords , planeCoords ):
    #GET CLOSEST POINT
    closestPointPlane = utils_getClosestPointOnPlane( lineCoords[0:3] , planeCoords )
    #GET ANGLE CLOSEST POINT PLANE - lineO - lineEND    
    vPlaneLineO = ompy.MVector( closestPointPlane[0] - lineCoords[0] , closestPointPlane[1] - lineCoords[1] , closestPointPlane[2] - lineCoords[2] )
    vline = ompy.MVector( lineCoords[3] - lineCoords[0] , lineCoords[4] - lineCoords[1] , lineCoords[5] - lineCoords[2] ) 
    dotPoduct = math.copysign( 1 , vline*vPlaneLineO )
    vline *= dotPoduct
    angle = vline.angle(vPlaneLineO)
    #DISTANCE CLOSEST POINT PLANE
    distClosestPointPlane = vPlaneLineO.length()
    #TRIGO: GET DISTANCE LINE ORIGINE - INTERSECTION POINT
    distLineOInter  = abs(distClosestPointPlane / math.cos(angle) )
    #GET INTERSECTION POINT
    vline.normalize()   
    vline *= distLineOInter     
    intersectionPoint = [ vline.x + lineCoords[0] , vline.y + lineCoords[1] , vline.z + lineCoords[2] ]
    return intersectionPoint

def utils_getClosestPointOnPlane( coords , planeCoords ):
    #GET PLANE NORMAL
    planVectorA      =  [ ( planeCoords[3] - planeCoords[0] ) , ( planeCoords[4] - planeCoords[1] ) , ( planeCoords[5] - planeCoords[2] )  ] 
    planVectorB      =  [ ( planeCoords[6] - planeCoords[0] ) , ( planeCoords[7] - planeCoords[1] ) , ( planeCoords[8] - planeCoords[2] )  ]    
    normalDir        =  [ ( planeCoords[0] - coords[0]    )   , ( planeCoords[1] - coords[1]    )   , ( planeCoords[2] - coords[2]      )  ]            
    vPlaneNormal = utils_get2VectorsNormal( planVectorA , planVectorB , normalDir  )
    #GET d OF THE PLAN EQUATION  2x + 3y + 7z +d = 0    
    d = ( ( vPlaneNormal[0] *  planeCoords[0] ) + ( vPlaneNormal[1] *  planeCoords[1] ) + ( vPlaneNormal[2] *  planeCoords[2] ) ) * -1 
    #GET DIST BETWEEN POINT AND PLANE
    dist = (  - ( vPlaneNormal[0] * coords[0] ) - ( vPlaneNormal[1] * coords[1] ) - ( vPlaneNormal[2] * coords[2] ) - d  ) / ( ( vPlaneNormal[0] * vPlaneNormal[0] ) + ( vPlaneNormal[1] * vPlaneNormal[1] ) + ( vPlaneNormal[2] * vPlaneNormal[2] )   )        
    #GET INTERSECT COORDS       
    iCoords = [  vPlaneNormal[0] * dist + coords[0] , vPlaneNormal[1] * dist + coords[1] , vPlaneNormal[2] * dist + coords[2] ] 
    return iCoords


def utils_get2VectorsNormal( vectorA , vectorB , vDir ):
    #GET NORMAL
    normalx = ((vectorA[1])*(vectorB[2])-(vectorA[2])*(vectorB[1]))
    normaly = ((vectorA[2])*(vectorB[0])-(vectorA[0])*(vectorB[2]))
    normalz = ((vectorA[0])*(vectorB[1])-(vectorA[1])*(vectorB[0]))
    vecteurNormal = ompy.MVector( normalx   , normaly   , normalz   )
    #GET MODIF IT WITH VECTOR DIR
    vectorDirection   = ompy.MVector( vDir[0] , vDir[1] , vDir[2] )     
    coef = math.copysign( 1 , vecteurNormal*vectorDirection )       
    vecteurNormal = ompy.MVector( vecteurNormal.x * coef , vecteurNormal.y * coef  , vecteurNormal.z * coef  )
    return [ vecteurNormal.x , vecteurNormal.y , vecteurNormal.z ]      


def camera_get_angles_of_view( h_film_aperture , focal_length , filmAspectRatio = 1.77777 ):

    inch_to_mm_ratio = 25.4
    h_film_aperture_conveted = h_film_aperture*inch_to_mm_ratio
    v_film_aperture          = h_film_aperture_conveted/ filmAspectRatio # mc.camera( cam_shape , q = True , verticalFilmAperture   = True )*inch_to_mm_ratio


    h_angle_of_view_rad = 2 * math.atan( h_film_aperture_conveted / (2 * focal_length) )
    v_angle_of_view_rad = 2 * math.atan( v_film_aperture          / (2 * focal_length) )

    h_angle_of_view = math.degrees(h_angle_of_view_rad)
    v_angle_of_view = math.degrees(v_angle_of_view_rad)    

    return [h_angle_of_view,v_angle_of_view]