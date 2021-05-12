'''


pathPythonFiles = 'D:/mcantat_BDD/projects/code/maya/' 
#__________________________ NODE INFO
nodeType       = 'annotate'  
useNodeCpp    = 0
highPoly      = 1
releaseMode   = 1
pathNodePython = r'D:\mcantat_BDD\projects\code\maya\python\plugIn\nodes\annotate.py'
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


mc.connectAttr( '{}.worldMatrix'.format(camera) ,   '{}.camMatrix'.format(newNode) )

mc.connectAttr( ( 'locator1' + '.translate' )  , '{}.coords[0]'.format( newNode)  )
mc.setAttr( newNode + '.shapes[0]'     , 8)
mc.setAttr( newNode + '.sizes[0]'      , 1)
mc.setAttr( newNode + '.colors[0]'     , 0,1,0 , type = "double3" )
mc.setAttr( newNode + '.names[0]'      , "test" , type = "string" )






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


class annotate(ompyui.MPxLocatorNode):

    name = 'annotate'
    id = ompy.MTypeId(0x00033448)
    drawDbClassification = "drawdb/geometry/annotate"
    drawRegistrantId     = "annotateNodePlugin"

    def __init__(self):
        print('annotate.__init__')
        ompyui.MPxLocatorNode.__init__(self)  
        '''                                                
        self.vectors       = []                                          
        self.vectorsSize   = []
        self.vectorsColor  = []
        self.vectorsName   = []
        self.triangles     = []
        self.trianglesSize = []              
        self.trianglesColor= []                             
        self.squares       = []
        self.squaresSize   = []            
        self.squaresColor  = [] 
        self.circles       = []
        self.circlesSize   = []                
        self.circlesColor  = []                    
        self.camPos        = [] 
        self.v2X           = []
        self.v2Y           = []
        self.distProjInt = 1
        self.distIncr = 0.01
        self.motionTrailMaxMemory = 40
        self.pointO = ompy.MFloatVector(0.0,0.0,0.0)
        self.StorePoints = DynamicStore( arrayFill = [self.pointO,self.pointO,self.pointO,self.pointO] , maxIndex = self.motionTrailMaxMemory )
        self.motionTrailSizeLast = 0
        ''' 

    def compute( self, plug , dataBlock ):
        print('annotate.compute') 
        return 1
        '''                                                 
        self.vectors            = utils.nodeAttrToMVectors(   dataBlock , self.attrInVectors      )                                            
        self.vectorsSize        = utils.nodeAttrToFloatArray( dataBlock , self.attrInVectorsSize  )
        self.vectorsColor       = utils.nodeAttrToMVectors(   dataBlock , self.attrInVectorsColor )
        self.vectorsName        = utils.nodeAttrToMStrings(   dataBlock , self.attrInVectorsName )        
        self.triangles          = utils.nodeAttrToMVectors(   dataBlock , self.attrInTriangles    )
        self.trianglesSize      = utils.nodeAttrToFloatArray( dataBlock , self.attrInTrianglesSize  )              
        self.trianglesColor     = utils.nodeAttrToMVectors(   dataBlock , self.attrInTrianglesColor )
        self.trianglesName      = utils.nodeAttrToMStrings(   dataBlock , self.attrInTrianglesName )                                      
        self.squares            = utils.nodeAttrToMVectors(   dataBlock , self.attrInSquares      )
        self.squaresSize        = utils.nodeAttrToFloatArray( dataBlock , self.attrInSquaresSize  )              
        self.squaresColor       = utils.nodeAttrToMVectors(   dataBlock , self.attrInSquaresColor )  
        self.squaresName        = utils.nodeAttrToMStrings(   dataBlock , self.attrInSquaresName  )          
        self.circles            = utils.nodeAttrToMVectors(   dataBlock , self.attrInCircles      )
        self.circlesSize        = utils.nodeAttrToFloatArray( dataBlock , self.attrInCirclesSize  )                  
        self.circlesColor       = utils.nodeAttrToMVectors(   dataBlock , self.attrInCirclesColor )  
        self.circlesName        = utils.nodeAttrToMStrings(   dataBlock , self.attrInCirclesName  )
        self.stars              = utils.nodeAttrToMVectors(   dataBlock , self.attrInStars      )
        self.starsSize          = utils.nodeAttrToFloatArray( dataBlock , self.attrInStarsSize  )                  
        self.starsColor         = utils.nodeAttrToMVectors(   dataBlock , self.attrInStarsColor )  
        self.starsName          = utils.nodeAttrToMStrings(   dataBlock , self.attrInStarsName  )

        self.motionTrail           = utils.nodeAttrToMVectors(   dataBlock , self.attrInMotionTrail      )
        self.motionTrailSize       = utils.nodeAttrToFloatArray( dataBlock , self.attrInMotionTrailSize  )                  
        self.motionTrailColor      = utils.nodeAttrToMVectors(   dataBlock , self.attrInMotionTrailColor )  
        self.motionTrailName       = utils.nodeAttrToMStrings(   dataBlock , self.attrInMotionTrailName  )
        self.motionTrailWorldSpace = utils.nodeAttrToInt(   dataBlock , self.attrInMotionTrailWorldSpace )
        self.motionTrailMaxMemory  = utils.nodeAttrToInt(   dataBlock , self.attrInMotionTrailMaxMemory  )

        self.pointTransparency       = utils.nodeAttrToFloat( dataBlock , self.attrInPointTransparency       )
        self.vectorTransparency      = utils.nodeAttrToFloat( dataBlock , self.attrInVectorTransparency      )
        self.motionTrailTransparency = utils.nodeAttrToFloat( dataBlock , self.attrInMotionTrailTransparency )
        self.motionTrailLinkTransparency = utils.nodeAttrToFloat( dataBlock , self.attrInMotionTrailLinkTransparency )

        self.textPos            = utils.nodeAttrToMVector(    dataBlock , self.attrInTextPos      )                    

        camMatrix          = utils.nodeAttrToMatrixFloatList( dataBlock , self.attrInCamMatrix )        
        #GET UNIT VECTOR
        self.camPos = ompy.MFloatVector( camMatrix[12] , camMatrix[13] , camMatrix[14] )         
        self.v2X    = ompy.MFloatVector( camMatrix[0] , camMatrix[1] , camMatrix[2] )
        self.v2Y    = ompy.MFloatVector( camMatrix[4] , camMatrix[5] , camMatrix[6] )


        for i in range( 0 , len(self.motionTrail) ):
            if not( self.motionTrail[i] == self.StorePoints[0][i] ):
                self.StorePoints.addFirst( self.motionTrail )
                break


        utils.floatToNodeAttr( dataBlock , self.attrOutTrig , 0.0 )




    def draw(self, view, path, style, status):
        #print('draw')
        view.beginGL()

        sizeAnnotation = 0.01
        sizeLine = 5
        sampleCircle = 60
        textIncr = 0.025
        textIncrLoadBar = 0.001   
        loadBarSize = 0.01     
        textShift = 2
        sizeIcone = 0.01
        dist = self.distProjInt 
        distBg = 500       
        textPos = convertToPointOnProjPlane( self.camPos , self.textPos  , self.v2X ,  self.v2Y , dist )


        #DRAW MOTION TRAIL LINK    
        index = 0
        for i in range( 1 , len( self.motionTrail ) ):
            color = [ 0.5 , 0.5 , 0.5 , self.motionTrailLinkTransparency ]                                 
            for j in range( 0 , self.StorePoints.maxIndex ):
                points = convertToPointsOnProjPlane( self.camPos , [ self.StorePoints[j][i] , self.StorePoints[j][i-1] ]   , self.v2X ,  self.v2Y , distBg )
                if( 0 < color[3] ):
                    glDrawLine( glFT , points , 0 , color )

        #DRAW MOTION TRAIL     
        index = 0
        for i in range( 0 , len( self.motionTrail ) ):
            distBg -= self.distIncr

            color = [ self.motionTrailColor[i].x , self.motionTrailColor[i].y , self.motionTrailColor[i].z , self.motionTrailTransparency  ]                                 
            for j in range( 1 , self.StorePoints.maxIndex ):
                points = convertToPointsOnProjPlane( self.camPos , [ self.StorePoints[j][i] , self.StorePoints[j-1][i] ]   , self.v2X ,  self.v2Y , distBg )
                if( 0 < color[3] ):
                    glDrawLine( glFT , points , sizeLine , color )

            #DRAW UI           
            view.drawText( self.motionTrailName[i] , ompy.MPoint(textPos) )
            textPos = textPos - self.v2Y * textIncr 




        #DRAW CRICLE
        for i in range( 0 , len( self.circles ) ):
            dist -= self.distIncr
            point = convertToPointOnProjPlane( self.camPos , self.circles[i]  , self.v2X ,  self.v2Y , dist )

            #COMPUTE RADIUS
            rPoint = self.circles[i] + self.v2X * self.circlesSize[i]
            rPointProj = convertToPointOnProjPlane( self.camPos , rPoint  , self.v2X ,  self.v2Y , dist )
            vRadiusProj = rPointProj - point 
            color = [ self.circlesColor[i].x , self.circlesColor[i].y , self.circlesColor[i].z , 1  ]
            if( 0 < color[3] ):
                glDrawCircle( glFT , point  , sampleCircle ,  self.v2X , self.v2Y , vRadiusProj.length() , color , sizeLine )

            #DRAW UI
            glDrawCircle( glFT , textPos  , sampleCircle , self.v2X , self.v2Y , sizeIcone , color , sizeLine  )        
            view.drawText( self.circlesName[i] , ompy.MPoint( textPos + self.v2X * sizeIcone * textShift ) )
            textPos = textPos - self.v2Y * textIncr 


        #DRAW SQUARE
        for i in range( 0 , len( self.squares ) ):
            dist -= self.distIncr
            point = convertToPointOnProjPlane( self.camPos , self.squares[i]   , self.v2X ,  self.v2Y , dist )
            color = [ self.squaresColor[i].x , self.squaresColor[i].y , self.squaresColor[i].z , self.pointTransparency  ]
            if( 0 < color[3] ):           
                glDrawSquare( glFT , point , self.v2X , self.v2Y , self.squaresSize[i] * sizeAnnotation , color )
            
            #DRAW UI
            glDrawSquare( glFT , textPos  , self.v2X , self.v2Y , sizeIcone , color )        
            view.drawText( self.squaresName[i] , ompy.MPoint( textPos + self.v2X * sizeIcone * textShift ) )
            textPos = textPos - self.v2Y * textIncr 

        #DRAW STAR
        for i in range( 0 , len( self.stars ) ):
            dist -= self.distIncr          
            point = convertToPointOnProjPlane( self.camPos , self.stars[i]   , self.v2X ,  self.v2Y , dist ) 
            color = [ self.starsColor[i].x , self.starsColor[i].y , self.starsColor[i].z , self.pointTransparency  ]
            if( 0 < color[3] ):                         
                glDrawStar( glFT , point  , self.v2X , self.v2Y , self.starsSize[i] * sizeAnnotation , color )

            #DRAW UI
            glDrawStar( glFT , textPos  , self.v2X , self.v2Y , sizeIcone , color )        
            view.drawText( self.starsName[i] , ompy.MPoint( textPos + self.v2X * sizeIcone * textShift ) )
            textPos = textPos - self.v2Y * textIncr 


        #DRAW TRIANGLE
        for i in range( 0 , len( self.triangles ) ):
            dist -= self.distIncr             
            point = convertToPointOnProjPlane( self.camPos , self.triangles[i]   , self.v2X ,  self.v2Y , dist )
            color = [ self.trianglesColor[i].x , self.trianglesColor[i].y , self.trianglesColor[i].z , self.pointTransparency  ]
            if( 0 < color[3] ):                        
                glDrawTriangle( glFT , point  , self.v2X , self.v2Y , self.trianglesSize[i] * sizeAnnotation , color )

            #DRAW UI
            glDrawTriangle( glFT , textPos  , self.v2X , self.v2Y , sizeIcone , color )        
            view.drawText( self.trianglesName[i] , ompy.MPoint( textPos + self.v2X * sizeIcone * textShift ) )
            textPos = textPos - self.v2Y * textIncr 

        #DRAW VECTOR      
        index = 0
        for i in range( 0 , len( self.vectors ) , 2 ):
            dist -= self.distIncr
            points = convertToPointsOnProjPlane( self.camPos , [ self.vectors[i] , self.vectors[i+1] ]   , self.v2X ,  self.v2Y , dist )
            color = [ self.vectorsColor[index].x , self.vectorsColor[index].y , self.vectorsColor[index].z , self.vectorTransparency  ] 
            if( 0 < color[3] ):                                 
                glDrawVector( glFT , points , self.camPos , self.v2X , self.v2Y , self.vectorsSize[index] * sizeAnnotation , sizeLine , color )

            #DRAW UI           
            view.drawText( self.vectorsName[index] , ompy.MPoint(textPos) )
            textPos = textPos - self.v2Y * textIncrLoadBar 
            glDrawLoadBar( glFT , textPos , (self.vectors[i+1] - self.vectors[i]).length() * loadBarSize  , self.v2X , self.v2Y , 3 , color )
            textPos = textPos - self.v2Y * textIncr

            index += 1
    
        view.endGL()
    '''        

    @staticmethod
    def creator():
        print('creator')
        return annotate()
    ''' 
    @classmethod
    def creator(cls):
        print('creator')
        return cls()
    ''' 

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
        cls.inAttrs.append( mAttr.create( 'camMatrix' , 'camMatrix' ,  nData.kFloat  )  )  

        drawPlaneMode_choices = [ 'none' , 'foreground' , 'background' ]
        cls.inAttrs.append( eAttr.create('drawPlaneMode', 'drawPlaneMode', 0 ) )
        for i in range(0,len(drawPlaneMode_choices)):
            eAttr.addField(drawPlaneMode_choices[i], i)
        eAttr.channelBox = True

        cls.inAttrs.append( nAttr.create( 'shapes', 'shapes', nData.kInt, 0 ) )
        nAttr.array = True
        #nAttr.dynamic = True
        nAttr.usesArrayDataBuilder = True

        cls.inAttrs.append( nAttr.createPoint( 'coords' , 'coords' ) )    
        nAttr.array = True
        #nAttr.dynamic = True
        nAttr.usesArrayDataBuilder = True


        cls.inAttrs.append( nAttr.createPoint( 'screenSpaceOffsets' , 'screenSpaceOffsets' ) )    
        nAttr.array = True
        #nAttr.dynamic = True
        nAttr.usesArrayDataBuilder = True


        cls.inAttrs.append( nAttr.create( 'sizes', 'sizes', nData.kFloat, 1.0 ) )
        nAttr.array = True
        #nAttr.dynamic = True
        nAttr.usesArrayDataBuilder = True


        cls.inAttrs.append( nAttr.create( 'thicknesses', 'thicknesses', nData.kFloat, 1.0 ) )
        nAttr.array = True
        #nAttr.dynamic = True
        nAttr.usesArrayDataBuilder = True


        cls.inAttrs.append( nAttr.createPoint( 'colors' , 'colors' ) )    
        nAttr.array = True
        #nAttr.dynamic = True
        nAttr.usesArrayDataBuilder = True


        cls.inAttrs.append( tAttr.create( 'names' , 'names', sData.kString ) )    
        tAttr.array = True
        #nAttr.dynamic = True
        tAttr.usesArrayDataBuilder = True



        '''
        cls.attrOutTrig = nAttr.create( 'outTrig', 'outTrig' , nData.kFloat  )   
        nAttr.setReadable(True) 
        nAttr.setStorable(True)
        nAttr.setConnectable(True) 
        '''         

        for i in range( 0 , len( cls.inAttrs ) ):
            cls.addAttribute( cls.inAttrs[i] )
         
        #INFLUENCE
        '''
        for i in range( 0 , len( cls.inAttrs ) ):
            cls.attributeAffects( cls.inAttrs[i] , cls.attrOutTrig )
        '''            
 


def initializePlugin(obj):  
    print('initializePlugin') 
    plugin = ompy.MFnPlugin( obj )
    plugin.registerNode( annotate.name, annotate.id, annotate.creator, annotate.initialize, ompy.MPxNode.kLocatorNode , annotate.drawDbClassification )
    ompyr.MDrawRegistry.registerDrawOverrideCreator(annotate.drawDbClassification, annotate.drawRegistrantId, annotateDrawOverride.Creator)



def uninitializePlugin(obj):
    print('uninitializePlugin')  
    plugin = ompy.MFnPlugin(obj)
    try:
        ompyr.MDrawRegistry.deregisterDrawOverrideCreator(annotate.drawDbClassification, annotate.drawRegistrantId)
    except:
        raise Exception('Failed to unregister node: {0}'.format(annotate.name) )

    try:
        plugin.deregisterNode( annotate.id )
    except:
        raise Exception('Failed to unregister node: {0}'.format(annotate.name) )




###############################################################################################################   
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################



class annotateDrawOverride(ompyr.MPxDrawOverride):


    def __init__(self , obj ):
        ompyr.MPxDrawOverride.__init__( self , obj , None )  

        self.shapesNames            = ["segment", "triangle", "pointTriangle" , "pointSquare", "pointCircle", "pointStar", "pointCross", "vector"  , "text" ]
        self.shapeToNbrElemForBuild = [ 2       , 3         ,  1              , 1            , 1            , 1          , 1           , 2         , 1      ]
        #fModelEditorChangedCbId = om.MEventMessage.addEventCallback("modelEditorChanged", self.OnModelEditorChanged, self)

    @classmethod
    def Creator(cls,obj):
        print('annotateDrawOverride.creator' )
        return cls(obj)

    '''
    def OnModelEditorChanged( self , clientData):
        print( clientData )
    '''

    def prepareForDraw( self , objPath, cameraPath, frameContext, oldData):
        DEBUG_C = 1
        if (DEBUG_C): print("glDrawDrawOverride________________________________________PREPARE - GET FROM MAYA")
        #DISPLAY
        camMatrix          = dagPath_getAttrMFloatMatrix(      objPath, annotate.inAttrs[0] )
        drawPlaneMode      = dagPath_getAttrInt(               objPath, annotate.inAttrs[1] )
        #OBJ INFO 
        shapes             = dagPath_getAttrIntArray(          objPath, annotate.inAttrs[2] ) 
        coords             = dagPath_getAttrMFloatVectorArray( objPath, annotate.inAttrs[3] )
        screenSpaceOffsets = dagPath_getAttrMFloatVectorArray( objPath, annotate.inAttrs[4] )
        sizes              = dagPath_getAttrFloatArray(        objPath, annotate.inAttrs[5] )
        thicknesses        = dagPath_getAttrFloatArray(        objPath, annotate.inAttrs[6] )
        colors             = dagPath_getAttrMFloatPointArray(  objPath, annotate.inAttrs[7] )
        names              = dagPath_getAttrMStringArray(      objPath, annotate.inAttrs[8] )

        '''
        MFloatMatrix      attrMatrix         = dagPath_getAttrMFloatMatrix(            objPath, glDraw::inAttrs[16]) 
        vector<MString>   attrNames          = dagPath_getAttrGenericArrayAttrNames(   objPath, glDraw::inAttrs[17])
        vector<MString>   attrValueType      = dagPath_getAttrGenericArrayValueType(   objPath, glDraw::inAttrs[17]) 
        vector<int>       attrValueInt       = dagPath_getAttrGenericArrayValueInt(    objPath, glDraw::inAttrs[17])
        vector<float>     attrValueFloat     = dagPath_getAttrGenericArrayValueFloat(  objPath, glDraw::inAttrs[17]) 
        vector<double>    attrValueDouble    = dagPath_getAttrGenericArrayValueDouble( objPath, glDraw::inAttrs[17]) 
        vector<MString>   attrValueEnum      = dagPath_getAttrGenericArrayValueEnum(   objPath, glDraw::inAttrs[17])
        '''
    
        if (DEBUG_C): print("glDrawDrawOverride________________________________________ CREATE DATA")
        #glDrawData* data = dynamic_cast<glDrawData*>(oldData);
        #if (!data) { data = new glDrawData(); }
        data = oldData

        if( data == None ):
            data = glDrawData()
        if (DEBUG_C): print("glDrawDrawOverride________________________________________PREPARE - FILL DATA ATTR")
    
        #FILL DATA ATTR
        data.shapes             = shapes
        data.coords             = coords
        data.screenSpaceOffsets = screenSpaceOffsets
        data.sizes              = sizes
        data.colors             = colors
        data.names              = names
    
        data.cameraPath         = ompy.MDagPath(cameraPath)
        data.drawPlaneMode      = drawPlaneMode
    
        '''
        data.attrMatrix      = attrMatrix
        data.attrValueType   = attrValueType
        data.attrNames       = attrNames
        data.attrValueInt    = attrValueInt
        data.attrValueFloat  = attrValueFloat
        data.attrValueDouble = attrValueDouble
        data.attrValueEnum   = attrValueEnum
        '''
        
        for i in range(0,len(data.shapes)):
            if( i == 0 ):
                data.screenSpaceOffsets.append( ompy.MFloatPoint(0.0, 0.0, 0.0))
                data.sizes.append( 1.0 )
                data.colors.append( ompy.MFloatPoint(1, 0, 0) )
                data.names.append( "" )
            else:
                data.screenSpaceOffsets.append( data.screenSpaceOffsets[i-1] )
                data.sizes.append(  data.sizes[i-1] )
                data.colors.append( data.colors[i-1] )
                data.names.append(  data.names[i-1] )

        return data
    
    def hasUIDrawables( self ):
        return True
    
    def addUIDrawables( self , objPath, drawManager, frameContext, data):
        DEBUG_C = 1

        if (DEBUG_C): print("glDrawDrawOverride________________________________________addUIDrawables - GET DATA");
    
        #glDrawData* data = (glDrawData*)dataRaw;
        #if (!data) { return; }

        cameraFn             = ompy.MFnCamera(data.cameraPath)
        cameraTrsf           = ompy.MFnDagNode(cameraFn.parent(0))
        camMatrix            = MMatrixToMFloatMatrix(cameraTrsf.transformationMatrix())
        camPlaneNearDistance = cameraFn.nearClippingPlane
        camPlaneFarDistance  = cameraFn.farClippingPlane
    
        if (DEBUG_C): print("glDrawDrawOverride________________________________________addUIDrawables - DRAW");
        drawManager.beginDrawable()
    
        iCoords = 0
        exitDrawing = False
    
        for i in range( 0 , len(data.shapes) ):
            #________________________________________GET COORDS FOR BUILDING ONE SHAPE
    
            nbrElementForBuild = self.shapeToNbrElemForBuild[data.shapes[i]];
    
            coordsForBuild    = ompy.MFloatPointArray()
            ssOffsetsForBuild = ompy.MFloatVectorArray()
            for j in range( 0 , nbrElementForBuild ):
                if ( len(data.coords) <= iCoords):
                    exitDrawing = True
                    break

                coordsForBuild.append(   data.coords[iCoords])
                ssOffsetsForBuild.append(data.screenSpaceOffsets[iCoords])
                iCoords+=1
            
    
            if (exitDrawing == True): break
    
            #________________________________________DRAW BUILD CONVERT COORDS
    
            distIncr       = 0.001
            foregroundDist = camPlaneNearDistance + 0.02
            backgroundDist = camPlaneFarDistance - 0.02
    
            coords = ompy.MFloatPointArray()
            size      = 1.0
            thickness = 1.0
            if ( (data.drawPlaneMode == 1) and (0 < coordsForBuild.length()) ):#FOREGROUND

                coords    = snapCoordsOnCameraPlane(camMatrix, foregroundDist, coordsForBuild)
                size      = snapLengthOnCameraPlane(camMatrix, foregroundDist, coordsForBuild[0], data.sizes[i])
                #thickness = data.thicknesses[i]
                foregroundDist += distIncr

            elif ((data.drawPlaneMode == 2) and (0 < coordsForBuild.length())):#sBACKGROUND

                coords    = snapCoordsOnCameraPlane(camMatrix, backgroundDist, coordsForBuild)
                size      = snapLengthOnCameraPlane(camMatrix, backgroundDist, coordsForBuild[0], data.sizes[i])
                #thickness = data.thicknesses[i]
                backgroundDist -= distIncr

            else:

                coords   = coordsForBuild
                size      = data.sizes[i]
                #thickness = data.thicknesses[i]

    
            ssOffsets = ompy.MFloatVectorArray( ssOffsetsForBuild )
    
            #________________________________________DRAW SHAPE
    
            if (      self.shapesNames[data.shapes[i]] == "segment"       ): glDrawSegments(       drawManager, camMatrix, coords, ssOffsets, data.colors[i], 0, 1.0)
            elif ( self.shapesNames[data.shapes[i]] == "triangle"      ): pass#glDrawTriangles(      drawManager, camMatrix, coords, ssOffsets, data.colors[i],    data.pColors[i])
            elif ( self.shapesNames[data.shapes[i]] == "pointTriangle" ): pass#glDrawPointTriangle(  drawManager, camMatrix, coords, ssOffsets, data.colors[i],    data.fills[i], size, thickness)
            elif ( self.shapesNames[data.shapes[i]] == "pointSquare"   ): pass#glDrawPointSquare(    drawManager, camMatrix, coords, ssOffsets, data.colors[i],    data.fills[i], size, thickness)
            elif ( self.shapesNames[data.shapes[i]] == "pointCircle"   ): pass#glDrawPointCircle(    drawManager, camMatrix, coords, ssOffsets, data.colors[i],    data.fills[i], size, thickness)
            elif ( self.shapesNames[data.shapes[i]] == "pointStar"     ): pass#glDrawPointStar(      drawManager, camMatrix, coords, ssOffsets, data.colors[i],    data.fills[i], size, thickness)
            elif ( self.shapesNames[data.shapes[i]] == "pointCross"    ): pass#glDrawPointCross(     drawManager, camMatrix, coords, ssOffsets, data.colors[i],    data.fills[i], size, thickness)
            elif ( self.shapesNames[data.shapes[i]] == "vector"        ): pass#glDrawVector(         drawManager, camMatrix, coords, ssOffsets, data.colors[i],    data.fills[i], size, thickness)
            elif ( self.shapesNames[data.shapes[i]] == "text"          ): glDrawText(           drawManager, camMatrix, coords, ssOffsets, data.names[i] ,    data.colors[i], True, size, 1.0)     
        
        drawManager.endDrawable()



###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################



class glDrawData( ompy.MUserData ):

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



#___________________________________________________________________________________________
#____________________________________________________________________________________ SIMPLE
#___________________________________________________________________________________________

'''
def glDrawPointTriangle( drawManager, camMatrix, coords, ssOffsets, color, fill, size, thickness):

    if (fill):
        coordsShape = matrix_getTrianglePoints(camMatrix, 2, "triangles", size)
        coordsShape = points_addVector(coordsShape, (coords[0] - matrix_getRow(3, camMatrix)))
        glDrawTriangles(drawManager, camMatrix, coordsShape, ssOffsets, color)
    else:
        coordsShape = matrix_getTrianglePoints(camMatrix, 2, "segments", size)
        coordsShape = points_addVector(coordsShape, (coords[0] - matrix_getRow(3, camMatrix)))
        glDrawSegments(drawManager, camMatrix, coordsShape, ssOffsets, color, false, thickness)

