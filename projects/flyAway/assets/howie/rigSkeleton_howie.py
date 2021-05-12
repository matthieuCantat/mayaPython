
'''




############################################################################ BUILD SKELETON
import maya.cmds as mc
import python
from python.projects.flyAway.assets.howie.rigSkeleton_howie import *
reload( python.projects.flyAway.assets.howie.rigSkeleton_howie)
#___________________________________________________________________________LOAD RIG BASE
from python.classe.readWriteInfo import *
reload(python.classe.readWriteInfo)
rwi = readWriteInfo()
rwi.mayaScene_load( 'D:/mcantat_BDD/projects/flyAway/assets/howie/maya/scenes/howie_rigBase.ma' , open = True )
#___________________________________________________________________________LOAD RIG BASE

import python.utils.utilsMaya as utilsMaya
utilsMaya.setSceneUnitToMeter()


#BUILD
puppet = rigSkeleton_howie()
puppet.printBuild = 1	
toExec = puppet.build()
exec(toExec)


#CLEAN ROOT 
toKeep = ['rigPuppet_GRP','all_GRP']
rootElem = mc.ls("|*" , type = "transform")
rootElem = [ elem for elem in rootElem if not (elem in toKeep ) ]
mc.delete(rootElem)


#___________________________________________________________________________SAVE TO SKELETON
rwi.mayaScene_save( 'D:/mcantat_BDD/projects/flyAway/assets/howie/maya/scenes/howie_rigSkeleton.ma' )
#___________________________________________________________________________SAVE TO SKELETON







'''

	


import maya.cmds as mc

from .....classe.rigPuppet import *  
from .....classe.rigCtrl import *  
from .....classe.rigModuleChain import *     
from .....classe.rigModuleArm import *    
from .....classe.rigModulePiston import *  
from .....classe.rigModuleProjector import *
from .....classe.rigModuleRotatingBeacon import *


