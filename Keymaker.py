#all of this for a Matrix reference....

def shift_characters(word, shift):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_word = ""
    shifted_letter = word.lower()

    for char in shifted_letter:

        if char not in alphabet:
            print("The characters of your string must be letters. Try again please.")
            break

        else:
            shifting_letter = chr((ord(char) - 97 + shift) % 26 + 97)
            shifted_word += shifting_letter

    print(shifted_word)
    return shifted_word


def pad_up_to(word, shift, n):
    final_word = word
    word2 = ""

    while float(len(final_word)) < float(n):
        x = shift_characters(word, shift)

        for element in x:
            final_word = final_word + element
            word2 = word2 + element
        word = word2

    return final_word[:n]


def abc_mirror(word):

    import string
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mirroring_word = word.lower()

    for char in mirroring_word:
        if char not in alphabet:
            print("ERROR: The characters of your string must be letters.")
            break

        else:
            letters = string.ascii_lowercase
            rep_dict = dict(zip(letters, letters[::-1]))
            mirror_word = ''.join(map(rep_dict.get, word.replace(" ", "").lower()))
            print(mirror_word)
            return mirror_word


def create_matrix(word1, word2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_word = ""
    shifted_letter = word1.lower()

    for element in word2:
        shift = ord(element)

        for char in shifted_letter:

            if char not in alphabet:
                print("ERROR: The characters of your string aren't all letters.")
                break

            else:
                shifting_letter = chr((ord(char) - 97 + shift) % 26 + 97)
                shifted_word += shifting_letter

        print(shifted_word + ", " + word2)
        return shifted_word

# final = []
# for x in word2:
#     shift = ord(x) - 97
#     final.append(shift_characters(word1,shift)
#     return final


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    'adgjkhebcfil'
    """
    pass


def rotate_right(word, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in word:
        if char not in alphabet:
            print("ERROR: The characters of your string must be letters.")
            break

    first_rotation = word[0:len(word) - n]
    second_rotation = word[len(word) - n:]
    print(word + ", " + (second_rotation + first_rotation))
    return (second_rotation + first_rotation)


def get_square_index_chars(word):

    result = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in word:
        if char not in alphabet:
            print("ERROR: The characters of your string must be letters.")
            break

    for letter in word:
        temp = letter
        result.append(alphabet.index(temp))
    return result


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    'bafedc'
    """
    pass


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


# if __name__ == '__main__':
#     name = input("Enter your name! ").lower()
#     print(f'Your key: {hash_it(name)}')
