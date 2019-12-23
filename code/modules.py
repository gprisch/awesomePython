import sys
# import os

sys.modules['os']

sys.path

_var_not_visible_outside = 2


def _func_not_visible_outside():
    print(_var_not_visible_outside)


_func_not_visible_outside()

# namespaces in Python

locals()
globals()

# overrides the list built-in
list = 3

print(list)

# remove list as int from scope
del list



