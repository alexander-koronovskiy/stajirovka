n_l = [39, 11, 17, 41, 22, 59, 88, 34, 16, 88, 11]


# бинарный поиск
def binary_search(l, t):
   start, end = 0, (len(l) - 1)
   while start <= end:
       mp = (start + end) // 2
       if l[mp] == t:
          return mp
       if t > l[mp]:
          start = mp +1
       else:
          end = mp - 1
   return False


# сортировка пузырьком
def bubble_sort(l):
   for i in range(len(l)):
      for j in range(len(l)):
         if l[i] < l[j]:
            tmp = l[j]
            l[j] = l[i]
            l[i] = tmp
   return l


# merge sort - ?
# быстрая сортировка
def quick_sort(l):
   if not l:
      return []
   else:
      return quick_sort([x for x in l if x < l[0]]) + \
             [x for x in l if x == l[0]] + \
             quick_sort([x for x in l if x > l[0]])


o_l = quick_sort(n_l)
print(binary_search(o_l, 34))
