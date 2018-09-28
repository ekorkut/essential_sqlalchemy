#!/opt/bb/bin/python

from sqlalchemy import inspect
from create_sqlite_inmemory_table import engine, metadata, cookies

print("Insert data start")

ins = cookies.insert().values(
    cookie_name="chocolate_chip",
    cookie_recipe_url="http://blabla.org",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50")
print str(ins)
result = engine.execute(ins)
print(result.inserted_primary_key)

ins = cookies.insert()
inventory_list = [
    {
        "cookie_name": "peanut butter",
        "cookie_recipe_url": "http://blablabla.org",
        "cookie_sku": "PB01",
        "quantity": "24",
        "unit_cost": "0.25"
    },
    {
        "cookie_name": "oatmeal raisin",
        "cookie_recipe_url": "http://blablablabla.org",
        "cookie_sku": "EW01",
        "quantity": "10",
        "unit_cost": "1.25"
    }
]
result = engine.execute(ins, inventory_list)

print("Insert data end")
