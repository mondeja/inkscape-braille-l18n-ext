# Implementation notes

You can use the document [World Braille Usage][world-braille-usage] to consult
what language you must use for your country.

## English - North American Braille ASCII code

Implementation of [North American Braille ASCII code][en-wiki].

## Spanish - Braille español (Grado 1)

Implementation of [CBE guide][es-cbe-guide].

- According to the guide, numbers with 10 or more digits and telephone numbers
 must be preceded by a numeric prefix `⠼` in the first number only. But
 this implementation currently precede the numerical prefix before any number.

## French - Code Braille Français Uniformisé (CBFU)

Implementation of [Code Braille Français Uniformisé (CBFU)][fr-cbfu].

## Galician - Braille español (Grado 1)

Uses same implementation as Spanish.

## Basque - Braille español (Grado 1)

Uses same implementation as Spanish.

## Catalan/Valencian

- Uses same implementation as Spanish except for accent marks which differs.
- The character "L geminate" has not been found in unicode database.

[en-wiki]: https://en.wikipedia.org/wiki/Braille_ASCII
[es-cbe-guide]: https://sid.usal.es/idocs/F8/FDO12069/signografiabasica.pdf
[fr-cbfu]: https://www.avh.asso.fr/sites/default/files/cbfu_edition_internationale_1.pdf
[world-braille-usage]: https://1kru3o1eyt4f2w3qy21ds14w-wpengine.netdna-ssl.com/wp-content/uploads/2021/07/world-braille-usage-third-edition.pdf
