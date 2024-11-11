# LaTex Einrichtung

- Plugins installieren 
   - Siehe dazu: https://hannah-sten.github.io/TeXiFy-IDEA/installation-guide.html       
      - Hab auch den vorgeschlagenen PDF Viewer genommen   
   - Zusätzlich ist was für .bat files nötig
- MikTex installieren
  - https://miktex.org/download
    - **WICHTIG**: Dabei nicht wie Alex verkacken und beim installieren beachten: `Install missing packages on the fly: yes`
    - Hab danach mal neugestartet
    - Nach dem Installieren das Programm öffnen und bei Pakete die Paketdatenbank aktualisieren
![img.png](BilderReadme/update db image.png)
- In Pycharm eine neue run config hinzufügen, hab meine als run config ins repo gelegt, hier aber als Beispiel
  - ![img.png](BilderReadme/run config.png)
  - WICHTIG: Im Arbeitsverzeichnis den LaTex Ordner angeben und als Skript die `compile.bat` auswählen

- Danach den run ausführen, kann beim ersten Mal was dauern weil der Pakete installiert