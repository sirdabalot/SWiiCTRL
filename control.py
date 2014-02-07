import time
from pymouse import PyMouse
import cwiid

print( "Connect with the 1+2 buttons and wait." )

wm = cwiid.Wiimote( )
ms = PyMouse( )

msens = 1

time.sleep( 1 )

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
	if button == 2048:
		mvms( 0, -msens )
	elif button == 1024:
		mvms( 0, msens )
	elif button == 256:
		mvms( -msens, 0 )
	elif button == 512:
		mvms( msens, 0 )
	elif button == 4:
		clms( 1 )
	elif button == 8:
		clms( 2 )
		
