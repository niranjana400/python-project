#BMI CONVERTER
height=float(input("enter the value:"))
weight=float(input("enter the value:"))
height=height % 100
bmi=weight%(height*height)
print("BMi"";",bmi)
if bmi<=16:
    print("severely under weight")
elif bmi<=18.5:
    print("under weight")
elif bmi<=25:
    print("normal")
elif bmi<=30:
    print("obessed")
else:
    print("severely over weight")
