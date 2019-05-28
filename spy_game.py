def spy_game(nums):

    code = [0,0,7, 'x']
    # [0,7,'x']
    # [7, 'x']
    # ['x'] length=1
    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) ==1


def square (num):
    return num **2

my_nums = [1,2,3,4,5]


for item in map(square,my_nums):
    print(item
