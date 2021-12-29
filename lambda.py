#LAMBDA , MAP , REDUCE , FILTER

#LAMBDA

def add10(x): return x+10


# print(add10(4))
points2D = [(4, 5), (2, 4)]
# sort based on the second value y in (x,y)
#print(sorted(points2D, key=lambda x: x[1]))
# instead of lambda we can use any function name not the call

#print(sorted(points2D, key=lambda x: x[0]+x[1]))


#MAP
a = [1,2,3,4,5]
# b = map(lambda x:x**2,a)
# print(list(b))



#filter return true or false for all the elements the function evaluates to true

d = filter(lambda x : x%2 == 0 , a)
print(list(d))


#reduce
from functools import reduce
product = reduce(lambda x,y: x*y,a)
print(product)