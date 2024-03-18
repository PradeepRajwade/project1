def add (num1,num2):
    return (num1+num2)
def sub (num1,num2):
    return(num1-num2)
def multiply (num1,num2):
    return(num1*num2)
def divide(num1,num2):
    return(num1/num2)

print("Please select operation--\n"\
    "1.add\n"\
    "2.sub\n"\
    "3.multiply\n"\
     "4.divide\n")
    
select=int(input("select operation from 1,2,3,4 :"))

number_1=int(input("enter your first number:"))
number_2=int(input("enter your second number:"))
if select==1:
    print(number_1,"+",number_2,"=",add(number_1,number_2))
elif select==2:
    print(number_1,"-",number_2,"=",sub(number_1,number_2))
elif select==3:
    print(number_1,"x",number_2,"=",multiply(number_1,number_2))
elif select==4:
    print(number_1,"/",number_2,"=",divide(number_1,number_2))
else:
    print("invalid input")






