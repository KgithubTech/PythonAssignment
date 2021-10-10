x=int(input("enter year"))
print(x)
if x%4 == 0:
	if x%100 == 0:
		if x%400 == 0:
			print ("leap year")
		else:
			print (" not a leap year because not divisible by 400")
	else:
		print (" not a leap year because not divisible by 100")
else :
	print (" not a leap year because not divisible by 4")