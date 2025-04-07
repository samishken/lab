# Questions for this assignment
# 1) Create a Tuple: Define a tuple named favorite_movies that contains the titles of five movies you enjoy. Use the following format:
favorite_movies = ("Heat", "Terminator", "God Father", "The President", "Tulsi")
print(favorite_movies)
# 2.0) Access Elements: Print the entire favorite_movies tuple.
# 2.a) Print the first movie in the tuple by accessing it with the index 0.
# 2.b) Print the last movie in the tuple using the index -1.
print(favorite_movies[0])
print(favorite_movies[-1])

# 3.0) Count Movies: Use the len() function to find and print the total number of movies in the favorite_movies tuple.
print(len(favorite_movies))

# 4.0) Display All Movies: Print all the movies in the new_favorite_movies tuple, each on a new line. You can use a for loop to iterate through the tuple.
for movie in favorite_movies:
    print(movie)