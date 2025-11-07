# Machine Learning

## Tag 1

### Übersicht Tag 1

- Supervised Learning
  - `X` Daten, `y` labels die wir schlussendlich predicten wollen
  - Preprocessing
    - Standardisierung
    - Encoding
    - Feature Selection
    - Feature Engineering (polynomisierung, etc)
  - Modell
    - eg. Linear Regression -> gibt eine Kontinuierliche Variabel
    - y-hat -> vorhersage
    - betas
  - Resultat
    - `y` neues
  - Metrik
    - hat eine kosten funktion die sagt wie gut die betas sind


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
  - Mean Absolute Error (alle fehler zusammengezählt) MAE 
    - -> Robust gegen ausreisser
  - Mean Squared Error (Summe aller quadrate) MSE 
    - -> nimmt ausreisser miteinbezogen und werden davon beeinflusst
  - Das sind standard metriken, es können auch custom sein, zb. ab 20'000 franken muss es genauer sein, etc.
- 45
  - Was sind die Kosten von unseren Parameter? -> gleich einer metrik
  - beta sind parameter und nicht die vorhersage
  - kosten meinen eigentlich dass es schlecht ist je höher
  - Schlechte betas hohe zahl (hohe kosten) das ist schlecht
  - was für ein fehler machen wir auf dem datensatz?
  - Kostenfunktion ist vergleich zu der gesetzten metrik parameterisiert mit den betas
- 47
  - Bei der Linearen Funktion ist die Kostenfunktion normalerweise der MSE die Kostenfunktion
  - Das wird normalerweise genommen, oftmals auch normalverteilt
  - sklearn hat das hard-coded
- 49
  - Metrk ist eine Zahl
- 50
  - Optimum wie wir die lernbaren parameter finden basierend auf einer Kostenfunktion und daten
  - Unterschiedliche algorythmen die unterschiedliche vorteile haben, meistens wird ein schneller verwendet
- 52
  - Jeder punkt auf der fläche ist eine andere gerade und jeder punkt sagt wie die kosten für diese kobination
  - Der tiefste punkt sind die besten betas -> kleinste fehler
  - Nicht bei allen modellen ist die kostenfunktion eine schüssel
- 53
  - Wo ist die Ableitung (steigung) null ist das beste beta
- 55: Gradient Descent
  - Andere optimierungs algorithums
  - iterativ, wir starten an einem punkt (zufällige betas)
  - wir haben am anfang eine zufällige linie
  - ist vielleicht noch nicht gut
  - Wir machen dann einen schritt in eine richtung -> neue lösung die leicht besser ist aber immernoch nicht gut
  - mit jedem schritt wird es etwas besser
  - macht das so lange bis wir zum minimum kommen
  - wir schauen wo es am steilsten runter geht, das funktioniert mit der ableitung
- 56
  - Analysis gibt die steigung der kosten funktion, mit mehreren variabeln muss mehrmals abgeleitet werden
  - Bei einer kurve ist die ableitung die tangente zu dem punkt
- 57
  - wir machen die funktion minus weil wir runter laufen wollen das "n" ist die schrittgrösse
  - es gibt verschiedene algorythem um eine lösung zu finden, wir nehmen normaler weise die die schneller ist weil wir sind am resultat interessiert und nicht am weg
- 58
  - Ist immer eine linie, weil es linear ist, andere modelle können auch ein krümmung lernen
  - Zwei features: ebene, kann auch keine krümmung lernen und sich mehr an die daten anpassen
  - die gefahr für overfitting ist kleiner bei linearen modellen als bei anderen weil sie starrer sind
- 61
  - 1:
    - lineare modell nimmt die lineare funktion an
    - wie wir das modell machen ist hard-coded weil es zwingend eine lineare formel nimmt
    - wir nehmen an das es eine lösung hat (die ableitung = 0)
    - nimmt meistens der MSE an (kann man aber auch leicht ändern) aber das ist meistens implizit mit definiert
  - 2:
    - betas
    - formel ist ausprogrammiert, die betas werden aus den daten gelernt
  - 3:
    - Gradient Descent, Analytisch mit dem minimum
- 64
  - genauigkeit der daten kann erhalten werden
- 65
  - Kategorische Features
- 66
  - Ordinal encoding
  - man hat einen text und will ihn in eine zahl verwandeln weil wir mit text nicht rechnen können
  - Zahl 0-n
  - 1 feature wird 1 neues feature, es sind kategorien aber NICHT eine ordnung (reihenfolge) oder unterschiedliche grössen
  - 3 kategorien 0, 1, 2
  - 1:1 feature aber ist nicht gut wenn es keine ordnung gibt, wenn es eine ordnung gibt kann es gut sein, so lange der die gaps zwischen den kategorien konsistent ist
- 67
  - One-hot-encoding
  - Auf einen n dimensionalen vektor
  - 3 Kategorien
  - 3 Vektorne [1, 0, 0] und [0, 1, 0] und [0, 0, 1]
  - Drei neue features 0 oder 1 an einer spezifischen stelle im vektor
  - 1 neues feature pro kategorie: ist besser wenn es keine ordnung gibt weil dann die hierarchy einen einfluss haben kann obwohl sie das nicht sollte.
- 68
  - Man will meistens keine Ordnung haben
  - Es ist auch möglich ein eigenes encoding zu machen mit domain knowledge
  - zb. 100 verschiedene Haus fassaden, werden auf 5 verschiedene eigenschaften gemapped, zb. Wert oder so
  - generiert hier 5 neue features, ist eine art expertenwissen einzubeziehen, aber ist natürlich sehr sensibel darauf das es korrekt ist
  - wenn wir die features von den kategorien mit ordinal machen, dann hat das dritte mit nummer 2 einen grösseren einfluss als 
  - `y = b0 + b1x1 + b2x2 ...` wenn x1 ordinal 1 ist und dann x2 ordinal 2 hat es einen grösseren einfluss, mit vektoren würde es nur einen einfluss auf das beta haben wenn es zu der kategorie gehört. Also fällen die parameter weg die sich gar nicht dazu bezeien

### Explizites Feature Engineering

- 73
  - Menge an gesammelten features, aus diesen gibt es ein neues feature, welches aber nicht in der reellen welt gesammelt wird.
  - Standard: z.b. aus der grösse des fisches können wir das volumen berechnen, das wäre dann hilfreich für das modell wenn es das gewicht schätzen will
  - In das feature engineering fliesst das expertenwissen rein, sodass man das richtige feature engineered wird
  - Man sagt dem modell teile der Kausalität sodass es es nicht alleine erraten muss. Also ein teil des learning wird abgenommen.
  - Es gibt so bessere Modelle
- Polynomielle Regression: x1, x2, (x1)^2, (x2)^2, x1*x2 (zu einem -n degree)
  - Man kann auch nur einen teil der berechnungen machen wenn sie so sinn machen, z.b. das volumen des fisches
  - Zuerst mit polynomien feature engineering, dann lienare regression, das ist ein neues modell 
- Code (poly_regression): 
  - skikit spezifisch: `sk.Pipeline` sagt, welche modelle es in welcher reihenfolge es macht
  - Jetzt hat es eine krümmung gelernt -> (x1)^2
  - Feature Space: Die features die in das modell gehen, es können variabeln drinn haben die engineert sind

### Modell evaluierung

