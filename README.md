# Aufgabe 3: Mario
Gegen Ende von Welt 1-1 in Nintendos Super Mario Brothers muss Mario eine rechts ausgerichtete Pyramide aus Blöcken erklimmen, wie unten abgebildet.

![Super Mario Pyramid](instruction-assets/pyramid.png)

Lass uns diese Pyramide in Python nachbilden, wenn auch in Textform, unter Verwendung von Hashes (#) als Bausteine, wie im Folgenden dargestellt. Jeder Hash ist ein bisschen höher als breit, so dass die Pyramide selbst auch höher als breit ist.

```
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

Das Programm, das wir schreiben werden, wird `mario` heißen. Und wir lassen den Benutzer entscheiden, wie hoch die Pyramide sein soll, indem wir ihn zunächst nach einer positiven ganzen Zahl zwischen, sagen wir, 1 und 8 einschließlich fragen.

So könnte das Programm funktionieren, wenn der Benutzer 8 eingibt, wenn er dazu aufgefordert wird:

```
$ ./mario
Height: 8
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

Und so könnte das Programm funktionieren, wenn der Benutzer eine 1 eingibt, wenn er dazu aufgefordert wird:

```
$ ./mario
Height: 1
#
```

Wenn der Benutzer auf die Aufforderung hin tatsächlich keine positive ganze Zahl zwischen 1 und 8 eingibt, sollte das Programm den Benutzer erneut auffordern, bis er kooperiert. Eine Abfrage für nicht numerische Werte ist nicht nötig, dies wird bereits vom Hauptprogramm (schau bei Interesse gerne vorbei: `main.py`) erledigt.

```
$ ./mario
Height: -1
Height: 0
Height: 42
Height: 50
Height: 4
   #
  ##
 ###
####
```
## Schritt 1: Das Gegenteil
Nun, da dein Programm (hoffentlich!) die Eingaben wie vorgeschrieben akzeptiert, ist es Zeit für einen weiteren Schritt.

Es stellt sich heraus, dass es etwas einfacher ist, eine linksbündige Pyramide zu bauen als eine rechtsbündige, wie in dem folgenden Ausschnitt:

```
#
##
###
####
#####
######
#######
########
```

Lass uns also zuerst eine linksbündige Pyramide bauen und dann, wenn das funktioniert, diese rechtsbündig ausrichten!

Ändere `mario.py` auf der rechten Seite so, dass es nicht mehr einfach die Benutzereingabe ausgibt, sondern eine linksbündige Pyramide dieser Höhe.

Fülle hierzu die bereits deklarierte Variable `pyramid`. Diese wird am Ende der Funktion zurückgegeben und durch die Datei `main.py` ausgegeben.

### Hinweise
- Denk daran, dass eine Raute nur ein Zeichen wie jedes andere ist, Sie können sie also mit print ausgeben.
- In Python kannst du beispielsweise mit `for i in range(n)` eine Code-Schleife erzeugen. Mehr dazu hier: [ForLoop - Python Wiki](https://wiki.python.org/moin/ForLoop).
- Du kannst Schleifen "verschachteln", indem du mit einer Variable (z. B. i) in der "äußeren" Schleife und einer anderen (z. B. j) in der "inneren" Schleife arbeitest. So könnte man zum Beispiel ein Quadrat mit der Höhe und Breite n ausgeben. Natürlich ist es kein Quadrat, das du ausgeben willst!


## Schritt 2: Rechtsbündig ausrichten mit Punkten
Richten wir nun diese Pyramide rechts aus, indem wir deine Hashes nach rechts verschieben, indem wir ihnen Punkte (d.h. Punkte) voranstellen, wie hier dargestellt.

```
.......#
......##
.....###
....####
...#####
..######
.#######
########
```

### Hinweis
Beachte, dass die Anzahl der Punkte, die in jeder Zeile benötigt werden, das "Gegenteil" der Anzahl der Hashes in dieser Zeile ist. Bei einer Pyramide der Höhe 8, wie der obigen, hat die erste Zeile nur 1 Hash und somit 7 Punkte. Die unterste Zeile hingegen hat 8 Hashes und damit 0 Punkte. Mit welcher Formel (oder Arithmetik) könnte man so viele Punkte ausgeben?

## Schritt 3: Entferne die Punkte
Jetzt fehlt nur noch der letzte Schliff! Änder die Datei `mario.py` so, dass das Skript Leerzeichen anstelle dieser Punkte ausgibt!

## Schritt 4: Ausprobieren
Glückwunsch, das war's.

Wenn alles geklappt hat, ist die Aufgabe nun bereit zum abgeben. Teste sie doch gleich aus. Die Prozedur ist dieselbe. Starte die Anwendung mit:

```bash
python main.py
```

und probier aus! :)

## Lösung
<details>
  <summary>Nur aufklappen, wenn du wirklich Hilfe brauchst! Probiere es zuerst ohne Lösung.</summary>
  
  ### mario.py
  ```python
    # No pyramids with height less than 1
    if (height < 1):
      return

    for i in range(height):
      # Loop to add spaces
      for k in range(height - i, 1, -1):
          pyramid += ' '
      # Loop to add hashes
      for j in range(0, i+1, 1):
          pyramid += '#'
      
      if (i < height - 1):
          pyramid += '\n'
  ```

  >Tipp: Achte immer darauf, dass die Zeilen richtig eingerückt sind!
</details>
