import py_div


print(py_div.__doc__)


# Dictionary
stock = {
    "name"      : ("google",80),
    "shares"    : 100,
    "price"     : 490.10
   }

print("name? " , stock["name"][0])

del stock["name"]

if "name" in stock:
    print("found")
else:
    print("not found")

syms = list(stock)

print(syms)

a = "Hello World"
b = ["Dave","Mark","Ann","Phil"]

for a_word in a:
    print(a_word);

for b_words in b:
    for b_word in b_words:
        print(b_words, b_word);



def remainder(a,b):
    q = a // b
    r = a - q*b
    return (q,r)

result, remind = remainder(37, 15)
print(remind)


def countdown(n):
    print ("Counting down!")
    while n > 0:
        yield n
        #print(n)
        n -= 1



class EventHAndlerssss():

    @staticmethod
    def printError():
        print("This is Error message")

    def __init__(self):
        self.result = 0

    def sum(self, b):
        self.result = 10 * b;
        return self.result

    



sum_result = EventHAndlerssss();

print(sum_result.sum(11))

EventHAndlerssss.printError()