- 79:
  - Auf den trainings daten ist es immer besser oder gleich gut
  - eher overfitting
  - Auf ungesehenen daten kann es schlechter sein, das ist ein grösseres problem
  - es kann die gewichtung eines feature vergrössern
  - das wichtigste ist jedoch ob es gut auf neuen daten ist
- 81
  - Random Forest ist am besten auf den trainingsdaten am besten, aber es ist krass overfittet auf neuen daten wird es komplett unbrauchbar sein
- 82
  - gleiche trainingsdaten, aber neue validierungsdaten andere fitts und es ist klar das random forest am schlechtesten ist
  - wird eigentlich immer auf neuen daten gerechnet, aber wenn die evaluierungsdaten sehr wenige sind oder viele ausreisser haben, kann das ergebnis verfälschen
- 86
  - Cross validation: trainings daten und dann validierungsdaten
- 87
  - Es gibt eine gefahr dass das modell durch das validierungsset nur durch zufall besser abschneidet
- 88
  - Zwei strategien -> noch ein weiteres test set
  - Oder grössere validation sets, dann aber weniger trainingsdaten...
- 89
  - train (training), 
  - validation (welches modell ist am besten), 
  - test (schauen ob es wirklich gut ist, bei daten die 0 einfluss haben), werden nie angeschaut
  - -> in der praxis am besten
  - wenn ein modell verworfen werden wegen einem test set, hat es einen einfluss auf das moell und muss weggeworfen werden und ein neues test set gesammelt werden
  - man kann auch auf ein validierungsset overfitten
- 90
  - "Herbei zaubern von test daten"
  - Wir möchten ein möglichst grosses validierungsset haben damit wir ein model nicht nur zufällig wählen
  - Einen trick das validierungsset zu vergrössern
  - K-Fold Cross Validation eine methodik
  - Alle daten sind validierung
- 91
  - 1, 2, 3, 4, 5 gelbes sind die validierungssets
  - Wir haben verschiedene arten von modellen
  - Ein model, zb. Lineare Regression trainieren sie 5 mal auf verschiedene teile vom Datenset
  - jedes model hat die validierungsdaten während dem training nicht gesehen
  - Dann werden die vorhersagen (von den verschiedenen modell arten verglichen, linear vs. polynom, etc) verglichen, wir wählen eine Modell art
  - Dann können wir die resultate der Modelle zusammen nehmen, oder eines auswählen oder wir können ein neues modell trainieren auf allen daten (keine validierungsdaten) weil wir es ja vorher validiert haben
- Hold-Out Cross validation -> train & validate
- K-fold corss validation -> gemäss 91
- 93
  - Komplex -> wie stark passt sich das model an? Wie flexibel ist es?
  - Sehr komplexes model & test schlecht -> overfitting
  - Sehr einfaches model beides nicht besonders gut -> underfitting
  - Also die komplexität richtig wählen
  - Model based view: Das model ist im zentrum, daten sind fix
  - Aber wir können nicht nur die modelle anpassen sondern auch neue daten erheben oder feature engineering
- 96
  - 1. Modell ist nicht gut es ist zu einfach, modelle sind tendenziell zu einfach
  - 2. Modell ist sehr gut auf test daten aber in der realität (neue daten) nicht. Modelle die overfittet sind, sind tendenziell komplexer
  - 3. Validierungsdaten sind schlecht
  - 4. Daten auf die seite
  - 5. Iterative über alle segmente, alles ist einmal im validierungsset, alles ist vier mal im trainings set


### Feature selection

- 98
  - nur ein teil der features werden genommen
  - macht es dem modell einfacher und das modell wird selbst einfacher
  - overfittet nicht auf zufällige features die nichts damit zu tun haben
- 101
  - grosse betas sind tendenziell eine indikation dass es overfittet ist

- 102 & 103
  - Die features müssen irgendwie standardisiert werden
  - Alle betas haben das gleiche lambda
- 102
  - L-1 Regularisierung
  - La Place verteilung
  - Wenn es ein sehr grosses beta ist, wird es durch diese kosten funktion bestraft
  - je grösser das beta desto höher die kosten funktion zusätzliche strafe in unsere kostenfunktion
  - lambda ist ein hyperparameter und wird nicht gelernt sondern von uns gesetzt. ist eine konstante
  - das modell sieht anders bei anderen lambdas
  - L-1 ist gut für feature selection, wenn ein beta nicht wichtig ist (feature) dann wird es auf null gesetzt schlussendlich
- 103: L-2 Regularisierung
  - Normalverteilung
  - betas sollten nahe 0 sind sonst wird es bestraft
  - Standardisierung ist quadratisch, wir machen wie vorher eine straffunktion dazu
  - Es wird dazu gezwungen kleinere betas zu nehmen
  - Zahlen unter 1 sind weniger streng bestraft bei L2 als bei L1
- 105
  - Standardisierung
  - Wie gross die betas werden hänge davon ab wie gross die gemessene daten sind
  - Wenn breite in meter und länge in cm dann hat die einheit einen einfluss auf die gewichtung obwohl es das nicht sollte
  - Also eigentlich die einheiten weg-werfen
- 106
  - Wenn standardisiert wird ist best practice alle einheiten losgeworden
  - z.b. wir rechnen es um so dass die werte vergleichbar sind, zum beispiel können wir grösse und geld nicht vergleichen
  - Wenn sie standardisiert werden, dann ist nur noch ein verhältnis übrig, dass nichts mehr mit den einheiten zu tun hat und sie können verglichen werden
  - die werte sind jetzt intutiv nicht mehr nachvollziehbar, die betas können auch nicht wirklich verstanden werden
  - Wenn die betas verstanden werden wollen, dann müssten wir noch viel machen, es geht nicht so einfach
  - Standard Scaler kann man als einen teil der pipeline vorstellen auch vor der regularisierung
  - Wenn standardisiert wird, muss dann der input des modells in der anwendung auch standardisiert werden
  - Achsen müssen vergleichbar werden
- 109
  - Wann standard scaler, ist wahrscheinlich keinen nachteil auch wenn wir es nicht benötigen aber die features sind dann nicht mehr interpretierbar
- 111
  - 1. Schränken die betas ein, das modell wird einfacher
  - 2. overfitting risiko weniger gross
  - 3. Einheiten entfernen sodass die achsen der features vergleichbar sind, das modell ist nicht abhängig von den einheiten der features
- 112
  - Es gibt noch weitere Hyperparameter als lambdas, zum beispiel lambdas und polynom grad
  - werden von hand gesetzt
  - z.b. wenn wir lambdas hoch machen dann müssen die betas näher bei null sein, wenn sie tief sind, ist es weniger "konfiguriert", weil das modell mehr freiheiten haben weil grosse betas nicht so stark bestraft werden
- 114
  - Manuell nach best practice ist fehleranfällig, aber wenn die rechen-kapazität nicht existiert
  - Suchen: wir versuchen verschiedene lambdas aus und dann schauen wir was am besten ist
- 115
  - Grid Search -> annhäherung, meistens nicht so gut wenn wir mehrere hyperparameter haben, weil alle kombinationen getestet werden müssen


## Tag 2

### Classification in Supervised Learning

- 123
  - Menge von vordefinierten klassen (kann auch binär sein)
- 124
  - Iris datensatz als beispiel
  - Blumenart basierend auf massen der blütenblätter
  - Output space muss keine achse sein, sondern jetzt kann es farbig sein, da es klassifikation ist
  - Kann auch durch lineare regression gemacht werden, es ist eine gerade
  - hier sind die massen standardisiert (fehler es steht im cm)

### Lineare Regression

