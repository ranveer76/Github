import turtle
juice = turtle.numinput("Juice", "Number of Juice Glasses?")
tea = turtle.numinput("Tea", "Number of Tea Cups?")
coffee = turtle.numinput("Coffee", "Number of Coffee Cups?")
cost_juice = 100
cost_tea = 20
cost_coffee = 50
bill = juice*cost_juice + tea*cost_tea + coffee*cost_coffee
GST = 0.18*bill
total_bill = bill + GST
print("Amount Rs.", bill)
print("GST 0.18% Rs.",GST)
print("Total Amount with GST Rs.",total_bill)
