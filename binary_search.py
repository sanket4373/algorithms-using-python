# This function is used to implement binary search which is basically guessing the number that 

def binary_search(mylist, number):
    low = 0
    high = len(mylist)-1

    while low <= high:
        mid = round((low + high)/2)
        print("mid here: ", mid)
        guess = mylist[mid]
        print("guess here: ", guess)

        if guess == number:
            print("mid here again: ", mid)
            return mid
        if guess > number:
            high = mid - 1
            print("high here: ", high)
        else:
            low = mid + 1
            print("low here: ", low)
    return None   


mylist = [1, 3, 5, 7, 9, 11]

print(binary_search(mylist, 4))