- 125
  - Auch wenn es regression heisst ist es eine klassifikation in ML language
- 126
  - Data Specification -> Auswahl (127)
  - Model -> ist in sklearn im fit drinn
  - Kostenfunktion -> definiert
- 129
  - Wir wollen das Lineare Modell nehmen (wie Tag 1), eigentlich werte zwischen -unendlich und + unendlich
  - Die formel muss modifiziert werden zwischen 0-1 -> ist die Wahrscheinlichkeit einer klasse
  - Wird mit der Logistischen Funktion (sigmoid) gemacht (`e` -> Eulerische Zahl)
  - Die genau an 0 oder 1 eine Annäherung
  - `sigmoid(Lineare Modell)` -> zuerst nehmen wir das resultat vom modell, dann wird es in die formel rein gesetzt das ist das `z`
- 131
  - y-hat -> die klasse die wir vorhersagen, dann ist es normalerweise wenn es mehr 50 %
  - Es sind so wenige werte die genau 0 sprich 50% kommen können, dass es besser ist sich für etwas zu entscheiden als einen fehler werfen
  - können das Modell erweitern dass es einen spezifischen wert vorgeben bei dem das modell nichts vorhersagt, wenn unsicherheit wichtig ist
  - wir können auch sagen, dass wir schon bei 20% sagen dass es schon true ist, anpassung an use case
- 132
  - beta kann auch negativ sein, daher können auch bei viel variabeln kleine `z` raus kommen
- 133
  - Weil wir den output farblich dargestellt wird, können 3 features 3-Dimensional dargestellt werden
  - Ein feature wird einfach auf einer achse angezeigt -> eine linie
  - 3 features ist eine fläche
- 135
  - Metrik -> fehler für jeden einzelnen Datenpunk
  - die unterscheidung kann relevant sein in gewissen use-case
- 137
  - Die resultate vom modell
  - Können die resultat von den Trainings oder Validierungs Daten machen
  - Wenn es schon auf den Trainingsdaten fehler macht ist es vielleicht zu starr
  - Wenn es die auch auf den Validierungsdaten macht ist es vielleicht overfittet oder so
  - Gute Darstellung für die Fehler, viele kategorien gut dargestellt
  - Keine Metrik weil es immer fehler von daten punkt, es ist nicht immer aussage kräftig ob ein modell besser ist als ein anderes
- 138
  - Accuracy -> sehr einfach
    - 9 mal korrekt von 10 (9/10) -> 90 % genauigkeit
    - Wird oft verwendet weil es ist intuitiv sehr verständlich
  - wenn wir von einem fall viel mehr beispiele haben als von einem anderen ist diese aussage nicht sehr gut
- 139
  - F1-Score
    - Harmonische Mittel, Binär -> mittel von den zwei Zahlen
    - Precision -> True positive / (true positive + false positive) -> echter positive / alle guten + alle die falsch gefunden wurden
    - Recall -> True positive / (true positive + false negative) -> echte positive / alle gute + alle falschen nicht gefundenen
    - F1 ignoriert 
- 141
  - weil eine klasse so viel öfter vor kommt ist dieser score sehr hoch obwohl das modell sehr schlecht ist
- 143
  - Kostenfunktion (Maximum Likelihood)
  - Man nimmt an dass die Wahrscheinlichkeiten unabhängig sind (ist in der praxis nicht immer so), wenn man das nicht annimmt kann man nichts machen
  - hier will man einen wert möglichst nahe bei 1
  - xi (feature) sind beobachtete werte
  - Produkt symbol (wie das summen symbol)
  - Positive Sample -> eg. alles spam mail
    - Wahrscheinlichkeiten für einen datenpunkt multipliziert mit den wahrscheinlichkeiten der restlichen datenpunkten
  - Negative Sample -> eg. alle keine Spam mail
    - 1 - (Wahrscheinlichkeiten multipliziert)
  - Beide Produkte werden auch miteinander multipliziert
  - Resultat is wie wahrscheinlich sind die labels die ich habe und unserem modell
  - je mehr datenpunkte desto näher geht er gegen 0, aber wenn man sie auf dieselben daten anwenden dass sind sie trotzdem vergleichbar
  - Mit gradient descent wird negative maximum likelihood
- 145
  - Weil es auch linear ist, haben wir immernoch ein minimum
- 147
  - Gradient ascent wäre auch möglich aber es hat sich eingebürgert, dass man einfach negative gradient descent macht
- 148
  - Für die nummerische stabilität nehmen wir noch den logarithmus, ist ok, weil es das minimum nicht verändert
  - Logarithmus von multiplikation macht es daraus additionen, von der theorie kommt das selbe raus, ist im kommputer besser, weil wir haben floating points und irgendwann wird das ungenau auf dem computer, addition ist bisser addieren ist stabiler im computer
- 149
  - Softmax ist wenn wir mehr klassen haben
  - wahrscheinlichkeitsverteilung über alle klassen
  - `x` kommt ins modell -> drei wahrscheinlichkeit für alle drei klassen
  - `K` beim summenzeichen sind die anzahl klassen
  - Der term macht dass es über alle klassen loopt
  - beweis für die ite klasse -> drei modelle wie wir es vorhin hatten
    - `z1` ist ein lineares modell
    - `z2` ist ein anderes lineares modell
    - `z2` ist ein drittes lineares modell
    - Statt die sigmoid funktion um einen wert zwischen 0-1 erhalten nehmen wir eine andere funktion
  - `i` ist der index des modells und `l` ist der index der klasse
  - Predicten zwischenergebnisse -> diese individuellen ergebnisse müssen in eine Zahl umgewandelt werden weil wir wollen am schluss eine zahl
- 150
  - Es sind zwar drei lineare modelle aber sie werden zusammen trainiert weil sie über den soft max verbunden weil sie alle zusammen immer 1 geben müssen
- Code: `slides/code-examples/classification/logistic_regression.ipynb`
  - Evaluierung auf test daten sollte gut sein, weil es hat sie gesehen
- 152
  - Es ist nicht für alles geeignet wenn die daten nicht mit einer geraden von einander getrennt werden können kommt nichts sinnvolles raus
  - Vielleicht ist es möglich mit mehr features die klassen noch mehr unterscheiden
  - Feature engineering wäre möglich (polynome feature engineering (rot umrandetes bild))
- Statisk -> wir machen annahmen über eine perfekte welt, LM wir schauen was am besten passt aber wir machen keine annahmen die wir prüfen
- 156
  - 1. Fixe Gruppen, zuweisung zu einer Gruppe (im vergleich zu clustering das gruppen selbst findet)
  - 2. Annahme, dass es eine dieser Gruppe ist, wie die betas verwendet werden ist lieanr, das lineare modell ist drinn. Es hat eher eine tendenz zu underfitting. Resultat ist zwischen 0-1 (bei 2 betas), ist eine wahrscheinlichkeit.



### K-Nearest Neighbour

- 165
  - Curse of Dimensionality -> Raum wir riesig bei vielen Achsen (Features), dann machen distanzen nicht mehr so viel Sinn
  - Andere Modell lernen besser die Features zu gewichten K-Nearest Neighbour kann das nicht

### Support Vector Machine

- 170
  - Binäre entscheidung
- 173
  - Kosten funktion geht nicht likelihood weil wir keine likelihood vorhersehen
- 175
  - Das ist eine Annahme um das beste modell zu wählen
  - geometrische intuition
  - geht in n dimensionen
  - position boundary und dann eine margin + / - von der position boundary, support vektoren sind die punkte die die position boundary entscheiden
