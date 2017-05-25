import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar","Marine on a alien planet and destroying their natural resources","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 	"https://www.youtube.com/watch?v=Bl8fkc4HsSs")

#avatar.show_trailor()

Avenger = media.Movie("Avenger","Superheroes saving the World","https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
						"https://www.youtube.com/watch?v=3PyrgGTFp0E") 

Don_jon = media.Movie("Don Jon","Nothing to tell","http://t0.gstatic.com/images?q=tbn:ANd9GcSiQ3OCkTsH61sbnIKWaoi3YTTffXDhUmWpv7tBNwskq2fswV8i","https://www.youtube.com/watch?v=6615kYTpOSU")

Bad_Sister = media.Movie("Bad Sister","Whea a teacher fall in love with a student and take it far beyond limits",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BODczOWNhZjktODliYS00ZTNjLTk1M2EtZGUxMjFiZDI2NGU0XkEyXkFqcGdeQXVyNjQ2MjQ5NzM@._V1_UY268_CR1,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=SU-JqbOojt4")
movies = [toy_story,avatar,Avenger,Don_jon,Bad_Sister]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__bases__)