#1
def power(base, exponent):
    if exponent <= 0:
        return 1
    return base * power(base,exponent-1)
print(power(2,4))

#2
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

#3
def numbers_to_n(n,list1=[]):
    if n <= 0:
        return reversed(list1)
    list1.append(n)
    return numbers_to_n(n-1,list1)
print(list(numbers_to_n(5)))

def numbers_to_n(n):
    if n == 1:
        return [1]
    return numbers_to_n(n-1) +[n]
print(numbers_to_n(5))

#4
def count_items(lst):
    if len(lst) == 0:
        return 0
    lst.pop(0)
    return count_items(lst) +1
print(count_items([1,2,3,4]))

#5
def count_evens(numbers):
    if len(numbers)==0:
        return 0
    if numbers[0] % 2 == 0:
        numbers.pop(0)
        return count_evens(numbers) +1
    return count_evens(numbers[1:])
print(count_evens([4,7,10,3,8]))

#6
def max_number(numbers):
    if len(numbers)==1:
        return numbers[0]
    if numbers[0]>numbers[1]:
        numbers.pop(1)
        return max_number(numbers)
    if numbers[1]>numbers[0]:
        numbers.pop(0)
        return max_number(numbers)
    
print(max_number([4,3,5,7]))

#7
def reverse_string(text):
    if len(text) == 0:
        return "" 
    return text[-1]+reverse_string(text[:-1])
print(reverse_string("moishi"))

#8
def is_palindrome(text):
    if len(text)==0:
        return True
    if text[0]!=text[-1]:
        return False
    return is_palindrome(text[1:-1])
print(is_palindrome("level"))

#9
def count_value(lst, value):
    if len(lst)==0:
        return 0
    if value==lst[0]:
        lst.pop(0)
        return 1+ count_value(lst,value)
    lst.pop(0)
    return count_value(lst, value)

print(count_value([1,2,2,3,2],2))

#10
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(69))



    
