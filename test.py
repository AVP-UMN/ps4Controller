from ps4_control import PS4_Control
import sys, pygame, time

def joystickControl():
	control = PS4_Control()
	while True:
		e = pygame.event.wait()
		if (e.type == pygame.JOYAXISMOTION or e.type == pygame.JOYBUTTONDOWN):
			control.handleJoyEvent(e)

def main():
	pygame.joystick.init()
	pygame.display.init()
	if not pygame.joystick.get_count():
		print "\nPlease connect a joystick and run again.\n"
		quit()
	else:
		print "\n%d joystick(s) detected." % pygame.joystick.get_count()
		for i in range(pygame.joystick.get_count()):
			myjoy = pygame.joystick.Joystick(i)
			myjoy.init()
			print "Joystick :{} ".format( myjoy.get_name())
	joystickControl()

if __name__ == '__main__':
	main()

