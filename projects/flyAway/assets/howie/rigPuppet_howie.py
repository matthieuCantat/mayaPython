
	
'''





############################################################################ BUILD RIG PUPPET

import maya.cmds as mc
import python
from python.projects.flyAway.assets.howie.rigPuppet_howie import *
reload( python.projects.flyAway.assets.howie.rigPuppet_howie)

#____________________________________________________________________________LOAD SKELETON
from python.classe.readWriteInfo import *
reload(python.classe.readWriteInfo)
rwi = readWriteInfo()
rwi.mayaScene_load( 'D:/mcantat_BDD/projects/flyAway/assets/howie/maya/scenes/howie_rigBoundB.ma' , open = True )
#____________________________________________________________________________LOAD SKELETON

#BUILD
puppet = rigPuppet_howie()	
puppet.debug = 1
toExec = puppet.build()
exec(toExec)

#____________________________________________________________________________LOAD SHAPE
from python.utils.utilsRigPuppet import *
reload( python.utils.utilsRigPuppet )
path = 'D:/mcantat_BDD/projects/flyAway/assets/howie/maya/scenes/howie_utils_ctrlShape.ma'
rigPuppet_importAndReplaceCtrlShape( path , adjustPosition = False )
#rwi.mayaScene_save( path )
#____________________________________________________________________________LOAD SHAPE


#CLEAN ROOT 
toKeep = ['rigPuppet_GRP']
rootElem = mc.ls("|*" , type = "transform")
rootElem = [ elem for elem in rootElem if not (elem in toKeep ) ]
mc.delete(rootElem)


#createSwitchVisibility
driver = 'traj_CTRL'
meshes = mc.ls('|rigPuppet_GRP|*_GEO')

from python.utils.utilsMaya import *

attr = addSpecialAttr( driver , 'ctrlVis'  , 'int+' , 9 , attrKeyable = False , attrCb  = True , attrLock  =  False )
mc.connectAttr( attr ,'rigPuppet_GRP.ctrlVis')

mc.setAttr( "pos0_JNT.v" , 0 )

pathSave = 'D:/mcantat_BDD/projects/flyAway/assets/howie/maya/scenes/howie_rigPuppet.ma'
addSpecialAttr( driver , 'path'  , 'string' , pathSave , attrKeyable = False , attrCb  = False , attrLock  =  False )

#____________________________________________________________________________SAVE TO RIG PUPPET
rwi.mayaScene_save( 'D:/mcantat_BDD/projects/flyAway/assets/howie/maya/scenes/howie_rigPuppet.ma' )
#____________________________________________________________________________SAVE TO RIG PUPPET



'''


import maya.cmds as mc

