def run():
    number = int(input("Choose a number to see if it's prime or not: "))
    if is_Prime(number):
        print("It is prime")
    else:
        print("It isn't prime")

def is_Prime(number):
    counter = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1

    if counter == 0 and number != 1:
        return True
    else
        return False

if __name__ == "__main__":
    run()