# bar.py

def bar_func():
    print("I am inside bar_func")

print("one  ",__name__)

if __name__ == "__main__":
    print("this part of code is only run when bar.py is called directly")
    print("Inside __name__ == __main__ block")
