# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    #base case
    if len(array) == 0:
        return False
    if array[0] == query:
        return True
    return search(array[1::], query)


# is_palindrome
def is_palindrome(text):
    #base case
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    #base case:
    if not num1 and not num2:
        return 1
    if not num1 or not num2:
        return 0
    current_match = 0
    
    if num1 < 10 and num2 < 10:
        if num1 % 10 == num2 % 10:
            return 1
        else:
            return 0
    else:
        if num1 % 10 == num2 % 10:
            current_match = 1
    return digit_match(num1 // 10, num2 // 10) + current_match

