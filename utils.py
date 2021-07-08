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
