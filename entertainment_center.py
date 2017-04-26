from media import Movie
import fresh_tomatoes

# Create Movie instances
toy_story = Movie("Toy Story",
                  "A boy with his toys that come to life",
                  "https://goo.gl/LPy5eG",
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movie("Avatar",
               "Human army on beautiful alien planet",
               "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

v_for_vendetta = Movie("V for Vendetta",
                       "A terrorist with Guy Fawkes mask comes for revenge and fights for freedom",
                       "http://www.impawards.com/2006/posters/v_for_vendetta.jpg",
                       "https://www.youtube.com/watch?v=k_13fFIrhPk")

watchmen = Movie("Watchmen",
                 "A deep story about superheroes",
                 "https://images-na.ssl-images-amazon.com/images/I/51hsuuC54ZL._SY450_.jpg",
                 "https://www.youtube.com/watch?v=PVjA0y78_EQ")

maze_runner = Movie("Maze runner",
                    "A group of youngsters is trapped in a maze and try to escape",
                    "https://goo.gl/9WaIzu",
                    "https://www.youtube.com/watch?v=64-iSYVmMVY")

warcraft = Movie("Warcraft",
                 "Battle of humans and orcs",
                 "http://www.impawards.com/2016/posters/warcraft_ver9.jpg",
                 "https://www.youtube.com/watch?v=RhFMIRuHAL4")

# Store movies in a list to render to web page
movies = [toy_story, avatar, v_for_vendetta, watchmen, maze_runner, warcraft]
# Render movies to web page
fresh_tomatoes.open_movies_page(movies)
