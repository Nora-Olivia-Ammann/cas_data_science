# Statistik

- https://rapp.fhnw.ch/RAPP/MarcelSteiner/

In hohen dimensionen (schon drei) sind distanzen berechnen schwieriger, da die Zahlen sehr gross werden.

- Qualitative Merkmale können nicht verglichen werden. Messwerte (haarfarbe) kann nicht als besser oder schlechter eingestuft werden. Im vergleich, fehlerquote (diskret) kann verglichen werden, weniger ist besser.

- Statistik hat eine Idee, wir minimieren etwas

- Summe der Beträge minimiere ist der Median, median zu minimieren ist schwieriger
  - median absolute deviation (MAD) -> die robustheit des Medians 
- Summe der Quadrate minimiere ist der Durchschnitt (arithmetisches Mittel) (Gauss)
    - Varianz (Standardabweichung)
    - Wie gross ist das mittlere Quadrat?
    - Die mittlere quadratwerte ist die Varianz, die Wurzel daraus ist die Standardabweichung


# 5 Grundlagen der Modellwelt (S. 22)

- In der Modellwelt sind die Buchstaben griechisch
- In der Realität sind die Buchstaben lateinisch
- Jetzt müssen die beiden Buchstaben arten zusammengeführt werden, das ist statistik.
- Dann müssen wir auch noch sagen wie gut der Wert ist.
- Zufallsgrösse X ist die Frage die ich stell oder messe, die kleinen x sind antworten
- Je nach frage erhalte ich andere Antworten
- Diskrete Verteilung (24)
  - Verteilungen die ich zählen kann
  - Wenn ich 10 mal werfe kann ich 0-10 treffer haben (Zufallsgrösse)
  - Davon kann ich die Wahrscheinlichkeit berechnen
  - Wie gross ist die wahrscheinlichkeit dass du genau x mal triffst?
  - Die **normiertheit**, alle Wahrscheinlichkeiten summieren sich zu 1 -> TODO: look up
- Erwartungswert: mit der heueristischen idee (25)
  - Ich werfe einen Würfel 6'000 mal
  - Ungefähr 1'000 sechser sollte gehen.
  - Ab welcher Zahl sagen wir dass eine Frequenz zu hoch oder tief ist? und der Würfel ist nicht fair
  - Wenn ich die Augenzahl alle aufschreibe, was ist as arithmetisch mittel aller augenzahlen SUM(augenzahl * frequenz) / 6'000
  - Modellwelt: 1/6 ist die Wahrscheinlichkeit eine 1 zu würfeln, etc. -> Erwarungswert
  - Erwartungswert (Modellwelt) -> SUM(wahrscheinlichkeit * wert)/anzahl
  - Varianz ist TODO: look up
- Binomialverteilung (Zwei) Versuch mit zwei möglichen Ausfällen (26)
  - Zwischen Erfolg und misserfolg kennen wir je nach dem ob ein resultat korrekt sein kann.
  - Wie viel treffe ich, wenn das niveau bekannt ist (wahrscheinlichkeit), können wir spühren ob ein resultat sein kann
  - 
-
# 7 Stetige Verteilungen

- Nicht zählen sondern Messen, stetige Zufallsvariabel
- Es ist alles möglich, wir können nicht mehr exakt sagen wie wahrscheinlich es ist eine Zahl zu haben, weil zwischen min max gibt es unendlich Zahlen
- Normalverteilung geht in beide richtungen undendlich weiter
- Wie gross ist die Wahrscheinlichkeit wenn ich die Breite eines Tisches messe, dass ich zwischen 74-75 cm messe?
- Flächeninhalt zwischen 74-75 cm, Python rechnet das
- Normierung, flächeninhalt unter der ganzen Kurve ist 1
- Erwartungswert (mü), Integralzeichen (brauchen wir nicht)
- Varianz, (realisierung - erwartungswert)^2

### Normalverteilung (32)

- Alle messen (tisch-länge) etwa dasselbe, aber nicht identisch
- Machen wir ein Histogram
- Wieso ist es symmetrisch und wieso wie eine Glockenkurve? -> niemand weiss es genau, erfahrung zeigt, dass es so verteilt ist
- Was passiert wenn viele kleine Fehler **aufsummiert** werden?
- Wenn wir die Wahrscheinlichkeiten addieren, passiert etwas
  - 1 Würfel -> verteilung stetig
  - 2 Wüfel -> Glockenform
  - 3 Würfel -> Glockenform
