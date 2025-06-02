from db.models import init_db
from services.customer_service import add_customer, get_all_customers, delete_customer_by_id
from services.invoice_service import create_invoice

items = [
    {"description": "Webdesign", "amount": 500.00},
    {"description": "Wartung", "amount": 120.00}
]

invoice_id = create_invoice(customer_id=1, items=items)

# Neuen Kunden anlegen
add_customer("Max Mustermann", "max@example.com", "Musterstraße 1\n12345 Musterstadt")

# Alle Kunden auflisten
customers = get_all_customers()
for c in customers:
    print(f"[{c['id']}] {c['name']} – {c['email']}")

# Kunde löschen
delete_customer_by_id(1)

if __name__ == "__main__":
    init_db()
# This script initializes the database by creating necessary tables.
# It imports the `init_db` function from the `db.models` module and calls it when the script is run.
# The `init_db` function connects to the database and creates the required tables if they do not already exist.
