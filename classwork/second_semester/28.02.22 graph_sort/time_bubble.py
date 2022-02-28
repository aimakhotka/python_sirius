import random
import time
import matplotlib.pyplot as pt

def bubble(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

#print(bubble([random.randint(0, 10) for _ in range(10)]))

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
        q = nums[len(nums) // 2]
        l_nums = [n for n in nums if n < q]

        e_nums = [q] * nums.count(q)
        b_nums = [n for n in nums if n > q]
        return quicksort(l_nums) + e_nums + quicksort(b_nums)

def times():
    times_bb, times_q, ns = [], [], []  
    for i in range(200, 401, 50):
        values = [i for i in range(i)]
        random.shuffle(values)
        values2 = values.copy()

        t = time.time()
        bubble(values)
        res_time = time.time() - t
        times_bb.append(res_time)
        ns.append(ns)

        t = time.time()
        quicksort(values2)
        res_time = time.time() - t
        times_q.append(res_time)
        ns.append(ns)

    pt.plot(times_bb, ns)
    pt.plot(times_q, ns)

times()