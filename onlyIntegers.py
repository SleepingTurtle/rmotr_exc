def add_only_integers(a, b):
    if isinstance(a, int) | isinstance(b, int):
        return a + b
    else:
        return 'invalid parameters'