def glDrawPointSquare( drawManager, camMatrix, coords, ssOffsets, color, fill, size, thickness):

    if (fill):
        coordsShape = matrix_getSquarePoints(camMatrix, 2, "triangles", size);
        coordsShape = points_addVector(coordsShape, (coords[0] - matrix_getRow(3, camMatrix)));
        glDrawTriangles(drawManager, camMatrix, coordsShape, ssOffsets, color);
    else:
        coordsShape = matrix_getSquarePoints(camMatrix, 2, "segments", size);
        coordsShape = points_addVector(coordsShape, (coords[0] - matrix_getRow(3, camMatrix)));
        glDrawSegments(drawManager, camMatrix, coordsShape, ssOffsets, color, false, thickness);

def glDrawPointCircle( drawManager, camMatrix, coords, ssOffsets, color, fill, size, thickness):
    
    if (fill):
        coordsShape = matrix_getCirclePoints(camMatrix, 2, "triangles", size);
        coordsShape = points_addVector(coordsShape, (coords[0] - matrix_getRow(3, camMatrix)));
        glDrawTriangles(drawManager, camMatrix, coordsShape, ssOffsets, color);
    else:
        coordsShape = matrix_getCirclePoints(camMatrix, 2, "segments", size);
        coordsShape = points_addVector(coordsShape, (coords[0] - matrix_getRow(3, camMatrix)));
        glDrawSegments(drawManager, camMatrix, coordsShape, ssOffsets, color, false, thickness);


