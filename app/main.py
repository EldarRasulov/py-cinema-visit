# main.py

from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie, customers, hall_number, cleaner):
    customer_objects = []

    for customer in customers:
        customer_instance = Customer(
            name=customer["name"],
            food=customer["food"]
        )

        customer_objects.append(customer_instance)

        CinemaBar.sell_product(
            product=customer_instance.food,
            customer=customer_instance
        )

    hall = CinemaHall(hall_number)
    cleaner_instance = Cleaner(cleaner)

    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaner_instance
    )