- 177
  - beta ist ein vektor, der ist normiert und ist 1, sonst kann M unendlich werden
- 183
  - HARD-MARGIN -> wenn es daten gibt die nicht richtig passen, dann gibt es keine lösung
  - darum soft margin
- 184
  - bei jeder variabel darf die margin ein wenig abweichen um einen "cheat" wert (zeta)
  - aber wir müssen sagen, dass in der summe möglichst wenig verletzt werden
  - wenn C sehr gross ist dann wird cheating minimiert (stärker bestraft) und umgekehrt, das sind hyper-parameter wenn ich C kleiner mache kann die margin grösser werden und mehr datenpunkte verletzten die margin
  - Cheating darf nicht negativ sein, man darf nur in die selbe richtung cheaten nicht bei einer positiv und bei einer anderen negativ
  - Es gibt immer eine lösung, aber es kann sein, dass das cheating relativ gross sein muss um eine lösung zu haben
- 185
  - alle daten punkte verletzten der margin und sind sogar falsch klassifiziert, aber sogar die die korrekt sind, können den margin verletzten
- 186
  - beeinflusst auch den winkel der geraden da bei jeder margin das optimum anders sein kann
  - C gross, wir passen das modell stark auf die einzelnen daten and bei klein generalisieren wir es mehr
- 187
  - Keine wahrscheinlichkeit bei mehreren klassen ist nicht möglich
  - es ist möglich mehrere modelle zu trainieren kann aber schnell gross werden bei mehreren klassen
  - logistische regression ist meistens besser


### Kernel Trick

- Normal: Wir loopen über anzahl features
- Kernel Trick: wir loopen über anzahl daten

- 193
  - kann man mit jedem modell machen
  - ist vorallem effizient von support vector machine
  - in den meisten fällen wir ein indirektes feature engineering
  - feature engineering gemacht hätten. Aber es springt direkt zur lösung.
  - Es kann sein dass es rechnerisch besser ist mit kernel trick zu arbeiten als feature egineering
  - Wir wählen immernoch den Kernel, der dan die art des feature engineering macht
  - Implikation ist, dass wir nicht das neue feature "materialisieren" (explizit machen)
  - mathematisch ist es nicht ganz dasselbe alber in der praxis hier ist es gleich genug
- 194
  - Representer Theorem wird angenommen
  - weil es über alle trainingsdaten looped ist es nicht effizient bei einem grossen trainings-daten set
  - so lerne ich die alphas statt betas
  - weil die lernbare parameter ist nicht mehr von den anzahl features sondern anhand der datenpunkte abhängig
  - wenn wir mehr features als datenpunkte haben als features (das ist seltener im vergleich zu mehr daten wie features)
- 197
  - RBF kernel -> oft genommen, wie ein smoother k-nearest neighbour, weil nicht nur k nächste sondern alle datenpunkte
- Bei SVM müssen wir nur über die support vektoren loopen die einen einfluss auf das modell haben. Diese support vektoren finden wir über das erste triaining


### Decision Tree

- 199
  - ist für viele probleme sehr erfolgreich
  - ist üblicherweise binär
- 201
  - Nichts muss standardisiert werden
- 203
  - die features werden in regionen aufgeteilt, innerhalb der region wird 
  - alles was in der region ist wird tendenzeiel vorausgesagt
  - keine schräge schritte weil es dann kein baum mehr ist
  - Dann haben wir zwei neue regionen, dann kann dort nochmals unterteilt werden
  - funktioniert auch in n dimensionen
  - wo es den cut gibt wird vom learning algorithmus entschieden
  - das kann undendlich gehen, dann ist es auf dem trainings set 100%, kann aber extrem overfittet sein
  - normalerweise abbruch bedingung
  - wir zerstückeln so lange wir unreinheiten haben
  - ist auch möglich nachträglich der baum aufgeräumt wird so dass es nicht overfitting ist
  - Es macht nur einen neuen cut wenn es etwas unterteilen kann
- 204
  - dann schauen wir die wahrscheinlichkeit für eine entscheidung -> blaue region -> 100% blau
  - in einer anderen region ist es vieleicht gemischt, dann ist wahrscheinlichkeit für x gemäss anzahl von klasse und dann geteilt durch anzahl punkte in region
  - das wird für jede klasse in jeder region gemacht
  - die prediction für diese region ist die wahrscheinlichkeit x%
  - wenn wir abbrechen bevor es 100% akkurat ist dann müssen wir eine wahrscheinlichkeit nehmen in der region
  - daran kann aber geschraubt werden
- 206
  - Wie können wir die kostenfunktion nehmen, wir müssen wissen welcher baum am besten ist, es haben alle dieselbe abbruch bedingung. Einfach andere bäume unter denselben konditionen
  - Verunreinigung in einer region, dann werden diese summiert und durch alle punkte
  - welche formel genommen wird ist ein hyper parameter
- 207
  - wie finden wir den richtigen cut?
  - theoretisch gesehen gibt es einen idealen baum, ist aber sehr rechenintensiv
    - Das machen wir nicht.
  - Praxis
    - Suchen guten baum mit greedy-algorithums, der die kostenfunktion gut minimiert
    - Ich schaue was ist im moment die beste lösung, dann gehe ich weiter. Der cut wird später nicht mehr hinterfragt
    - P-Hard wenig rechenzeit
    - Ist vielleicht nicht so schlimm, dass wir nicht den besten nehmen weil wir sonst vieleicht auf die test daten overfitten
  - Die möglichen cuts sind immmer in der mitte zwischen zwei punkten.
- 212
  - ebenen müssen auch rechtwinklig sein
- 213
  - ensemble: mehrere Modelle und nehmen den durchschnitt der individuellen vorhersagen als unsere endgültige vorhersage (als einfachste version)
  - die modelle müssen nicht derselben art sein
  - random forest sind mehrere decision trees
  - die interpretierbarkeit geht verloren weil es zu viele komponenten hat
  - Bagging -> ensemble mit allen modellen gleicher art
- 213
  - ein split ist immer auf einem feature gemacht, daher sind sie robust bei vielen features, weil diese den cut einfach nicht beeinflussen
  - es ist weniger anfällig aber es können natürlich auch features geben die einen negativen einfluss haben
  - in regression, bekommt jedes feature ein beta auch wenn es keinen einfluss haben sollte
- 216
  - Meistens sehr gut auf strukturierten daten, vorallem als ensemble
  - Klare limite
  - ist eine regressions task (sinus kurve), hier hat es ein globales muster
  - sobald wir ausserhalb der gemessenen daten sind, ist es sehr schnell sehr schlecht
- 219
  - 1. feature grösser gleich oder kleiner gleich -> gibt ein spezifisches resultat, regionen links und rechts davon
  - 2. Ja, aber nur sinnvoll wenn der optimale cut horizontal oder vertikal ist
- 220
  - Modelle, Preprocessing und Feature Engineering nur auf den trainingsdaten entwerfen und trainieren


## Tag 3

### Unsupervised Learning

- Keine zugehörigen outputs, nur daten und wollen etwas machen

#### Clustering

- 228
  - Bei der Klassifikation geben wir die Gruppen vor
  - Gruppen in Daten, finden sie selbst
  - Wir wissen auch nicht was ein cluster überhaupt ist
  - Das müssen wir später analysieren um zu verstehen was da überhaupt drinn ist, kann sein, dass es gar keinen sinn macht
  - k-means Algorithm
