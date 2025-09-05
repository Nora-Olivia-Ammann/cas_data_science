# Lineare Algebra


## Skript

### Kapitel 2

Nur quadratische Matrixen sind invertierbar, weil bei anderen multiplikationen gehen dimensionen verloren, die können nicht mehr wiederhergestellt werden.

Division muss über die Multiplikation definiert werden weil es sonst nicht die Umkehroperation ist.

A^-1 -> Inverse muss mit A*A^-1 die Einheitsmatrix geben (1 in diagonal, sonst 0)

Determinante (determiniert) ist das im Nenner, so wissen wir ob sie invertierbar ist.
Nicht invertierbar, wenn nenner Null ist

Selten, dass sie nicht invertierbar ist

**Drei Lösungsmöglichkeiten**

- 1 Lösung -> invertierbar -> det nicht 0 (Vektor schneidet 1 mal)
- Keine Lösung -> nicht invertierbar -> det 0 (Vektor sind parallel)
- Unendlich Viele Lösungen -> nicht invertierbar -> det 0 (Vektor liegen aufeinander)

### Kapitel 3

Spiegelung oft, matrix in eine dimension zu bringen um sie zu verwenden (also zeilen und spalten zahl vertauschen.)

Transponierte Matrix mit sich selbst multipliziert wird eine quadratische Matrix.

Symmetrisch, an diagonalen gespiegelt symemetrisch, müssen quadratisch sein.
Symmetrische matrix ist ihre eigene Transponierte.
Ist in data science häufig.

Reihenfolge in matrix multiplikation spielt eine Rolle. Nicht gleiches resultat.


### Kapitel 4 Vektoren

Vektor länge ist nicht eindeutig, es gibt euklidisch, manhattan, etc. Ist problem-spezifisch


p = 1 ist manhattan norm, weil wurzel aus 1 kann weg genommen werden
p = 2 ist euklidisch weil quadtratwurzel...

max norm -> ist der grösste betrag eines Vektors. (grösste Zahl im vektor von Betrag (also minus egal))


**Skalarprodukt** zwei vektoren multiplizieren, sodass wir eine Zahl erhalten (Skalar)
**Matrizenmultiplikation** zwei Vektoren multiplizieren, sodass wir eine Matrix erhalten


Zwischenwnkel ausrechnen ist relevant z.b. für recommender systeme für ähnlichkeit zu berechnen

### Kapitel 6: Abbildungen

Abbildung irgend eine geometrische operation

- **Projektionsabbildung** -> macht immer kleiner (nimmt dimensionen weg)
- **Strecken / Stauchen** -> länge verändern
- **Drehen** -> um einen winkel drehen
- **Spiegelung** -> an axe spiegeln