from .....classe.rigPuppet import *  
from .....classe.rigCtrl import *  
from .....classe.rigModuleChain import *     
from .....classe.rigModuleArm import *    
from .....classe.rigModulePiston import *  
from .....classe.rigModuleProjector import *
from .....classe.rigModuleRotatingBeacon import *


       
class rigPuppet_howie(rigPuppet):

	def __init__( self , **args ):
		rigPuppet.__init__( self , **args )
		#UTILS	
		#CLASSE

		self.classeType = 'rigPuppet_howie'
		#NAME
		self.Name.add( 'quadri' , baseName = self.classeType    , type = 'GRP' )			
		#INSTANCE_______________________________BLUEPRINT
		#CLASSE BLUE PRINT
		posLocs         = ['pos0_JNT' ]
		trajLocs        = ['traj0_JNT']
		bodyLocs        = ['body0_JNT']
		rootLocs        = ['root0_JNT']		
		centerLocs = [x.encode('UTF8') for x in mc.ls('center?_JNT' , type = 'transform' )]
		pelvisLocs = [x.encode('UTF8') for x in mc.ls('pelvis?_JNT' , type = 'transform' )]

		spineLocs  = [x.encode('UTF8') for x in mc.ls('spine?_JNT'  , type = 'transform' )]
		neckLocs   = [x.encode('UTF8') for x in mc.ls('neck?_JNT'   , type = 'transform' )]

		tailLocs   = [x.encode('UTF8') for x in mc.ls('tail*_JNT'   , type = 'transform' )]

		clavicleLocs    = ['r_clavicle0_JNT']
		armLocs         = [x.encode('UTF8') for x in mc.ls('r_arm?_JNT'    , type = 'transform' )]
		thuLocs         = [x.encode('UTF8') for x in mc.ls('r_thu?_JNT'    , type = 'transform' )]
		indLocs         = [x.encode('UTF8') for x in mc.ls('r_ind?_JNT'    , type = 'transform' )]
		midLocs         = [x.encode('UTF8') for x in mc.ls('r_mid?_JNT'    , type = 'transform' )]
		pinLocs         = [x.encode('UTF8') for x in mc.ls('r_pin?_JNT'    , type = 'transform' )]

		legLocs         = [x.encode('UTF8') for x in mc.ls('r_leg?_JNT'     , type = 'transform' )]
		footLocs        = [x.encode('UTF8') for x in mc.ls('r_foot?_JNT'    , type = 'transform' )]
		toeThuLocs      = [x.encode('UTF8') for x in mc.ls('r_toeThu?_JNT'  , type = 'transform' )]
		toeIndLocs      = [x.encode('UTF8') for x in mc.ls('r_toeInd?_JNT'  , type = 'transform' )]
		toeMidLocs      = [x.encode('UTF8') for x in mc.ls('r_toeMid?_JNT'  , type = 'transform' )]
		toePinLocs      = [x.encode('UTF8') for x in mc.ls('r_toePin?_JNT'  , type = 'transform' )]
		footInvLocs     = [x.encode('UTF8') for x in mc.ls('r_footInv?_JNT' , type = 'transform' )]

		headLocs        = [x.encode('UTF8') for x in mc.ls('head?_JNT'   , type = 'transform' )]
		eyeLocs         = ['r_eye0_JNT']
		noseLocs        = [x.encode('UTF8') for x in mc.ls('nose?_JNT'      , type = 'transform' )]
		earLocs         = [x.encode('UTF8') for x in mc.ls('r_ear?_JNT'     , type = 'transform' )]
		eyebrowLocs     = ['r_eyebrow0_JNT']
		eyeLidUpperLocs = ['r_eyeLidUpper0_JNT']
		eyeLidLowerLocs = ['r_eyeLidLower0_JNT']
		dimpleLocs      = ['r_dimple0_JNT']
		lipUpperALocs   = ['r_lipUpperA0_JNT']
		lipUpperBLocs   = ['r_lipUpperB0_JNT']
		lipUpperCLocs   = ['lipUpperC0_JNT']
		jawLocs         = ['jaw0_JNT']
		tongueLocs      = [x.encode('UTF8') for x in mc.ls('tongue?_JNT'   , type = 'transform' )]
		lipLowerALocs   = ['r_lipLowerA0_JNT']
		lipLowerBLocs   = ['r_lipLowerB0_JNT']
		lipLowerCLocs   = ['lipLowerC0_JNT']		
		
		self.CurveShape.add(  'root' , value = { 'form' : 'crossArrow' , 'colors' : ['green'] , 'axe' : 'y' , 'offset' : [0,0,0,0,0,0,1,1,1] , 'scale' : self.ctrlScale*1 }  )
		#SUBRIG
		self.Root   = rigCtrl(        n = 'root'   , pos = [ [0,0,0 , 0,0,0 , 1,1,1] ] , shape = self.CurveShape.root , joint = None , offset = None , ctrlVisPriority = 0  , parent = self.Name.topNode ) 	
		self.Center = rigCtrl(        n = 'center' , pos = centerLocs , form = 'crossArrow' , colors = ['green']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4 , parent = self.Name.topNode )
		self.Pelvis = rigCtrl(        n = 'pelvis' , pos = pelvisLocs , form = 'cube'       , colors = ['red']            , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.2 , parent = self.Name.topNode )
		
		self.Spine  = rigModuleChain( n = 'spine'  , pos = spineLocs  , form = 'plane'      , colors = ['yellow']         , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.2 , aim = True, parent = self.Name.topNode)
		self.Neck   = rigModuleChain( n = 'neck'   , pos = neckLocs   , form = 'plane'      , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.1 , aim = True, parent = self.Name.topNode)    
	
		self.Tail   = rigModuleChain( n = 'tail'   , pos = tailLocs   , form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05 , aim = True, parent = self.Name.topNode)    
		
		self.Clavicle = rigCtrl(        n = 'clavicle' , pos = clavicleLocs, form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05 , aim = True, parent = self.Name.topNode)    
		self.Arm      = rigModuleArm(   n = 'arm'      , pos = armLocs     , ik = True , fk = True, pv = True, skeleton = True , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.15 , parent = self.Name.topNode)
		self.Thu      = rigModuleChain( n = 'thu'      , pos = thuLocs     , form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05,  aim = True, parent = self.Name.topNode)    
		self.Ind      = rigModuleChain( n = 'ind'      , pos = indLocs     , form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05,  aim = True, parent = self.Name.topNode)    
		self.Mid      = rigModuleChain( n = 'mid'      , pos = midLocs     , form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05,  aim = True, parent = self.Name.topNode)    
		self.Pin      = rigModuleChain( n = 'pin'      , pos = pinLocs     , form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05,  aim = True, parent = self.Name.topNode)    
		
		self.Leg      = rigModuleArm(     n = 'leg'    , pos = legLocs     , ik = True , fk = True, pv = True, skeleton = True , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.15 , parent = self.Name.topNode)  
		self.Foot     = rigCtrl(          n = 'foot'   , pos = footLocs    , form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05, aim = True, parent = self.Name.topNode)    
		self.ToeThu   = rigModuleChain(   n = 'toeThu' , pos = toeThuLocs  , form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05, aim = True, parent = self.Name.topNode)    
		self.ToeInd   = rigModuleChain(   n = 'toeInd' , pos = toeIndLocs  , form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05, aim = True, parent = self.Name.topNode)    
		self.ToeMid   = rigModuleChain(   n = 'toeMid' , pos = toeMidLocs  , form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05, aim = True, parent = self.Name.topNode)    
		self.ToePin   = rigModuleChain(   n = 'toePin' , pos = toePinLocs  , form = 'circle'     , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05, aim = True, parent = self.Name.topNode)  
		self.FootInv  = rigModuleChain(   n = 'footInv', pos = footInvLocs , form = 'circle'     , colors = ['red']            , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05, aim = True, parent = self.Name.topNode)      

		self.Head        = rigCtrl(        n = 'head'          , pos = headLocs          , form = 'cube'   , colors = ['red']            , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.2 , parent = self.Name.topNode)
		self.Eye         = rigCtrl(        n = 'eye'           , pos = eyeLocs           , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode)
		self.Nose        = rigModuleChain( n = 'nose'          , pos = noseLocs          , form = 'circle' , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05, aim = True, parent = self.Name.topNode)     
		self.Ear         = rigModuleChain( n = 'ear'           , pos = earLocs           , form = 'circle' , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05, aim = True, parent = self.Name.topNode)     
		self.Eyebrow     = rigCtrl(        n = 'eyebrow'       , pos = eyebrowLocs       , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode) 
		self.EyeLidUpper = rigCtrl(        n = 'eyeLidUpper'   , pos = eyeLidUpperLocs   , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode) 
		self.EyeLidLower = rigCtrl(        n = 'eyeLidLower'   , pos = eyeLidLowerLocs   , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode) 
		self.Dimple      = rigCtrl(        n = 'dimple'        , pos = dimpleLocs        , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode) 
		self.LipUpperA   = rigCtrl(        n = 'lipUpperA'     , pos = lipUpperALocs     , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode) 
		self.LipUpperB   = rigCtrl(        n = 'lipUpperB'     , pos = lipUpperBLocs     , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode) 
		self.LipUpperC   = rigCtrl(        n = 'lipUpperC'     , pos = lipUpperCLocs     , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode)
		self.Jaw         = rigCtrl(        n = 'jaw'           , pos = jawLocs           , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode) 
		self.Tongue      = rigModuleChain( n = 'tongue'        , pos = tongueLocs        , form = 'circle' , colors = ['yellow']         , ctrlVisPriority = 2 , ctrlScale = self.ctrlScale*0.05,  aim = True, parent = self.Name.topNode)    	 					
		self.LipLowerA   = rigCtrl(        n = 'lipLowerA'     , pos = lipLowerALocs     , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode)
		self.LipLowerB   = rigCtrl(        n = 'lipLowerB'     , pos = lipLowerBLocs     , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode)
		self.LipLowerC   = rigCtrl(        n = 'lipLowerC'     , pos = lipLowerCLocs     , form = 'circle' , colors = ['red']          , ctrlVisPriority = 1 , ctrlScale = self.ctrlScale*0.4  , parent = self.Name.topNode)
		
		self.SubRigs     += [ self.Root , self.Center , self.Pelvis ]		
		self.SubRigsName += [     'Root',     'Center',     'Pelvis']

		self.SubRigs     += [ self.Spine , self.Neck , self.Tail ]		
		self.SubRigsName += [     'Spine' ,    'Neck',     'Tail']	

		self.SubRigs     += [ self.Head  , self.Nose , self.Jaw , self.Tongue , self.LipUpperC , self.LipLowerC ]
		self.SubRigsName += [     'Head' ,     'Nose',     'Jaw',     'Tongue',     'LipUpperC',     'LipLowerC']

		#SUBRIG MIRROR
		argsMirrorX = {}
		argsMirrorX['value']             = [0,0,0 , 0,1,0 , 0,0,1]
		argsMirrorX['mode']              = 'mirror'
		argsMirrorX['pivot']             = [0,0,0 , 0,0,0 , 1,1,1]
		argsMirrorX['namePrefix']        = ['r','l']
		argsMirrorX['nameReplace']       = ['','']
		argsMirrorX['nameIncr']          = ''
		argsMirrorX['nameAdd']           = []
		argsMirrorX['noneMirrorAxe']     = 4


		rigsToDuplicate = []
		rigsToDuplicate.append( self.Clavicle    )
		rigsToDuplicate.append( self.Arm         )     
		rigsToDuplicate.append( self.Thu         )     
		rigsToDuplicate.append( self.Ind         )     
		rigsToDuplicate.append( self.Mid         )     
		rigsToDuplicate.append( self.Pin         )     

		rigsToDuplicate.append( self.Leg         )   
		rigsToDuplicate.append( self.Foot        )   
		rigsToDuplicate.append( self.ToeThu      )  
		rigsToDuplicate.append( self.ToeInd      )  
		rigsToDuplicate.append( self.ToeMid      )  
		rigsToDuplicate.append( self.ToePin      )  
		rigsToDuplicate.append( self.FootInv     ) 
       
		rigsToDuplicate.append( self.Eye         )                
		rigsToDuplicate.append( self.Ear         )       
		rigsToDuplicate.append( self.Eyebrow     )     
		rigsToDuplicate.append( self.EyeLidUpper ) 
		rigsToDuplicate.append( self.EyeLidLower )  
		rigsToDuplicate.append( self.Dimple      )     
		rigsToDuplicate.append( self.LipUpperA   )    
		rigsToDuplicate.append( self.LipUpperB   )        		 					
		rigsToDuplicate.append( self.LipLowerA   )  
		rigsToDuplicate.append( self.LipLowerB   )  

		print('duplicateRigs IN')
		duplicated = self.duplicateRigs( argsMirrorX , rigsToDuplicate )
		print('duplicateRigs OUT')

		self.ClavicleR    , self.ClavicleL    = duplicated[0 ][0] , duplicated[0 ][1]  
		self.ArmR         , self.ArmL         = duplicated[1 ][0] , duplicated[1 ][1]       
		self.ThuR         , self.ThuL         = duplicated[2 ][0] , duplicated[2 ][1]       
		self.IndR         , self.IndL         = duplicated[3 ][0] , duplicated[3 ][1]       
		self.MidR         , self.MidL         = duplicated[4 ][0] , duplicated[4 ][1]       
		self.PinR         , self.PinL         = duplicated[5 ][0] , duplicated[5 ][1]       

		self.LegR         , self.LegL         = duplicated[6 ][0] , duplicated[6 ][1]     
		self.FootR        , self.FootL        = duplicated[7 ][0] , duplicated[7 ][1]     
		self.ToeThuR      , self.ToeThuL      = duplicated[8 ][0] , duplicated[8 ][1]    
		self.ToeIndR      , self.ToeIndL      = duplicated[9 ][0] , duplicated[9 ][1]    
		self.ToeMidR      , self.ToeMidL      = duplicated[10][0] , duplicated[10][1]    
		self.ToePinR      , self.ToePinL      = duplicated[11][0] , duplicated[11][1]  
		self.FootInvR     , self.FootInvL     = duplicated[12][0] , duplicated[12][1]  

		self.EyeR         , self.EyeL         = duplicated[13][0] , duplicated[13][1]                    
		self.EarR         , self.EarL         = duplicated[14][0] , duplicated[14][1]          
		self.EyebrowR     , self.EyebrowL     = duplicated[15][0] , duplicated[15][1]        
		self.EyeLidUpperR , self.EyeLidUpperL = duplicated[16][0] , duplicated[16][1]    
		self.EyeLidLowerR , self.EyeLidLowerL = duplicated[17][0] , duplicated[17][1]     
		self.DimpleR      , self.DimpleL      = duplicated[18][0] , duplicated[18][1]        
		self.LipUpperAR   , self.LipUpperAL   = duplicated[19][0] , duplicated[19][1]       
		self.LipUpperBR   , self.LipUpperBL   = duplicated[20][0] , duplicated[20][1]           		 					
		self.LipLowerAR   , self.LipLowerAL   = duplicated[21][0] , duplicated[21][1]     
		self.LipLowerBR   , self.LipLowerBL   = duplicated[22][0] , duplicated[22][1]    

		self.SubRigs += [ self.ClavicleR    , self.ClavicleL ]
		self.SubRigs += [ self.ArmR         , self.ArmL      ]
		self.SubRigs += [ self.ThuR         , self.ThuL      ]
		self.SubRigs += [ self.IndR         , self.IndL      ]
		self.SubRigs += [ self.MidR         , self.MidL      ]
		self.SubRigs += [ self.PinR         , self.PinL      ]

		self.SubRigs += [ self.LegR         , self.LegL     ]
		self.SubRigs += [ self.FootR        , self.FootL    ]
		self.SubRigs += [ self.ToeThuR      , self.ToeThuL  ]
		self.SubRigs += [ self.ToeIndR      , self.ToeIndL  ]
		self.SubRigs += [ self.ToeMidR      , self.ToeMidL  ]
		self.SubRigs += [ self.ToePinR      , self.ToePinL  ]
		self.SubRigs += [ self.FootInvR     , self.FootInvL ]

		self.SubRigs += [ self.EyeR         , self.EyeL         ]
		self.SubRigs += [ self.EarR         , self.EarL         ]
		self.SubRigs += [ self.EyebrowR     , self.EyebrowL     ]
		self.SubRigs += [ self.EyeLidUpperR , self.EyeLidUpperL ]
		self.SubRigs += [ self.EyeLidLowerR , self.EyeLidLowerL ]
		self.SubRigs += [ self.DimpleR      , self.DimpleL      ]
		self.SubRigs += [ self.LipUpperAR   , self.LipUpperAL   ]
		self.SubRigs += [ self.LipUpperBR   , self.LipUpperBL   ]
		self.SubRigs += [ self.LipLowerAR   , self.LipLowerAL   ]
		self.SubRigs += [ self.LipLowerBR   , self.LipLowerBL   ]
	
		self.SubRigsName += [ 'ClavicleR'    , 'ClavicleL'    ]
		self.SubRigsName += [ 'ArmR'         , 'ArmL'         ]
		self.SubRigsName += [ 'ThuR'         , 'ThuL'         ]
		self.SubRigsName += [ 'IndR'         , 'IndL'         ]
		self.SubRigsName += [ 'MidR'         , 'MidL'         ]
		self.SubRigsName += [ 'PinR'         , 'PinL'         ]

		self.SubRigsName += [ 'LegR'         , 'LegL'         ]
		self.SubRigsName += [ 'FootR'        , 'FootL'        ]
		self.SubRigsName += [ 'ToeThuR'      , 'ToeThuL'      ]
		self.SubRigsName += [ 'ToeIndR'      , 'ToeIndL'      ]
		self.SubRigsName += [ 'ToeMidR'      , 'ToeMidL'      ]
		self.SubRigsName += [ 'ToePinR'      , 'ToePinL'      ]
		self.SubRigsName += [ 'FootInvR'     , 'FootInvL'     ]

		self.SubRigsName += [ 'EyeR'         , 'EyeL'         ]
		self.SubRigsName += [ 'EarR'         , 'EarL'         ]
		self.SubRigsName += [ 'EyebrowR'     , 'EyebrowL'     ]
		self.SubRigsName += [ 'EyeLidUpperR' , 'EyeLidUpperL' ]
		self.SubRigsName += [ 'EyeLidLowerR' , 'EyeLidLowerL' ]
		self.SubRigsName += [ 'DimpleR'      , 'DimpleL'      ]
		self.SubRigsName += [ 'LipUpperAR'   , 'LipUpperAL'   ]
		self.SubRigsName += [ 'LipUpperBR'   , 'LipUpperBL'   ]
		self.SubRigsName += [ 'LipLowerAR'   , 'LipLowerAL'   ]
		self.SubRigsName += [ 'LipLowerBR'   , 'LipLowerBL'   ]


		self.Link.add( 'FootInvR' , Sources = [ self.FootInvR.outs[3] ] , Destinations = [ self.LegR.ins[1] ] , type = 'parent' , operation = 'oneMaster' , maintainOffset = 1 )
		self.Link.add( 'FootInvL' , Sources = [ self.FootInvL.outs[3] ] , Destinations = [ self.LegL.ins[1] ] , type = 'parent' , operation = 'oneMaster' , maintainOffset = 1 )

		#INSTANCE MODIF
		name = args.get( 'n' , None )	
		if not( name == None ): self.Name.add( 'base' , copy = name ) 
		

		'''											
		if not( shape  == None ): self.CurveShape.add(  'ctrl'    , shape                 )
		if not( form   == None ): self.CurveShape.add(  'ctrl'    , { 'form'   : form   } )
		if not( colors == None ): self.CurveShape.add(  'ctrl'    , { 'colors' : colors } )	
		'''
