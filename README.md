Baas over eigen mail
====================

Ben jij baas over je eigen mail? Weet je waar je mail langs gaat voor het zijn doel bereikt? Wie heeft er nog meer inzage in jouw mail?

Ontwerp
-------

Een standaard analyse voor mail is om te kijken hoe dit in DNS afgehandeld wordt. Daarin wordt technisch aangegeven op welk adres mail voor een domein moet worden afgeleverd. Dit werkte tot een paar jaar terug nog wel, maar tegenwoordig wordt er veel spamfiltering gedaan voor mail bij de bestemming wordt afgeleverd. Dit geeft al aan dat je niet meer volledig baas over je eigen mail bent, maar maakt de volledige analyse ook moeilijk.

In dit project analyseren we het probleem van de andere kant, als een mail wordt verstuurd vanaf de mailserver, welke weg legt het dan af naar onze mailserver?

Het idee is als volgt:

- Simpele webpagina met uitleg, en een `mailto` link om een test te starten
- Mail naar dat adres wordt op een of andere wijze gecorreleerd (subject of uniek gegenereerd adres)
- Script analyseert alle `Received` headers en verwerkt dat met GeoIP
- Website toont gebruiker een kaart met het traject en extra info.

Implementatie
-------------

De implementatie is redelijk gevorderd.

- Er is een mail-opvang script `baas_filter.py` (dit kan ingezet worden met een `.forward`)
- Er is een website backend (in Django `/baas/`)

Volgende dingen ontbreken nog:
- Frontend en design
- Extracten van de juiste informatie uit `Received` headers (regex?)
- Koppelen van een gebruiker aan een resultaat
