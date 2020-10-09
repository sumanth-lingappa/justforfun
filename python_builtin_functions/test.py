import python_builtin_functions as bif

assert(bif.myabs(-5) == abs(-5))
assert(bif.myabs(5) == abs(5))
assert(bif.myabs(0) == abs(0))

assert(bif.myall([1, 4j, {1:1}]) == all([1, 4j, {1:1}]))
assert(bif.myall([1, 4j, {1:1}, set()]) == all([1, 4j, {1:1}, set()]))

assert(bif.myany((0,0.0,[],(),{})) == any((0,0.0,[],(),{})))
assert(bif.myany((0,0.0,[],(),{}, True)) == any((0,0.0,[],(),{}, True)))

assert(bif.mylen('python') == len('python'))

assert(bif.mysum([1,2,3,-1,-2,-3]) == sum([1,2,3,-1,-2,-3]))

assert(bif.mymax([1,2,3,-1,-2,-3]) == max([1,2,3,-1,-2,-3]))
assert(bif.mymin([1,2,3,-1,-2,-3]) == min([1,2,3,-1,-2,-3]))

assert(bif.mydivmod(14, 3) == divmod(14,3))

assert(bif.mybool('') == bool(''))

assert(bif.mypow(3, 4) == pow(3,4))

assert(list(bif.myreversed('python')) == list(reversed('python')))

assert(bif.myenumerate('py') == list(enumerate('py')))

assert(bif.mybin(123) == bin(123) )
assert(bif.myhex(123) == hex(123))
assert(bif.myoct(123) == oct(123))

#assert(bif.myisinstance(object, classinfo))
#assert(bif.myround(number, ndigits=None))
#assert(bif.mysorted(iterable, reverse=False))


print('ALL TEST SUCCESSFUL!')
