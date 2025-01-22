
# pip install IMDBPY
from imdb import IMDb

def movie_rating():
    movie_name=input("Enter Movie Name : ")
    ia=IMDb()
    movies=ia.search_movie(movie_name)

    if movies:
        movie=movies[0]
        ia.update(movie)
        rating=movie.get('rating','N/A')
        print(f'The IMDB rating of {movie_name} is : {rating}')
    else:
        print(f'The {movie_name} not Found!!')

movie_rating()