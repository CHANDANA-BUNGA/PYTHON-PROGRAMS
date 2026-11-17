def sumSquares(numbers):
    total=0
    for num in numbers:
        total=total+(num*num)
    return total
list=[2,3,4,5]
print("sum of squares=",sumSquares(list))
