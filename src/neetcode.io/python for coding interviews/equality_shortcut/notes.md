Inequality

Python allows us to take a small shortcut when making multiple comparisons.

The following code:

x = 5

if 0 < x and x < 10:
    print('x is between 0 and 10')

is equivalent to:

x = 5

if 0 < x < 10:
    print('x is between 0 and 10')

Notice that we didn't need the boolean and in the second example. This is a small shortcut, but now you may start to see why people consider Python to practically be pseudocode.
Challenge

Implement the following function:

    is_arr_valid(names: List[str], max_length: int) -> bool. It should return True if the length of the names list is greater than 0 and less than or equal to the parameter max_length. Otherwise it should return False.
