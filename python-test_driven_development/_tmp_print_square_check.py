mod = __import__('4-print_square')
print_square = mod.print_square
cases = [
    ('no arg', None),
    ('True', True),
    ('string', '4'),
    ('float', 4.0),
    ('negative', -1),
    ('zero', 0),
    ('four', 4)
]
for name, val in cases:
    print('CASE', name)
    try:
        if name == 'no arg':
            print_square()
        else:
            print_square(val)
    except Exception as e:
        print(type(e).__name__, e)
    print('---')
