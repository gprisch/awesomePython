import sys
# import os

sys.modules['os']

sys.path

_var_not_visible_outside = 2


def _func_not_visible_outside():
    print(_var_not_visible_outside)


_func_not_visible_outside()



