#1 arb_args takes in any number of arguments and prints them one at a time.
def arb_args(*args):
  for a in args:
    print(a)

#inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(x, y):

  def inner_1():
    return x + y

  def inner_2():
    return x - y

  print(inner_1() + inner_2())


  #lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

  def lunch_lady(name, lunch="Mystery Meat"):
    print(name, lunch)

    #sum_n_product - Accepts two integers and returns both the sum and the product.
    def sum_n_product(x, y):
        return x + y, x * y

#alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.

alias_arb_args = arb_args
