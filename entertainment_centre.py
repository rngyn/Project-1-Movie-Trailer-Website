import fresh_tomatoes
import media

# Movies to appear on the website with relevant data using the media module
# including movie title, poster source, and YouTube trailer URL.
inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

interstellar = media.Movie("Interstellar",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

dunkirk = media.Movie("Dunkirk",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

memento = media.Movie("Memento",
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=0vS0E9bBSL0")

the_revenant = media.Movie("The Revenant",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=LoebZZ8K5N0")

wonder_woman = media.Movie("Wonder Woman",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")

# Compiles the movies into an array.
movies = [inception, interstellar, dunkirk,
          memento, the_revenant, wonder_woman]
# Calls the open_movies_page function in fresh_tomatoes module
# to populate the website with the movie array.
fresh_tomatoes.open_movies_page(movies)
