import python_builtin_functions as bif

# from python_builtin_functions import myany
# from python_builtin_functions import mymax
# from python_builtin_functions import mymin
# from python_builtin_functions import mypow

# from python_builtin_functions import *


x = bif.myany([3,4, "sumanth"])
y = bif.mymax([4,3,5,3,2])
z = bif.mymin([4,3,5,3,2])
p = bif.mypow(4,3)

print("any:{}    max:{}    min:{}".format(x,y,z))
