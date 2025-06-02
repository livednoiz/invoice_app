import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def init_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Kunden-Tabelle
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            address TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Rechnungs-Tabelle
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT NOT NULL,
            invoice_number VARCHAR(20) NOT NULL,
            date DATE,
            total DECIMAL(10, 2),
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        );
        """)

        # Leistungs-Positionen
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS invoice_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            invoice_id INT NOT NULL,
            description TEXT,
            amount DECIMAL(10, 2),
            FOREIGN KEY (invoice_id) REFERENCES invoices(id)
        );
        """)

        conn.commit()
        print("✅ Tabellen wurden erfolgreich erstellt.")
    except Error as e:
        print(f"❌ Fehler bei Datenbankverbindung: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
