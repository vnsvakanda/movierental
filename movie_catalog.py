from movie import Movie
import csv


class MovieCatalog:

    def __init__(self) -> None:
        with open("movies.csv", newline='') as self.csv_file:
            reader = csv.reader(self.csv_file)
            for row in reader:
                self.movies_list = [i for i in reader]

    def get_movie_details(self, title: str) -> Movie:
        for details in self.movies_list:
            if title == details[1]:
                return Movie(title, int(details[2]), details[3].split("|"))
