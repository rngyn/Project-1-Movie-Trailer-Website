# Movie Trailer Website
This application creates a website showcasing movies with their movie posters.
When a poster is clicked, it will play the respective movie trailer.

## Files
* `entertainment_centre.py` creates the website when executed.
It holds relevant movie data including
the movie title, movie poster image URL, and YouTube trailer URL.
* `media.py` contains the class `Movie()` that creates instances for the data
for each movie.
* `fresh_tomatoes.py` holds the actual style and
functionality code for the website.

## Dependencies
Python 2.7 must be installed, which can be found
[here](https://www.python.org/downloads/).

All Movie Trailer Website files must be within the same directory for it
to work.

## Microsoft Windows Instructions
1. Run `IDLE` (Python GUI) from the Start menu.

2. From `IDLE`, open `entertainment_centre.py`. This will show the code in
another window called `terminal`.   

3. Populate the `entertainment_centre.py` module in the `terminal` window with
your own list of movies by changing the variable name and string arguments for
each movie. An example from the default code is shown here:
```
inception = media.Movie("Inception",
            "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
            "https://www.youtube.com/watch?v=d3A3-zSOBT4")
```
Here you would change the variable `inception` to any appropriate variable name
for your chosen movie. Change the three arguments within `media.Movie` to
ones pertaining to the chosen movie. The order of the arguments is `movie_title`
, `poster_image` URL, and `trailer_youtube` URL.

4. Be sure to change the `movies` array with the correct arguments (the variable
names you have chosen).
```
movies = [inception, interstellar, dunkirk,
          memento, the_revenant, wonder_woman]
```

5. Run `entertainment_centre.py` by hitting F5 in the `terminal` window to
create the HTML file and automatically open the website in your default browser.

6. Click a movie poster on the page in the browser to bring up and play the
movie trailer.

7. You can edit the `fresh_tomatoes.py` code by opening the file through the
`IDLE` window to change the way the website looks!

## Disclaimer
This application was written by Robert Nguyen with the help and guidance
of Udacity's Full Stack Web Developer Nanodegree Program.
