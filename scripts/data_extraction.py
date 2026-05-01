from faker import Faker
import faker_commerce
import json

fake=Faker() 
fake.add_provider(faker_commerce.Provider)

PRODUCT_COUNT=5000
FILE_PATH="../data/raw/"
products_list=[]


for i in range(PRODUCT_COUNT):
    product={
        "id":fake.uuid4(),
        "name":fake.ecommerce_name(),
        "price":fake.ecommerce_price(),
        "category":fake.ecommerce_category(),
        "ratings":fake.pyfloat(min_value=0,max_value=5,right_digits=1),
        "stock":fake.random_int(min=0,max=1000),
        "sku":fake.bothify(text='PROD-??-###',letters='ABCDE'),
        "timestamp":fake.date_time_this_year().isoformat()
    }
    products_list.append(product)


with open (FILE_PATH+"products.json","w") as add_prod:
    json.dump(products_list,add_prod)