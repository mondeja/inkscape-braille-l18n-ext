# Implementation notes

You can use the document [World Braille Usage][world-braille-usage] to consult
what language you must use for your country.

## English - North American Braille ASCII code

Implementation of [North American Braille ASCII code][en-wiki].

## Spanish - Braille español (Grado 1)

Implementation of [CBE guide][es-cbe-guide].

### Numbers treatment

- According to the guide, numbers with 10 or more digits and telephone numbers
 must be preceded by a numeric prefix `⠼` in the first number only. But
 this implementation currently precede the numerical prefix before any number.

## French - Code Braille Français Uniformisé (CBFU)

Implementation of [Code Braille Français Uniformisé (CBFU)][fr-cbfu].

- Ordinals are ignored.

## German - Das System der deutschen Brailleschrift

Implementation of [Das System der deutschen Brailleschrift][de-system] (created
by [BSKDL][bskdl]).

### Capital letters treatment

The handling of capital letters has been simplified in this implementation.
The [guide][de-system] indicates that:

1. Individual capital letters and sequences of capital letters are identified
 by placing the character‌ `⠘` in front of them (capital letter ad symbol).
1. Lowercase letters are marked by prefixing them with the character `⠠`
 (lowercase advertisement character).

However, these rules don't apply. For each capital letter, only the character
`⠨` is prepended regardless of its context.

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
[de-system]: http://bskdl.org/textschrift.html
[bskdl]: http://bskdl.org
[world-braille-usage]: https://1kru3o1eyt4f2w3qy21ds14w-wpengine.netdna-ssl.com/wp-content/uploads/2021/07/world-braille-usage-third-edition.pdf
