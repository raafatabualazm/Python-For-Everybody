import re

reg_file = open('regex_sum_102434.txt')

all_words = reg_file.read()

num_list = re.findall('[0-9]+', all_words)

sum = 0

for number in num_list:
    sum = sum + int(number)
print(sum)