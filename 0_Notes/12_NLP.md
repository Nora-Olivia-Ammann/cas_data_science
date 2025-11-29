# NLP

Lektion 1-4 -> "Klassisches NLP", alles vor Chatbots, wird wahrscheinlich in der praxis weniger verwendet
Nach chat bots Lektion 5 + viel besser

### Essentials:
  - Gut genug: ist richtwort von NLP, perfekt geht nicht (memory restrictions auch)
  - 
Neural network:
- Bag of words als direkter input: sparse binary ints -> schlechter für netzwerke
- With Embedding (vektor) hidden layer bei Neural Network: dense floats -> besser für netzwerke

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
- synonyme im klassischen NLP ist schwierig, von hand does not scale



## 5 Neural Networks in NLP

0. Pytorch (5-)

- 6
  - Grösser als Matrix ist Tensor
  - Tensor Processing Unit (TPU) -> rechner die spezialisiert sind die auf berechnung mit tensors
  - praktisch alles ist ein tensor
- 8
  - CPU -> wenige cores aber die können schwierige sachen machen
  - GPU -> viele cores die aber nur eine operation sehr schnell machen (weil parallel) können, sehr spezialisiert

1. Classifier (10)

- 11
  - input text dokumente
  - output: 3 kategorien
- Wie können wir das mit Neural Networks machen?

2. Embedding (17)

Bag of words: sparse binary ints -> schlechter für netzwerke
With Embedding (vektor) schicht vor Neural Network: dense floats -> besser für netzwerke

- 18
  - Bag of Words
    - Problem : no semantic
    - langer vektor
    - meistens nullen im vektor
    - zu viele input die keine neuronen aktivieren
    - dichte vektoren sind besser die weniger 0 haben
    - keine synonyme
    - binär keine nuancen
- 21
  - Embedding
  - **Embedding is ein normales hidden layer, wenn input layer ein sparse vektor ist, ist es gut den zu reduzieren in einem ersten hidden layer.**
    - hier sind es floats, netzwerke werden besser mit dichten floats als mit sparse ints
    - input sehr grosser input vektor
    - embedding schicht die dimensionen reduziert
    - der rest des netztes bleibt gleich
    - dieses embedding muss auch trainiert werden
    - bei embedding führen ähnliche wörter zu ähnlichen vektoren
    - das embedding zusammen mit allem anderem trainiert, das model wird besser wenn wir alles ende to end trainieren

3. RNN (Recurrent Neural Networds): Limitation von Episode 2 (26)

-> watch video (not to understand in detail)

- Bag of words annahme ist ein problem
- Wichtig ist kontext, also memory zu wissen was vorher und nachher kommt
- Recurrent Abbildung 28 
  - -> das output eines layers wird im nächsten durchgang auf das selbe layer angewendet
  - in dieser architektur kann ein wort nur auf das vorherige hinschauen nicht länger
- am ende liesst es nur das gewicht des letzten neuron
- Problem wenn der satz sehr gross ist und das sentiment ist im ersten wort, dann geht es lang bis wir zum resultat kommen, da es erst beim letzten raus kommt. Dann funktioniert es nicht so gut

4. RNN Language Model: Generative (33)

- Es wird sequentiell immer ein wort nach dem anderen generiert
- Gib dem netzwerk ein satz verstecke das letze word, und dann evaluiere das generierte wort, wenn es schlecht ist, dann wird es negativ bewertet sonst enforcing
- Generiert labels indem man das letzte wort als label nutzt
- Temperature
  - Wenn jedesmal das höchstwahrscheinlichste wort genommen wird, ist der output immer sehr ähnlich. 
  - Daher muss ein gewisses ausmass an zufälligkeit hinzugeüft werden, sodass es aus einem set von möglichen wörter auswählt
  - Tiefe temperatur ist es deterministisch > zuverlässig aber langweilig

5. Attention Mechanism (40): Kernpunkt vom Kapitel

Die ganze architektur mit den gewichten und layers ist ein Transformer (ein namen die die entwickler ausgesucht haben). Ist eine kluge verstapelung von matrix multiplikationen, die architektur ist Transformer genannt.

- problem:
  - Ich kann nur ein wort nach dem anderen berechnen
  - Wenn es lange sätze sind dann ist es schwierig von anfang nach ende information zu propagieren
- Attention
  - Ein wort darf auf alle vorherigen wörter schauen um das nächste vorherzusagen
  - komplexer zu trainieren als nur RNN
  - Diesen effekt von kontext muss in das netzwerk
- Wie kontext: (45)
  - 3 Konzepte:
    - Query:
      - Adjective in front of me?
    - Key: zwei wörter ja (fluffy, blue) aktivation (matrizen) von den "positiven" antworten
    - Query + Key wird kombiniert -> Value
    - Value: effekt von der kombination von key und query transformation -> geht weiter
    - -> dann werden die matrizen multipliziert
  - 1 query in einer attention schicht, wird in jeder schicht wiederholt
  - Das netzwerk lernt während dem training diese queries zu stellen die sind nicht vorgegeben (keine hyperparameter)
- Wurde von Google durch trial und error von 8 Jahren entwickelt. Es sind bastler die ausprobieren und die architektur verändern um es besser zu machen. Es hat kein fundiertes konzept das sie von vorher gemacht haben und anwenden.
- Nur die kombination von Hardware, Software leute und grosser Korpus hat es möglich gemacht es zu entwickeln
- Transformer-Aarchitektur hat sich für text entwickelt. Wurde nicht gedacht und dann implementiert.
- Die queries sind nicht zwingend von menschen interpretierbar
  
- Attention Head
  - 1 attention head hat N attention layers (query / key / value)
    - Alle layer können parallel laufen
    - Man wählt die anzahl von attention heads die in parallel laufen basierend auf den GPU kapazitäten, optimiert auf die GPU architektur
  - Mehrere attention heads in parallel, jeder schaut dasselbe wort an mit einer anderen query an
  - GPUs sind gut in parallel, darum ist das netzwerk auch parallel konzipiert
  - Zwischebn den attention heads sind normale netzwerke
- Code beispiel ist zum lesen, weniger zu laufen: solcher code wird genutz um GPT-3 zu trainieren

- Episeode 6 nano-gpt annotation -> bezieht sich auf ML folien


Exam Questions: Seite 92

## 6 Transformers

- S. 4 -> Definition von transformer
- 8: erste transformer der veröffentlicht wurde
- 10: wichtig: pre-training und dann als zweites fine-tuning
  - fine tuning ist billiger, und ein allgemeines modell wird auf die spezifische task spezifiziert, aber wir müssen nicht englisch lernen
- 12: grund training ein teil des satzes wird versteckt -> dann evaluation mit richtigem
- 13: andere zwei sätze werden zusammen gesetzt die zusammen wirklich vorkommen. Dann nehmen wir zwei neue sätze und fragen ob es zusammen gesetzt sinn macht. Non-supervised
- ich fine-tune ein transformer auf meine eigene task, nur die letzte schicht wird verändert
- 
- Reinforced learning ist der fine-tuning teil


## 7 Chatbots

- 14 
  - -> hier ist fokus auf details in das model einzugreiffen, und sich auf die grössere architektur fokusieren
- 15 Chain of Thought
  - Input: Beispiel frage und beispiel antwort. Dann kommt richtige frage
  - Wenn mein promt zeigt wie ich die antwort will, ist die chance höher dass es so raus kommt wie wir es gerne wollen
- 




