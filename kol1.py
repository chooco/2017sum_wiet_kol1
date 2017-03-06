Flight simulator. Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
The program should print out current orientation, and applied tilt correction. 
The program should run in infinite loop, until user breaks the loop. 
Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
With every simulation step the orentation should be corrected, applied and printed out.

#!/usr/bin/python
import random

class planePosition(position):

 current_position = 0
 correction = random.gauss(0,1)
 correct_position = current_position - correction

 return correct_position

print "/n"

while(True):
 print "Current orientation: " + correct_position
 print "Applied correction: " + correction 
