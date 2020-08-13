def myabs(number):
    return -number if number<0 else number


def myall(iterable):
    for item in iterable:
        if not item:
            return False
    return True


def mylen(s):
    count = 0
    for item in s:
        count += 1
    return count


def myany(iterable):
    for item in iterable:
        if item:
            return True
    return False


def mybin(x):
    binstr = ""
    while True:
        q, r = mydivmod(x, 2)
        binstr += str(r)
        if q == 0:
            break
        else:
            x = q
    return '0b' + binstr[::-1]


def mybool(x):
    return True if x else False


def mydivmod(a,b):
    return a//b, a%b


def myenumerate(iterable, start=0):
    returnlist = []
    for index in range(mylen(iterable)):
        returnlist.append((index,iterable[index]))
    return returnlist


def myhex(x):
    def hexvalue(d):
        if 0 <= d <= 9: return str(d)
        if d == 10: return 'a'
        if d == 11: return 'b'
        if d == 12: return 'c'
        if d == 13: return 'd'
        if d == 14: return 'e'
        if d == 15: return 'f'
    hexstr = ""
    while True:
        q, r = mydivmod(x, 16)
        hexstr += hexvalue(r)
        if q == 0:
            break
        else:
            x = q
    return '0x' + hexstr[::-1]


def myisinstance(object, classinfo):
    return True if str(classinfo) in str(type(object)) else False


def mymax(iterable):
    maxitem = iterable[0]
    for item in iterable[1:]:
        if item > maxitem:
            maxitem = item
    return maxitem

def mymin(iterable):
    minitem = iterable[0]
    for item in iterable[1:]:
        if item < minitem:
            minitem = item
    return minitem
    

def myoct(x):
    octstr = ""
    while True:
        q, r = mydivmod(x, 8)
        octstr += str(r)
        if q == 0:
            break
        else:
            x = q
    return '0o' + octstr[::-1]


def mypow(base, exp):
    return base ** exp


def myreversed(seq):
    return seq[::-1]


def myround(number, ndigits=None):
    pass


def mysorted(iterable, reverse=False):
    pass


def mysum(iterable):
    sumvar = 0
    for item in iterable:
        sumvar += item
    return sumvar


