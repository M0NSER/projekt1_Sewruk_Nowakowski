my_list1 = [x for x in range(1, 10 + 1)]
my_list2 = my_list1[5:]
my_list1 = my_list1[:5]


print(my_list1)
print(my_list2)



my_list1 += my_list2
print(my_list1)

my_list1 = [0]+my_list1
print(my_list1)


copy_my_list1 = my_list1
copy_my_list1.sort(reverse=True)
print(copy_my_list1)
