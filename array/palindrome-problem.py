

# def check_palindrome(str):

#     start_index = 0
#     end_index = len(str) - 1

#     while start_index < end_index:
#         if (str[start_index] != str[end_index]):
#             return False
#         start_index += 1
#         end_index -= 1

#     return True

def check_palindrome(str):

    if str != str[::-1]:
        return False

    return True


if __name__ == "__main__":

    str = "tot"
    print(check_palindrome(str))
