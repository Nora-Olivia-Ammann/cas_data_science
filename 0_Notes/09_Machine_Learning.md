# Machine Learning

## Tag 1

- 10: 
  - beim tictactoe ist es möglich das perfekt zu machen, 
  - Wenn es perfekt möglich ist dann sind wir meistens nicht in ML
- 11:
  - Schach ist zu komplex um alles durch-zusimulieren
  - Perfekte lösung nicht möglich, aber eine sehr gute lösung ist gut genug
  - Idee von perfektion wird aufgegeben
- 12:
  - räpresentieren das objekt in der reelen welt mit features
  - die features sind wichtig, aber es gibt immer ein informationsverlust aber meistens können wir es gut genug räpresentieren
- 13:
  - modell kann ausprogrammiert sein (imperativer code mit if, else, etc.). Ist immernoch AI weil es intelligent erscheint. Obwohl es nicht gelernt ist.
  - Wie ein modell lernt ist auch ausprogrammiert sein
- 14:
  - AI -> Tic Tac Toe
  - ML -> Schach-Spiel
  - Deep Learning -> Das Modell ist zusätzlich ein neurales netz
- 15:
  - Im kurs nehmen wir immer an, dass die Daten sauber sind und korrekt sind (Clean Data)
- 17:
  - 1 -> Hunderte Daten aber viel Wissen
  - 3 -> eigentlich alles aus den Daten, in den bereichen bei denen die Daten schwierig ist zu definieren. Eg. Bilderkennung, haben wir pixel es ist zu klein um zu wissen was ein hund ist, daher wird mehr gelernt
  - Im praxis alltag (asser grosse player) sind wir bei 1 & 2
  - Wir haben aber immer ein paar annahmen und daten
- 19:
  - Vorteil mehr kontrolle, und wir können analysieren wo es gut ist. Und dann gezielt verbessern
  - Nachteil modell kann mit der zeit out of date sein
  - Meistens offline in der realen welt weil es einfacher ist
  - Beispiel online learning dass schief ging, Microsoft AI dass ein Twitter bot gab, der rassistisch wurde
- 20: 
  - wir sind im bereich von 5-6
  - Aber 3 & 4 müssen auch miteinbezogen werden
  - Visualisierung ist auch gut um bugs zu finden, die auch in den daten sein können
- 22
  - Möchten output vorhersagen
  - Abhängige Variabel -> output
- 24:
  - kontinuierlich -> eg. Preis eine Zahl
- 25:
  - expertenwissen zum beispiel dass es kein negatives gewicht
- 26:
  - Encoden -> zu beispiel text -> die fischart
  - Standardisiert -> nummern
- 30
  - Betas ist das was wir lernen
  - das modell kann die formel nicht verändern sondern nur die betas lernen
- 34:
  - Gewichtete Summe der Features -> unterschiedliche "wichtigkeit"
  - es gibt keine interaktion zwischen den features, das ist auch die Schwäche des Modells
- 35
  - echtes gewicht = vorhersage + fehler = modell formel + fehler
  - jetzt kann man über den fehler eine vorhersage machen
- 36
  - Alles dieselbe Former in anderen notationen, das Lineare Model
  - 3. kann es auch als vekoren schreiben
  - 4. Wir wissen dass es vektoren sind, wir lassen es weg
- 37
  - Visualisierung ist gut für die Intuition aber es hört schnell auf
- 39
  - 1: summe von gewichtungen * features
  - 2: Nein kann auch eine fläche sein (hyper-ebene)

### Regressions Metrik

- 41
  - fehler pro datenpunkt kann einfach gemessen werden
  - residual (epsilon) -> fehler
  - Der fehler pro datenpunkt ist nicht genügend um zu beurteilen ob es gut ist
  - Es muss zusammengezählt werden -> Metrik
- 42
  - Verschiedene Fragen um die Metrik zu erstellen
  - Wir brauchen eine Metrik um zu entscheiden was besser ist.
  - Die metrik ist stark abhängig von der Fragestellung
  - Häuserpreise, sollen wir das Schloss wegnehmen?
  - Müssen aussreisser mit einbezogen werden? Dann andere metrik
- 43
  - MAE -> Robust gegen ausreisser
  - MSE -> nimmt ausreisser miteinbezogen und werden davon beeinflusst
- 


