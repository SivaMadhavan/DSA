def getMinMax(a, n):
    _min = _max = a[0]
    for i in a:
        if i < _min:
            _min = i
        if i > _max:
            _max = i

    return [_min, _max]


print(getMinMax([3,2, 1, 56, 1000, 167], 6))