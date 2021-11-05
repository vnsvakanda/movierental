# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from price_code import PriceCode
from movie_catalog import MovieCatalog


def make_movies():
    movies = [
        MovieCatalog().get_movie_details("The Irishman"),
        MovieCatalog().get_movie_details("CitizenFour"),
        MovieCatalog().get_movie_details("Frozen"),
        MovieCatalog().get_movie_details("El Camino"),
        MovieCatalog().get_movie_details("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
