
def say_verse(verse):
    twelve_dict = {
        1: {"num": "first", "phrase": "a Partridge in a Pear Tree."},
        2: {"num": "second", "phrase": "two Turtle Doves"},
        3: {"num": "third", "phrase": "three French Hens"},
        4: {"num": "fourth", "phrase": "four Calling Birds"},
        5: {"num": "fifth", "phrase": "five Gold Rings"},
        6: {"num": "sixth", "phrase": "six Geese-a-Laying"},
        7: {"num": "seventh", "phrase": "seven Swans-a-Swimming"},
        8: {"num": "eighth", "phrase": "eight Maids-a-Milking"},
        9: {"num": "ninth", "phrase": "nine Ladies Dancing"},
        10: {"num": "tenth", "phrase": "ten Lords-a-Leaping"},
        11: {"num": "eleventh", "phrase": "eleven Pipers Piping"},
        12: {"num": "twelfth", "phrase": "twelve Drummers Drumming"}}

    song = []
    begin_phrase = "On the " + \
        str(twelve_dict[verse]["num"]) + \
        " day of Christmas my true love gave to me: "
    song.append(begin_phrase)
    for s in range(verse, 0, -1):
        if s == 1 and verse == 1:
            song.append(twelve_dict[s]["phrase"])
        elif s == 1:
            song.append("and " + twelve_dict[s]["phrase"])
        else:
            song.append(twelve_dict[s]["phrase"] + ', ')
    return ''.join(song)


def recite(start_verse, end_verse):
    full_song = []
    for verse in range(start_verse, end_verse + 1):
        full_song.append(say_verse(verse))
    return full_song
