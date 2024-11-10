#Project1:Traffic Light Simulator
light=input("enter the colour of  traffic signal: ")
light=light.lower()
if light=="red":
    print("the vehicle cannot move")
elif light=="yellow":
    print('get ready to move')
elif light=="green":
    print("the vehicle can move")
else:
    print('please give the correct input')
