#!/bin/bash

out="content/pages/publications.htm"

echo "<html>
    <head>
        <title>Publications</title>
    </head>
    <body>
        <H2>Congress Proceedings or Abstracts</H2>" > $out

curl --silent ""https://api.zotero.org/groups/206974/collections/E34TM43M/items?format=bib\&style=journal-of-medical-internet-research"" >> $out

echo "    </body>
</html>" >> $out
