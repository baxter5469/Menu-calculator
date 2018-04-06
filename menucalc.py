''' Menu Calculator v.01 By Andrew Ault
4/5/18
'''
userinput = ""
manyinput = True
print("Welcome to Menu Calculator! Press Enter to contiune.")
input()
print("There is five different options for what food you can order.")
input()
print("'1'Pizza - Small $8.99\n'2'Pizza - Medium $11.99\n'3'Pizza - Large $14.99\n'4'Breadsticks - Regular $4.99\n'5'2 Liter Soda - $3.99")
while userinput != "quit":
    print("When you are done ordering type quit and the program will move on")
    userinput = input("Please type in the number next to the item you want: ")
    if userinput == "quit":
        break
    try:
        userinput = int(userinput)
        if userinput > 5:
            print("not in range, try again")
            continue
    except:
        print("Oops! That is not a number!")
        continue
    while True:
        howmany = input("How many?: ")
        try:
            howmany = int(howmany)
            break
        except:
            print("Oof, not a number!")
            continue