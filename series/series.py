def slices(series, length):
    s_len = len(series)
    s = series[:length]
    return s, s_len


print(slices("123456", 2))
