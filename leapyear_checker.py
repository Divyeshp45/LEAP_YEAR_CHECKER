year = int(input("Which year do you want to check? "))

#CHECKS IF A YEAR IS A LEAP YEAR
year_1=year/4
integer_year1=int(year_1)   #CONVERTED FLOAT TO INTEGER
year_2=year/400
integer_year_2=int(year_2)  #CONVERTED FLOAT TO INTEGER
year_3=year/100
integer_year_3=int(year_3)
if year_1 == integer_year1 :            #HERE IN CONDITION I MATCHED FLOAT==INT
    if year_2 == integer_year_2  :
      print(" Leap year")
    elif year_3 == integer_year_3:
      print(" Leap year.")
    else :
      print("Leap year")
else:
    print("Not a leap year")        




