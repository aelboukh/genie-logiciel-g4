# genie-logiciel-g4

Dans cette version  on réaliser un fichier choix.bat

+xml.bat:

-Ce fichier fait le fonctionnement des deux fichiers précédent (bach.bat & xml.bat) sauf que y a une amélioration dans la coté du convertation au XML.

-Ce fichier permet de de faire le choix de convertation (XML ou TXT). Aprés la convertation ce fichier créer un dossier text1 pour les fichiers TXT qui sont convertés et un autre dossier textXml pour les fichiers XML qui sont convertés.
comment utiliser

red_circle IMPORTANT ! : il faut déplacer vos fichiers pdfs dans le dossier Papers red_circle

Etape 1

-pour consulter les fichiers pdf et les indices dans votre dossier Papers executez la commande

    ./convert1.bat


pour convertir la forme de coverte(txt ou XML)
executez la commande :
     ./choix.bat -t *indice* pour  obtenir un fichier txt
     ./choix.bat -x *indice* pour  obtenir un fichier XML

Etape 2

-Pour convertir un fichier pdf vous pouvez choisir votre fichier pdf en saisissant le numéro du fichier dans le dossier (numero selon l'ordre du pdf dans le dossier) et choisir le type de la sortie XML ou TXT donc la commande sera de cette façon:

    gl-tp-scrum$ ./choix.bat -t 1 2 : cette commande convetit le pdf d'indice 1 et 2 en Format text.

    gl-tp-scrum$ ./choix.bat -x 1 2 : cette commande convetit le pdf d'indice 1 et 2 en Format XML.

