#1
def max_num(*args):
    return max(args)
# print(max_num(1,2,3,4,5,6))

#2
def multi_list(*args):
    return sum(args)
# print(multi_list(1,2,3,4,5,6))

#3
def rev_string(string):
    return string[::-1]
# print(rev_string("hello"))

#4
def num_within(number, start, end):
    return start <= number <= end

# print(num_within(5,1,10))

#5
def pascal(n):
    pascal_list = []
    for i in range(n):
        pascal_list.append([])
        for j in range(i+1):
            if j == 0 or j == i:
                pascal_list[i].append(1)
            else:
                pascal_list[i].append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
    return pascal_list

print(pascal(5))