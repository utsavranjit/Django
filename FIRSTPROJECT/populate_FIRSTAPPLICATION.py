import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FIRSTPROJECT.settings')

import django
django.setup()

#Populate  script

import random
from FIRSTAPPLICATION.models import Name_ID, Contact, Address
from faker import Faker

fake=Faker()


def populate(n):
    for entry in range(n):
        fake_name=fake.name()
        fake_contact=fake.phone_number()
        fake_address=fake.address()

        nname=Name_ID.objects.get_or_create(name=fake_name)[0]
        cont=Contact.objects.get_or_create(nam=nname, contact=fake_contact)[0]
        add=Address.objects.get_or_create(con=cont, addr=fake_address)[0]


if __name__=='__main__':
    print("Populating my script using Faker Library")
    populate(30)
    print("populating of script is done")

