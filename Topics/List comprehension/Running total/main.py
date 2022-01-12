numbers = input()
number_list = [int(x) for x in numbers]
sum1 = 0
a = []
# list_sum = [sum1 := sum1 + int(x) for x in number_list]
total = [0]
for i in number_list:
    total.append(total[-1] + i)
total.pop(0)

print(total)
