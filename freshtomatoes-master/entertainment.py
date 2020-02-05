import media
# imports the file media made by the user

import fresh_tomatoes
# imports the file fresh_tomatoes made by the user

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys which come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# init function of class Movie gets called when we create this instance(toy_story).

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.freemovieposters.net/posters/avatar_2009_2681_poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

SuicideSquad = media.Movie("Suicide Squad",
                           "A secret government agency recruits some of the most dangerous incarcerated super-villains to form a defensive task force.",
                           "http://www.flickeringmyth.com/wp-content/uploads/2016/01/Suicide-Squad-poster-600x889.jpg",
                           "https://www.youtube.com/watch?v=CmRih_VtVAs/")
Conjuring_two = media.Movie("Conjuring 2",
                            "Lorraine and Ed Warren travel to north London to help a single mother raising four children alone in a house plagued by a malicious spirit.",
                            "http://img10.deviantart.net/5fd7/i/2016/156/e/1/the_conjuring_2_poster__fanmade__by_mintmovi3-da52nge.png",
                            "https://www.youtube.com/watch?v=kTTCi55jpL4")

GoGoaGone = media.Movie("Go Goa Gone",
                        "A group of friends, just looking to have a good time in a rave party on a remote island in Goa, find out that the island is infested with Zombies. ",
                        "https://upload.wikimedia.org/wikipedia/en/5/5e/Go_Goa_Gone_poster.jpg",
                        "https://www.youtube.com/watch?v=4Ai1AUuHEOE")
Msd = media.Movie("M.S. Dhoni: The Untold Story",
                  "The untold story of Mahendra Singh Dhoni's journey from ticket collector to trophy collector - the world-cup-winning captain of the Indian Cricket Team. ",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BOTY5ODQxMTY3M15BMl5BanBnXkFtZTgwOTA3NTA4OTE@._V1_UY1200_CR100,0,630,1200_AL_.jpg",
                  "https://www.youtube.com/watch?v=6L6XqWoS8tw")

movies = [toy_story, avatar, SuicideSquad, Conjuring_two, GoGoaGone, Msd]
# array of movies to check the order of display.

fresh_tomatoes.open_movies_page(movies)
# open_movies_page takes a list of movies as arguments.
