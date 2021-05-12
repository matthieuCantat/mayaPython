
'''




############################################################################ BUILD SKELETON
import maya.cmds as mc
import python
from python.projects.quadriped.assets.lion.rigSkeleton_lion import *
reload( python.projects.quadriped.assets.lion.rigSkeleton_lion)
#___________________________________________________________________________LOAD RIG BASE
from python.classe.readWriteInfo import *
reload(python.classe.readWriteInfo)
rwi = readWriteInfo()
rwi.mayaScene_load( 'D:/mcantat_BDD/projects/quadriped/assets/lion/maya/scenes/lion_rigBase.ma' , open = True )
#___________________________________________________________________________LOAD RIG BASE

import python.utils.utilsMaya as utilsMaya
utilsMaya.setSceneUnitToMeter()


#BUILD
puppet = rigSkeleton_lion()
puppet.printBuild = 1	
toExec = puppet.build()
exec(toExec)


#CLEAN ROOT 
toKeep = ['rigPuppet_GRP','all_GRP']
rootElem = mc.ls("|*" , type = "transform")
rootElem = [ elem for elem in rootElem if not (elem in toKeep ) ]
mc.delete(rootElem)


#___________________________________________________________________________SAVE TO SKELETON
rwi.mayaScene_save( 'D:/mcantat_BDD/projects/quadriped/assets/lion/maya/scenes/lion_rigSkeleton.ma' )
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


class rigSkeleton_lion(rigPuppet):

	def __init__( self , **args ):
		rigPuppet.__init__( self , **args )
		#UTILS	
		#CLASSE
		self.classeType = 'rigSkeleton_lion'
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
		bellyLocs       = ['pos_belly1']
		cageLocs        = ['pos_cage1']
		chestLocs       = ['pos_chest1']
		neckLocs        = [x.encode('UTF8') for x in mc.ls('pos_neck*'   , type = 'transform' )]
     
		tailLocs        = [x.encode('UTF8') for x in mc.ls('pos_tail*'   , type = 'transform' )]

		clavicleLocs    = ['pos_clavicle1']
		armLocs         = [x.encode('UTF8') for x in mc.ls('pos_arm*'    , type = 'transform' )]
		scapulaLocs     = ['pos_scapula1']
		thuLocs         = [x.encode('UTF8') for x in mc.ls('pos_thu*'    , type = 'transform' )]
		indLocs         = [x.encode('UTF8') for x in mc.ls('pos_ind*'    , type = 'transform' )]
		midLocs         = [x.encode('UTF8') for x in mc.ls('pos_mid*'    , type = 'transform' )]
		rngLocs         = [x.encode('UTF8') for x in mc.ls('pos_rng*'    , type = 'transform' )]
		pnkLocs         = [x.encode('UTF8') for x in mc.ls('pos_pnk*'    , type = 'transform' )]
		handInvLocs     = [x.encode('UTF8') for x in mc.ls('pos_handInv*', type = 'transform' )]

		legLocs         = [x.encode('UTF8') for x in mc.ls('pos_leg*'    , type = 'transform' )]
		footLocs        = [x.encode('UTF8') for x in mc.ls('pos_foot?'   , type = 'transform' )]
		toeIndLocs      = [x.encode('UTF8') for x in mc.ls('pos_toeInd*' , type = 'transform' )]
		toeMidLocs      = [x.encode('UTF8') for x in mc.ls('pos_toeMid*' , type = 'transform' )]
		toeRngLocs      = [x.encode('UTF8') for x in mc.ls('pos_toeRng*' , type = 'transform' )]
		toePnkLocs      = [x.encode('UTF8') for x in mc.ls('pos_toePnk*' , type = 'transform' )]	
		footInvLocs     = [x.encode('UTF8') for x in mc.ls('pos_footInv*', type = 'transform' )]	

		headLocs        = [x.encode('UTF8') for x in mc.ls('pos_head*'   , type = 'transform' )]
		eyeLocs         = ['pos_eye1']
		earLocs         = [x.encode('UTF8') for x in mc.ls('pos_ear*'      , type = 'transform' )]
		jawLocs         = ['pos_jaw1']
		tongueLocs      = [x.encode('UTF8') for x in mc.ls('pos_tongue*'   , type = 'transform' )]

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
		self.Belly    = rigSkeletonChain( n = 'belly'         , pos = bellyLocs   , parent = self.Spine.outs[2] )
		self.Cage     = rigSkeletonChain( n = 'cage'          , pos = cageLocs    , parent = self.Spine.outs[4] )
		self.Chest    = rigSkeletonChain( n = 'chest'         , pos = chestLocs   , parent = self.Spine.outs[5] )
								
		self.Neck     = rigSkeletonChain( n = 'neck'          , pos = neckLocs    , parent = self.Spine.outs[-1] )
		
		self.Tail     = rigSkeletonChain( n = 'tail'          , pos = tailLocs    , parent = self.Pelvis.outs[-1] )

		self.Clavicle = rigSkeletonChain( n = 'clavicle'      , pos = clavicleLocs, parent = self.Spine.outs[-1] )
		self.Arm      = rigSkeletonChain( n = 'arm'           , pos = armLocs     , parent = self.Clavicle.outs[-1] )
		self.Scapula  = rigSkeletonChain( n = 'scapula'       , pos = scapulaLocs , parent = self.Arm.outs[0])
		self.Thu      = rigSkeletonChain( n = 'thu'           , pos = thuLocs     , parent = self.Arm.outs[-1] )
		self.Ind      = rigSkeletonChain( n = 'ind'           , pos = indLocs     , parent = self.Arm.outs[-1] )
		self.Mid      = rigSkeletonChain( n = 'mid'           , pos = midLocs     , parent = self.Arm.outs[-1] )
		self.Rng      = rigSkeletonChain( n = 'rng'           , pos = rngLocs     , parent = self.Arm.outs[-1] )
		self.Pnk      = rigSkeletonChain( n = 'pnk'           , pos = pnkLocs     , parent = self.Arm.outs[-1] )
		self.HandInv  = rigSkeletonChain( n = 'handInv'       , pos = handInvLocs , parent = self.Position.outs[-1] )

		self.Leg      = rigSkeletonChain( n = 'leg'           , pos = legLocs     , parent = self.Pelvis.outs[-1] )
		self.Foot     = rigSkeletonChain( n = 'foot'          , pos = footLocs    , parent = self.Leg.outs[-1] )
		self.ToeInd   = rigSkeletonChain( n = 'toeInd'        , pos = toeIndLocs  , parent = self.Foot.outs[-1] )
		self.ToeMid   = rigSkeletonChain( n = 'toeMid'        , pos = toeMidLocs  , parent = self.Foot.outs[-1] )
		self.ToeRng   = rigSkeletonChain( n = 'toeRng'        , pos = toeRngLocs  , parent = self.Foot.outs[-1] )		
		self.ToePnk   = rigSkeletonChain( n = 'toePnk'        , pos = toePnkLocs  , parent = self.Foot.outs[-1] )
		self.FootInv  = rigSkeletonChain( n = 'footInv'       , pos = footInvLocs , parent = self.Position.outs[-1] )

		self.Head        = rigSkeletonChain( n = 'head'          , pos = headLocs          , parent = self.Neck.outs[-1] ) 
		self.Eye         = rigSkeletonChain( n = 'eye'           , pos = eyeLocs           , parent = self.Head.outs[-1] ) 
		self.Ear         = rigSkeletonChain( n = 'ear'           , pos = earLocs           , parent = self.Head.outs[-1] ) 
		self.Jaw         = rigSkeletonChain( n = 'jaw'           , pos = jawLocs           , parent = self.Head.outs[-1] ) 
		self.Tongue      = rigSkeletonChain( n = 'tongue'        , pos = tongueLocs        , parent = self.Jaw.outs[-1] )		 					

		self.SubRigs     += [ self.Position , self.Traj , self.Body , self.Root , self.Center , self.Pelvis ]		
		self.SubRigsName += [     'Position' ,    'Traj',     'Body',     'Root',     'Center',     'Pelvis']

		self.SubRigs     += [ self.Spine , self.Belly , self.Cage , self.Chest , self.Neck , self.Tail ]		
		self.SubRigsName += [     'Spine' ,    'Belly',     'Cage',     'Chest',     'Neck',     'Tail']	

		self.SubRigs     += [ self.Head  , self.Jaw , self.Tongue ]
		self.SubRigsName += [     'Head' ,     'Jaw',     'Tongue']
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
		rigsToDuplicate.append( self.Scapula     )     
		rigsToDuplicate.append( self.Thu         )     
		rigsToDuplicate.append( self.Ind         )     
		rigsToDuplicate.append( self.Mid         ) 
		rigsToDuplicate.append( self.Rng         ) 		    
		rigsToDuplicate.append( self.Pnk         )  
		rigsToDuplicate.append( self.HandInv     )    

		rigsToDuplicate.append( self.Leg         )   
		rigsToDuplicate.append( self.Foot        )    
		rigsToDuplicate.append( self.ToeInd      )  
		rigsToDuplicate.append( self.ToeMid      ) 
		rigsToDuplicate.append( self.ToeRng      )		 
		rigsToDuplicate.append( self.ToePnk      )
		rigsToDuplicate.append( self.FootInv     ) 
       
		rigsToDuplicate.append( self.Eye         )                
		rigsToDuplicate.append( self.Ear         )        

		print('duplicateRigs IN')
		duplicated = self.duplicateRigs( argsMirrorX , rigsToDuplicate )
		print('duplicateRigs OUT')

		self.ClavicleR    , self.ClavicleL    = duplicated[0 ][0] , duplicated[0 ][1]  
		self.ArmR         , self.ArmL         = duplicated[1 ][0] , duplicated[1 ][1]     
		self.ScapulaR     , self.ScapulaL     = duplicated[2 ][0] , duplicated[2 ][1]    
		self.ThuR         , self.ThuL         = duplicated[3 ][0] , duplicated[3 ][1]       
		self.IndR         , self.IndL         = duplicated[4 ][0] , duplicated[4 ][1]       
		self.MidR         , self.MidL         = duplicated[5 ][0] , duplicated[5 ][1]  
		self.RngR         , self.RngL         = duplicated[6 ][0] , duplicated[6 ][1]      
		self.PnkR         , self.PnkL         = duplicated[7 ][0] , duplicated[7 ][1]   
		self.HandInvR     , self.HandInvL     = duplicated[8 ][0] , duplicated[8 ][1]     

		self.LegR         , self.LegL         = duplicated[9 ][0] , duplicated[9 ][1]     
		self.FootR        , self.FootL        = duplicated[10][0] , duplicated[10][1]       
		self.ToeIndR      , self.ToeIndL      = duplicated[11][0] , duplicated[11][1]    
		self.ToeMidR      , self.ToeMidL      = duplicated[12][0] , duplicated[12][1] 
		self.ToeRngR      , self.ToeRngL      = duplicated[13][0] , duplicated[13][1]   
		self.ToePnkR      , self.ToePnkL      = duplicated[14][0] , duplicated[14][1]    
		self.FootInvR     , self.FootInvL     = duplicated[15][0] , duplicated[15][1] 

		self.EyeR         , self.EyeL         = duplicated[16][0] , duplicated[16][1]                    
		self.EarR         , self.EarL         = duplicated[17][0] , duplicated[17][1]             

		self.SubRigs += [ self.ClavicleR    , self.ClavicleL ]
		self.SubRigs += [ self.ScapulaR     , self.ScapulaL  ]
		self.SubRigs += [ self.ArmR         , self.ArmL      ]
		self.SubRigs += [ self.ThuR         , self.ThuL      ]
		self.SubRigs += [ self.IndR         , self.IndL      ]
		self.SubRigs += [ self.MidR         , self.MidL      ]
		self.SubRigs += [ self.RngR         , self.RngL      ]
		self.SubRigs += [ self.PnkR         , self.PnkL      ]
		self.SubRigs += [ self.HandInvR     , self.HandInvL  ]

		self.SubRigs += [ self.LegR         , self.LegL     ]
		self.SubRigs += [ self.FootR        , self.FootL    ]
		self.SubRigs += [ self.ToeIndR      , self.ToeIndL  ]
		self.SubRigs += [ self.ToeMidR      , self.ToeMidL  ]
		self.SubRigs += [ self.ToeRngR      , self.ToeRngL  ]
		self.SubRigs += [ self.ToePnkR      , self.ToePnkL  ]
		self.SubRigs += [ self.FootInvR     , self.FootInvL ]

		self.SubRigs += [ self.EyeR         , self.EyeL         ]
		self.SubRigs += [ self.EarR         , self.EarL         ]
	
		self.SubRigsName += [ 'ClavicleR'    , 'ClavicleL'    ]
		self.SubRigsName += [ 'ScapulaR'     , 'ScapulaL'     ]
		self.SubRigsName += [ 'ArmR'         , 'ArmL'         ]
		self.SubRigsName += [ 'ThuR'         , 'ThuL'         ]
		self.SubRigsName += [ 'IndR'         , 'IndL'         ]
		self.SubRigsName += [ 'MidR'         , 'MidL'         ]
		self.SubRigsName += [ 'RngR'         , 'RngL'         ]
		self.SubRigsName += [ 'PnkR'         , 'PnkL'         ]
		self.SubRigsName += [ 'HandInvR'     , 'HandInvL'     ]

		self.SubRigsName += [ 'LegR'         , 'LegL'         ]
		self.SubRigsName += [ 'FootR'        , 'FootL'        ]
		self.SubRigsName += [ 'ToeIndR'      , 'ToeIndL'      ]
		self.SubRigsName += [ 'ToeMidR'      , 'ToeMidL'      ]
		self.SubRigsName += [ 'ToeRngR'      , 'ToeRngL'      ]
		self.SubRigsName += [ 'ToePnkR'      , 'ToePnkL'      ]
		self.SubRigsName += [ 'FootInvR'     , 'FootInvL'     ]

		self.SubRigsName += [ 'EyeR'         , 'EyeL'         ]
		self.SubRigsName += [ 'EarR'         , 'EarL'         ]

		#CLASSE UTILS

		#UPDATE
		name = args.get( 'n'   , None )	
		pos  = args.get( 'pos' , None )
		if not( name == None ): self.Name.add( 'base' , copy = name ) 
		if not( pos  == None ): pass


       