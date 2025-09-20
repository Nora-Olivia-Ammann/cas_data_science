# Regression

- Wir können fast alles mit regressions rechnung machen
- Realität -> lateinische Buchstaben, modell welt ist griechisch
- 3: Simple Linear Regression Model: 1 input variabel und 1 output variable -> gerade linie
- 5: Realität
  - Extrem fälle sind selten
  - Daten gehen trichterförmig auseinander
  - Je mehr aufzufüllen desto grösser die streuung
  - Wenn wir eine gerade einfügen, menschen können gut abschätzen
  - Geht es durch 0? Was bedeutet es wenn es durch 0 geht oder nicht?
- 6: Modell Welt
  - beta steigung
  - Epsilon ist der fehler
  - Input x, y output
  - epsilon (fehler), gerade wird nicht exakt durch die punkte durchgehen, daher fehler hinzu (10 flaschen unterschiedliche zeit)
  - epsilon streuut um 0, wir wissen nicht wie viel es streuut (varianz)
  - Relative fehler (trichterförmige verteilung)
  - annahme fehler sind konstant
- 7: Es gibt verschiedene Modell Welte
  - Mechanistische Modelle: Physik, etc. fast alles lässt sich aus sachen ableiten (action reaktion, etc). Relativ stabil
  - Empirisch: Alkhohol und Krebsrisiko, gibt keine pyhsik formel die das erklärt. Sondern daten die den zusammenhang suggerieren. Relativ instabil. Wir suchen nach modellen. Welche variabeln sind signifikant. Hat das Körpergewicht einen einfluss? Welche variablen sind wirklich entscheidend?
- 8: Wir wollen eine vorhersage machen
  - Vorhersagen müssen mit dem vertrauensinterval versehen
  - In mechanische modelle gibt es oft variabeln die oft eine physikalische bedeutung haben. (strom, etc.)
  - Welche variablen sind signifikant?
  - Optimierung, wenn wir nach einem Wunschresultat suchen, werden wir schauen welche input variablen gut sind um das optimum zu erreichen.
- 9:
  - Regression -> die modell welt sollte die resultate der realen welt am besten passen
- 10:
  - beta 0 (hier nicht immer) -> y achsen abschnitt wenn x = 0 (oftmals nicht interessant, weil wir ja nicht interessiert sind wenn nichts passiert)
  - beta 0 ist vielleicht nicht klar definiert (zeit an dem angefangen wird zu messen)
  - der fehler können wir nicht schätzen, sondern nur wie sie streuut
- 11:
  - legen durch die datenpunkte die "best passende gerade" zu legen
  - die suchen wir so, dass wir den abstand zwischen dem realen y wert (punkt) zu dem y wert der auf der gerade liegt zu messen
  - die best passende gerade ist die bei denen alle abstände (betrag können negativ positiv sein) zusammengezählt möglichst klein.
  - Wir minimieren die summe der quadrate aller abstände. Wir haben dann eine gerade und haben parameter so lange bis die summe der quadrate minimal ist.
  - Wenn nur die summer angeschaut wird ist es schwierig, weil wir haben zwei parameter. Wie finde ich das optimum? -> lineare algebra
  - die summe der quadrate können wir uns als fläche vorstellen. Wir haben so eine senke. Die Senke finden wir in dem wir dem gradienten entlang nach unten gehen.
  - Im Minimum in der Senke hat es eine horizontale tangentialebene (die fläche wird nur einmal berührt)
- 12: Wir abgeleitet und setzten gleich 0 -> beobachtung, wir leiten nach beta 0 ab und beta 1. Sie sind linear und daher einfach auch wenn sie lange ist. Weil sie sauber ausgeklammert werden können
  - x werte kennen wir, egal wievile es sind. Die y werte sind auch bekannt. Dann können wir einfach nach den anderen auflösen.
- 13: die gleichungen sind bekannt, und es kann ausgerechnet werden
  - der fehler term haben wir nicht
- 14: Residual für den fehler term
  - messwert - fitteten wert -> es gibt so viele fehler wie beobachtungen. Im schnitt sind die fehler null
  - die gerade bei der die Fehler im schnitt null sind gibt dasselbe resultat wie minum der quadrate
  - summe aller kleinster quadrate (minus plus geht ja weg) ist error sum
  - hüte auf den buchstaben -> wenn ich der hypothese (griechisch) einen wert zuweise dan gibt es einen "Hut" (hat) auf die variabel
