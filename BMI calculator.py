#BMI CALC 
counter = 0 

while counter < 1:
    meassure = str(input("which system would you like to use: metric or imperial? "))
    weight = float(input("input your weight(lbs/kg)!"))
    height = float(input("input your height!(m/in)"))
    if meassure == "metric":
        if height > 0.64 and height < 2.73:
            if weight > 6.5 and  weight < 79:
                bmi = weight / (height * height)
                print("your body mass index in metric units is: ", bmi)
                counter += 1
    elif meassure == "imperial":
        if weight > 14.2 and  weight < 174:
            if height > 25.6 and height < 107:
                bmi = weight / (height * height) * 703
                print("your body mass index in imperial is: ", bmi)
                counter += 1
    else:
        print("some information you input was incorrect")


'''height values: 
met_______________
smallest in m: 0.65 
tallest in m:2.72 

imp_______________
smallest in inc: 2ft 1.6 
tallest in inc: 8ft 11 

weight values:
met________________
smallest in kg: 6.5 
tallest in kg: 79 

imp________________
smallets in lbs: 14.3 
tallest in lbs: 174 
'''