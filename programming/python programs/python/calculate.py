print("Let's Do Your Maths Homework")
problem = input("Enter a math problem, or 'E' to Exit:")
while(problem!="E"):
    print("The Answer to", problem, "is:", eval(problem))
    problem = input("Enter a math problem, or 'E' to Exit:")
