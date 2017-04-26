# Nanodegree : Movies trailer website

## Installation :

#### *Requires* :
* Python 2

Clone this repository.

## Deploy :

Run this command : ```python entertainment_center.py```

## Modification guide :
#### *Create new movie* :
In entertainment_center.py :
```
new_movie = Movie("Movie title",
                "Movie storyline",
                "Movie poster image url",
                "Movie youtube trailer url")

# Store movies in a list to render to web page
movies = [..., new_movie]
# Render movies to web page
fresh_tomatoes.open_movies_page(movies)
```