- Wenn wir zufahlszahlen addieren, erhalten wir etwas dass aussieht wie eine Glauss'sche Glockenkurve
- Ist auch nur eine Approximation der realtät weil es ist möglich auch negativ werte zu haben, auch wenn es in der realität nicht möglich ist.
- Sigma -> Wendepunkt (zweite Ableitung 0) TODO: look up
- Distanz zwischen den zwei Wendepunkten ist die Standardabweichung
- Flächeninhalt unter der Kurve ist 1 -> muss daher noch normiert werden
- Es gibt keine Integralrechung für die Kurve, sie kann nicht genau berechnet werden sondern nur approximiert
- Hat eine breite und ein Zentrum (Kurve)
- Standardisierte Normalverteilung (34)
  - Zentrum = 0
  - Sigma = 1
  - Ist eine Standard normalverteilung
  - Brauchte man früher vor computer
- Transformation zur standardisierten Noramlverteilung -> **z = (x-mü) / sigma** wichtigste formel in statistik
- Quantil, ich weiss die Wahrscheinlichkeit und will wissen was der wert ist (39-40)
- 

## Statistische Tests 8 (43)

- H0 -> Null hypothese (H not in eng)
- H0 -> Wahrscheinlichkeit eine 6 zu würfeln, der rest ist egal
- Wie gross ist die Wahrscheinlichkeit für diesen Event?
- Berechnent der Flächeninhalt zwischen 2'107 bis 12'000 führ die Wahrscheinlichkeit -> p wert
- Grenze zwischen kann noch sein und ist unmöglich (kritischer Wert)
- (46)
  - Weil wir diskrete daten haben müssen wir noch 1 abziehen in der rechnung
  - Cummulative density function (`scipy.stats.binom.cdf`)
  - Statistischer Schluss kann immer einen Fehler machen. Es ist extrem unwahrscheinlich dass es eintritt aber nicht 0
  - Häufig mit 5 % verglichen, 5 % ist das signifikanz niveau -> 95% des ganzen von minus unendlich
  - Wenn beide grenzen dann 2.5 % eine seite und 2.5 % andere seite
  - Look at jupyter notebook 8.1.1

**Mögliche Fehler bei Tests**

- 48
  - H0 -> der Würfel ist fair
  - Signifikanzniveau -> prozentzahl ist Abhängig von der Anwendung, Politik hat 10%, Medizin 5%, etc.
  - Im zweifelsfall gehen wir nach zweiseitig signifikanz niveau ausser es ist ganz klar
- Fehler 1. und 2. Art (51/52)
    - Annahme und Ablehnung ist definiert
    - z ist im annahmebereich -> richtiger Entscheid
  - **Feler 1. Art** (51)
    - Corona Test: Ich habe kein Corona aber der test gibt an, *falscher Alarm*.
    - Annahme H0 ist korrekt, wissen es aber nicht
    - Per Zufall fällt der Test so aus dass wir im Ablehungsbereich (obwohl er richtig) -> Fehler
    - Wahrscheinlichkeit für den Fehler ist 5 % (alpha)
  - **Fehler 2. Art** (52)
    - Corona Test: Der Test gibt an ich habe kein Corona, aber der test gibt nicht an, *unterlassener Alarm*.
    - Wahrscheinlichkeit für Fehler ist beta (dunkel grau)
    - Man kann die gestrichelte Linie eruieren, kennen wir jedoch nicht
    - Häufig machen, wir gehen davon aus dass das beta zwischen mü0 und mü1 liegt.
- In zwei fällen machen wir einen Fehler, wie hoch ist die Wahrscheinlichkeit den Fehler zu machen.
- alpha und beta hängen zusammen, wenn ich alpha klein mache wird beta grösser
  - Um gleichzeitig Fehler 1. und 2. zweiter Art gleichzeitig zu minimieren müssen die anzahl messungen erhöt werden! 

## Prüfung von Erwartungswerten (53)

- Wir nehmen an, dass zwei Maschienen produzieren teilen
- Beispiel: Qualitätsmerkmal ist durchmesser von Kreide
  - Sind normalverteilt
  - Jede Maschiene hatte eine Produktion mit normalverteilung
  - H0: Ist mü1 gleich mü2, sind die mittelwerte gleich?
  - Stichprobe machen.
  - Nur der unterschied im mittelwert ist noch nicht aussagekräftig, wenn die Streuung miteinbezogen werden
  - Grosse Streueung -> aussage kraft vom mittelwert ist klein
  - Kleine Streuung -> aussage kraft vom Mittelwert ist gross
  - Ich rechne die distanz von gemessen und erwartet -> und setzte sie in relation 
  - Hypothetische Test:
    - Sind die stichproblen durchschnitte gleich
