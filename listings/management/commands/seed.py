import random
from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        sample_data = [
            {"name": "Cozy Cottage", "description": "A cozy cottage in the mountains.", "price_per_night": 100.00, "location": "Mountain View"},
            {"name": "Beach House", "description": "A luxurious beach house with a stunning ocean view.", "price_per_night": 250.00, "location": "Malibu"},
            {"name": "City Apartment", "description": "A modern apartment in the heart of the city.", "price_per_night": 150.00, "location": "New York City"},
        ]

        for data in sample_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with sample listings.'))
