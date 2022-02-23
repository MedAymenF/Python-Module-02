def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
Args:
function_to_apply: a function taking an iterable.
iterable: an iterable object (list, tuple, iterator).
Returns:
An iterable.
None if the iterable can not be used by the function."""
    def id(x):
        return x
    if not function_to_apply:
        function_to_apply = id
    for item in iterable:
        try:
            result = function_to_apply(item)
        except Exception:
            raise
        if (result):
            yield item
