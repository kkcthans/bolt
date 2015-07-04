from numpy import ndarray, asarray, any

def tupleize(arg):
    """
    Coerce singletons and lists and ndarrays to tuples
    """
    if not isinstance(arg, (tuple, list, ndarray)):
        return tuple((arg,))
    elif isinstance(arg, (list, ndarray)):
        return tuple(arg)
    else:
        return arg

def argpack(args):
    """
    Coerce a list of arguments to a tuple
    """
    if isinstance(args[0], tuple):
        return args[0]
    else:
        return tuple(args)

def check_axes(shape, axes):
    """
    Checks to see if a list of axes are contained within the shape of a BoltArray

    Throws a ValueError if the axes are not valid for the given shape.

    Parameters
    ----------
    shape: tuple[int]
        the shape of a BoltArray
    axes: tuple[int]
        the axes to check against shape
    """
    valid = all([(axis < len(shape)) and (axis >= 0) for axis in axes])
    if not valid:
        raise ValueError("axes not valid for an ndarray of shape: %s" % str(shape))

def allclose(a, b):
    """
    Test that a and b are close and match in shape
    """
    from numpy import allclose
    return (a.shape == b.shape) and allclose(a, b)

def tuplesort(seq):

    return sorted(range(len(seq)), key=seq.__getitem__)

def listify(lst, dim):
    """
    Flatten lists of indices and ensure bounded by a known dim
    """
    if not all([l.dtype == int for l in lst]):
        raise ValueError("indices must be integers")

    if any(asarray(lst) >= dim):
        raise ValueError("indices out of bounds for axis with size %s" % dim)

    return lst.flatten()

def slicify(slc, dim):
    """
    Force a slice to have defined start, stop, and step from a known dim
    """
    if isinstance(slc, slice):
        if slc.start is None and slc.stop is None and slc.step is None:
            return slice(0, dim, 1)

        elif slc.start is None and slc.step is None:
            return slice(0, slc.stop, 1)

        elif slc.stop is None and slc.step is None:
            return slice(slc.start, dim, 1)

        elif slc.step is None:
            return slice(slc.start, slc.stop, 1)

        else:
            return slc

    elif isinstance(slc, int):
        return slice(slc, slc+1, 1)

    else:
        raise ValueError("Type for slice %s not recongized" % type(slc))

