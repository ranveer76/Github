import turtle

your_height = turtle.numinput("your height", "what is your height")
your_weight = turtle.numinput("your weight", "what is your weight")
BMI = your_height/(your_weight/100)**2
print("your BMI is = ",BMI) 
