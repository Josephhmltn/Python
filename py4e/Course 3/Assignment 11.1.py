import re
file = open("regex_sum_1765682.txt")
lines = file.read()
numbers = re.findall('[0-9]+',lines)
sum = 0
for number in numbers:
    number = int(number)
    sum = sum + number
print(sum)