import mysql.connector
from mysql.connector import Error
from datetime import date, datetime
from config import DB_CONFIG

def generate_invoice_number():
    """Erzeugt eine laufende Rechnungsnummer im Format YYYYMMDD-XXXX"""
    today = date.today().strftime("%Y%m%d")
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM invoices WHERE DATE(date) = CURDATE()")
        count_today = cursor.fetchone()[0] + 1
        return f"{today}-{count_today:04d}"
    except Error as e:
        print(f"❌ Fehler beim Generieren der Rechnungsnummer: {e}")
        return None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def create_invoice(customer_id, items: list[dict]):
    """
    Erstellt eine neue Rechnung mit zugehörigen Positionen.
    items = [ { 'description': 'Service A', 'amount': 99.99 }, ... ]
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        invoice_number = generate_invoice_number()
        today = date.today()

        total = sum(item["amount"] for item in items)

        # Rechnung anlegen
        cursor.execute("""
            INSERT INTO invoices (customer_id, invoice_number, date, total)
            VALUES (%s, %s, %s, %s)
        """, (customer_id, invoice_number, today, total))
        invoice_id = cursor.lastrowid

        # Positionen speichern
        for item in items:
            cursor.execute("""
                INSERT INTO invoice_items (invoice_id, description, amount)
                VALUES (%s, %s, %s)
            """, (invoice_id, item["description"], item["amount"]))

        conn.commit()
        print(f"✅ Rechnung {invoice_number} erfolgreich erstellt.")
        return invoice_id
    except Error as e:
        print(f"❌ Fehler beim Erstellen der Rechnung: {e}")
        return None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_invoice_details(invoice_id):
    """Liefert alle Infos zur Rechnung + Positionen"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)

        # Rechnung
        cursor.execute("""
            SELECT i.*, c.name AS customer_name, c.address AS customer_address
            FROM invoices i
            JOIN customers c ON i.customer_id = c.id
            WHERE i.id = %s
        """, (invoice_id,))
        invoice = cursor.fetchone()

        # Positionen
        cursor.execute("""
            SELECT * FROM invoice_items WHERE invoice_id = %s
        """, (invoice_id,))
        items = cursor.fetchall()

        return {
            "invoice": invoice,
            "items": items
        }
    except Error as e:
        print(f"❌ Fehler beim Abrufen der Rechnungsdetails: {e}")
        return {}
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
