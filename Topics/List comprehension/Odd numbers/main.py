numbers = input()
# new_list = [num for num in numbers if int(num) % 2 != 0]
new_list = [int(x) for x in numbers if int(x) % 2 != 0]
print(new_list)