- 229
  - Suchgergebnisse die Zusammengehören werden gruppiert und werden zusammen angezeigt
  - Von der Forschung hatten sie daten von gesichter, hat gelernt personen zu erkennen (ungefähr)

#### Dimensionality Reduction

- 1 Dimension -> 1 feature
- Anstatt jeden Datenpunkt mit drei Features zu beschreiben, wollen wir nur noch zwei features haben die sinn machen
- 2D-Manifold -> ist eine 2D ebene die im 3D raum abgebildet ist
- Informationsverlust, aber die die man wegnimmt ist nicht so wichtig
- Manifold-Annahme: wissen nicht ob es für die Daten stimmt, eg. Bilder mit vielen Pixeln, liegen eigentlich auf einem tieferen manifold
- 233
  - 3 farb kanäle -> 3072 features 1 pro pixel und 3 für farbkanäle
  - Mit 3072 features können wir viele Daten räpresentieren, die in der echten welt gar nicht vorkommen also können wir etwas weg nehmen
  - Wir versuchen die 3072 auf weniger features reduzieren die aber die Daten präzieser beschreiben (ein feature sagt mehr aus als eines vorher)
- 234 Encoder -> reduktion von features (sind auch ML modelle)
  - Wir verwenden Machine Learning um die features zu reduzieren um ein ML zu trainieren oder für visualisierung
  - Wörter original sind immer gleich voneinander entfernt, macht keinen sinn, dann encoder die es mehr gruppieren so dass es näher ist
  - Die Features die raus kommen sind gelernte features, es hat kein natürliches label für uns, wir verstehen eigentlich das resultat des encodings eigentlich nicht
- 235
  - bei dimensionsreduktion braucht es keine labels, daher können z.b. mehr bilder gelernt werden und dann auf weniger gelablede bilder reduziert werden dann hat es ein supervised model einfacher
  - Motivation: anzahl info auf wesentliche features reduzieren, feature engineering macht tendenziell mehr features
  - Obwohl die dimensionality reduction auf den daten gelernt wird, wollen wir sie meistens auf nur auf die eigenen daten anwenden. Darum wird es nicht in training, validierung und test getrennt, weil man z.b. alles visualisieren will. Das resultat wird dann einfach genommen wenn es sinnvoll erscheint
- 238
  - kann sein, dass wenn es zu viele features hat, das es overfitted (gibt einem pixel zu viel gewicht). Mit weniger features ist das fitting eventuell besser
- Encoder kann auf allen daten die wir finden trainieren, keine labels, lerne nur bilder anders zu räpresentieren. Und dann kann ich ein encoder auf daten verwenden die labels brauchen.
- 240: Feature selection ist eine dimensionsreduktion, kann aus einer reduktionssicht sehr dumm sein, weil das was übrig ist, nicht mehr viel wert ist. Muss aber nicht, weil es features gibt die noise sind
- 241
  - Rote Gerade ist das neue feature, räpresentiert die original daten besser als wenn wir ein feature entfernen
  - Muss nicht zwingend eine Gerade sein
  - Haben immernoch informationsverlust
  - Bei Linearer Regression minimieren die square (vertikale linie), aber hier minimieren die distanz rechtwinkling zu der geraden, was feature loss minimiert. Andere Motivation als lin. reg. Da ist vorhersage hier ist kombination, daher andere optimierung

- **Principal Component Analysis (PCA)** 243 ist ein
- 244:
  - Keine zielvariabel sondern nur features
  - Encoding: eg. Texte
  - Nummern müssen mit standard scaler standardisiert werden
- 246
  - 1. Hauptkomponente: die achse die am meisten streuung erklärt
  - 2. Hauptkomponente: die nächste achse die am meisten streuung erklärt (ist rechtwinklig auf der 1.)
  - -> neues koordinaten system für pc1
- 247
  - Nach rotation nehmen wir die wichtigsten feature raus, und nehmen die zweite weg, also eigentlich feature selection
  - Man macht immer alle hauptkomponenten und werfen dann weg. Wir geben die hautpkomponenten vor
- 248
  - Macht einen matrix multiplikation (lineare transformation)
  - Wir machen immer eine rotation der daten
  - matrix ist 3000 mal 200 gross dann kommt 200 raus
- 250
  - kommt mit decoder -> macht die ursprünglichen features aus den reduzieren wiederherstellen
  - Das resultat ist ein wenig unscharf weil es info verloren hat
  - Bild nehmen encoden und dann decoden mit matrix transposition
- 251
  - Wie viele streueung bleibt erhalten bei anzahl haupt komponenten -> verliefen 10% streeung wenn wir auf 200 features gehen
  - Wie viele Hauptkomponente es waren wieder zurück ins original
- 253
  - Wenn wir 200 pixel auswählt statt PCA dann bewahren wir nur 9.3% der info mit PCA bewahren wir 94.4% der streuung
  - hier zeigt es das feature selection in diesem fall sehr dumm wäre
- 254
  - Kostenfunktion ist bei PCA immer dieselbe -> L2 distanz -> squared error der rekonstruktion
  - J(W) = (ursprünglichen bilder (jedes Pixel) - rekonstruktion der Bilder (jedes Pixel))^2 dann aufsummiert
  - Die W die minimal sind nehmen wir, das sind die hauptkomponenten
  - PCA ist so definiert dass es L2 distanz ist, wenn man eine andere Kostenfunktion wäre, wäre es nicht mehr PCA einfach ein anderer Algorithmus
- 257: Optimierung ist lineare algebra
- 258
  - Nicht linearer Zusammenhang geht nicht
  - Swiss Roll funktioniert mit PCA auch nicht weil es eine gerade rein tut
  - sehr gut wenn es linear ist, aber es ist nur gut wenn es linear ist
- 259
  - Sollte nur für Performance genutzt werden (eg. wenn wir einen algorithmus haben der sehr langsam ist)
  - andere dimensionsreduktionen können gegen overfitting genutzt werden aber PCA weniger
- Wenn die daten linear sind, dann ist es die optimale wahl, aber viele Daten sind halt nicht linear. Nicht lineare modelle overfitten eher als dies
- Manifold ist schon eine annahme die vielleicht auch nur halb wahr ist
- Aber die annahme dass sie noch linear ist, ist noch eine extra annahme die vielleicht nicht stimmt

Code (Slides/pca):
- n_components: man kann sagen wie viel prozent streuung wir haben wollen, es schaut selbst wie viele komponenten es braucht
- hier sind 90% streuung sind 31 PCA von 64 features (slide 251 hat die kurve analysiert)
- optimierung ist nicht enorm rechenintensiv
- Üblicherweise wird meistens 90% gemacht


#### Non-Negative Matrix Factorisation (263)

- Pixel ist es gegeben
- speziell, dass sie nur positiv sein dürfen
- einheitliche grösse haben (wenn alle features pixel sind, ist das auch gegeben). Wir können nicht standardisieren, weil es hier negative werte gibt. Also einheitlich aber nur positiv
- 267
  - Intuition, Möchten Matrix A und B lernen, sodass wenn ich A*B rechne kommen ungefähr unsere daten raus
  - wir wählen A und B so, dass A*B möglichst nahe bei X ist
  - Die anzahl features wird von uns definiert
  - Bedingung beide Positiv -> also X (unsere Features) muss auch positiv sein
  - B ist der Decoder
  - k ist kleiner als anzahl features, aber dieselbe anzahl samples
