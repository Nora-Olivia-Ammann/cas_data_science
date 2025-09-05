# SQL Notes

## Folien

Abkürzungen

- `JOIN` == `INNER JOIN`
- `LEFT OUTER JOIN` == `LEFT JOIN`

7. Prüfung (grün)

6. `JOIN` ist immer `INNER JOIN`

11. `FULL OUTER JOIN` alle egal ob die beiden Tabellen überschneidungen haben

14. From macht zwei Kopien von der tabelle, die dann verbunden werden, hier über die ID

26. Mengenlehre -> ist DISTINCT per default. wenn man alles sehen will dann `ALL` 

27. Schnittmenge

28. `EXCEPT` / `MINUS` was ist in T1 aber nicht in T2, hier ist die Reihenfolge ausschlaggebend

29. `FULL OUTER JOIN` könnte auch mit `UNION` machen
30. `UNION` muss von gleichen daten typ sein aber die Spaltennamen können mit einem Alias zusammengefügt werden
    UNION kann nicht optimiert werden `FULL OUTER JOIN` ist vorzuziehen wenn es unterstützt wird

32. Sub-Select 
32. Ein Wert (wenn es mehrere Werte hat, dann gibt es eine Fehlermeldung)
33. Wenn es mehrere Werte hat
34. Wenn invoice existiert gib es aus




# Workshop

## WS01 JOINS & Sub-Queries

### Aufgabe 10

Zeige für Tracks, die zwischen 470 und 480 Sekunden dauern, deren Namen, den Albumtitel 
und den Namen des Artisten. (WHERE milliseconds BETWEEN 470000 and 480000)

Join the two on album id

```sql
SELECT tracks.name , albums.title
FROM tracks JOIN albums
ON (tracks.albumid = albums.albumid)
```

```sql
SELECT albums.title AS album_title , artists.name AS artist_name
FROM albums JOIN artists
ON (albums.artistid = artists.artistid)
```

```sql
SELECT *
FROM TRACKS
WHERE 470000 < MILLISECONDS < 480000 ;
```

**FINAL**

```sql
SELECT tracks.name AS track_name, albums.title AS album_title, artists.name AS artis_name
FROM TRACKS
JOIN albums ON (tracks.albumid = albums.albumid)
JOIN artists ON (albums.artistid = artists.artistid)
WHERE milliseconds BETWEEN 470000 AND 480000 ; 
```

## Aufgabe #11 
Finde die Anzahl Tracks mit Mediatype 'MPEG audio file', die pro Person/Customer gekauft 
wurden.


media_types.mediatypeid -> tracks.mediatypeid -> invoice_items.trackid -> invoices.customerid

Number of media

```sql
SELECT media_types.name , COUNT(tracks.mediatypeid) AS number_of_media
FROM TRACKS
JOIN MEDIA_TYPES ON (tracks.mediatypeid = MEDIA_TYPES.MEDIATYPEID)
GROUP BY media_types.name
```


Filtered

```sql
SELECT media_types.name , COUNT(tracks.mediatypeid) AS number_of_media
FROM TRACKS
JOIN MEDIA_TYPES ON (tracks.mediatypeid = MEDIA_TYPES.MEDIATYPEID)
WHERE media_types.name = 'MPEG audio file'
GROUP BY media_types.name
```

**FINAL**

```sql
SELECT customers.firstname, customers.lastname, COUNT(media_types.name)
FROM CUSTOMERS
JOIN invoices ON (CUSTOMERS.CUSTOMERID = invoices.customerid) 
JOIN INVOICE_ITEMS ON (invoices.INVOICEID = invoice_items.INVOICEID)
JOIN tracks ON (invoice_items.trackid = tracks.trackid)
JOIN MEDIA_TYPES ON (tracks.mediatypeid = media_types.mediatypeid)
WHERE media_types.name = 'MPEG audio file'
GROUP BY customers.firstname, customers.lastname
```


### Aufgabe 12

Gibt es Manager, die in derselben Stadt wohnen, wie ihre Mitarbeitenden? Benötigt werden die 
Vornamen und die Stadt.



```sql
SELECT employed.lastname AS em_name , boss.lastname AS boss_name , employed.city as loc
FROM employees employed
JOIN employees boss ON (boss.employeeid = employed.reportsto)
WHERE (employed.city = boss.city)
```

### Aufgabe 13

Wir suchen den kürzesten track und wollen wissen wie dieser heisst (name), wer ihn kompo-
niert hat (composer) und wie lange dieser ist (milliseconds)

**Artist von diesem kürzestem song:**

tracks.milliseconds
tracks.name AS track_name
tracks.albumid = albums.albumid
albums.artistid = ARTISTS.artistid
albums.artistid = ARTISTS.name as artist_name


```sql
SELECT tracks.name AS track_name, ARTISTS.name AS artist_name , milliseconds
FROM tracks
JOIN ALBUMS ON (tracks.albumid = albums.albumid)
JOIN ARTISTS ON (albums.artistid = ARTISTS.artistid)
WHERE milliseconds = (SELECT min(tracks.milliseconds) 
  FROM tracks
  )
GROUP BY tracks.name , ARTISTS.name , milliseconds
```
