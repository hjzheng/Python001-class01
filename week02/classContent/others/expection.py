numGen = (i for i in range(3))

print(next(numGen))
print(next(numGen))
print(next(numGen))

try:
    print(next(numGen))

except StopIteration:
    print('last number')
