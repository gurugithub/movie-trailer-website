#Code logic - Guru Shetti 3/25/2015 v1
# Please note fres_tomatoes has been modified
from AllMovies import Movie

# importing class Movie from file AllMovie
import fresh_tomatoes

earth_to_echo = Movie("Earth to Echo", "92", "PG", "When a construction project begins in their neighborhood, four friends start receiving bizarre encoded text messages on their cell phones", "http://ia.media-imdb.com/images/M/MV5BMjEwMzA5Nzk2Ml5BMl5BanBnXkFtZTgwMDM2NzE4MTE@._V1_SY317_CR0,0,214,317_AL_.jpg", "novzGPgeY4c")


escape_planet = Movie("Escape from Planet Earth", "118", "PG-13", "This all-ages animated comedy follows the adventures of astronaut Scorch Supernova, a hero of the blue aliens who has a vast appetite for adventure", "http://ia.media-imdb.com/images/M/MV5BMjAyOTUzMTcxN15BMl5BanBnXkFtZTgwMjkyOTc1MDE@._V1_SX214_AL_.jpg","Q1NhAUsyslk")


interstellar = Movie("Interstellar", "92", "PG", "Space Movie", "http://ia.media-imdb.com/images/M/MV5BMjA3NTEwOTMxMV5BMl5BanBnXkFtZTgwMjMyODgxMzE@._V1._SY412_CR103,0,412,412_.jpg","0vxOhd4qlnA")

movies = [earth_to_echo, escape_planet, interstellar]

fresh_tomatoes.open_movies_page(movies)

