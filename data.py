from faker import Faker
import os
fake = Faker()

os.system('cls')
for i in range(5):
    print(f"Name: {fake.name()}")
    print(f"email: {fake.email()}")
    print(f"phone_number: {fake.phone_number()}")
    print(f"address: {fake.address()}")
    print("="*100)