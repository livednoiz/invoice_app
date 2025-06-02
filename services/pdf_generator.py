import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS
from datetime import datetime
from services.invoice_service import get_invoice_details

TEMPLATE_DIR = "templates"
OUTPUT_DIR = "output"
CSS_FILE = os.path.join(TEMPLATE_DIR, "css", "styles.css")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def generate_invoice_pdf(invoice_id):
    data = get_invoice_details(invoice_id)
    if not data:
        print("❌ Fehler: Keine Rechnungsdaten gefunden.")
        return

    invoice = data["invoice"]
    items = data["items"]

    # Jinja2-Template laden und HTML generieren
    template = env.get_template("invoice_template.html")
    html_out = template.render(invoice=invoice, items=items, date=datetime.now())

    # PDF-Dateipfad
    filename = f"{invoice['invoice_number']}.pdf"
    filepath = os.path.join(OUTPUT_DIR, filename)

    try:
        # HTML-String in PDF umwandeln
        HTML(string=html_out, base_url=".").write_pdf(
            filepath,
            stylesheets=[CSS(CSS_FILE)]
        )
        print(f"✅ PDF erfolgreich erstellt: {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ Fehler beim Erstellen der PDF: {e}")
        return None
