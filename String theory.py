def is_palindrome(text):

    t_len = len(text)
    temp = ""

    for i in range(t_len):

        if text[i].isalpha():

            temp = temp + text[i].lower()

    print(temp)
    """
    >>> is_palindrome('Mr. Owl ate my metal worm')
    True
    >>> is_palindrome('Eva, can I see bees in a cave?')
    True
    """


def is_isogram(text):

    verify_word = text.lower()
    letter_list = []

    for letter in verify_word:

        if letter.isalpha():

            if letter in letter_list:
                print("Nope, not an isogram.")

                return False

            letter_list.append(letter)

    print("You've got yourself an isogram.")
    return True

    """
    >>> is_isogram('uncopyrightables')
    True
    """


def is_pangram(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in alphabet:
        if char not in str.lower():
            return False

    return True

    string = text

    if (is_pangram(string) == True):
        print("Yes")

        return True

    else:
        print("No")

        return False
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """


def is_anagram(text1, text2):

    string_one = text1
    string_two = text2

    if(sorted(string_one) == sorted(string_two)):
        print("The strings are anagrams.")

        return True

    else:
        print("The strings aren't anagrams.")

        return False
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """


def is_blanagram(text1, text2):
    # uh... this one is a bit interesting. I think the anagram func works here
    # but would need to be changed?
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
