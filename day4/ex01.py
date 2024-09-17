movies = [("Goblin", "Kim NamJoon", 2004, 100)]

title = input("title: ")
director = input("director: ")
year = int(input("year of release: "))
budget = float(input("budget: "))
new_movie = title, director, year, budget

print(f"{new_movie[0], new_movie[2]}")

movies.append(new_movie)

print(movies[0])
print(movies[1])

movies.remove(movies[0])

print(movies)

# del movies[0]
print(movies)

movies.pop(0)
print(movies)
