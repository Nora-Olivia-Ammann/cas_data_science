# Recommender Systems

- 8
  - Long Tail, einzelne werden nicht verkauft, aber es gibt viele davon, dann lohnt es sich trotzdem
- 10
  - Recommender Systeme sind auf benutzerinnen zugeschnitten
- 11
  - IMDB: gewichtete bewertung, siehe übung 1
  - m -> alles weniger als diese anzahl stimmen wird bestraft
- 13
  - Oftmals bewertungsmatrix
  - viele benutzerinnen
  - viele bewertungen
  - so gibt es eine matrix
- 15: herausforderung
  - Ratings erhalten
  - was machen wir mit allen fehlenden bewertungen, sprich die fehlenden orte
  - -> Wir wollen die unbekannten bewertungen finden die ein user hoch bewerten würde
  - evaluation muss am schluss gemacht werden
- 16: sammlung von bewertungen
  - explizit: 
    - fragt user nach bewertung
    - was jetzt am besten ist sind sie nicht einig
    - user experience welche skala gewählt wird, kommt auch ins spiel
  - implizit: 
    - Verhalten lernen und evaluieren
    - negative ist schwieriger zu lernen, einfluss von zeitdauer
    - range von ratings ist nicht klar definiert
- 17: extrapolation
  - kernstück jedes systems -> leere kästchen in der matrix ausfüllen und das höchste leere kästchen vorschlagen
  - Schwierig: matrix ist sehr sparse, wenige bewertungen für eine person, teilweise wenige bewertungen pro object
  - Cold-start problem: neue dinge, neue user oder wenn wir neu anfangen haben gar keine bewertungen
  - 3 Ansätzte
    - Content Based
    - Collaborative Filtering
    - Matrix Faktorisierung

### Content Based 19

- 20: Text -> längerer text schwieriger das profil zu erstellen
- ähnliche objekte präsentieren, wenn ein user ein objekt betrachtet
- 23: ähnlichkeits matrix aufbauen, wie ähnlich sind sich zwei filme
  - es kommt auf die features darauf an welche ähnlichkeits matrix art wir wählen
  - bei binär is hamming oder jaccard macht es mehr sinn, dann ist wenn alle features die sie nicht gemeinsam haben uns egal. Zum beispiel bei Regiseur name von filmen (wenn sparse dann eher jaccard sonst werden auch die werte sehr klein)
  - cosinus eher bei kontinuierlichen werten (erscheinungsjahr)
  - Hemming
    - Schnittmenge wo beide zutreffen und die schnittmenge wo beide 0 sind
    - und vergleichen es mit der gesammtmenge
    - da ziehen wir dinge die bei beiden unähnlich sind auch ein
  - Jaccard: (todo: noch besser recherchieren)
    - Schnittmenge aber teilen es nicht durch das gesammte
    - wenn beide 0 haben, ziehen wir es nicht in betracht
  - wenn wir die matrix haben, dann können wir sortieren und die ähnlichsten den user präsentieren
  - Hier wird für alle user dieselbe objekte präsentiert, projektprofiele aber user rating wird nicht miteinbezogen
- 24
  - user hat 2 objekte positiv bewertet
  - daraus machen wir ein profil
  - abgleichen mit user profil und nicht mit dem einzelnen objekt profil abgleichen
- 25
  - Abhängig wie die objektprofile aussehen und wie die bewertungsmethode gewählt ist
  - Hier ist explizit rating im beispiel
  - zb. gewichteter durchschnitt, gewichte sind da die bewertung der user
  - Rot wir schauen nur die romance kategorie
  - alle filme die bewertet wurden sind fantasy, romance is tiefer weil nicht alle filme sind romance
  - wenn gegensätzliche präferenzen sind, dann gibt es eine gemischte bewertung und sehr gut wird um die 0.5 sein nicht 1
  - dann werden die objektprofile mit den user profilen verglichen werden
