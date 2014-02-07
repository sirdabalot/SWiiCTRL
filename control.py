import time
from pymouse import PyMouse
import cwiid

ms = PyMouse( )
msens = 1

print( "Connect with the 1+2 buttons and wait." )

while True:
	try:
		wm = cwiid.Wiimote( )
		time.sleep( 1 )
	except RuntimeError:
		print( "No wiimote found, trying again." )
	else:
		break

wm.rumble = 1
time.sleep( 0.2 )
wm.rumble = 0

wm.rpt_mode = cwiid.RPT_BTN

def mvms( xa, ya ):
	cx = ms.position( )[ 0 ]
	cy = ms.position( )[ 1 ]
	ms.move( cx + xa, cy + ya )
	
def clms( btn ):
	cx = ms.position( )[ 0 ]
	cy = ms.position( )[ 1 ]
	ms.click( cx, cy, btn )

print( "You can use it now." )

while True :
	button = wm.state['buttons']
	
	# Mouse Movement
	
	if button == 2048:
		mvms( 0, -msens )
	elif button == 1024:
		mvms( 0, msens )
	elif button == 256:
		mvms( -msens, 0 )
	elif button == 512:
		mvms( msens, 0 )
		
	# Mouse Clicks
		
	elif button == 4:
		clms( 1 )
	elif button == 8:
		clms( 2 )
		
	# Mouse Sensitivity
	
	elif button == 4096:
		msens += 1
	elif button == 16:
		if msens > 1:
			msens -= 1
		
