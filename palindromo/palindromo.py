def palindrome(word):

    word = word.replace(' ', '').lower()
    if word == word[::-1]:
        return True
    else:
        return False


def run():
    word = input('Write a word: ')

    if palindrome(word) == True:
        print('Is a palindrome')
    else:
        print("Isn't a palindrome")


if __name__ == '__main__':
    run()
