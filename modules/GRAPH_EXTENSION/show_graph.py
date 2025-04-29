from matplotlib import pyplot
import sqlite3
from pathlib import Path
from matplotlib import pyplot

def get_plot_data(sensor: str, column: str, startDate: str, endDate: str):
    conn = sqlite3.connect(Path(__file__).parent.parent.parent / 'feinstaub.db')
    cursor = conn.cursor()


    # count_query = f"""
    # SELECT COUNT(*) FROM {sensor}
    # WHERE timestamp BETWEEN '2022-{startDate}T00:00:00' AND '2022-{endDate}T23:59:59'
    # """
    # cursor.execute(count_query)
    # row_count = cursor.fetchone()[0]
    # print(f"Anzahl der Datensätze im Zeitraum: {row_count}")


    query = f"""
    SELECT timestamp, {column}
    FROM {sensor}
    WHERE timestamp BETWEEN '2022-{startDate}T00:00:00' AND '2022-{endDate}T23:59:59'
    ORDER BY timestamp
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    if not results:
        print("Keine Daten gefunden.")
        return [], []

    sample_rate = 100  # nur jeden 100. Wert verwenden
    x_values = [row[0] for i, row in enumerate(results) if i % sample_rate == 0]
    y_values = [row[1] for i, row in enumerate(results) if i % sample_rate == 0]

    pyplot.plot(x_values, y_values)
    pyplot.title(f"im Zeitraum von {startDate} bis {endDate} ")
    pyplot.xlabel("Zeit")
    pyplot.ylabel(f"{column}")
    pyplot.show()








if __name__ == "__main__":
    get_plot_data("dht22_metric","temperature","01-01", "01-15")