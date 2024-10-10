movies: list[tuple] = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for movie in movies:
    print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

"""
Eternal Sunshine of the Spotless Mind (2004), by Michel Gondry
Memento (2000), by Christopher Nolan
Requiem for a Dream (2000), by Darren Aronofsky
"""
