# NLP


## Tag 1

### Essentials:
  - Gut genug: ist richtwort von NLP, perfekt geht nicht (memory restrictions auch)
  - 

- **Data Wrangling in NLP:**
  - Stop Words -> häufigste weg
  - Stemming & Lemmatisierung -> vielfalt der Wörter reduzieren


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
- 