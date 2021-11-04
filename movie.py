class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, year, genre):
        # Initialize a new movie.
        self.__title = title
        self.__year = int(year)
        self.__genre = genre

    def get_title(self):
        return self.__title

    def get_yesr(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def __str__(self):
        return self.__title
