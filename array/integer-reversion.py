

# excludes "0"

def reverse_integer(nums):

    reversed_nums = 0
    remainder = 0

    while nums > 0:
        remainder = nums % 10
        reversed_nums = reversed_nums*10 + remainder
        nums = nums // 10

    return reversed_nums


if __name__ == "__main__":
    print(reverse_integer(1234))