- in Python -> 08-Regression-notebooks/Example 7.1.1-7.4.2 Vending Machines (minimal).ipynb
  - Im summary output steht viel, wir konzentrieren uns jetzt auf die koeffizienten 
                    **coef**    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    **Intercept      3.3208**      1.371      2.422      0.024       0.484       6.157
    **Volume         2.1762** 

- 17: Jetzt fängt die arbeit an.
  - Analyse ob die antwort gut ist.
  - Kann das Model verwendet werden um eine vorhersage zu machen?
  - Wir haben angenommen, dass die varianz konstant ist.
  - Interpelation:
  - Extrapelation:
    - Veranstaltung, alles ist leer, müssen wir mehr leute anstellen um alle maschienen aufzufüllen. Dafür haben wir keine Messwerte. Können wir die gerade weiterziehen ausserhalb der Messwerte
- 18: Zusätzlich neue annahmen
  - Wir nehmen an, dass unsere fehler normalverteilt sind. Das haven wir vorher nicht gemacht.
  - Wir haben unsere Gerade, punkte die nahe sind, sind wahrscheinlich. Punkte die weit davon entfernt sind, sind unwahrscheinlich. -> Wir nehmen an dass die fehler in einer Normalverteilung sind. Machen wir damit das was folgt, handle bar ist.
  - Wir haben eine vending maschiene eine person füllt sie auf. Am nächsten tag mit gleichem elan. Ist immer gleich schnell beim auffüllen. Die geraden verändern sich etwas mit jeder neuen messung. Wir können alle steigungen zusammen nehmen und ein histogramm machen. Die verteilung der steigungen sind auch normalverteilt. Wir wissen auch die breite der Normalverteilung
  - Wenn die verteilung schmal ist dann ist die varianz klein, wenn die normalverteilung breit ist hat es eiine grosse varianz
  - Kleines Sxx
    - kleine streuung der messdaten
    - viel bewegung durch steigung
  - Grosses Sxx
    - grosse streuun der mess daten
    - kleine bewegung durch steigung
  - Wenn wir im labor sind wollen wir ein grosses Sxx sodass die gerade auf dem maximum stabil ist. Wenn wir zahlen empirische zahlen haben ist das vielleicht nicht möglich
- 19: Test statistic (werte die ich gemessen habe - annahme test (0 hypothese)) / (standard fehler)
- 20: P wert ausrechnen basierend auf dem statistischen test um zu wissen wie wahrscheinlich es ist
- 22: Per default kommt in python raus, ob die steigung auch 0 sein kann, nicht mein wert "2". Annahme, wenn ich keine flaschen auffüllen muss kann es keinen einfluss haben auf die output variabel.
-                  coef    std err          t      **P>|t|**      [0.025      0.975]
    ------------------------------------------------------------------------------
    Intercept      3.3208      1.371      2.422      **0.024**      0.484       6.157
    Volume         2.1762      0.124     17.546      **0.000**     1.920       2.433  
    kann die steigung 0 sein? -> nein weil **P>|t|** = 0.
    Wenn es 0 flaschen hat hat es hat einen einfluss

- 23: 
  - welcher wert ist der plausibelste wert? Die kleinste quadrate
  - Kann ein anderer Wert auch plausiebel sein -> Hypothesen test (ist 2 auf plausibel wenn ist 2.17 gemessen habe)
  - Welche werte sind überhaupt pausibel? -> vertrauensinterval
- 24: Vertrauensinterval
  - Alle werte die die 0 Hypothese erfüllen. Zwischen dem unteren und dem oberen kritischen wert (signifikanz niveau ist per default 5%)
  - Von - bis -> `[unterinterval grenze , oberinterval grenze]`
-                   coef    std err          t      P>|t|      **[0.025      0.975]**
    ------------------------------------------------------------------------------
    Intercept      3.3208      1.371      2.422      0.024     **0.484       6.157**
    Volume         2.1762      0.124     17.546      0.000     **1.920       2.433**
    
    Ist 2 Volume auch möglich? Ja es ist zwischen den zwei interval grenzen

- 25: Wie interpretiere ich den Vertrauensinterval?
- 

