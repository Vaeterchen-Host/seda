#this file is only for testing purposes and can be discarded 

#ai generated example to display a dashboard with Flet 

import flet as ft

def main(page: ft.Page):
    # main window
    page.title = "seda - version 0.1."
    page.bgcolor = "#f4f4f9"
    page.padding = 30

    # --- Daten ---
    daten = [
        ("Frühstück", 450),
        ("Mittag", 750),
        ("Snack", 200),
        ("Abendessen", 600)
    ]
    gesamt_kalorien = sum(d[1] for d in daten)

    # --- UI Komponenten ---

    # Überschrift 
    header = ft.Text("seda - version 0.1.", size=32, weight="bold")

    # Statistik-Anzeige
    stats = ft.Container(
        padding=20,
        bgcolor="white",
        border_radius=10,
        content=ft.Text(f"Heute: {gesamt_kalorien} kcal", size=24, color="green", weight="bold")
    )

    # Balken-Diagramm
    balken_reihe = ft.Row(alignment="spaceEvenly", vertical_alignment="end")
    
    for label, wert in daten:
        # Wir bauen die Balken ganz simpel
        hoehe = (wert / 1000) * 200
        balken_reihe.controls.append(
            ft.Column([
                ft.Container(
                    width=50,
                    height=hoehe,
                    bgcolor="blue", # Blau ist immer sicher
                    border_radius=5
                ),
                ft.Text(label)
            ], horizontal_alignment="center")
        )

    # Layout zusammenfügen
    page.add(
        header,
        ft.Container(height=20),
        stats,
        ft.Container(height=20),
        ft.Text("Kalorien nach Mahlzeit", size=18, weight="bold"),
        ft.Container(content=balken_reihe, padding=20, bgcolor="white", border_radius=10)
    )

#if __name__ == "__main__":
    #ft.app(target=main)


if __name__ == "__main__":
# Öffnet die App direkt in deinem Standard-Browser (Safari/Chrome/etc.)
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)