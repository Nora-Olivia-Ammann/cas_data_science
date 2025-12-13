# Zeitreihenanalyse

Leistungsbeurteilung -> was kann es 
Seite 7: Vor der prüfung überprüfen (ersetzte die folien mit neuen grau wird nicht gemacht)

Links auf der Folie zu mehr info


1. Was hat eine zeitreihe mit sich selbst zusammen zu tun? (wetter über jahrzehnte)
2. Was hat eine zeitreihe mit einer anderen zu tun? (Niederschlag und temperatur)


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
- **Parsimonious model**: wenn ein model mit weniger parameter gleich gut auskommt wie eines mit mehr, dann nehmen wir das mit weniger (über-parameterisierung ist nicht gut)
- **Kovariaten**: Die x, externe faktoren
- **Scheinkorrelation**: korrelation die stark korreliert aussehn aber hat nichts damit zu tun
- **Granger kausalität**: Leading indicator (vorauseilender indikator) -> zeigt in die zukunft für die trailing variabel

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

### Explorative Data Analyse (EDA)
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

### Zerlegung

- 13
  - Zerlegung: gruppieren die Inhalte
  - Seasonal Decompose
    - Trend der unterschiede: optimaler kompromiss zwischen glattheit und information
    - Seasonal: Wenn jedes Jahr gleich aussehen würde, was bleibt übrig, wenn wir das seasonal raus nehmen und sehr regelmässig machen dann hilft das uns für die Zukunft
    - Residuen: Modell, alles was übrig bleibt sind die Residuen, Zeitreihe - Modell (normalverteilt, zufällig), residuen sollten über die zeit nicht korrelieren
    - Domänenwissen brauchen um ausreisser zu erklären, ist es ein messgerät fehler oder ein extrem event
  - Es gibt auch noch andere möglichkeiten es zu auseinander zu nehmen
  - Loesdekomosition: kontrolle über rolling window und period

### Zeitreihe komposition

- Zeitreihe komposition
  - Trend
  - Saisonalität: (können auch tages saison sein)
  - Residuen: Das was übrig bleibt
  - Zeitreihe = Trend + Saisonalität + Residuen (additives Model)
  - Die komposistion kann beliebig modelliert sein, wenn additiv nicht sinn macht (wenn es keine negative werte gibt), können die Daten transformiert werden, zum Beispiel logarithmus und dann kann ein additives Model gebraucht werden
- Am Anfang und am Ende können die Daten nicht verwendet werden weil ein teil des Fensters leer wäre

### Stationarität

- Stationarität von Residuen:
  - Bedingung die an die Residuen gestellt werden sollten
  - Im linearen modell wollen wir sie so klein wie möglich haben wollen
  - 1. Es ist zufällig verteil (Normalverteilt)
  - 2. Die bedingungen ändern sich nicht, der Würfel in der Vergangenheit muss den selben regeln folgen wie in der zukunft
  - Wir möchten ein modell anhand der vergangenheit trainiert auf die Zukunft anwenden. Die spielregeln müssen gleich bleiben sonst kann die vergangenheit nicht auf die zukunft angewendet werden. In der praxis ist nichts ganz schwarz-weiss, es muss aus der domäne beurteilt werden ob die veränderung einen sehr grossen einfluss hat um das modell unbrauchbar zu machen. Wie manifestiert sich die veränderung der spielregeln sich in der variabel die mich interessiert. 


### Kriterien der zeitreihe (18)
- 1. kriterium: durchschnitt 
  - Ich habe alle änderungen im trend drinn, sodass sich an den residuen nichts mehr ändert
  - Durchschnitt muss konstant bleiben, wenn der durchschnitt des würfels in der vergangenheit 1 war und jetzt 6 dann folgt es nicht den selben regeln
- 2. Kriterium: Varianz
  - Die streuung muss konstant sein
  - Es existiert eine obere schranke die typisch ist für die zeitreihe, muss visuell getestet werden gibt keine metrik
  - Co-varianz von zeitreihe zu zeitpunkt T, verschiebung mit 4 lags, neuer zeitpunkt, vergleich mit 4 langs, wenn diese varianz gleich ist, wissen wir, dass der zusammenhang besteht bleibt
- 3. Kriterium: ähnliche verteilung über die zeit
  - Stationarität, zusammenhänge über die Zeit ist nicht erhalten
  - Unterschiedliche Muster zu unterschiedlichen Zeiten
  - Mit domänen modelle kann es sein, dass es eine regelmässigkeit erhalten sind, dann muss man die dekomposition
- Analysen sind am einfachten, wenn die zeitpunkte konstanter abstand von einander zu haben, alle x minuten, etc.

### Statistischen Test (16)

- Kann die Zeitreihe **stationär** sein? - Augmented Dickey-Fuller Test (TODO: more investigation)
  - -> können wir etwas mit den residuen anfangen?
  - -> müssen wir noch weiter modellieren?
  - -> stationarität ist auch hilfreich zum sehen ob sich etwas verändert?
  - -> versuche die regel zu modellieren, in den residuen sehen wir ob sich etwas verändert
  - Hat es einen random walk (next move depends only on the current position), ist es stationär
  - Hypothesen test: 0 Hypothese: zeitreihe ist nicht stationär
  - Wenn der p wert unterschiedliche von 0 ist, dann kann es nicht stationär sein. Wenn er 0 ist, kann es stationär sein, muss aber nicht. Keine false negative aber false positive
  - visuelle überprüfung ist trotzdem wichtig
  - Saisonalität: ein hoher wert folgt einen tiefen wert, etc. hier ist p=0 also 
- Dummy Variabel: eg. ist es ein Wochenende, brauche ich ein anderes Modell als wenn es ein wochentag ist.
  - Wenn die residuen nicht stationär sind, dann gehen wir zurück in die modellieren, zum beispiel neue dummy variabel gefunden, wochenende arbeitswoche, etc. Prozess ist nicht linear
