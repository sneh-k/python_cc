import  u8_media
import fresh_tomatoes
toy_stoty = u8_media.Movie("Toy Story",
                           "A story of a boy and his toys that come to life.",
                           "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                           "https://youtu.be/KYz2wyBy3kc")

frozen = u8_media.Movie("Frozen",
                           "A story of a fearless princess who sets off on an epic journey to find her estranged sister",
                           "http://target.scene7.com/is/image/Target/57626-160613_1465794713056?wid=1200&fmt=pjpeg&qlt=80",
                           "https://youtu.be/TbQm5doF_Uc")

school_of_rock = u8_media.Movie("School of Rock",
                                "Using rock music to learn",
                                "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
                                "https://youtu.be/LqEszt5wG9I")

midnight_in_paris = u8_media.Movie("Midnight in Paris",
                                   "Going back in time to meet authors",
                                   "http://t3.gstatic.com/images?q=tbn:ANd9GcTk3ssys2bKM5-U6XMgvoD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
                                   "https://youtu.be/BYRWfS2s2v4")

zootopia = u8_media.Movie("Zootopia",
                          "A rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy",
                          "https://lh3.googleusercontent.com/qlxBnASxAN35_JMRPT94NZA37BgpvxveC1WzjUjFigPMN3WNqAaYKF9FY8KRJpbIl9c=w300",
                          "https://youtu.be/bY73vFGhSVk")

despicable_me = u8_media.Movie("Despicable Me",
                               "When a criminal mastermind uses a trio of orphan girls as pawns for a grand scheme, he finds their love is profoundly changing him for the better.",
                               "http://static.rogerebert.com/uploads/movie/movie_poster/despicable-me-2010/large_4zHJhBSY4kNZXfhTlmy2TzXD51M.jpg",
                               "https://youtu.be/j2bAEnBQWvM")

movies= [toy_stoty, frozen, school_of_rock, midnight_in_paris, zootopia, despicable_me]
fresh_tomatoes.open_movies_page(movies)

#print (u8_media.Movie.VALID_RATINGS)

#print (u8_media.Movie.__doc__)
#print (u8_media.Movie.__name__)
#print (u8_media.Movie.__module__)
