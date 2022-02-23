def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
Args:
function_to_apply: a function taking an iterable.
iterable: an iterable object (list, tuple, iterator).
Returns:
A value, of same type of elements in the iterable parameter.
None if the iterable can not be used by the function."""
    try:
        iter(iterable)
    except Exception:
        raise TypeError('ft_reduce() arg 2 must support iteration')
    if not iterable:
        raise TypeError('ft_reduce() of empty sequence')
    for i, item in enumerate(iterable):
        if i:
            try:
                result = function_to_apply(result, item)
            except Exception:
                raise
        else:
            result = item
    return result
