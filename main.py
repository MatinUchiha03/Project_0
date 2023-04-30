kms = input("How many kilometers did you drive?")

miles = float(kms) / 1.60934

if miles > 15:                                                    #Condition:
    print("Error")
elif miles < 15:
    print("Error")
else:
    print(f"You drove {miles} miles ") 

kilogram = input("How many kilograms do you weight?")                                                #Conversion:
gram = float(kilogram) * 1000

if gram > 100000:                                                 #Condition:
    print("Error")
else:
    print(f"your weight is {gram} g")