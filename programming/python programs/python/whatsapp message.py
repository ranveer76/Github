import pywhatkit as p
a = '+91'+input('enter no. you want to send message:\n')
print()
b = input('enter message you want to send:\n')
li = int(input('enter no. of times you want to send:\n'))
for i in range(li):
    p.sendwhatmsg_instantly(a, b)
