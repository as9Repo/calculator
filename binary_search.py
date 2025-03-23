def binary_search(a, low, high, x):
    # check if high is greater than or equal to low
    if high >= low:
        # calculate mid as the sum of high divided by low divided by 2
        mid = (high + low) // 2
        # if the item in the list at the index mid is equal to x
        if a[mid] == x:
            # return the value mid
            return mid
        # otherwise if the item in the list at the index mid is greater than x
        elif a[mid] > x:
            # return the value from calling binary_search with a, low, mid-1 and x
            return binary_search(a, low, mid - 1, x)
        # otherwise if neither of the above are true
        else:
            # return the value from calling binary_search with a, mid + 1, high and x
            return binary_search(a, mid + 1, high, x)
    # otherwise if high isn't greater than or equal to low
    else:
        # return the value None
        return None

# List of test data containing 2, 3, 4, 10 and 40
data = [ 2, 3, 4, 10, 40 ]

# Set num to 10
num = 10

# Call binary_search with data, 0, len(data)-1 and num and store the return
# value into the index variable
index = binary_search(data, 0, len(data)-1, num)
 
# if the index doesn't equal None
if index != None:
    # Output the number found at index
    print("Number found at index", str(index))
else:
    # Otherwise output Number is not in the list
    print("Number is not in the list")