- 268
  - wir haben keinen encoder, wir lernen direkt unsere reduzieren features -> lernen A und dann lernen wir B
  - weil wir keinen encoder haben, können wir es nicht nochmals auf andere daten anwenden weil A direkt gelernt ist
  - Nicht als pre-processing geeignet
  - Wenn wir eine pipeline zweimal laufen lassen, dann rechnet es NMF neu aus, wir können nichts verwenden dass es vorher gerechnet hat. Also keine gute idee für pre-processing
- 269
  - PCA sehr schwer zu verstehen was ein feature genau macht weil es immer im zusammenhang mit anderen features verstanden wird
  - NMF: die reduktion ist einfacher verständlich (die gelernten features) weil es alles positiv ist
- 271
  - selbe Kostenfunktion wie PCA aber die rekonstruktion ist A*B
- 273
  - zufällige werte (klever zufällig)
  - Coordinate-Descent -> zuerst A dann B, etc.
  - Wenn sich A verändert muss ich B verändern
  - darum optimiere ich A, ich verändere A mit dem gefixten decoder
  - Dann wchseln, ich verändere B und halte A fix
  - Lokales minimum, ist vielleicht global nicht die beste lösung

- K-means geht in die richtung von der struktur, cluster zugehörigkeit mit fixen schwerpunkt, dann neues cluster zentrum, etc. Auch coordinate descent

- 275
  - 1. Wir gehen von 100% info auf ungf. 90%, weniger features mit möglichst viel variation erhalten
  - 2. 
    - Ich identifiziere die hauptachsen mit meister streuung (info)
    - dann nehme ich die anzahl hauptachsen wie ich will
    - Nimmt linearität und manifold an
  - 3.
    - Nicht negative
    - wir können neue datenpunkte nicht mappen weil es immer nur auf die existierenden daten sinn macht
    - wird viel in NLP verwendet bei vielen wörter und dann nachher clustering gemacht werden soll
  - Gemeinsamkeit
    - gleiche kostenfunktion
    - das modell funktioniert aber anders


#### Deep Learning (277)

- Grosses Teilgebiet von ML
- Wenn das Model ein neurales Netz ist spricht man von deep learning
- bei vielem steckt DL dahinter
- 279: Vorher
  - model geholfen mit feature engineering und dimensionality reduction und dann ML
  - Früher auch mit bilder / text, etc wurde das gemacht
  - Vor deep learning waren die approaches nicht sehr erfolgreich
- 280
  - Motivation bevor wir wussten dass es sinnvoll ist
  - Aufwand räpresentation soll irgendwie automatisch gelernt wird
  - können einfache symbolische regeln lernen (wie zum beispiel was ist ein onkel in einem Stammbaum)
  - Kann immer wie abstrakter werden für eine vorhersage
  - Decision trees, machen eher interpolation, keine gloable muster ausserhalb der daten
- 281
  - Ohne annahmen geht es nicht, wie es lernen soll muss bestimmt werden
  - Viele Daten für ein modell ohne overfitting
- 282
  - Unstrukturiert bedeutet dass ein einziges feature sehr wenig aussagt (ein pixel sagt nicht viel)
  - Bei strukturierten Daten sind sie mieistens nicht die beste wahl (empirisch belegt)
- 283
  - Biologische Gehirn ganz anders wie heutiges NN

#### Fully Connected NN (284)

-> linear + liner neben und nacheinander + nicht lineare aktivierungsfunktion
layer für layer ist alles mit allem verbunden horizontal

- Das üblichste
- 268
- Spezifikation:
  - Kostenfunktion immer vorgeben, idee ist dass diese verändert werden kann
  - Features: Was kommt in das modell rein
  - Encoding (eg. Text muss in Zahlen gemacht werden)
  - Standardisiert (weil gradient descent)
  - Arbeiten mit Gradient Descent
- Model (288) (kein neurales netz)
  - Die formel ist das lineare model
  - so würde die regression als graph aussehen
  - Der pfeil ist das beta
  - letzter knoten ist die summe
- Idee: 289 (noch kein neurales netz)
  - Wir fügen zwischen input und output layer ein neues layer hinzu (hidden layer)
  - Hidden layer sind eigentlich wie zwischenergebnisse
  - Von den knoten im hidden layer gehen wir zum output
  - Im fully connected NN sind alle x mit allen z verbunden (x0 und z0 sind die bias)
  - ein pfeil räpresentiert ein beta, die sind alle unterschiedlich
  - die anzahl von x ist nicht zwingend gleich wie die anzahl von z
  - Es sind wie mehrere lineare modelle nebeneinander und hintereinander
  - Das hier könnte man immernoch umschreiben in mathe um ein lineares modell machen also noch kein NN
- 290
  - Wir summmieren alle inputs in z und kreieren eine aktivierungsfunktion
  - gibt unterschiedliche Aktivierungsfunktionen, muss gewisse eigenschaften haben
  - **ReLU** -> wenn input negativ ist dann gebe ich 0 weiter sonst, funktioniert gut
    - Input: -5 -ReLU -> 0 weiter
    - input: 5 - ReLU -> 5 weiter
    - Kann auch umgekehrt sein, es kann auch sein dass es alle positiven auf 0 setzt (beta wir angepasst)
  - Man braucht irgendetwas dass nicht linear ist
  - binary step funktioniert nicht so gut
  - Es gibt viele weiterentwicklung von ReLU
  - Es muss nicht überall die gleiche Aktivierungsfunktion haben. Zum beispiel bei klassifikation wollen wil 0 / 1 haben, im zwischenlayer aber kann es ReLU sein wo die werte anders sein können
  - Normalerweise sind die Aktivierungsfunktionen pro layer gleich
- 291
  - Die logistische regression ist ähnlich wie die aktivierungsfunktionen in NN
- 292
  - Gute an NN ist das mehrere vorhersagen problemlos hinzugefügt werden beim gleichen input
  - in der theorie sollte noise features keinen einfluss haben
  - aber in der praxis lernt es dann komische zusammenhänge -> overfitting also auch feature selection ist relevant
  - wir können recht viel konfigurieren, input / output ist fix, aber layer, anzahl neuronen, aktivierungsfunktionen kann überall daran geschraubt werden
- 294 (wichtige slide)
  - DL kann sich wie vorgestellt werden dass wir ein modell konfiguireren können sehr komplexe architektur
  - mehr layer -> mehr betas -> kann sich stärker anpassen ist mächter aber auch einfacher overfitting
  - wenn wir sehen dass es overfittet, können wir das modell
  - Fixe architektur, anzahl layer, anzahl knoten pro layer sind von uns vorgegeben, nicht vom modell!
  - Beim training lernt es nur die betas (gewichtung)
  - Mehr layers -> meistens ist es besser mehrere layers hinzuzufügen als mehr nodes pro layer
  - Kostenfunktion 
    - muss ableitbar sein für gradient descent
    - Wird problemspezifisch gewählt
    - kommt auf die funktion darauf an (regression -> squared error, etc.)
- 295
  - Hidden layer kann wie ein gelerntes feature engineering  (10 features mach 100 knoten im hidden layer)
    - oder kann auch als gelernte dimensionsreduktion gesehen werden (100 features auf 10 im hidden layer)
  - PCA hat möglichst wenig info weggeworfen, aber vielleicht hat es etwas weggeworfen dass bei diesem ziel wichtig wäre, weil es ist in isolation gemacht wurde
  - Hidden Layer wirft weg was es sieht dass für dieses problem output nicht wichtig ist
