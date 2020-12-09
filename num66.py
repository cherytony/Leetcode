# class Solution:
#     def plusOne(self, digits):
#
#         s = 0
#         a_list = []
#
#         for i in digits:
#             s = s * 10 + i
#
#         for j in str(s + 1):
#             a_list.append(int(j))
#
#         return a_list

def plusOne(digits):
    s = 0
    a_list = []
    add_list = []

    for i in digits:
        s = s * 10 + i
    print(s)

    for j in str(s + 1):
        print(j)
        print('int(j),', int(j))
        a_list.append(int(j))
    print('a_list:', a_list)
    if len(digits) > len(a_list):
        add_zero = len(digits) - len(a_list)

        for i in range(0, add_zero):
            add_list.append(0)

        add_list.extend(a_list)

        return add_list
    else:
        return a_list


plusOne([0, 0])
