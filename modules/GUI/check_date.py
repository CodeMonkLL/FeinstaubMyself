import calendar
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funktion zur Überprüfung des Datums
def check_date(month, day, year=2022):
    try:
        # Überprüfen, ob der Monat gültig ist (zwischen 1 und 12)
        if month < 1 or month > 12:
            raise ValueError("Ungültiger Monat! Monat muss zwischen 1 und 12 liegen.")
        
        # Bestimme die Anzahl der Tage im Monat
        _, max_day = calendar.monthrange(year, month)  # _ gibt den ersten Wochentag zurück, max_day gibt die Anzahl der Tage im Monat zurück

        # Überprüfen, ob der Tag innerhalb der maximalen Anzahl an Tagen liegt
        if day < 1 or day > max_day:
            raise ValueError(f"Ungültiger Tag! Der Monat {month} hat nur maximal {max_day} Tage.")

        # Erstelle das Datum
        date = f"{day:02d}-{month:02d}-{year}"
        return date  # Gibt das erstellte Datum zurück

    except ValueError as e:
        return str(e)  # Gibt die Fehlermeldung zurück, falls es einen Fehler gibt
