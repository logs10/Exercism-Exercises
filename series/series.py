def slices(series, length):
    if (length <= 0) or (length > len(series)):
        raise ValueError('Invalid parameters.')
    else:
        entries = []
        for index, num in enumerate(series):
            entry = series[index:index + length]
            if len(entry) == length:
                entries.append(entry)
    return entries
