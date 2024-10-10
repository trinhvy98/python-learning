from pprint import pprint

album = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
)

lst = ("album_name", "artist", "year", "track_list")
# album_dict = dict(zip(lst, album))

# album_dict = {}
#
# for i in range(len(lst)):
#     key = lst[i]
#     value = album[i]
#     album_dict[key] = value

album_dict = {
    # lst[i]: album[i]
    # for i in range(len(lst))
    key: value
    for key, value in zip(lst, album)
}

pprint(album_dict)
