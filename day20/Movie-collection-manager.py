class Movie:
    def __init__(self, title, director, rating) -> None:
        self.title = title
        self.director = director
        self.rating = rating
        self.watched = False
    def watch_movie(self):
        if self.watched == False:
            self.watched = True
            return "You've watched this movie!"
        else:
            return "Already watched!"
    def is_good(self):
        if self.rating >= 8:
            return True
        else:
            return False
    def show_info(self):
        status1 = "good movie" if self.is_good() else "Not so good movie"
        status2 = "watched!" if self.watched == True else "not watched yet"
        return f"{self.title} | {self.director} | {self.rating} | {status1} | {status2}"

movies = [
    Movie("The Shawshank Redemption" , "Frank Darabont" , 9.3),
    Movie("The Godfather" , "Francis Ford Coppola" , 9.2),
    Movie("The Dark Knight" , "Christopher Nolan" , 9.0),
    Movie("Inception" , "Christopher Nolan" , 8.8),
    Movie("Interstellar" , "Christopher Nolan" , 8.7),
    Movie("The Matrix" , "Wachowski Sisters" , 8.7),
    Movie("Avatar" , "James Cameron" , 7.9),
    Movie("Transformers" , "Michael Bay" , 7.0),
    Movie("The Amazing Spider-Man" , "Marc Webb" , 6.9),
    Movie("Batman v Superman" , "Zack Snyder" , 6.5)
]

movies[0].watch_movie()
movies[2].watch_movie()
movies[5].watch_movie()

for movie in movies:
    print(movie.show_info())

def watched_movies(movies):
    count = 0
    for movie in movies:
        if movie.watched == True:
            count += 1 
    return count
result = watched_movies(movies)
print("how many movies you've watched?", result)

def good_movies(movies):
    count = 0
    for movie in movies:
        if movie.is_good():
            count += 1
    return count
result = good_movies(movies)
print("perfect movies=", result)

def find_best_movie(movies):
    best_title = None
    highest_rate = -1
    for movie in movies:
        if movie.rating > highest_rate:
            highest_rate = movie.rating
            best_title = movie.title
    return best_title, highest_rate
result = find_best_movie(movies)
print(result) 
