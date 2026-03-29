# Projektstruktur (ai-generiert)

> Diese Datei beschreibt den aktuellen Aufbau des Workspaces und soll als einfache Orientierung für das Projekt dienen.

## Kurzüberblick

SEDA ist aktuell ein Python-Projekt mit drei Hauptbereichen:

- Fachlogik in `model/`
- Benutzeroberflächen in `ui/`
- Daten in `data/`
- Tests in `tests/`
- Dokumentation in `docs/`

Zusätzlich gibt es Hilfsdateien, ältere Experimente und einige Legacy- oder Utility-Dateien, die nicht direkt zum Kernablauf gehören.

## Ordner im Projekt

### `model/`
Hier liegt die eigentliche Anwendungslogik.

Wichtige Dateien:
- `classes.py`: zentrale Klassen wie `User`, `WaterLog`, `WeightLog`, `Food`, `Meal`
- `database.py`: SQLite-Zugriff, Tabellenaufbau und Datenbankmethoden
- `controller.py`: CLI-Steuerung und Verbindung zwischen Eingaben, Logik und Datenbank

### `ui/`
Dieser Ordner enthält alles rund um die Benutzeroberfläche.

Wichtige Dateien:
- `ui.py`: grafische Oberfläche mit Flet
- `cli_view.py`: Ein- und Ausgaben für die Kommandozeile
- `ui_discardable.py`: eher experimentelle oder austauschbare UI-Datei
- `tutorial/`: kleine Flet-Beispiele und Lernschritte


### `data/`
Hier liegen Projektdateien mit echten Nutzdaten.

Aktuell:
- `database.db`: die SQLite-Datenbank des Projekts

### `tests/`
Hier liegen automatisierte Tests.

Aktuell:
- `test_classes.py`: Tests für Klassen aus `model/classes.py`
- `test_database.py`: Tests für Datenbankfunktionen
- `test.db`: zusätzliche Testdatenbank

### `docs/`
Hier liegt die Projektdokumentation.

Aktuell:
- `de_struktur.md`: deutsche Beschreibung der Projektstruktur
- `en_structur.md`: englische Version der Strukturübersicht

### `utils/`
Hier liegen Hilfsdateien, Einzeltests oder ältere Zusatzskripte.

Beispiele:
- `tobi_classes.py`
- `bine_cli_main.py`
- `test_bine.py`

Dieser Ordner wirkt im Moment wie ein Sammelbereich für Zwischenstände oder ergänzende Werkzeuge.

### `legacy/`
Hier liegt älterer Code, der nicht mehr zum Hauptpfad gehört, aber noch aufbewahrt wird.

Aktuell:
- `ui_german.py`

### `test_db/`
Dieser Ordner wird für temporäre Testdatenbanken verwendet.

Die Tests in `tests/test_database.py` erzeugen dort isolierte Datenbankdateien.

## Wichtige Dateien im Hauptordner

### `main.py`
Das ist der Einstiegspunkt des Programms.

Aktuell:
- fragt ab, ob die GUI oder die CLI gestartet werden soll
- startet bei `y` die Flet-Oberfläche
- startet bei `n` den CLI-Controller


### `config.py`
Hier stehen zentrale Einstellungen und Pfade.

Aktuell:
- `BASE_DIR`
- `DB_PATH`
- `DB_TEST_PATH`
- `DEVS`
- `VERSION`


### `bug_tracker.py`
Diese Datei sammelt bekannte Probleme und technische Baustellen des Projekts.

Sie ist keine Laufzeitlogik, aber nützlich für Planung und Wartung.

### `requirement.txt`
Hier stehen die Python-Abhängigkeiten des Projekts, zum Beispiel:
- `flet`
- `Flask`
- `pytest`-nahe Testumgebung
- weitere Hilfsbibliotheken


## Was nicht direkt zum Kern gehört

Im Workspace gibt es außerdem:

- `venv/`: lokale virtuelle Python-Umgebung
- `__pycache__/`: automatisch erzeugte Python-Zwischendateien
- `.git/`: Git-Verwaltung
- `.codex/`: lokale Werkzeug- oder Editor-Datei

Diese Dinge sind wichtig für die Entwicklung, aber nicht Teil der eigentlichen Fachstruktur.

## Was macht `.gitignore`?

Die Datei `.gitignore` legt fest, welche Dateien oder Ordner Git nicht verfolgen soll.

Im aktuellen Projekt betrifft das unter anderem:
- Python-Caches
- virtuelle Umgebungen
- Editor-Dateien

Wichtig:
`.gitignore` löscht nichts. Sie verhindert nur, dass bestimmte Dateien versehentlich versioniert werden.

- `utils/` sollte nur Hilfsfunktionen enthalten oder später sauber auf andere Ordner verteilt werden.
- `legacy/` ist sinnvoll für alten Code, sollte aber nicht mit aktivem UI-Code verwechselt werden.
- `ui_discardable.py` könnte später entfernt oder klar als Experiment markiert werden.


