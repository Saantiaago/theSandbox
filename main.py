# from someFunc import skobochki
# # from django import *
# import django
# from calculations import dig_pow
# from sumof import digital_root
#
# from pyramid import *
#
# from accun import accum
#
# from sentece import *
#
# # print(django.get_version())
# # print(skobochki("abcdeaa"))
#
# from persostance import *
# import duplicate
#
# from anagrams import *
#
# stro = "Ab cd ef"
#
#
# def cheto(strr):
#     arrayOfStr = [0] * len(strr)
#
#     for i in range(len(strr)):
#         arrayOfStr[i] = strr[i]
#
#     # for i in range(len(arrayOfStr)):
#     #     if (arrayOfStr[i] == " "):
#     #         arrayOfStr[i+1].upper()
#
#     for i in range(len(strr)):
#         arrayOfStr[0] = strr[0].upper()
#         if strr[i] == " ":
#             arrayOfStr[i + 1] = strr[i + 1].upper()
#             # print(strr[i+1].upper())
#
#     finalStr = ""
#
#     for i in range(len(strr)):
#         finalStr += arrayOfStr[i]
#
#     print(finalStr)
#     return (finalStr)
#
#
# def valid_parentheses(s):
#     while '()' in s or 'hi' in s:
#         s = s.replace('()', '')
#         s = s.replace('hi', '')
#     print(s)
#     if s == '':
#         return True
#     elif s.isalpha():
#         return True
#     else:
#         return False
#
#
# # print(valid_parentheses("hi(())"))
#
#
# def validBraces(s):
#     while '{}' in s or '()' in s or '[]' in s:
#         s = s.replace('{}', '')
#         s = s.replace('[]', '')
#         s = s.replace('()', '')
#     return s == ''
#
#
# # print(strr)
# #
# # dig_pow(92, 1)
# #
# # accum("RqaEzty")
# #
# # tower_builder(6)
# #
# # digital_root(99)
#
# # persistence(4)
#
# # order("4of Fo1r pe6ople g3ood th5e the2")
#
#
# # anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
#
# # duplicate.duplicate_count('Indivisibilities')
#
# # estimators = [
# #     ('rf', RandomForestClassifier(n_estimators=10, random_ state=42)),
# #      ('svr', make_pipeline (StandardScaler(), LinearSVC(random state=42))) ]
# #
# # model = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression()
# # CV = ShuffleSplit(n_splits=5, test_size=0.3, random_state=0)
# # print (cross_val_score(model, X_train, y_train, cv=CV).mean())
#
# # duplicate.sum_pairs([1, 4, 8, 7, 3, 15], 8)
#
#
# # print(duplicate.next_bigger(1257429))
# #
# # print(duplicate.is_solved([ [0, 0, 1],
# #                             [0, 1, 2],
# #                             [2, 1, 0]]))
#
# print(alphabet_string = string. ascii_lowercase)
# alphabet_string = string.ascii_lowercase


# A recently added
import collections
def findValue(s):
    counter = collections.Counter(s)
    res = 0
    levels = 1
    setOf = set(s)
    print(counter)
    for i in range(len(setOf)):
        if i > 8:
            levels = 2
        if i > 17:
            levels = 3
        maxFreq = max(counter, key = counter.get)
        print(maxFreq, ' ', i)
        res =res + levels * counter[maxFreq]
        # del counter[]
        del counter[maxFreq]

    print(res)

findValue('aabcdefghij')

def countFamilyLogins(logins):
    sett = set(logins)
    res = 0
    for item in logins:
        sb = ''
        for c in item:
            print(c)
            if  c == 'z':
                c = 'a'
            else:
                i = ord(c)
                i = i + 1
                c = chr(i)

                # c += 1
            sb += c
        print(sb)
        if (sb in sett):
            res += 1
    print(sett)

    return res
import math
import queue
import heapq

# def findeClosest(points, k):
#     points.sort(key = lambda x: (x[0]**2+x[1]**2, x[0]))
#
#     print(points)
#     return points[:k]
import collections

