# 💼 Freelancer Rechnungsprogramm

Ein leichtgewichtiges Rechnungsprogramm für Freelancer, erstellt mit Python und MariaDB. Die Anwendung läuft im Terminal und bietet PDF-Erstellung mit eigenem Template.

---

## 🚀 Projektübersicht

Dieses Tool richtet sich an Freelancer, die lokal Rechnungen erstellen, verwalten und speichern wollen – ohne Cloud, ohne unnötige Komplexität.

### Features:

* 👤 Kundenverwaltung (anlegen, anzeigen, bearbeiten)
* 🧾 Rechnungserstellung mit laufender Rechnungsnummer (z. B. 20250602-0001)
* 📦 Leistungen mit Beschreibung und Preis eintragbar
* 📄 PDF-Export mit eigenem Template (HTML zu PDF)
* 🖥️ Terminal-Interface (klassisch oder mit Textual)
* 🗄️ Speicherung in MariaDB

---

## 🗺️ Roadmap & Zeitplanung

| 🧩 Meilenstein                              | ⏳ Zeitaufwand | ✅ Status |
| ------------------------------------------- | ------------- | -------- |
| 📁 Projektstruktur anlegen                  | 1h            |  [x]     |
| 🛠️ Datenbankmodell definieren               | 1h            |  [x]     |
| 🔗 Datenbank-Anbindung (MariaDB) einrichten | 1h            |  [ ]     |
| 👥 Kundenverwaltung implementieren          | 2h            |  [x]     |
| 🧾 Rechnungserstellung (inkl. Nummernlogik) | 2h            |  [x]     |
| ✍️ Eingabemaske für Leistungen und Preise   | 1.5h          |  [x]     |
| 📄 HTML-Rechnungstemplate erstellen         | 2h            |  [ ]     |
| 📤 PDF-Export via WeasyPrint integrieren    | 1.5h          |  [x]     |
| 🖥️ Terminal-UI (basic CLI) bauen            | 2h            |  [ ]     |
| 🧪 Tests & Debugging                        | 2h            |  [ ]     |
| 📦 Ausgabeordner für PDFs                   | 0.5h          |  [ ]     |
| 🧰 Setup-Skript / Installationsanleitung    | 1h            |  [ ]     |

> ⏱️ Gesamtaufwand (geschätzt): **17.5 Stunden**

---

## 📦 Installationshinweise

```bash
# Abhängigkeiten installieren (Beispiel)
pip install mysql-connector-python jinja2 weasyprint
```

Datenbankverbindung konfigurieren in `config.py`:

```python
DB_CONFIG = {
  'user': 'dein_user',
  'password': 'dein_passwort',
  'host': 'localhost',
  'database': 'rechnungen_db'
}
```

---

## 📁 Projektstruktur (geplant)

```
invoice_app/
├── main.py
├── config.py
├── db/
│   ├── __init__.py
│   └── models.py
├── services/
│   ├── customer_service.py
│   ├── invoice_service.py
│   └── pdf_generator.py
├── templates/
│   └── invoice_template.html
├── static/
│   └── logo.png
└── output/
    └── (generierte PDFs)
```

---

## 🙌 Mitmachen / Feedback

Ideen, Bugs oder Verbesserungsvorschläge? Erstelle ein Issue oder kontaktiere den Entwickler direkt.

---

Made with ❤️ for Freelancer, die es gerne einfach halten.
