import math
m = __import__('0-add_integer')
f = m.add_integer
print('1+2 ->', f(1,2))
try:
    print('True+2 ->', f(True,2))
except Exception as e:
    print('True error:', type(e).__name__, e)
try:
    print('nan+2 ->', f(math.nan,2))
except Exception as e:
    print('nan error:', type(e).__name__, e)
try:
    print('inf+2 ->', f(float('inf'),2))
except Exception as e:
    print('inf error:', type(e).__name__, e)
