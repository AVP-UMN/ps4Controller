import sys, pygame, time

class PS4_Control():
	def handleJoyEvent(self, e):
		if e.type == pygame.JOYAXISMOTION:
			if(e.dict['axis'] == 0):
				pos = e.dict['value']
				move = round(pos * -45, 0)
				print "Left_joy :" + str(move)
				return ["left_joy", int(move)]

			if ((e.dict['axis'] == 2)):
				pos_y = e.dict['value']
				speed = round(pos_y * -10)
				print "Right_joy :" + str(speed)
				return ["right_joy", int(speed)]

			if ((e.dict['axis'] == 1)):
				print "I am axis 1"

		elif e.type == pygame.JOYBUTTONDOWN:
			if(e.dict['button'] == 0):
				print "button S"
				return ["button", "S"]
			if(e.dict['button'] == 1):
				print "button X"
				return ["button", "X"]
			if(e.dict['button'] == 2):
				print "button O"
				return ["button", "O"]
			if(e.dict['button'] == 3):
				print "button T"
				return ["button", "T"]

