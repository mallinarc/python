x = 1
if x == 1:
    # indent four spaces
    print("x is 1:")

thisString = 'Hello'
print(thisString)
dblQuoteString = "Ramesh's blog."
print(dblQuoteString)
# single quote without string termination slash
anotherString = 'Ramesh\'s blog.'
print(anotherString)
# this will not work
one = '1'
two = '2'
hello = 'hello'
print(one+two+hello)

myString = 'hello'
myFloat = 10.0
myInt = 20
if myString == 'hello':
    print("String: %s" % myString)
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float %f" % myFloat)
if isinstance(myInt, int) and myInt == 20:
    print("Integer: %d" % myInt)
