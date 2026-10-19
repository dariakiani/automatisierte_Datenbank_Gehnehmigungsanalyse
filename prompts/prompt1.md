AUFGABE

Analysiere alle bereits hochgeladenen PDF-Genehmigungsdokumente vollständig.

Bearbeite ausschließlich das Sheet:

Contents

Fülle ausschließlich folgende Spalten:

A = Konformitätsanforderung ID
B = Abschnitts-ID
C = Ebene

Alle anderen Spalten dürfen nicht verändert werden.

==================================================
GRUNDSATZ
==================================================

Ziel dieses Schrittes ist ausschließlich die vollständige Ermittlung der Dokumentstruktur.

Es erfolgt:

- keine fachliche Bewertung
- keine Anforderungsart-Bestimmung
- keine Sachgebietszuordnung
- keine Geltungsbereichszuordnung
- keine Anforderungstexterstellung

Die Aufgabe gilt erst als abgeschlossen, wenn kein einziger Strukturknoten des Dokumentes ohne Excel-Zeile existiert.

==================================================
SPALTE A – KONFORMITÄTSANFORDERUNG ID
==================================================

Übernimm für jede Zeile die ID aus Zelle A2.

Alle erzeugten Zeilen erhalten dieselbe ID.

==================================================
SPALTE B – ABSCHNITTS-ID
==================================================

Ein Strukturknoten liegt nur vor, wenn es sich tatsächlich um einen eigenständigen Abschnitt der Dokumentstruktur handelt.

Beispiele:

- Kapitel
- Unterkapitel
- Entscheidung
- Bestimmung
- Auflage
- Bedingung
- Hinweis
- Begründung
- Rechtsmittelbelehrung
- Rechtsgrundlagenverzeichnis
- sonstige eigenständige Abschnittseinheiten

Jeder Strukturknoten ist einzeln zu erfassen.

Beispiel:

5
5.1
5.1.1
5.1.1.1
5.1.1.2

sind fünf unterschiedliche Strukturknoten und müssen fünf unterschiedliche Excel-Zeilen erzeugen.

Zusammenfassungen sind unzulässig.

Nicht übernehmen:

- Seitenzahlen
- Datumsangaben
- Aktenzeichen
- Fundstellen
- Gesetzeszitate
- Gebührenbeträge
- Telefonnummern
- Flurstücksnummern
- Fußnoten
- Tabellennummern
- Bildbeschriftungen
- Anlagenverzeichnisse

Es dürfen ausschließlich echte Strukturknoten übernommen werden.

==================================================
SPALTE C – EBENE
==================================================

Die Ebene ergibt sich ausschließlich aus der Dokumenthierarchie.

Regeln:

Ebene 0:
Gesamtdokument

Direkter Unterknoten:
+1 Ebene

Geschwisterknoten:
gleiche Ebene

Die Hierarchie muss vollständig konsistent sein.

==================================================
ABSOLUTE VOLLSTÄNDIGKEITSREGEL
==================================================

Vor dem Schreiben in die Excel:

1. Dokument vollständig lesen.
2. Alle Strukturknoten identifizieren.
3. Interne vollständige Strukturknotenliste erzeugen.
4. Vollständigkeit prüfen.
5. Erst danach Excel befüllen.

Während der Excel-Erstellung dürfen keine neuen Strukturknoten mehr erkannt werden.

==================================================
QUALITÄTSPRÜFUNG
==================================================

Prüfe abschließend:

- Jeder Strukturknoten wurde genau einmal erfasst.
- Kein Strukturknoten wurde ausgelassen.
- Kein Strukturknoten wurde doppelt erfasst.
- Die Reihenfolge entspricht exakt dem Dokument.
- Die Hierarchie ist vollständig konsistent.
- Jeder Strukturknoten besitzt genau eine Excel-Zeile.

Speichere die bearbeitete Excel-Datei.
