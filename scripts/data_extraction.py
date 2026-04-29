from faker import Faker
import faker_commerce

fake=Faker() 
fake.add_provider(faker_commerce.Provider)

for i in range(10):
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
    print(product)