class rigSkeleton_howie(rigPuppet):

	def __init__( self , **args ):
		rigPuppet.__init__( self , **args )
		#UTILS	
		#CLASSE
		self.classeType = 'rigSkeleton_howie'
		#NAME
		self.Name.add( 'quadri' , baseName = self.classeType    , type = 'GRP' )			
		#INSTANCE_______________________________BLUEPRINT
		posLocs         = ['pos_pos1' ]
		trajLocs        = ['pos_traj1']
		bodyLocs        = ['pos_body1']
		rootLocs        = ['pos_root1']
		centerLocs      = [x.encode('UTF8') for x in mc.ls('pos_center*' , type = 'transform' )]
		pelvisLocs      = [x.encode('UTF8') for x in mc.ls('pos_pelvis*' , type = 'transform' )]
		     
		spineLocs       = [x.encode('UTF8') for x in mc.ls('pos_spine*'  , type = 'transform' )]
		neckLocs        = [x.encode('UTF8') for x in mc.ls('pos_neck*'   , type = 'transform' )]
     
		tailLocs        = [x.encode('UTF8') for x in mc.ls('pos_tail*'   , type = 'transform' )]

		clavicleLocs    = ['pos_clavicle1']
		armLocs         = [x.encode('UTF8') for x in mc.ls('pos_arm*'    , type = 'transform' )]
		thuLocs         = [x.encode('UTF8') for x in mc.ls('pos_thu*'    , type = 'transform' )]
		indLocs         = [x.encode('UTF8') for x in mc.ls('pos_ind*'    , type = 'transform' )]
		midLocs         = [x.encode('UTF8') for x in mc.ls('pos_mid*'    , type = 'transform' )]
		pinLocs         = [x.encode('UTF8') for x in mc.ls('pos_pin*'    , type = 'transform' )]

		legLocs         = [x.encode('UTF8') for x in mc.ls('pos_leg*'    , type = 'transform' )]
		footLocs        = [x.encode('UTF8') for x in mc.ls('pos_foot?'   , type = 'transform' )]
		toeThuLocs      = [x.encode('UTF8') for x in mc.ls('pos_toeThu*' , type = 'transform' )]
		toeIndLocs      = [x.encode('UTF8') for x in mc.ls('pos_toeInd*' , type = 'transform' )]
		toeMidLocs      = [x.encode('UTF8') for x in mc.ls('pos_toeMid*' , type = 'transform' )]
		toePinLocs      = [x.encode('UTF8') for x in mc.ls('pos_toePin*' , type = 'transform' )]	
		footInvLocs     = [x.encode('UTF8') for x in mc.ls('pos_footInv*', type = 'transform' )]	

		headLocs        = [x.encode('UTF8') for x in mc.ls('pos_head*'   , type = 'transform' )]
		eyeLocs         = ['pos_eye1']
		noseLocs        = [x.encode('UTF8') for x in mc.ls('pos_nose*'     , type = 'transform' )]
		earLocs         = [x.encode('UTF8') for x in mc.ls('pos_ear*'      , type = 'transform' )]
		eyebrowLocs     = ['pos_eyebrow1']
		eyeLidUpperLocs = ['pos_eyeLidUpper1']
		eyeLidLowerLocs = ['pos_eyeLidLower1']
		dimpleLocs      = ['pos_dimple1']
		lipCornerLocs   = ['pos_lipCorner1']
		lipUpperLocs    = [x.encode('UTF8') for x in mc.ls('pos_lipUpper*'      , type = 'transform' )]
		jawLocs         = ['pos_jaw1']
		tongueLocs      = [x.encode('UTF8') for x in mc.ls('pos_tongue*'   , type = 'transform' )]
		lipLowerLocs    = [x.encode('UTF8') for x in mc.ls('pos_lipLower*'      , type = 'transform' )]

		#NAME
		self.Name.add( 'pos'   , baseName = 'pos'    )
		self.Name.add( 'traj'  , baseName = 'traj'   )	
		self.Name.add( 'body'  , baseName = 'body'   )
		#MAIN CTRLS
		self.Position = rigSkeletonChain( n = self.Name.pos   , pos = posLocs     , parent = self.Name.topNode )
		self.Traj     = rigSkeletonChain( n = self.Name.traj  , pos = trajLocs    , parent = self.Position.outs[-1]  )
		self.Body     = rigSkeletonChain( n = self.Name.body  , pos = bodyLocs    , parent = self.Traj.outs[-1] )
		self.Root     = rigSkeletonChain( n = 'root'          , pos = rootLocs    , parent = self.Body.outs[-1] ) 	
		self.Center   = rigSkeletonChain( n = 'center'        , pos = centerLocs  , parent = self.Root.outs[-1] )
		self.Pelvis   = rigSkeletonChain( n = 'pelvis'        , pos = pelvisLocs  , parent = self.Center.outs[-1] )
		
		self.Spine    = rigSkeletonChain( n = 'spine'         , pos = spineLocs   , parent = self.Pelvis.outs[-1] )
		self.Neck     = rigSkeletonChain( n = 'neck'          , pos = neckLocs    , parent = self.Spine.outs[-1] )
		
		self.Tail     = rigSkeletonChain( n = 'tail'          , pos = tailLocs    , parent = self.Pelvis.outs[-1] )

		self.Clavicle = rigSkeletonChain( n = 'clavicle'      , pos = clavicleLocs, parent = self.Spine.outs[-1] )
		self.Arm      = rigSkeletonChain( n = 'arm'           , pos = armLocs     , parent = self.Clavicle.outs[-1] )
		self.Thu      = rigSkeletonChain( n = 'thu'           , pos = thuLocs     , parent = self.Arm.outs[-1] )
		self.Ind      = rigSkeletonChain( n = 'ind'           , pos = indLocs     , parent = self.Arm.outs[-1] )
		self.Mid      = rigSkeletonChain( n = 'mid'           , pos = midLocs     , parent = self.Arm.outs[-1] )
		self.Pin      = rigSkeletonChain( n = 'pin'           , pos = pinLocs     , parent = self.Arm.outs[-1] )

		self.Leg      = rigSkeletonChain( n = 'leg'           , pos = legLocs     , parent = self.Pelvis.outs[-1] )
		self.Foot     = rigSkeletonChain( n = 'foot'          , pos = footLocs    , parent = self.Leg.outs[-1] )
		self.ToeThu   = rigSkeletonChain( n = 'toeThu'        , pos = toeThuLocs  , parent = self.Foot.outs[-1] )
		self.ToeInd   = rigSkeletonChain( n = 'toeInd'        , pos = toeIndLocs  , parent = self.Foot.outs[-1] )
		self.ToeMid   = rigSkeletonChain( n = 'toeMid'        , pos = toeMidLocs  , parent = self.Foot.outs[-1] )
		self.ToePin   = rigSkeletonChain( n = 'toePin'        , pos = toePinLocs  , parent = self.Foot.outs[-1] )
		self.FootInv  = rigSkeletonChain( n = 'footInv'       , pos = footInvLocs , parent = self.Position.outs[-1] )

		self.Head        = rigSkeletonChain( n = 'head'          , pos = headLocs          , parent = self.Neck.outs[-1] ) 
		self.Eye         = rigSkeletonChain( n = 'eye'           , pos = eyeLocs           , parent = self.Head.outs[-1] ) 
		self.Nose        = rigSkeletonChain( n = 'nose'          , pos = noseLocs          , parent = self.Head.outs[-1] )  
		self.Ear         = rigSkeletonChain( n = 'ear'           , pos = earLocs           , parent = self.Head.outs[-1] ) 
		self.Eyebrow     = rigSkeletonChain( n = 'eyebrow'       , pos = eyebrowLocs       , parent = self.Head.outs[-1] ) 
		self.EyeLidUpper = rigSkeletonChain( n = 'eyeLidUpper'   , pos = eyeLidUpperLocs   , parent = self.Head.outs[-1] ) 
		self.EyeLidLower = rigSkeletonChain( n = 'eyeLidLower'   , pos = eyeLidLowerLocs   , parent = self.Head.outs[-1] ) 
		self.Dimple      = rigSkeletonChain( n = 'dimple'        , pos = dimpleLocs        , parent = self.Head.outs[-1] ) 
		self.LipUpperA   = rigSkeletonChain( n = 'lipUpperA'     , pos = [lipUpperLocs[0]] , parent = self.Head.outs[-1] ) 
		self.LipUpperB   = rigSkeletonChain( n = 'lipUpperB'     , pos = [lipUpperLocs[1]] , parent = self.Head.outs[-1] ) 
		self.LipUpperC   = rigSkeletonChain( n = 'lipUpperC'     , pos = [lipUpperLocs[2]] , parent = self.Head.outs[-1] )
		self.Jaw         = rigSkeletonChain( n = 'jaw'           , pos = jawLocs           , parent = self.Head.outs[-1] ) 
		self.Tongue      = rigSkeletonChain( n = 'tongue'        , pos = tongueLocs        , parent = self.Jaw.outs[-1] )		 					
		self.LipLowerA   = rigSkeletonChain( n = 'lipLowerA'     , pos = [lipLowerLocs[0]] , parent = self.Jaw.outs[-1] ) 
		self.LipLowerB   = rigSkeletonChain( n = 'lipLowerB'     , pos = [lipLowerLocs[1]] , parent = self.Jaw.outs[-1] ) 
		self.LipLowerC   = rigSkeletonChain( n = 'lipLowerC'     , pos = [lipLowerLocs[2]] , parent = self.Jaw.outs[-1] ) 

		self.SubRigs     += [ self.Position , self.Traj , self.Body , self.Root , self.Center , self.Pelvis ]		
		self.SubRigsName += [     'Position' ,    'Traj',     'Body',     'Root',     'Center',     'Pelvis']

		self.SubRigs     += [ self.Spine , self.Neck , self.Tail ]		
		self.SubRigsName += [     'Spine' ,    'Neck',     'Tail']	

		self.SubRigs     += [ self.Head  , self.Nose , self.Jaw , self.Tongue , self.LipUpperC , self.LipLowerC ]
		self.SubRigsName += [     'Head' ,     'Nose',     'Jaw',     'Tongue',     'LipUpperC',     'LipLowerC']
		#SIDES CTRLS

		#SUBRIG

		#MIRROR
		argsMirrorX = {}
		argsMirrorX['value']             = [0,0,0 , 0,1,0 , 0,0,1]
		argsMirrorX['mode']              = 'mirror'
		argsMirrorX['pivot']             = [0,0,0 , 0,0,0 , 1,1,1]
		argsMirrorX['namePrefix']        = ['r','l']
		argsMirrorX['nameReplace']       = ['','']
		argsMirrorX['nameIncr']          = ''
		argsMirrorX['nameAdd']           = []
		argsMirrorX['noneMirrorAxe']     = 4
		argsMirrorX['debug']             = self.debug

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

		#CLASSE UTILS

		#UPDATE
		name = args.get( 'n'   , None )	
		pos  = args.get( 'pos' , None )
		if not( name == None ): self.Name.add( 'base' , copy = name ) 
		if not( pos  == None ): pass


       