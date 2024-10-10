album = {'album_name': 'The Dark Side of the Moon',
         'artist': 'Pink Floyd',
         'track_list': ('Speak to Me',
                        'Breathe',
                        'On the Run',
                        'Time',
                        'The Great Gig in the Sky',
                        'Money',
                        'Us and Them',
                        'Any Colour You Like',
                        'Brain Damage',
                        'Eclipse'),
         'year': 1973}
del album["track_list"]
# print(album["track_list"])
print(album.get("track_list"))
