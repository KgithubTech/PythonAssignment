# If the driver is married. // # If the driver is unmarried, male & above 30 years of age. // # If the driver is unmarried, female & above 25 years of age. // # In all other cases the driver is not insured. If the marital status, sex // and age of the driver are the inputs, write a program to determine // # whether the driver is to be insured or not.
Driver_MaritalStatus, Driver_Sex , Driver_Age= input("MaritalStatus","Sex","Age")
print(MaritalStatus,Sex,Age)


 if (Driver_MaritalStatus == "unmarried" and  Driver_Sex == "male" and Driver_Age> 30):
 print("Insured")

 if(Driver_MaritalStatus == "unmarried" and Driver_Sex == "female" and Driver_Age > 25):
  print("not Insured")



