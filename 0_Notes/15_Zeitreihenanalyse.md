# Zeitreihenanalyse

Leistungsbeurteilung -> was kann es 
Seite 7: Vor der prüfung überprüfen (ersetzte die folien mit neuen grau wird nicht gemacht)

## Wichtige Begriffe

- **Regelmässige Abtastung**: einteilung von kontinuierlichen Daten in punkte -> wir machen daraus diskrete zeit (von kontinuierlich)
- **Lag**: Zeitspanne von einem zeitpunkt zum nächsten (verzögerung, zeit differenz)
- **Extrapolation**: neue Daten ausserhalb der Zeitreihe (davor / nachher) darf man nicht, da würde man das Modell auf das Modell anwenden.
- **Interpolation / Imputation**: füllen von Lücken innerhalb der Daten ist ok
  - Lineare Interpolation: Mit dem mittelwert zwischen den zwei zeit zeitpunkten ergänzen
  - Forward / Backward fill: nehme den jetzigen punkt und fülle alle bis zum nächsten mit dem wert, ist schlechter
  - Kallman-Filter: guter filter, besonders gut für lange lücken mit viel struktur
- **Residuen**: Zeitreihe - Trend - Saisonalität -> Residuen
- **LOESS**: -> STL (seasonal trend decompose), MSTL (multi seasonal trend decompose)


## Notizen

- Vorteil klassische Zeitrehie vs. ML
  - Nachvollziehbar
  - Weniger compute
  - Kann mit weniger Daten umgehen
- 5
  - Zeitlich geordnete Daten
  - Wenn wir stark von der Sollkurve abweichen, zeigt es dass es eventuell handlung braucht
  - Ökonomen waren zuerst bei Zeitreihenanalyse -> andere Begriffe
  - Es gibt nicht eine Methode die für alle Zeitreihen funktionieren
- 6
  - Bedinge Vorhersage: wir sind im einem Jahr da, was brauchen wir dann (eg. Wie viel strom)
  - Zusammenhänge: sonnen und produktion bei solar, geht es der anlage gut?
  - Seltene Ereignisse die wir nicht eingeplant haben, was kann man tun?
- 8
  - gibt vorher nachher, x Zeit, y irgend eine Variabel die uns interessiert
  - Typischer weise werden die aufgeteilt (gleiche intervalle, zum Beispiel pro Monat) weil es zu viele datenpunkte hat
  - vorhersage ganzer Zahlen anders als bei kontinuierlichen Zahlen
  - Regression punkt ist punkt, sind aber nicht geordnet, in Zeitreihen sind sie geordnet nach Zahl
- 9: Refernzprozess
  - 2. Zerlegung wir nehmen sie auseinander
- 10: 
  - Zu viele Daten
    - Wenn weit in die Zukunft, dann gröberes Sampling
    - Wenn nah in die Zukunft hohe granularität
  - Unterschiedliche Sasonalitäten. eg. strom (Tag (licht), Woche, Jahr (saison))
- 12
  - Explorative Data Analyse (EDA):
    - Wir fragen die Daten eine Frage, die Daten geben uns eine Antwort
  - EDA: Zoom in von einem Lag (eine Zeitspanne)
  - Extrapolation: Lücken füllen in den Daten (eg. keinen niederschlag) gibt wird nicht gemacht
    - Lücke in der Zeitreihe (interpolation) -> für einen Monat keinen Datenpunkt, kann ergänzt werden
    - Extrapolation ausserhalb des Datensatztes kann nicht gemacht werden
- Imputation (Ergänzung von Lücken)
  - Eine range mit einem anderen lag
  - Ergänzung von leeren daten, alle werte die näher als 10 Tag weg sind können benutzt werden um eine lücke zu füllen
  - Lineare Interpolation: Mit dem mittelwert zwischen den zwei zeit zeitpunkten ergänzen
  - Forward / Backward fill: nehme den jetzigen punkt und fülle alle bis zum nächsten mit dem wert, ist schlechter
- Wenn Daten keine Saisonalität haben ist es einfacher vorhersagen, weil es noch einen Trend haben kann
- 13
  - Zerlegung: gruppieren die Inhalte
  - Seasonal Decompose
    - Trend der unterschiede: optimaler kompromiss zwischen glattheit und information
    - Seasonal: Wenn jedes Jahr gleich aussehen würde, was bleibt übrig, wenn wir das seasonal raus nehmen und sehr regelmässig machen dann hilft das uns für die Zukunft
    - Residuen: Modell, alles was übrig bleibt sind die Residuen, Zeitreihe - Modell (normalverteilt, zufällig), residuen sollten über die zeit nicht korrelieren
    - Domänenwissen brauchen um ausreisser zu erklären, ist es ein messgerät fehler oder ein extrem event
  - Es gibt auch noch andere möglichkeiten es zu auseinander zu nehmen
  - Loesdekomosition: kontrolle über rolling window und period
- Zeitreihe komposition
  - Trend
  - Saisonalität: (können auch tages saison sein)
  - Residuen: Das was übrig bleibt
  - Zeitreihe = Trend + Saisonalität + Residuen (additives Model)
  - Die komposistion kann beliebig modelliert sein, wenn additiv nicht sinn macht (wenn es keine negative werte gibt), können die Daten transformiert werden, zum Beispiel logarithmus und dann kann ein additives Model gebraucht werden
- Am Anfang und am Ende können die Daten nicht verwendet werden weil ein teil des Fensters leer wäre
- Stationarität:
  - Bedingung die an die Residuen gestellt werden sollten
  - Im linearen modell wollen wir sie so klein wie möglich haben wollen
  - 1. Es ist zufällig verteil (Normalverteilt)
  - 2. Die bedingungen ändern sich nicht, der Würfel in der Vergangenheit muss den selben regeln folgen wie in der zukunft
### Kriterien der zeitreihe (18)
- 1. kriterium: durchschnitt 
  - Ich habe alle änderungen im trend drinn, sodass sich an den residuen nichts mehr ändert
  - Durchschnitt muss konstant bleiben, wenn der durchschnitt des würfels in der vergangenheit 1 war und jetzt 6 dann folgt es nicht den selben regeln
- 2. Kriterium: Varianz
  - Die streuung muss konstant sein
  - Es existiert eine obere schranke die typisch ist für die zeitreihe, muss visuell getestet werden gibt keine metrik
- 3. Kriterium: ähnliche verteilung über die zeit
  - Stationarität, zusammenhänge über die Zeit ist nicht erhalten
  - Unterschiedliche Muster zu unterschiedlichen Zeiten
  - Mit domänen modelle kann es sein, dass es eine regelmässigkeit erhalten sind, dann muss man die dekomposition
- 

