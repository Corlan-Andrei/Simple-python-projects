def numbers_listing():
    numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
    print(numbers)
    i = 0
    N = len(numbers)

    while i < N - 1:
        j = 0

        while j < N - i - 1:

            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp

            j = j + 1

        i += 1

    print(numbers)


numbers_listing()


#and this is why you provide your variables with legible, understandable names
#seriously, I get that math looks like this, but this is stupid.
#I suppose I should be using comments for stuff like this then? Still feels stupid

#In any case, the program has a list that it will iterate through,
#setting the values of the list into the two variables "i" and "j"
#and comparing them against each other until you have a list of ascending values
