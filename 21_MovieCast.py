
from imdb import IMDb

def movie_cast():
    name = input('Enter Movie Name: ')
    ia = IMDb()
    movies = ia.search_movie(name)

    if movies:
        movie = movies[0]  
        ia.update(movie)  
        cast = movie.get('cast', [])  

        if cast:
            print(f'\nMain Cast of "{name}" is:\n')
            for actor in cast[:10]:
                print(f'- {actor["name"]}')
        else:
            print(f'No cast information found for "{movie["title"]}".')
    else:
        print(f'Movie "{name}" not found!')

movie_cast()

