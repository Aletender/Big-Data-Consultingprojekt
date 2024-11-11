echo "Um dieses Skript zu nutzen, muss detex auf dem Rechner installiert sein."
echo "Unter macOS kann es mit dem folgenden Befehl installiert werden: brew install opendetex"

# Entferne die Datei mit den Wortzählungen, falls sie existiert
rm total_count.txt 2> /dev/null

# Extrahiere den Text ohne LaTeX-Kommandos aus der Hauptdatei
detex thesis_main.tex > thesis_main.txt

# Definiere die Begriffe, um den relevanten Abschnitt des Textes zu identifizieren
START_MARKER="Einleitung"
END_MARKER="Anhang"
TEXT_SECTION_FOUND="n"

while read line; do
  # Beende das Lesen der Datei, wenn der Endmarker gefunden wurde
  echo "$line" | grep $END_MARKER && break
  if [ "$TEXT_SECTION_FOUND" == "y" ]; then
      # Speichere die Zeilen im Zielbereich in die Wortzähldatei
      echo "$line" >>total_count.txt
      # Uncomment the following line if you want to remove specific patterns from the text
      # echo "$line" | sed 's/\[[\w. ]*\][[\w. ]*\]\w+\.\w+/ /g' >>total_count.txt
  fi
  # Beginne das Speichern der Zeilen, wenn der Startmarker gefunden wurde
  echo "$line" | grep $START_MARKER >/dev/null && TEXT_SECTION_FOUND="y"
done <thesis_main.txt

echo
echo "Anzahl der Wörter vom Kapitel Einleitung bis Anhang:"
wc -w total_count.txt # Ausgabe der Anzahl von Zeilen, Wörtern und Zeichen
# Bereinige die temporären Dateien
rm total_count.txt 2> /dev/null
rm thesis_main.txt 2> /dev/null

rm bericht.html 2> /dev/null
texcount -html -inc -sum  thesis_main.tex > bericht.html
echo "report generated in bericht.html"
