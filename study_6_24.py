# nums = [1, 3, 5, 11, 20, 22, 35, 36, 37, 40, 45, 46,57,84,93,99,101,156]
# # 二分法
# # 找到列表中间的值，比较中间的值和目标值。目标值比中间值大，就将列表切片为右边部分，反之，切片为左边，找到的话就直接打印


# def binary_search(find_num, nums):
#     print(nums)
#     if  not nums == []:
#         mid_val = (nums[len(nums)//2])
#         if find_num > mid_val:
#             num = nums[len(nums)//2+1:]
#             binary_search(find_num, num)
#         elif find_num < mid_val:
#             num = nums[0:len(nums)//2]
#             binary_search(find_num, num)
#         elif find_num == mid_val:
#             print("找到了")
#     else:
#         print('找不到')


# binary_search(66, nums)



# def func(k):
#     return salaries[k]


# salaries = {
#     'siry': 2000,
#     'tom': 7000,
#     'lili': 10000,
#     'jack': 200
# }
# 找出薪资最高的那个人
# res=max(salaries, key=func)
# print(res)
# res=max(salaries,key=lambda k:salaries[k])
# print(res)


#模块
# 


# print(foo.x)
# print(foo.func1)
# x=3333333
# foo.func1()