- 297
  - Google hat zusätzlich versucht zu verstehen bei welchem input bild welche nodes angehen
- 299
  - Kostenfunktion
  - man muss es immer sagen
  - aber es gibt klare kostenfunktionen bei verschiedenen mathe vorgehen
  - kann natürlich auch eine eigene machen, zum beispiel wenn überschäzten schlimmer ist wie unterschätzen
- 301
  - Gradient Descent aber ist es nicht so einfach weil es unterschiedliche minimum hat -> Lokale minimum
  - unterschiedliche lösungen je nach dem wo ich starte
  - mehrfach starten ist eine möglichkeit um das beste minimum zu finden, macht man bei NN in der praxis nicht weil es zu lange dauert (teuer)
  - lösung in der Praxis, das lokale minimum akzeptieren, es hat sich mit grösseren netzwerken herausgestellt, dass es nicht schlimm ist wenn wir nicht das globale minimum gefunden haben
  - wenn ich viele parameter habe und viele richtungen wo das minimum ist, ist das lokale minimum gut genug
  - weil wir es nur 3-d anschauen sieht es dramatischer aus als es in der praxis ist
- 302
  - Z.b. wenn wir mean square error rechnen, dann müssten wir über alle unserer Daten iterieren (alle y and y predicted) ist sehr blöd wenn wir um 1 beta verbessern wollen (1 schritt) dann müssten wir über eg. 1 Mio. Daten iterieren.
  - Anderes Extrem: Stochasitc Gradient Descent nimmt nur ein beispiel
  - Normalerweise nimmt mini batch (ein sub-sample) um die funktion zu berechnen (kompromis)
  - In der Praxis geht man immer einmal über alles, es fängt von vorne an und nimmt dann den nächsten batch
- NN werden mit Mini Batch Gradient Descent gemacht
- 304
  - Ist ein algorithmus der den gradient effizient berechnet
  - wir fangen hinten
  - Backpropagation geht bei jeder Kostenfunktion
  - wird immer mit backpropagation gemacht
- 305
  - Man trifft immer annahmen um das lernen vereinfacht wird aber es soll flexibel sein

- 307
  - 1. Zwischenergebnis, Feature Engingeering oder Dimensions Reduktion
  - 2. Aktivierungsfunktion -> transformierung vom wert, was passiert in einem knoten bevor man den Wert weitergibt
        ReLU hat sich als gute gezeigt

- 308
  - Pitfalls, wann benutze ich was?
  - sklearn user guide ist ein wenig zu einfach
  - muss das modell am schluss interpretierbar sein? oder kann es eine black box sein? Im medizinischen bereich kann es sein, dass das modell nachvollziehbar sein muss
- Vorgehen
  - Gibt es ähnliche probleme? Haben andere erfahrungen? Was haben die gemacht?
  - bei strukturierten daten ist feature engineering oftmals einfacher weil es klare kategorien hat
  - weil es bei strukturierten daten hat es weniger daten da sind fehler viel schlimmer
- Transfer Learning: Nehmen betas eines existierendes Modell und trainiert es weiter mit eingenen kleineren daten (wie verfeinert)
- 311
  - Resultate Interpretieren, wir müssen das resultat eines modells richtig interpretieren
  - Was kann mein modell und was kann es nicht?
  - Ein modell ist nicht grenzenlos und die grenzen müssen klar kommuniziert werden
  - dass man die resultate nicht zu sehr generalisiert, wenn ich sehr homogene trainigsdaten habe dann ist es nicht auf die ganze welt anwendbar
  - Ein einfaches modell ist ein qualitätmerkmal für sich
  - kleine verbesserungen im validation score könnten auch zufall sein
- code Beispiel
  - Wenn man wenig inputs hat -> dann grösser und dann kleiner
  - Wenn man viele inputs hat wird man incrementell kleiner
  - Die knoten anzahl sind oftmals 2^irgendwas -> hardware gründe anzahl cashes, so dass es nicht wieder ins ram gehen muss etc. Also auf die Hardware abgestimmt
  - `Reshape` -> aus 8 mal 8 Bild kommt ein eindimensionalen Vektor, kann auch extern gemacht werden, der zusammenhang der pixel geht weg sie sind losgelöst voneinander
  - `Dense` -> dass alles miteinander verbunden ist, das ist das layer dass alles mit allem verbindet. Die anderen layer typen gibt es auch zur auswahl
    - `activation=` -> Aktivierungsfunktion ReLu
    - `kernel_regularizier` -> regularisierung optional
    - Letztes Layer -> Lienar aber oftmals `softmax`
  - `compile` -> optimisierung `sgd` -> stochastic gradient descent
  - `loss` -> Maximum likelihood, `from_logits=True` muss nicht softmax oben haben -> so kann man mathematisch einen term kürzen -> ist schneller
  - letzte funktion -> beide versionen identisch
    - softmax dann `from_logits=False`
    - linear dann `from_logits=True` -> schneller
  - Summary
    - Output Shape -> 64 -> next 10 --> param 650 `(10*64) + 10`
  - `batch_size` -> 128
  - `epochs` -> gehe 10 mal durch alle daten
  - 11 mal in einer epoche -> dann ist es durch alle trainings daten durch
  - Immer eine validierung am schluss mit den validierungsdaten
  - Dann sieht man wann die validierung gut ist oder ob sie schlechter wird bei overfitting


## Tag 4

  - Bei statistik weiss man genau wass man macht
  - Bei neural networks muss man kreativer sein als nur neue layer
  - Die rechnung kann man zwar aufschreiben aber man kann sie nicht mehr verstehen
  - Aber man kann schauen welche pixel wie viel einfluss haben
  - Schauen dass es auch das richtige pixel anschaut (krebszellen und massstag)

#### Convolution Neural Network

Annahme, die Nachbarschaft von einem input wert hat einen Einfluss auf den Wert.

- Folie
  - Wichtiger Forscher, ist jetzt bei Meta
  - Altes beispeil, erstes network dass tatsächlich funktioniert hat in der praxi
  - Hier ein bisschen schlauer, nicht alles hat auf alles einen einflus
  - Aus einem bild unterschiedliche interpretation
  - Dann kleiner, und wieder grösser
  - dann am schluss flach (re-shape)
  - Hier Guassian, heute wäre es softmax
- Convolution Neural Network
  - Wir verändern die verkabelung im netzwerk um den input besser zu berücksichtigen. Aber die andere verkabelung ist nicht zufällig sondern sehr systematisch
  - Statt alles flach zu machen, berücksichtigen wir die nachbarschaft der pixel
  - Es schaut immer zwangsweise auf die nachbarschaft. Wenn die nachbarschaft keine rolle spielt ist CNN nicht die richtige wahl
  - Um ein Pixel zu verstehen, schaut es sich die pixel die am nächsten sind, also einen neuen wert der aus einer gewichteten rechnung der nachbarschaft pixel sodass ein pixel einen neuen wert erhält, "translation equivariance"
  - Das wird für alle pixel gemacht
  - Es wird nie grösser
  - Das bild anzahl input bleibt gleich gross
  - Bei reshape geht der zusammenhang zwischen den pixel verloren
  - Die betas welche angewendet werden, sind gelernt aus dem ganzen Bild, es hat wie eine maske die über das ganze geht und die selben betas auf das ganze bild anwendet, "Weight Sharing" es bildet eine maske die es auf das ganze bild anwendet
  - Die ursprünglichen betas sind komplett zufällig, wenn per zufall die anfangs betas gut waren, trainiert es schneller. Aber sie werden innerhalb einer range zufällig gewählt also Carefully Selected Randomness
  - Alle layers werden immer parallel optimiert basierend auf dem resultat von dem output layer, man fokusiert sich nicht auf ein layer bei jeder iteration
  - wir können nicht nur ein solchen filter haben sondern mehrere filte die auf dasselbe bild angewendet wird, dann haben wir mehrere neue bilder. Zum beispiel könnte die farbe beschreiben, etwas anderes eine kante beschreiben etc.
  - Dann werden die werte zusammen gefügt und das maximum wird genommen und dann haben wir die grösse halbiert (maximum 2D pooling). Das bild ist wie weniger aufgelöst aber wir verschärfen die unterschiede
  
