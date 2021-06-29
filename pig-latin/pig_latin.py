def translate(text):
    if text[0:1].lower() in ['a', 'e', 'i', 'o', 'u']:
        result = text + 'ay'
    elif text[0:2].lower() in ['xr', 'yt']:
        result = text + 'ay'
    return result

print(translate("ai"))