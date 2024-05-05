from django.core.management.base import BaseCommand
from faker import Faker
import random
from vendors.models import Vendor
from purchase_orders.models import PurchaseOrder

fake = Faker()

class Command(BaseCommand):
    help = 'Generates fake data for vendors and purchase orders'

    def handle(self, *args, **options):
        num_vendors = 10
        vendors = self.generate_vendors(num_vendors)
        self.generate_purchase_orders(vendors)
        self.stdout.write(self.style.SUCCESS("Fake data generated successfully!"))

    def generate_vendors(self, num_vendors=10):
        vendors = []
        for _ in range(num_vendors):
            name = fake.company()
            contact_details = fake.phone_number()
            address = fake.address()
            vendor_code = fake.unique.uuid4().split('-')[-1]
            vendor = Vendor.objects.create(name=name, contact_details=contact_details, address=address, vendor_code=vendor_code)
            vendors.append(vendor)
        return vendors

    def generate_purchase_orders(self, vendors, num_purchase_orders_per_vendor=5):
        for vendor in vendors:
            for _ in range(num_purchase_orders_per_vendor):
                po_number = fake.unique.uuid4().split('-')[-1]
                order_date = fake.date_time_this_month(before_now=True, after_now=False)
                delivery_date = fake.date_time_between(start_date=order_date, end_date='+30d')
                items = [{'name': fake.word(), 'quantity': random.randint(1, 10)} for _ in range(random.randint(1, 5))]
                quantity = sum(item['quantity'] for item in items)
                status = random.choice(['pending', 'completed', 'canceled'])
                quality_rating = random.randint(1, 5) if status == 'completed' else None
                issue_date = fake.date_time_between(start_date=order_date, end_date=delivery_date)
                acknowledgment_date = fake.date_time_between(start_date=issue_date, end_date=delivery_date) if status == 'completed' else None
                PurchaseOrder.objects.create(po_number=po_number, vendor=vendor, order_date=order_date, delivery_date=delivery_date, items=items, quantity=quantity, status=status, quality_rating=quality_rating, issue_date=issue_date, acknowledgment_date=acknowledgment_date)