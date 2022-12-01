def function_increment_number (a, b, c):
    out_message = ""
    while a < b:
        out_message = out_message + str(a) + ","
        a += c
    print("Congrats! Increment history is: " + out_message + str(a))

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
function_increment_number (a,b,c)

