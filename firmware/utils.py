def partial(func, *args, **kwargs):
    def _partial(*more_args, **more_kwargs):
        kw = kwargs.copy()
        kw.update(more_kwargs)
        return func(*(args + more_args), **kw)

    return _partial


def update_wrapper(wrapper, wrapped, assigned=None, updated=None):
    # Dummy impl
    return wrapper


def wraps(wrapped, assigned=None, updated=None):
    # Dummy impl
    return lambda x: x


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

def compare_arrays (a1, a2):
    a1.sort()
    a2.sort()
    return a1 == a2

def clear_display_group (group):
    groups_to_remove = []
    for gr in group:
        groups_to_remove.append(gr)
    for gr in groups_to_remove:
        group.remove(gr)

def number_to_array (number):
    number_array = []
    for digit in list(str(number)):
        number_array.append(int(digit))

    return number_array

def restore_after_save (bytearray, as_int = False):
    array = []
    for byte in bytearray:
        str_byte = str(byte)
        if len(str_byte) == 2:
            array.append(str_byte[0] if as_int else int(str_byte[0]))
            array.append(str_byte[1] if as_int else int(str_byte[1]))
        else:
            array.append('0' if as_int else 0)
            array.append(str_byte if as_int else int(str_byte))

    if as_int:
        return int(('').join(array))
    return array

def prepare_to_save (value, size = None):
    if type(value) == int:
        value = number_to_array(value)
    doubled = []
    for i, val in enumerate(value):
        if not i%2:
            second_value = value[i + 1] if i + 1 < len(value) else ''
            merged_int = str(val) + str(second_value)
            doubled.append(int(merged_int))
    if size and size - len(doubled) > 0:
        doubled = [0] * (size - len(doubled)) + doubled
    return doubled
