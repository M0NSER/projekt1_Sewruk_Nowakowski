def foo1(a_list, b_list):
    result = []

    for i in range(0, len(a_list)):
        result.append(a_list[i])
        result.append(b_list[i])

    return result



a = [1,3,5]
b=[2,4,6]

print(foo1(a,b))