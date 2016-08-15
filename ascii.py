def main():
    num = getNumber()
    print("{} {:>2s}".format(num, chr(num)))

def getNumber():
    valid = False
    while valid != True:
        try:
            num = int(input("please enter a number (10 - 50)"))
            valid = True
        except ValueError:
            print("Please enter a valid integer.")

    while num > 50 or num < 10:
        valid = False
        while valid != True:
            try:
                num = int(input("please enter a number (10 - 50)"))
                valid = True
            except ValueError:
                print("Please enter a valid integer.")
    return num

main()