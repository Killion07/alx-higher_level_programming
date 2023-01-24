num1, num2 = input("Please enter two numners: ").split()

try:
    div = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, div))

except ZeroDivisionError:
    print("You can't divide by zero")

else:
    print("You did't raise an error")
finally:
    print("I will always execute")
