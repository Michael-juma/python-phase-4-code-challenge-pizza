#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    # Reset the database schema
    print("Resetting database schema...")
    db.drop_all()
    db.create_all()

    # Delete existing data (not strictly needed after drop_all, but safe)
    print("Deleting data...")
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    # Create restaurants
    print("Creating restaurants...")
    shack = Restaurant(name="Karen's Pizza Shack", address='address1')
    bistro = Restaurant(name="Sanjay's Pizza", address='address2')
    palace = Restaurant(name="Kiki's Pizza", address='address3')
    restaurants = [shack, bistro, palace]
    db.session.add_all(restaurants)

    # Create pizzas
    print("Creating pizzas...")
    cheese = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    california = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")
    pizzas = [cheese, pepperoni, california]
    db.session.add_all(pizzas)

    # Commit to get IDs
    db.session.commit()

    # Create RestaurantPizza entries using IDs
    print("Creating RestaurantPizza...")
    pr1 = RestaurantPizza(restaurant_id=shack.id, pizza_id=cheese.id, price=1)
    pr2 = RestaurantPizza(restaurant_id=bistro.id, pizza_id=pepperoni.id, price=4)
    pr3 = RestaurantPizza(restaurant_id=palace.id, pizza_id=california.id, price=5)
    restaurant_pizzas = [pr1, pr2, pr3]
    db.session.add_all(restaurant_pizzas)

    # Final commit
    db.session.commit()

    print("Seeding done!")
