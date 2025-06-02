import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def add_customer(name, email, address):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = "INSERT INTO customers (name, email, address) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, address))
        conn.commit()
        print(f"✅ Kunde '{name}' wurde erfolgreich hinzugefügt.")
    except Error as e:
        print(f"❌ Fehler beim Hinzufügen des Kunden: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_all_customers():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers")
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"❌ Fehler beim Abrufen der Kunden: {e}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def delete_customer_by_id(customer_id):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = "DELETE FROM customers WHERE id = %s"
        cursor.execute(sql, (customer_id,))
        conn.commit()
        print(f"🗑️ Kunde mit ID {customer_id} wurde gelöscht.")
    except Error as e:
        print(f"❌ Fehler beim Löschen des Kunden: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
