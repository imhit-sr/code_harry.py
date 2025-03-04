def main():
    return f"The is it and you are welcome to"

def add(num1,num2):
    return num1+num2+34
print(f"And the name is {__name__}")   # The Value of Name is main 
# is the same where __name__ == '__main__': is defined
# at the file where it is imported it will print the file where name and main
# is defined
if __name__ == '__main__':
    print(main())
    print(add(5,2))
