from functools import wraps
# decorator to trace execution of recursive function
def trace(func):

    # cache func name, which will be used for trace print
    func_name = func.__name__
    # define the separator, which will indicate current recursion level (repeated N times)
    separator = '|  '

    # current recursion depth
    trace.recursion_depth = 0

    @wraps(func)
    def traced_func(*args, **kwargs):

        # repeat separator N times (where N is recursion depth)
        # `map(str, args)` prepares the iterable with str representation of positional arguments
        # `", ".join(map(str, args))` will generate comma-separated list of positional arguments
        # `"x"*5` will print `"xxxxx"` - so we can use multiplication operator to repeat separator
        print(f'{separator * trace.recursion_depth}|-- {func_name}({", ".join(map(str, args))})')
        # we're diving in
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        # going out of that level of recursion
        trace.recursion_depth -= 1
        # result is printed on the next level
        print(f'{separator * (trace.recursion_depth + 1)}|-- return {result}')

        return result

    return traced_func


def factorial(n):
   if n == 1: return 1
   else: return n * factorial(n-1)


# since the name of decorated func is the same as the name of original one
# decorator will be applied to nested calls too
factorial = trace(factorial)

# this will print all the recursion trace and the result at the bottom
#print(factorial(7))

@trace
def sumR(array):
    if len(array)>0:
        #print(array[-1])
        n = sumR(array[:-1])
        #print(n)
        return n+array[-1]
    else:
        return 0
@trace
def sumRh(array):
    if len(array)>0:
        #print(array[0])
        n = sumRh(array[1:])
        #print(n,array[0])
        return n+array[0]
    else:
        return 0

if __name__ == '__main__':
    print(sumR([1,2,3]))
    print(sumRh([1,2,3]))