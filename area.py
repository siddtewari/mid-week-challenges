import math

def areaCalc(choice, param1, param2):
	if not((choice == 1) or (choice == 2) or (choice ==3)):
		print 'Please enter a valid choice - 1 for Triangle; 2 for Rectangle; 3 for Circle'
	else:
		if choice == 1:
			triangleArea = .5 * float(param1) * float(param2)
			print ("Triangle area is %f" %triangleArea)
		elif choice == 2:
			rectArea = float(param1) * float(param2)
			print ("Rectangle area is %f" %rectArea)
		elif choice == 3:
			circleArea = math.pi *  param1 * param2
			print ("Area of the Circle is %f" %circleArea)

areaCalc(choice = 1, param1= 5, param2=4)
areaCalc(choice = 2, param1= 5, param2=4)
areaCalc(choice = 3, param1= 5, param2=5)		