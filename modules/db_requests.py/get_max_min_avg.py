import sqlite3

conn = sqlite3.connect('feinstaub_db')
cursor = conn.cursor()

datum = '2022-03-14'

query = """
SELECT
    MIN(P1) AS min_p1,
    MAX(P1) AS max_p1,
    AVG(P1) AS avg_p1,
    MIN(P2) AS min_p2,
    MAX(P2) AS max_p2,
    AVG(P2) AS avg_p2
FROM messwerte
WHERE DATE(timestamp) = ?
"""


cursor.execute(query, (datum,))
result = cursor.fetchone()


if result and any(result):
    print(f"Feinstaubdaten für den {datum}:")
    print(f"P1 - Min: {result[0]:.2f}, Max: {result[1]:.2f}, Durchschnitt: {result[2]:.2f}")
    print(f"P2 - Min: {result[3]:.2f}, Max: {result[4]:.2f}, Durchschnitt: {result[5]:.2f}")
else:
    print(f"Keine Daten für den {datum} gefunden.")


conn.close()

"SELECT MIN(p1) "
"FROM messwerte "
"WHERE DATE(2022-03-14)"


SELECT timestamp, P1, P2
FROM messwerte
WHERE DATE(timestamp) = '2022-03-14'
ORDER BY timestamp;
