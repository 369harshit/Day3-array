# Python3 program to find Majority element in an array

# Function to find Majority element
# in an array
def findMajority(arr, n):
    flag = 0
    for i in range(n):
        count = 0
        for j in range(i, n):
            if (arr[i] == arr[j]):
                count += 1

        # If count is greater than n/3 means
        # current element is majority element
        if (count > int(n / 3)):
            print(arr[i], end=" ")
            flag = 1

    # If flag is 0 means there is no
    # majority element is present
    if (flag == 0):
        print("No Majority Element")

arr = [11, 33, 33, 11, 33, 11]
n = len(arr)

# Function calling
findMajority(arr, n)
