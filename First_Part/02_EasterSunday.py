def main():

    #ask the user to enter a number for the year
	y = eval(input("Enter year: "))

	#Below are all the caculation needed for getting the date
	a = y % 19

	b = y // 100
	c = y % 100

	d = b // 4
	e = b % 4

	g = (8*b+13) // 25
	h = (19*a + b - d - g+15)%30

	j = c // 4 
	k = c % 4

	m = (a + 11*h) // 319
	r = (2*e + 2*j - k -h + m + 32) % 7 

	n = (h - m + r + 90) // 25

	p = (h - m + r +n + 19) % 32
    
    #after the whole calculation, print the Easter Sunday information to the user
	print ("In", y, "Easter Sunday is on", p, "April.")

main()