# print(findeClosest([ [4, 1] , [1, 4], [1, 1], [1, 3], [3, 1] ], 2))
k = 4
nums = [20, 4, 3, 1, 9]
score = 0


# pq = queue.PriorityQueue()
# for i in range(len(nums)):
#     pq.put(nums[i])
# while not pq.empty():
#     nextItem = pq.get()
#     print(nextItem)

# heapq.heapify(nums)
# print(nums)
# while k > 0:
#     maxi = heapq.nlargest(1, nums)
#     score += maxi
# # print(math.ceil(20/3))
# nums.sort(reverse=True)
# # print(nums)
# while k > 0:
#     score += max(nums)
#     index = nums.index(max(nums))
#     nums[index] = math.ceil(nums[index] / 3)
#     k -= 1
# print(score)
# heapq.heapify(nums)

# maxi = heapq.nlargest(1, nums)
# print(maxi)


# print(countFamilyLogins(['abc', 'abc', 'bcd']))
#
# private static int countFamilyLogins(List<String> logins){
#
#         HashSet<String> set = new HashSet<String>(logins);
#         int res = 0;
#         for(String item : logins){
#             StringBuilder sb = new StringBuilder();
#             for(char c : item.toCharArray()){
#                 if(c == 'z'){
#                     c = 'a';
#                 }else
#                     c += 1;
#
#                 sb.append(c);
#             }
#             if(set.contains(sb.toString())){
#                 res++;
#             }
#         }
#
#         return res;
#     }

import math
def check(stockPrice):
    for i in range(1,len(stockPrice)-1):

        firstHalf = stockPrice[:i]
        secondHalf = stockPrice[i:]
        print(firstHalf)
        print(secondHalf)
        print('------------')
        averageFirst = math.floor(sum(firstHalf) / len(stockPrice[:i]))
        averageSecond  = math.floor(sum(secondHalf) / len(secondHalf))
        if averageSecond == averageFirst:
            return i

print(check([1, 3, 2 ,3]))



def window(processes, n):
    left = 0
    right = n - 1
    currMax = 0
    while right < len(processes):
        print(processes[left], processes[right])
        print(processes[left:right+1])
        currMax = max(currMax, sum(processes[left:right+1]))

        left += 1
        right += 1
    return currMax

# print(window([10,4,8,13,20], 2))

def robot(lot):
    res = []
    def go(i, j, count):
        # print(lot)
        print('op')
        if i < 0 or j < 0 or i > len(lot) - 1 or j > len(lot[0]) -1:
            return
        if lot[i][j] == 9:
            res.append(count)
            return res
        if lot[i][j] == 1:
            lot[i][j] +=1
            go(i+1, j, count+1)
            go(i, j + 1, count + 1)
            go(i-1, j, count+1)

            go(i, j-1, count+1)

    go(0, 0, 0)
    return res
# print(robot([[1, 1, 1, 1],
#              [1, 1, 1, 9],
#              [1, 1, 1, 1]]))