#### Reconstruction Based Methods

- Auto Encoder -> macht eine dimensionality reduction
- 
  - Ist ein neurales netzwerk, dass eine dimensionsreduktion
  - Nachher gehen wir von der reduktion, gehen wir wieder auf mehrere features
  - Es muss nicht komplett symetrisch sein
  - Es können auch convolution layers sein, nicht nur fully connected
  - Anreiz ist dimensionsreduktion zu machen ohne labels von hand zu machen
  - Trainiert alleine um die reduktion zu lernen
  - Aber es wird eigentlich immer mit dem decoder verwendet
- Folie
  - Machen ein bottelneck -> gelernte dimensionsreduktion
- 
  - Kostenfunktion kann der rekonstruktionsfehler sein (L1 oder L2 distanz)
  - Wird für pre-processing angewendet, zum beispiel dann sind rgb werte nicht mehr so einflussreich bei clustering, weil diese sind meistens eher störend
- 
  - Beispiel von nicht liear bild oben rechts
    - Encoder - [2 (features) - 20 (zwischenergebnisse)]
    - 1 (ist das zweite bild) 
    - Decoder - [20 (zwischenergebnisse) 2 (features)]
- 
  - Egal wo genau das blatt ist um ein baum zu erkennen, aber der encoder lernt sehr start auf pixel information
  - Eigentlich mehr rechts ist ein baum, links eine Wiese
- 
  - Autoencoder kann man nicht linear machen mit der Aktiverungsfunktion, wenn diese linear ist, kann es nicht mehr als PCA ist einfach nicht so effizient
- 
  - Word2Vec -> damals ein wichtiger baustein dass zeigte, dass deep learning funktioniert, basis auch für LLM
  - Würde man heute nicht mehr so machen, heutzutage 
  - Die reihenfolge der wörter speilen keine rolle
  - Task: Lückentext
  - One Hot encoded words
  - Matrix, überall dieselbe matrix
  - Jedes Wort wird auf einen Vektor mit 300 zahlen gemapped
  - Dann wird vektoraddition gemacht
  - Vektor mit 300 Zahlen dass die 6 wörter beschreibt
  - Klassifikation mit softmax
  - Die Vektoren die wir nicht verstehen, mit denen kann man dinge berechnen die wir als menschen sinnvoll verstehen
  - Präziese -> weniger zahlen als mit one hot encoding, model hat es leicher, weil es sysnonyme nicht lernen muss
- Heuzutage encoden sie den ganzen satz und macht den ganzen satz zu einem vektor
- Die bilder könnten corrupt sein, also nur einen teil des bild reingeben, die learning taks ist schwieriger für das motell, lernt aber mehr über die welt

#### Constrastive Learing


- zum Beispiel Gesichtserkennung
  - Bilder von einer Person müssen sehr nahe liegen
  - Distanz zu anderen Personen muss maximal gross sein
  - Das wird gelernt
  - Vorteil ist, dass ein Bild von einer neuen Person, welche nicht ein teil von trainingsdaten ist, sollte eine Person ungefährl plaziert werden, das nächste bild von der neuen person soll dan in die nähe der neuen person sein ohne neu trainiert werden zu müssen
  - Weil wir nicht klassifikation lernen kann einfach eine neu person genommen werden und wird einbezpgen
  - Wenn das Modell gut generalisiert ist, ist es gut zum wieder verwenden
  - One-Shot-Learning -> anhand von einem beispiel einer neuen person kann ich das modell nutzen um eine neue person zu erlenen
- Zu jedem Bild ein Text
  - Das bild und der Text die gleich sind müssen in die gleiche richtung zeigen
  - Gemeinsamer label space von bild und text
- Zero-Shot-Learning
  - Modell konstruieren ohne dass wir etwas lernen
  - zb. "A photo of a dog" & "A photo of a cat" -> Text Encoder -> Vektor von 300 Dimensionen
  - und Bild von Hund -> image encoder -> Vektor von 300 Dimensionen 
  - Lade zwei Encoding modell herunter die zusammen trainiert wurden
  - Ich mache basierend darauf ein neues Modell machen das nur einen input haben


#### Skip Connection

- Wir können manche layers überspringen
- Wenn man 20-30 layers hat, hatte man probleme einzelne layers zu trainieren
- Die dimensionen müssen identisch sein
- Mit skip connection kann man tiefere netzwerke trainieren
- Kann man auch als ensemble von verschiedenen netzwerken ansehen
- Die unterschiedlichen Wege werden parallel trainiert, dann haben wir für ein Beta mehrere Werte, diese werden dann aufsummiert um ein schlussendliches beta zu verwandeln
- Niemand macht so grosse netzwerke 1202, sondern nur proof of concept, dass es möglich ist dass es möglich ist sehr tiefe netzwerke zu trainieren
- U-Net wird eigentlich immer für segmentierung verwendet
  - Um für ein pixel muss man pixel perfekt zu sein (genau auf ein pixel), zweite herausforderung das ganze bild als gesammtes muss verstanden werden
  - Das U -> layer nach layer (convolution layer), das bild wird immer kleiner, hilft das bild global zu verstehen
  - Dann müssen wir uns auf pixel ebene verstehen
  - Wir wollen nicht das in das U pixel perfekt lernen muss
  - Über die horizontalen lernt es die pixel perfekte, weil es bei der kompression nicht geeignet ist
  - Auch in CNN werden die heutzutage immer angewendet


#### In Context Learning (362)

- mehr kontext als word2vek, mehr kontext um ein nächstes wort vorherzusagen
- 70 milliarden betas
- betas sind eingefrohren!
- in-context learning (ICL) (363)
  - Wenn wir learning definieren als es verändert die betas, dann ist es kein learning
  - promt engineering -> wie schreiben wir die task welche die absicht beschreibt
  - man spricht von learning hier, weil wir den output verbessern können durchdas wir beispiele geben
  - wir machen eigentlich kein training mehr
  - wir machen ein allgemeinen wrapper um ein modell
  - "trainingsdaten" können als beispiel hinzugefügt werden
- solche modelle können benutzt werden um few-shot oder zero-shot modelle gebaut zu werden
- Task beschreibung kommt von uns, ist programmiert in der software
  - promt ist dan von den usern -> welches einen output von llm gibt
- zero-shot -> ohne beispiel
- one-shot -> mit einem beispiel, etc.
- RAG -> sodass das gut funktioniert muss das retrieval sehr gut sein
  - Auch bei RAG kann es haluzinieren
  - weil es generiert einfach plausibeln text
- ACU (368)
  - in der forschung, dass es die ganze code applikation steuern kann
  - Agentic Coding ist ein teil, das sehr spezifisch darauf eingegrenzt


#### 



