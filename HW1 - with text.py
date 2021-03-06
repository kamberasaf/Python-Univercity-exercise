# Question 1:

def vowels(sentence):
    """ This will count letters in a given word that are A-Z
    or a-z minus case vowels ['a','e','i','o','u','y']. """
    not_vowels_letters = 0

    for i in sentence:
        if (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122) and i not in ['a','e','i','o','u','y']:
            not_vowels_letters += 1

    return not_vowels_letters


# Question 2:

def valid_input(x, n):
    """This function checks n is an integer, abs(x)<=0.7 and n>=0. """
    if not n.is_integer():
        return False
    elif not -0.7 <= x <= 0.7:
        return False
    elif not -0 <= n:
        return False

    return True


def taylor_appx(x, n):
    """ Taylor  series approximation of ln(1+x) of order n.
    if input is invalid, prints 'error' """
    if not valid_input(x, n):
        print('error')
        exit()
    taylor_sum = 0
    t = 1
    while t <= n:
        taylor_sum += (((-1) ** (t + 1)) * x ** t) / t
        t += 1
    print(taylor_sum)
    exit()


# This is to test Q2 only.
# taylor_appx(0.2,10)


# Question 3:

def play_with_strings(given_string):
    upper_case = []
    lower_case = []
    num = 0
    list_of_words = given_string.split()  # Will create a list of words from a given string.

    for i in range(len(list_of_words)):
        if i % 2:
            lower_case.append(list_of_words[num].lower())  # Adds the word as lowercase to the lowercase list.
            num += 1
        else:
            upper_case.append(list_of_words[num].upper())  # Does the same for the uppercase list.
            num += 1

    upper_case.sort()  # This will sort uppercase in ascending order.
    lower_case.sort(reverse=True)  # This will sort descending order for lowercase
    print(*upper_case, *lower_case)
    exit()


# Question 4:

def lychrel_numb(x):
    # This function is checking whether or not a given number is a Lychrel number.

    is_palindromic = False
    num_of_iterations = 0

    while not is_palindromic:
        if str(x) == str(x)[::-1]:  # Checks if a number is palindromic.
            print(num_of_iterations)
            break

        elif num_of_iterations > 500:
            print('True')
            is_palindromic = True

        else:
            x_rev = int(str(x)[::-1])  # This will reverse the digits on a given x.
            x += x_rev
            num_of_iterations += 1

    exit()


def welcome_menu():
    select = input('''
    (1) Vowels.
    (2) Taylor Approximation.
    (3) Playing with Strings.
    (4) Lychrel Numbers.

    Please select a number: ''')

    try:
        select = int(select)
    except ValueError:
        print("error")
        exit()

    if select == 1:
        word = input("\nEnter a sentence: ")
        print(vowels(word))
        exit()

    elif select == 2:
        number1 = input('\nPlease select a first number: ')
        number2 = input('\nPlease select a second number: ')
        try:
            number1 = float(number1)
            number2 = float(number2)
        except ValueError:
            print('error')
            exit()
        taylor_appx(number1, number2)

    elif select == 3:
        string = input('\nPlease enter a string: ')
        play_with_strings(string)

    elif select == 4:
        numb = int(input('\nPlease select a number: '))
        lychrel_numb(numb)

    else:
        print("error")
        exit()

if __name__ == '__main__':
    welcome_menu()