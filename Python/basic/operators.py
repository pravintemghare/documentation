"There are 7 types of Operators in Python."

# 1: Exponential (**) - 3 ** 3 = 9
# 2: Multiplication (*) = 2 * 3 = 6
# 3: Division (/) = 6 / 2 = 3.0 (Always retuns a floot)
# 4: Floor Division (//) = 6 // 2 = 3 (Lesser integer value)
# 5: Modulo (Remainder) (%) = 5 % 2 = 1
# 6: Addition (+) = 5 + 2 = 7
# 7: Substraction (-) = 6 - 2 = 4

"""
Priority Highest:
    unary ( + OR -) integers
    **
    * / // %
    + - binary
Prioritu Lowest
"""

# Sub experssion are calculated first 
print ( 10 - 6 ** 2 / 9 * 10 + 1)
print ( 5 * (3 + 5))
print (2 * 3 ** 3 * 4)