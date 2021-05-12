
import math
def catenary(a,b,r_length,N,sagInit):
	maxIter	= 100       # maximum number of iterations
	minGrad	= 1e-10     # minimum norm of gradient
	minVal	= 1e-8      # minimum norm of sag function
	stepDec	= 0.5       # factor for decreasing stepsize
	minStep	= 1e-9		 # minimum step size
	minHoriz	= 1e-3		 # minumum horizontal distance
	if( sagInit < 5):
		sag = 1
	else:
		sag = sagInit

	#DEAL
	if( a[0] > b[0] ):
		aTmp = a[:]
		a = b[:]
		b = aTmp[:]

	#GET DIMENTION BTW TWO POINTS
	d = b[0]-a[0]
	h = b[1]-a[1]

	#ALMOST VERTICAL MODE
	if( abs(d) < minHoriz ):
		X = [ (a[0]+b[0])/2 for nTmp in range(0,N) ]
		print('ALMOST VERTICAL MODE')

		if( r_length < abs(h) ): # rope is stretched
			Y		= linspace(a[1],b[1],N)
		else:
			sag	= (r_length-abs(h))/2
			n_sag = math.ceil( N * sag/r_length )
			y_max = max(a[1],b[1])
			y_min = min(a[1],b[1])
			Y	  = linspace( y_max, y_min-sag, N-n_sag ) + linspace( y_min-sag, y_min, n_sag)
		return [ X , Y ]

	#NORMAL MODE
	X = linspace(a[0],b[0],N)
	dist = math.sqrt( pow(d,2) + pow(h,2) )

	if( r_length <= dist  ):# rope is stretched
		Y = linspace(a[1],b[1],N)	
	else:
		# find rope sag

		for i in range( 0 , maxIter ):
			val		= g(sag,d,h,r_length) 
			grad    = dg(sag,d)
			if( abs(val) < minVal )or( abs(grad) < minGrad ):
				break

			search	= -g(sag,d,h,r_length) /dg(sag,d)
			
			alpha   = 1
			sag_new = sag + alpha*search;
			
			while( sag_new < 0 )or( abs( g(sag_new,d,h,r_length) ) > abs(val) ):
				alpha		= stepDec*alpha
				if( alpha < minStep):
					break
				sag_new	= sag + alpha*search			

			sag = sag_new

		# get location of rope minimum and vertical bias
		x_left	= 1.0/2.0*( math.log((r_length+h)/(r_length-h))/sag-d)
		x_min		= a[0] - x_left
		bias		= a[1] - math.cosh(x_left*sag)/sag
		
		Y			= [ math.cosh((x-x_min)*sag)/sag + bias for x in X ]

	return [X,Y]



def linspace( valA , valB , nbr ):
	delta = (valB - valA)/float(nbr)

	vals = []
	current = valA
	for nTmp in range(0,nbr):
		vals.append( current )
		current += delta

	return vals
	

def g(s,d,h,r_length):
	return 2*math.sinh(s*d/2)/s - math.sqrt( pow(r_length,2)-pow(h,2))

def dg(s,d):
	return 2*math.cosh(s*d/2)*d/(2*s) - 2*math.sinh(s*d/2)/pow(s,2)



'''

import maya.cmds as mc

Ax = mc.getAttr( 'A.translateX' )
Ay = mc.getAttr( 'A.translateY' )
Bx = mc.getAttr( 'B.translateX' )
By = mc.getAttr( 'B.translateY' )

length = 35
nbrPoints = 11

X,Y = catenary([Ax,Ay],[Bx,By],length,nbrPoints,1)


for i in range(0,len(X)):
    mc.setAttr( 'locator{}.translateX'.format(i) , X[i] )
    mc.setAttr( 'locator{}.translateY'.format(i) , Y[i] )
        




'''