#
from collections import deque
def removeObstacle(lot):
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]] # L R U B
    rows = len(lot)
    cols = len(lot[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = 1

    q = deque()
    q.append([0,0,0])

    while len(q) > 0:
        r,c, distance = q[0]
        if lot[r][c] == 9: # obstacles
            return distance
        q.popleft()
        for dr, dc in directions:
            row = r + dr
            col = c + dc
            if row >= 0 and col >= 0 and row < rows and col < cols:
                if (lot[row][col] == 1 or lot[row][col] == 9) and not visited[row][col]:
                    visited[row][col] = 1
                    q.append([row, col, distance+1])
    return -1

res = []
def bubblesort(elementss, count):
    swapped = False
    # Looping from size of array from last index[-1] to index [0]
    for n in range(len(elementss) - 1, 0, -1):
        for i in range(n):

            if elementss[i] > elementss[i + 1]:
                swapped = True
                count += 1
                # swapping data if the element is less than next element in the array
                elementss[i], elementss[i + 1] = elementss[i + 1], elementss[i]
                print(elementss)
                # res.append(count)
        # if not swapped:
        #     print(count)
        #     # exiting the function if we didn't make a single swap
        #     # meaning that the array is already sorted.
        #     return count
    return count

#
elements = [3, 2, 1, 4, 1]
cnt = 0
# print(bubblesort(elements, cnt))
# print(res)
# print(elem®ents)

import heapq
#
# def solution(arr, k):
#     positives = [v for v in arr if v>-1]
#
#     sm = sum(positives)
#     heap = [sm]
#
#     for v in arr:
#         if v == 0:
#             continue
#         s = sm + (v if v < 0 else -v)
#         heapq.heappush(heap, s)
#
#     while len(heap) > k:
#         heapq.heappop(heap)
#
#     return [heapq.heappop(heap) for _ in range(k)][::-1]
#
# print(solution([5,-1,-2], 3))
# print(solution([5,3,10,1,2,1,-2],3))

# Python3 program for the above approach

# Function to count the pairs such that
# given condition is satisfied
# def CountPairs(a, b, n):
#     # Stores the sum of element at
#     # each corresponding index
#     C = [0] * n
#
#     # Find the sum of each index
#     # of both array
#     for i in range(n):
#         C[i] = a[i] + b[i]
#     print(C)
#     # Stores frequency of each element
#     # present in sumArr
#     freqCount = dict()
#
#     for i in range(n):
#         if C[i] in freqCount.keys():
#             freqCount[C[i]] += 1
#         else:
#             freqCount[C[i]] = 1
#     print(freqCount)
#     # Initialize number of pairs
#     NoOfPairs = 0
#
#     for x in freqCount:
#         y = freqCount[x]
#
#         # Add possible valid pairs
#         NoOfPairs = (NoOfPairs + y *
#                      (y - 1) // 2)
#
#     # Return Number of Pairs
#     print(NoOfPairs)
#
# CountPairs(
#     [1, 2, 3, 2, 1], [1, 2, 3, 2, 1], 5)


# def vul(m, n, matrix):
# def reorder(arr):17
#     s = sorted(set(arr))
#     ct = {key:i for i, key in enumerate(s)}
#     for i in range(len(arr)):
#         arr[i] = ct[arr[i]] + 1
#     return arr
#
# print(reorder([1, 3, 7, 3]))

# import collections
# def maxSize(riceBags):
#
#
#     if 1 in riceBags:
#         print('!')
#         count = 0
#         while 1 in riceBags:
#             riceBags.remove(1)
#             count += 1
#     print(riceBags)
#     riceBags.sort()
#     print(count)
#     # q = collections.deque(riceBags)
#     cop = riceBags.copy()
#     sets = []
#     # for element in riceBags:
#     while riceBags != []:
#         element = riceBags[0]
#
#         tmp = []
#         print(element)
#         cop = riceBags.copy()
#         for x in cop:
#             print('-----' + str(x))
#             d = x
#             while d % element == 0:
#                 d = d / element
#             if d != 1:
#                 continue
#             else:
#                 tmp.append(x)
#                 riceBags.remove(x)
#         print(tmp)
#         sets.append(len(tmp))
#         print(riceBags)
#     return max(sets) + count
#
# print(maxSize([1,2, 3, 9 , 4, 16, 27, 81]))

# 1 2 3 4 5 6
#  3 5 7 9 1
#   8 2 6 0
#    0 8 6
#     8 4

import collections

def reversePascalTriangle(numbers):
    # while len(numbers) > 2:
    #     i = 0
    #     while i < len(numbers) - 1:
    #         numbers[i] = (numbers[i+1] + numbers[i])%10
    #         i += 1
    #     numbers.pop()
    # return numbers

    while len(numbers) > 2:
        numbers = [(numbers[i] + numbers[i+1]) % 10 for i in range(len(numbers)-1)]
        print(numbers)
    return str(numbers[0]) + ' ' + str(numbers[1])

    # q = collections.deque()
    # for i in range(len(numbers)):
    #     q.append(numbers[i])
    # newQ = collections.deque()
    # first = q.popleft()
    # second = q.popleft()
    #
    # while q:
    #     newQ.append((first+second)%10)
    #     first = second
    #     second = q.popleft()
    #     if not q:
    #         newQ.append((first+second)%10)
    #         if len(newQ) == 2:
    #             print(newQ)
    #             break
    #         q = newQ.copy()
    #         first = q.popleft()
    #         second = q.popleft()
    #         newQ.clear()
    # return str(newQ.popleft()) + ' ' + str(newQ.popleft())

# 4 5 5
# print(reversePascalTriangle([4, 5, 6, 7]))

# Server selection
# def selection(arr):
#     maximums = [0]* len(arr[0])
#     for i in range(len(arr[0])):
#         maximum = 0
#         for j in range(len(arr)):
#             maximum = max(maximum, arr[j][i])
#         maximums[i] = maximum
#     toChoose = []
#     for subArr in arr:
#         for element in subArr:
#
#     return maximums
#
# print(selection([[1, 3, 1],[3, 1, 1],[1, 2, 2],[1, 1, 3]]))


# def prior(orderList):
#     nums, letters = [], []
#     for element in orderList:
#         if element.split()[1].isdigit():
#             nums.append(element)
#         else:
#             letters.append(element)
#     letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
#     return letters + nums
#     # print(nums)
#     # print(letters)
#
# print(prior(['zld 93 12', 'fp kindle book', '10a echo show', '17g 12 25 6', 'ab1 kindle book', '125 echo dot second generation']))

import heapq

def solution(arr, k):
  positives = [v for v in arr if v>-1]

  sm = sum(positives)
  heap = [sm]

  for v in arr:
    if v == 0: continue
    s = sm + (v if v < 0 else -v)
    heapq.heappush(heap, s)

  while len(heap) > k:
    heapq.heappop(heap)

  # return [heapq.heappop(heap) for _ in range(k)][::-1]

print(solution([5,3,-2], 5))
print(solution([5,3,10,1,2,1,-2], 3))


def sol(a):

    return

# print(sol())



# class Solution:
#     def largestVariance(self, s: str) -> int:
#         counter = Counter(s)
#         res = 0
#         for a,b in itertools.permutations(counter,2):
#             max_subarray=0
#             has_a,has_b = False,False
#             remain_a,remain_b = counter[a],counter[b]
#             for ch in s:
#                 if ch!=a and ch!=b:
#                     continue
#                 if max_subarray<0 and remain_a!=0 and remain_b!=0:
#                     max_subarray=0
#                     has_a,has_b = False,False
#                 if ch==a:
#                     max_subarray+=1
#                     remain_a-=1
#                     has_a = True
#                 elif ch==b:
#                     max_subarray-=1
#                     remain_b-=1
#                     has_b = True
#                 if has_a and has_b:
#                     res = max(res, max_subarray)
#         return res


def words(searchStr, resultStr):
    count = 0
    j = 0
    for i in range(len(searchStr)):
        print(searchStr[i] + ' ' + resultStr[j])
        if searchStr[i] != resultStr[j]:
            continue
        else:
            count += 1
            j += 1
    return len(resultStr) - count

# print(words('armaze', 'armazn'))


def parcels(n, arr):
    remaining = n - len(arr)
    arr.sort()
    i = 0
    # j = 0
    sum = 0
    k = 1
    while remaining > 0:
        if k in arr:
            k += 1
        else:
            sum += k
            k += 1
            remaining -= 1


    return sum

# print(parcels(5, [6, 5, 4, 1, 3]))

import collections

s = 'abb'
q = collections.deque(s)
cc = collections.Counter(q)

# print(cc)
count = collections.Counter(s[0:2])

if count[max(count, key = count.get)] > 1:
    print(False)
else:
    print(True)


def validate(arr, window):
    l = 0
    r = window - 1
    # q = collections.deque(arr)
    # count = collections.Counter(q)
    maximum = 0
    while r < len(arr):

        count = collections.Counter(arr[l:r+1])
        print(count)


        if count[max(count, key = count.get)] == 1:
            maximum = max(maximum, sum(arr[l:r+1]))
        r += 1
        l += 1

    return maximum

print(validate([1,2,3,3,4,5, 6], 3))