- Zerlegung: Manuell mit Vorwissen, zum beispiel wochenende
- Differenzieren wenn wir einen linearen trend haben, dann gibt es eine konstante, wenn der zuwachs linear ist, dann ist die differenz zwischen dem vorherigen und jetzigen wert
- Stationaritätstest kann uns auch sagen, haben wir wirklich verstanden was wir analysiert haben, gibt es noch mehr die modelliert werden muss?
- 19
  - Stochastisch heisst "zufall" ist im spiel. Ist nicht unbedingt zufall aber wir verstehen es einfach nicht.
  - Wenn wir etwas erklären können kommt es nicht in die residuen

### Analyse der Residuen (20)

- hat der "würfel" ein gedächniss, oft ja, wenn es gestern geregnet hat ist die wahrscheinlichkeit grösser dass es heute regnet. Es gibt eine trägheit
- 1 lag ist ein Zeitschritt und ist eine zeitdifferenz (eg 1 monat). 1 lag von `i` ist `i+1`

- Code: Partielle Autokorrelationsfunktion (und Autokorrelationsfunktion) des Trends
- Autokorrelationsfuktion (TODO: mehr recherche)
  - nach 6 Monaten sind sie anti-korreliert, eine zeitreihe die um 6 lags verschoben ist, wenn die verschobene ein maximum hat, dann hat die unverschobene hat ihren miinimum
- Wir können etwas mit der trägheit machen, eg. einen Monat ist mit einem anderen Monat leicht anti-korreliert
- Wir wissen den trend von Dezember, wir kennen den trend von Januar, wir wissen wie der Dezember ist, dann können wir anhand von dem abschätzen wie der Februar wird. Ein kleines fenster: was macht der zufall in der zukunft?

- langsamer trend, nahe gelegende werte sind ähnlich von einander auch wenn
- Glatte komponente: langsamer trend (folie 21)
- Periodischer Trend: wie saison
- Keine korrelation der residuen

- Code: Partielle Autokorrelationsfunktion (und Autokorrelationsfunktion) der Residuen
- bei langsam ändernde signale, dann hat der vormonat auch einen einfluss nicht nur der vorherige
- Verkettung:
  - gestern bestimmt heute
  - vorgestern bestimmt gestern
  - -> verkettung miteinbeziehen
- Was bleibt übrig wenn wir die verkettung wegnehmen? Ist die Frage
- mit der verkettung kann es sein, dass zwei monate für den nächsten überkorrelieren, und der nächste doch nicht so nahe ist (TODO: research), minus zeigt die differenz 

- Partielle Autokorrelationsfunktion und Autokorrelationsfunktion zusammen anschauen und zusammen mit der ganzen zeitreihe
- Darstellung empfohlen (21): Code: Zur Interpretation ist ein Vergleich mit der Zeitreihe hilfreich


- Die zeit mit sich selbst korrelieren

- Kreuzkorrelationsfunktion
  - Wenn die einte überdurchschnittlich ist, ist die andere auch überdurchschnittlich oder unterdurchschnittlich?
  - Hatt eine gute wettervorhersage einen einfluss auf die anzahl passagiere? So können wir das Wetter verwenden um die passagiere vorherzusagen
  - 


### Wandtafel (Foto)

- Korrelationsfunktionen (oben)
- Zeitreihen (unten)
- Welche gehören, was ist die darstellung wenn es ungefähr so aussieht
  - Gehören zusammen (kann mehrere haben)
    - a: Steigend / 3
    - b: Periodisch glatt schwankend / 1
    - c: Sinkend / 3
    - d: Chaotisch / 2: Keine korrelation weisses rauschen & 4: gibt es wirklich hier noch zusammenhänge?

- 1: Periodisch
- 2: White noise
- 3: wir wisschen nicht dass es einen absteigenden trend ist, wir wissen nicht ob nach oben oder unten
- 4: kurzlebige zusammenhänge, übersieht man fast immer in der reihe, ist aber nicht nur white noise

### Was haben zwei Zeitreihen mit anderen zu tun?

- Niederschlag und temperatur
- Die residuen wurden zusammen 
- Was hat ein überdurchschnittlich warmer monat mit einem überdurchschnittlichen regenreichen zu tun?
- pearson korrelation -> korrlation von x & y
- Wir verschieben eine zeitreihe um einen lag, die andere nicht und schauen ob die andere etwas mit ihr zu tun hat.
- vielleicht braucht es eine weile dass wir einen unterschied von x in y sehen
- -> Anitkorreliert: ohne zeitverschiebung sind sie negativ korreliert (überdurchschnittlich warm hat weniger regen)
  - Wenn wir die eine um 1 verschieben haben sie immernoch etwas miteinander zu tun? Es ist sehr unwahrscheinlich dass nur aus zufall eine korrelation bei den residuen gefunden wird.
  - mit einem lag sehe ich einen zusammenhang, aber es kann sein, dass die abhängige variabel in die falsche richtung verschoben wir. Es kann keine verursachung vorlieben.
  - 1. Art der Kausalität: philosophische domäne wissen
  - 2. Schwächere: Granger kausalität, was war zuerst huhn oder ei?
- Es ist nicht klar ersichtlich welches jetzt die leading indicator ist. Gibt keine konvention, kann nur durch ausprobieren herausgefunden werden welches leading oder trailing ist. (code: Welches Signal ist zuerst - anhand von Demodaten)
  - Hier die blaue ist vor der roten, jede library macht es etwas anders, die zusammenhänge zwischen der einen und anderen, wenn man berücksitigt, dass es eine weile dauern kann bis man etwas sieht.
- 