def glDrawPointStar( drawManager, camMatrix, coords, ssOffsets, color, fill, size, thickness):
    
    if (fill):
        coordsShape = matrix_getStarPoints(camMatrix, 2, "triangles", size);
        coordsShape = points_addVector(coordsShape, (coords[0] - matrix_getRow(3, camMatrix)));
        glDrawTriangles(drawManager, camMatrix, coordsShape, ssOffsets, color);
    else:
        coordsShape = matrix_getStarPoints(camMatrix, 2, "segments", size);
        coordsShape = points_addVector(coordsShape, (coords[0] - matrix_getRow(3, camMatrix)));
        glDrawSegments(drawManager, camMatrix, coordsShape, ssOffsets, color, false, thickness);

def glDrawPointCross( drawManager, camMatrix, coords, ssOffsets, color, fill, size, thickness):

    if (fill):
        coordsShape = matrix_getCrossPoints(camMatrix, 2, "triangles", size);
        coordsShape = points_addVector(coordsShape, (coords[0] - matrix_getRow(3, camMatrix)));
        glDrawTriangles(drawManager, camMatrix, coordsShape, ssOffsets, color);
    else:
        coordsShape = matrix_getCrossPoints(camMatrix, 2, "segments", size);
        coordsShape = points_addVector(coordsShape, (coords[0] - matrix_getRow(3, camMatrix)));
        glDrawSegments(drawManager, camMatrix, coordsShape, ssOffsets, color, false, thickness);


def glDrawVector( drawManager, camMatrix, coords, ssOffsets, color, fill, size, thickness):
  
    if (fill):
        coordsShape = gl_getShapeCoordsVector(camMatrix, coords, "triangles", size);
        glDrawTriangles(drawManager, camMatrix, coordsShape, ssOffsets, color);
    else:
        coordsShape = gl_getShapeCoordsVector(camMatrix, coords, "segments", size);
        glDrawSegments(drawManager, camMatrix, coordsShape, ssOffsets, color, false, thickness);

'''
def glDrawText( drawManager, camMatrix, coords, ssOffsets, text ,color, fill, size, thickness):

    vOffset = utils_screenTo3dOffset(camMatrix, coords[0], ssOffsets[0])

    textPos = coords[0] + vOffset

    drawManager.setColor(ompy.MColor( [color[0], color[1], color[2] ] ))
    drawManager.setFontSize(int(size * 15) )
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



