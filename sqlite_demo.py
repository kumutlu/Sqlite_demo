import sqlite3

from cars import Cars

conn = sqlite3.connect('cars.db')

c = conn.cursor()

#c.execute("""CREATE TABLE cars (
#            brand text,
#            model text,
#            year integer,
#            price integer
#            )""")


def insert_car(car):
    with conn:
        c.execute("INSERT INTO cars VALUES (:brand, :model, :year, :price)",
                  {'brand': car.brand, 'model': car.model, 'year': car.year, 'price': car.price})


def get_cars_by_model(model):
    c.execute("SELECT * FROM cars WHERE model=:model", {'model': model})
    return c.fetchall()


def update_year(car, year):
    with conn:
        c.execute("""UPDATE cars SET year = :year
                    WHERE brand = :brand AND model = :model""",
                  {'brand': car.brand, 'model': car.model, 'year': year, 'price': car.price})


def update_price(car, price):
    with conn:
        c.execute("""UPDATE cars SET price = :price
                            WHERE brand = :brand AND model = :model""",
                  {'brand': car.brand, 'model': car.model, 'year': car.year, 'price': price})


def update_model(car, model):
    with conn:
        c.execute("""UPDATE cars SET model = :model
                            WHERE brand = :brand AND year = :year""",
                  {'brand': car.brand, 'model': model, 'year': car.year, 'price': car.price})


def remove_car(car):
    with conn:
        c.execute("DELETE from cars WHERE brand = :brand AND model = :model",
                  {'brand': car.brand, 'model': car.model})


car_1 = Cars("Honda", "Civic", 2016, 85000)
car_2 = Cars("Renault", "Fluance", 2015, 80000)
car_3 = Cars("Hyundai", "i20", 2009, 35000)
car_4 = Cars("Volkswagen", "Polo", 2016, 75000)

update_price(car_2, 80000)

update_year(car_2, 2015)

update_model(car_2, 'Fluence')

print(get_cars_by_model('Fluence'))