- 34
  - Kosinus ähnlichkeit, wir haben zwei vektoren (wie nahe sind die winkel im n dimensionalen raum)
  - hier nur positive werte also zwischen 0 und 1, dann mal 10 rechnen um das approximierte rating im verhältnis zu den tatsächlien ratings hast
- Vorteile
  - privacy muss nicht in betracht gezogen werden weil andere user nicht miteinbezogen werden
  - cold-start ist kein problem weil ein neuer film hat ein objekt profil
  - neue user muss ein profil erstellt werden bevor vorschläge kommen, kann gemacht werden durch ein welcome quiz
  - ungewöhnliche geschmacke sind kein problem
- Nachteil
  - mehrere interessen die sehr unterschiedliche sind, ist schwieriger
  - user bleibt in der eigenen bubble
  - objekt profile können kompliziert sein (zb. text, bilder), film oder e-commerce ist einfacher weil sie klare features haben
  - nachteil auch andere user bewertungen werden nicht einbezogen, können wertvolle informationen enthalten

- Die wahl der features und die gewichtung ist sehr objektspezifisch, zb. werden studios bei filemen berücksichtigt?


### Collaborative Filtering 37

- zunächst ähnliche user identifizieren
- dann was haben diese sonst noch bewertet dann für den user
- Hier haben wir keine meta-informationen über die objekte mehr, sondern nur noch bewertungen

- 40
  - Ähnliche user finden
  - Vektor von einem user ist der feature vektor, statt objektprofile
  - dafür benötigen wir wieder eine ähnlichkeitsmetrik
  - Jaccard geht der wert der bewertung verloren daher wenn sie nicht binär sind weniger gut 
  - Pearson Correlation coefficient
    - wird meist verwendet
    - für den vergleich verwenden wir nur objekte die von beiden bewertet wurden
- 42:
  - jaccard schaut nur wo haben sie beide eine bewertung gegeben
  - negative werte -> sie haben nur einen gleich bewertet, kommt durch die normierung mit dem durchschnits bewertung
- 45
  - nächste user die das objekt bewertet haben
  - durch schnitt aller dieser bewertungen normal oder gewichtet, gewichtung da ist die ähnlichkeit der user

- objekt-Objekt collaborative filtering (46)
  - Man kann auch dies auf objekt ebene tun, ähnliche objekte suchen die user bewertet hat
- 47
  - n = 2 -> hyper parameter der bestimmt werden muss auswahl von n hat einen einfluss auf die wertung
    - n auch abhängig mach von der anzahl bewertung, user und objekte
  - 1. ähnliche filme finden
- 50
  - praxis ist objekt-objekt besser als user-user (können auch mehrere präferenzen haben)
  - vorteil auch ist erklärbar gegenüber deep learning
  - oftmals wird custom mix verwenden, bei cold start ist content based sinnvoll, später dann auch user, etc.
- es gibt auch noch, dass man user aus der bubble raus bringt indem man random objekte noch reinstreuut


### Matrix Faktorisierung 57

- 1 matrix für objekte 1 für user
- Für die faktorisierung gibt es verschiedene algorithmen
- 61
  - Dimensionsreduktion bei faktorisierung dadurch dass die zwei matrixen schmal sind
  - user fallen in denselben raum wie filme und so zeigt sich präferenz
- 66
  - Fehler minimieren pro element in der matrix
  - dann geht man mehrmals durch bis der fehler klein genug ist (fixe anzahl oder unterschied von jetzt zu nächsten klein genug)

### Evaluation 68

- ähnlich wie in ML
- bewertungsmatrix
- kann wieder test / validation set rausziehen und dann evaluation darauf
- Fehler metrik RMSE kann gewählt werden, gibt unterschiedliche metriken
- unterschiedliche arten der metriken, da wir oftmals mehrere vorschläge raus geben
- auch live evaluation, hat es gewirkt?

### Was ist aktuell im Einsatz 73

- Kontext ist wichtig