- Qualitätskontrolle -> Qualität is 1 / Variablitätl -> grosse variabilität ist schlecht
- 55
  - Im vertrag (legal) steht ein erwartungswert (mü) durchmesser kreide
  - Um zu schauen ob der Vertrag eingehalten wurde, nehme ich eine Stichprobe und messe den Durchmesser.
  - Ist der mittelwert aus den zwanzig messungen gleichgross wie das was im vertrag steht?
  - Stichproben wählen ist am schwierigsten
  - (gemessen - erwartet) / standarddiviation
  

- 56
  - Wieso sthet hier wurzel N?
  - Standard fehler des mittelwert
  - rapp.fhnw.ch -> apps von ihm
  - Stichprobemunfang * 100  -> aritmethische mittelwert ist stabiler um 10%
  - Wenn ich die genauigkeit des mittelwerts verdoppeln will muss ich die stichprobengrösse vervierfachen
  - t wie fest streut sich der Mittelwert
- **Student-t-Verteilung ist KEINE NORMALVERTEILUNG** -> sieht aber ganz ähnlich aus
  - Ich erhalte für jede stichproblengrösse eine andere t-verteilung
- 58
  - Grösser 2 oder kleiner 2 immer ablehnen (pi mal daumen)
- Jupyter 9.2.1
  - mü0 vertraglich abgemacht
  - s standard abweichung `ddof=1` degrees of freedom n-1 (nicht default)
  - `ttest_1samp` -> datensatz & `population_mean=mü0`

## Vertrauensintervall (62)

https://rapp.fhnw.ch/RAPP/MarcelSteiner/20_Vertrauensintervall/

- Kommunikation von Vertrauensintervall ist wichtig
- Jedesmal wenn wir einen Wert aus der Modellwert berechnen gehört der Vertrauensintervall hinzu, kann sehr schwer sein auszurechnen
- Wie sicher ist dieser Messwert?
- Unterer wert <= Echterwert <=oberer wert
- Beinhaltet der Vertrauensinterval den erwarteten werden
- Wenn der Wert drinn liegt, dann wir die Nullhypothese angenommen

## Stichprobenumfang (63)

- Wenn ich weiss wie viel der Prozess streut (s), dann kann ich nach N auflösen
- Hängt von sehr vielen Dingen ab, die ich nicht unter kontrolle habe aber wissen muss
- Das N ist sehr schnell gross
- Wir müssen entscheiden ob unsere Daten normalverteilt sind. Wenn sie das nicht sind, dann können diese Methoden nicht angewant werden.
- Das können wir schauen indem wir ein histogram zeichnen
- Wie sieht eine Normalverteilung aus? Wissen wir nicht.
- Nehmen ein histogram, machen ein kummulirtes histogram (66) -> 1 / 1+2 / 1+2+3 / etc. (geht auf ein hoch weil es auf das normiert ist)
- Ist das Integral -> sieht es S förmig aus? Sind wir nicht einig. Hier hat es einen teil der relativ gerade ist.
- 67 -> wird auf eine gerade gezogen (nicht linear) aussen wird fest gezogen, in der mitte gar nicht
- Jetzt gibt es ein Wahrscheinlichkeitspapiert -> jetzt können wir es rein plotten (68)
- 68 -> wenn unser datensatz ungefähr auf der geraden liegt, ist es normalverteilt!
- 68 -> Normal QQ Plot (Normal quantile quantile plot), was heisst es gerade?
- https://rapp.fhnw.ch/RAPP/MarcelSteiner/ -> QQ-Plot

- 69
  - Wenn die Daten nicht normalverteilt sind? Dann flicken wir sie!
  - Dann nehmen wir den `log(z)` dann funktionierit es meisten
  - Falls nicht dann die quadratwurzel


## Vergleich zweier Mittelwerte (70)

- 73 -> streuungen von zwei messwerten werden zusammengenommen
- Wir nehmen den test für den die Voraussetzungen erfüllt sind.
  - Sind die Stichproben normalverteilt?
  - Wir müssen mit p werten umgehen können
- 78
- 79 H0 sagt alle differenzen sind = 0
- Fragestellung, Irgendeinen Test, Dann Read the manual und sucht die richtige Python funktion, dann rechne es aus


## Fehlerquellen (86)

- 


# Prüfung

- 1 / 2 / 5 / 7 -> Vorallem statistische Tests

- Am Freitag im Mathematikzentrum, ein Helpdesk der bei Mathematischen Fragen helfen
- Auf der Seite keep it simple, nimm das einfachste mögliche Verfahren

