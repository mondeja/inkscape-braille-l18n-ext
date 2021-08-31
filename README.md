# Braille l18n Inkscape extension

This extension adds localized capabilities to Inkscape's built-in
text-to-Braille converter.

## Supported alphabets

| Locale | Description |
| ------ | ----------- |
| English | [North American Braille ASCII code][en-wiki] |
| Spanish | [Braille español (Grado 1)][es-cbe-guide] by [CBE][cbe-once] |

## Installation

1. Download this repository.
1. Move `text_braille_l18n.inx` and `text_braille_l18n.py` files to your user's
 extensions directory. If you don't know its location, open it from `Edit` ->
 `Preferences` -> `System` -> `Users extensions`.
1. Run Inkscape and you'll see the extension in `Extensions` -> `Text`.

## How to use

Select a text that you want to convert in Braille, open this extension,
choose a locale and press `Apply`.

## TODO

- [x] ~~Spanish Braille conversion for texts not prepared for Braille
 translation. Add prefixes before numbers and before uppercased letters.~~
- [ ] Catalán/valenciano ([link](https://www.once.es/servicios-sociales/braille))
- [ ] Gallego ([link](https://www.once.es/servicios-sociales/braille))
- [ ] Euskera ([link](https://www.once.es/servicios-sociales/braille))
- [x] ~~Spanish combinations ([link](https://sid.usal.es/idocs/F8/FDO12069/signografiabasica.pdf))~~

[en-wiki]: https://en.wikipedia.org/wiki/Braille_ASCII
[es-cbe-guide]: https://sid.usal.es/idocs/F8/FDO12069/signografiabasica.pdf
[cbe-once]: https://www.once.es/servicios-sociales/braille/comision-braille-espanola/comision-braille-espanola-cbe
