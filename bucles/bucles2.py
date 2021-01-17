def run():
    name = input("What's your name?: ")
        
    for character in name:
        print(character, end=", ")

if __name__ == '__main__':
    run()
