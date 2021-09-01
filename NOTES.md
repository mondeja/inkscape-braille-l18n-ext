# Implementation notes

## English - North American Braille ASCII code

Same implementation as the current Inkscape `text_braille`  extension.

## Spanish - Braille español (Grado 1)

Implementation of [CBE guide][cbe-guide] for uniformed Spanish Braille.

- According to the guide, numbers with 10 or more digits and telephone numbers
 must be preceded by a numeric prefix `⠼` in the first number only. But
 this implementation currently precede the numerical prefix before any number.

## Galician - Braille español (Grado 1)

Uses same implementation as Spanish.

## Basque - Braille español (Grado 1)

Uses same implementation as Spanish.

## Catalan/Valencian

- Uses same implementation as Spanish except for accent marks which differs.
- The character "L geminate" has not been found in unicode database.

# Other useful resources

- [World Braille Usage][world-braille-usage]

[cbe-guide]: https://sid.usal.es/idocs/F8/FDO12069/signografiabasica.pdf
