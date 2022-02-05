##88
# from array import*
# nums = array('i', [])
# for i in range(5):
#     a = int(input("숫자를 입력하세요. : "))
#     nums.append(a)
# nums = sorted(nums)
# nums.reverse()
# print(nums)



##89
# from array import*
# import random
# nums = array('i',[])
# for i in range(5):
#     num = random.randint(1,10)
#     nums.append(num)
# for i in nums:
#     print(i)



##90번
# from array import*
# nums = array('i', [])
# n = 0
# while n < 5 :
#     num = int(input("숫자를 입력하세요. : "))
#     if 10<=num<=20:
#         nums.append(num)
#         n += 1
#     else:
#         print("Outside the range")

# print("감사합니다.")
# for i in nums:
#     print(i)



##91번
# from array import*
# nums = array('i', [1,2,3,3,4])
# print(nums)

# num = int(input("리스트에 있는 숫자들 중 하나를 입력하세요 : "))
# print(f"입력한 숫자는 {nums.count(num)}개 있습니다.")



##92번
# from array import*
# nums1 = array('i',[])
# nums2 = array('i',[11,22,33,44,55])

# for i in range(3):
#     num = int(input("숫자를 입력하세요. : "))
#     nums1.append(num)
# nums1.extend(nums2)
# nums1 = sorted(nums1)
# for i in nums1:
#     print(i)



##93번
# from array import*
# nums = array('i',[])
# for i in range(5):
#     num = int(input("숫자를 입력하세요. : "))
#     nums.append(num)

# nums = sorted(nums)
# print(nums)

# remove_num = int(input("숫자들 중 하나를 고르세요. : "))
# nums.remove(remove_num)
# print(nums)



##94번
# from array import*
# nums = array('i',[1,2,3,4,5])
# for i in nums:
#     print(i)


# while True:
#     idx = int(input("숫자들 중 하나를 고르세요. : "))

#     if idx in nums:
#         print(nums[idx])
#         break
#     else :
#         print("올바른 숫자를 입력하세요. : ")
#         continue




##95번
# from array import*
# nums = array('d', [10.23, 20.34, 34.56, 45.67, 78.99])


# while True:
#     num = int(input("2와 5사이의 정수를 입력하세요. : "))
#     if 2 <= num <= 5 :
#         for i in nums:
#             print(f"{i}/{num} = {i/num : .2f}")
#         break

#     else:
#         print("범위를 벗어난 숫자 입니다.")
#         continue