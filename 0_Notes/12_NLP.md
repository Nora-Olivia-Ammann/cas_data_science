# NLP

Lektion 1-4 -> "Klassisches NLP", alles vor Chatbots, wird wahrscheinlich in der praxis weniger verwendet
Nach chat bots Lektion 5 + viel besser

### Essentials:
  - Gut genug: ist richtwort von NLP, perfekt geht nicht (memory restrictions auch)
  - 

- **Data Wrangling in NLP:**
  - Stop Words -> häufigste weg
  - Stemming & Lemmatisierung -> vielfalt der Wörter reduzieren
  - Levenstein: 
    - Wort dass ich nicht kenne im korpus
    - Ich sage, du kannst max 2 edits mache
    - Wenn es nach edit ein teil meines wortschatzes ist dann darfst du die edits machen

## 1 Intro

- 8
  - Sprache ist für menschen natürlich
  - Nicht für computer
- 9-13
  - Kernproblem
  - Die unterscheidung ist nicht trivial 
- 14
  - Um zu erklären werden milliarden betas benötigt
- 17
  - Formal: 
    - Aufgrund der grammatik können wir programme schreiben
    - keine mehrdeutigkeit
  - Natural:
    - Umgekehrt aufgrund der benutzung wird eine grammatik abgeleitet
    - Historisch entwickelt

### Wörter / Morphologie (Lexikon / Vokabulary / Wortschatz)

- 25
  - Zu selten -> weg nehmen weil ich nicht weiss wie umgehen
  - Zu häufig -> weg nehmen weil nicht aussagekräftig
  - Zipf's Law -> "power low" der frequenz
- 28 -> Out of Vocabulary
  - Wörter die ganz selten sind
  - Kommen nicht im Wortschatz vor (eg. begrenzung auf 50k wörter)
  - kommt relative häufig vor
  - Auch wenn wir uns mühe gegeben haben das Vokabular zu definieren kommt oft vor
- 29
  - text wrangling
  - https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
  - encoding problem wenn komische special characters
- 30
  - Stop Words: zu häufig
  - gibt viele öffentliche verfügbare listen die man nehmen können
  - wird in der pipeline nicht beachtet
  - für gewisse programme müssen diese listen verändert werden
  - sind 20 häufigste oder 200 häufigsten wegwerfen?
  - weniger rechenkapazität wenn weniger wörter
  - je nach der fragestellung genügt es ohne stop words, dann weg werfen
- 31
  - zweites des data wrangling
  - Stemming: ende abschneiden
  - Lemmatisierung: häufigste vorm des wortes
  - Entfernung der diversität im wortschatz durch gleiche wörter zu vereinheitlichen
- 32: n-grams: 
  - Anzahl wörter pro Token "New York" zwei wörter separat haben nicht die selbe bedeutung wie zusammen
  - nicht häufiger als tri gram -> kombinatorische explosition
  - NLP: ist pragmatisch, kann ich es überhaupt auf der maschiene laufen lassen?
- 33
  - Entscheidung von NLP engineer
  - gibt viele libraries die helfen dies gut genug zu machen
- 34
  - Schreibfehler sind häufig
  - Spelling Error Algorithmus -> wie bei google vorschlag
  - Ist nicht trivial, aber kann verwendet werden wenn dies sehr wichtig ist

### Syntax (Satz)

- Welche regeln gibt es um die einheiten von wörter zusammenzufügen
- 36
  - Syntax tree: 
    - viele grammatische interpretationen, beide bäume haben unterschiedliche bedeutung
    - 1: Mensch 1 auge
    - 2: Hund 1 auge
- 39
  - Information Extraction 
    - -> Roh-text extraktion von information
    - NER
  - AI ist falsch im Text (geografische entität)
- 40
  - Classifier auch mit NLP
  - eg. Spam filter zusammen mit metadaten (woher geschickt, etc.)
- 42
  - beispiel, alles nach freundliche grüsse weg nehmen in email, ist wahrscheinlich signatur, etc.
  - reduktion mit länge, um nur die relevanten information zu behalten und die rechenkomplexität zu reduzieren
  - viel sinn ist verloren (zum beispiel "nicht" im letzten satz ist verloren gegangen)
  - Kompromiss wie viel reduzieren um es rechenbar machen und nicht information zu verlieren
- 43
  - Diagnostik Notizen
  - NLP pipeline aufbauen der vom Rohtext interpretation machen
  - Bridge abkürzung, was es bedeutet
- 47
  - Wenige Daten -> Deep Learning NLP
    - Man fangt nicht von 0 an
    - Kann ich ein netzwerk nehmen, dass auf natürlicher sprache gelernt ist. 
    - Dann wird nur das letztes stück gelernt (fine tuning)
  - Klassisches NLP -> muss von grund an lernen
     - Nachvollziehbarkeit ist besser
     - Viel mehr kontrolle
     - Möglich dass es nicht möglich ist ein LLM in-house laufen zu lassen (medizin), es ist aber auch nicht möglich es extern zu senden. Dann Klassisches
   - Es gibt kein einfaches rezept welche lösung zwischen klassisch und deep learning besser ist
  - Oftmals ist labelling trainings daten ist aufwändig als ein paar GPUs zu mieten
- Trainingsdaten in NLP ist text mit labels


## 2 Evaluation

- 2
  - in einer pipeline gibt es eine evaluation
  - messung um die nächste iteration zu verbessern
- 3
  - Kriterien von anfang an definieren
  - eg. Ich möchte dass die personen richtig erkennt sind, aber es sollte auch einen fuzzy match machen können
- 4
  - manual evaluation
    - quick and dirty (vorteil und nachteil)
    - one shot und wird nicht oft evaluiert
  - automatic
    - wenn oft evaluiert
- 5
  - intrinsisch kleiner teil vom system
- 6
  - Was ist falsch bei dem kreis -> overfitting problem
  - was verhindern -> cross evaluation (train, eval, test)

## 3 Regex

- Summary 1 & 2 (seite 4-5) ist für prüfung


## 4 TF-IDF

- 4
  - Invertierter Index: Wir haben wörter und dann pointer zu dem dokument
  - Index: eg. buch konzept -> seite auf dem es ist
  - Invertierter Index -> schnell zu finden
- 5
  - Nur matches reicht nicht weil wir wollen die besten oben haben
  - Wie kann ich sinnvolle dokumente haben und nicht nur alle die die wörter haben
  - Bag of words -> reihenvolge der wörter vergessen
- 6 (beispiel)
  - Korpus: 3 Dokumente
  - Wortschatz 9 Wörter
  - Mit word counts
- 10
  - Term Frequency -> relative häufigkeit
  - all wörter auf einer zeile summieren sich auf 1
  - Wichtig weil nicht alle dokumente gleich lang sind. Ein langes dokument hat mehr wahrscheinlichkeit als ein kürzeres. Das ist nicht erwünscht.
- 11
  - Inverse Document Frequency
  - Häufige sind weniger wichtig als seltene (aussagekräftiger) über den gesammten korpus
  - logarithmus ist einfach für smoothing
- 12 TF-IDF -> kombination von beiden
- 13
  - "is" ist so häufig dass es 0 gewicht hat
- 14
  - "a" kommt im query zwei mal vor -> score wird *2 gerechnet
- 17
  - TF-IDF sind werte die in dem resultat angezeigt werden
  - berechnung des scores ist nachvollziehbar und validierbar
- 
- 


