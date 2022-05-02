def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 0 and len(tuple_b) == 0:
        new_tuple = 0, 0

    elif len(tuple_a) == 2 and len(tuple_b) == 2:
        new_tuple = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))

    elif len(tuple_a) == 1:
        if len(tuple_b) == 2:
            new_tuple = tuple_a[0] + tuple_b[0], tuple_b[1]
        elif len(tuple_b) == 1:
            new_tuple = tuple_a[0] + tuple_b[0], 0

    elif len(tuple_b) == 1:
        if len(tuple_a) == 2:
            new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1]
        elif len(tuple_a) == 1:
            new_tuple = tuple_a[0] + tuple_b[0], 0

    elif len(tuple_a) == 0:
        if len(tuple_b) == 2:
            new_tuple = tuple_b
        elif len(tuple_b) == 1:
            new_tuple = tuple_b[0], 0

    elif len(tuple_b) == 0:
        if len(tuple_a) == 2:
            new_tuple = tuple_a
        elif len(tuple_a) == 1:
            new_tuple = tuple_a[0], 0

    else:
        new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]

    return new_tuple
