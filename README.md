# Braille l18n Inkscape extension

![Inkscape versions][inkscape-versions-badge]
[![Tests][tests-image]][tests-link]
[![License][license-image]][license-link]

Text-to-Braille Inkscape extension with multiple localized alphabets.

## Supported alphabets

| Locale | Source |
| ------ | ------ |
| English | [North American Braille ASCII code][en-wiki] |
| Spanish | [Braille español (Grado 1)][es-cbe-guide] by [CBE][cbe-once] |
| Galician | [Braille español (Grado 1)][es-cbe-guide] by [CBE][cbe-once] |
| Euskera | [Braille español (Grado 1)][es-cbe-guide] by [CBE][cbe-once] |
| Catalan/Valencian | [Braille español (Grado 1)][es-cbe-guide] by [CBE][cbe-once] |

> See [NOTES.md][notes] to check the limitations of each implementation.

## Installation

1. [Download][download-repo] and extract this repository.
1. Move [text_braille_l18n.inx][ext-inx] and [text_braille_l18n.py][ext-py]
 files to your user's extensions directory. If you don't know its location,
 open it from `Edit` -> `Preferences` -> `System` -> `Users extensions`.
1. Run Inkscape and you'll see the extension in `Extensions` -> `Text`.

## Usage

1. Select a text that you want to convert in Braille.
1. Open this extension.
1. Choose an alphabet for character mappings.
1. Press `Apply`.

<!-- Badges -->

[inkscape-versions-badge]: https://img.shields.io/static/v1?label=inkscape&message=1.0%20|%201.1&color=blue&logo=Inkscape
[tests-image]: https://img.shields.io/github/workflow/status/mondeja/inkscape-braille-l18n-ext/CI?logo=github&label=tests
[tests-link]: https://github.com/mondeja/inkscape-braille-l18n-ext/actions?query=workflow%3ACI
[license-image]: https://img.shields.io/static/v1?label=license&message=BSD-3-Clause&color=brightgreen&logo=freebsd
[license-link]: https://github.com/mondeja/inkscape-braille-l18n-ext/blob/master/LICENSE

<!-- Internal links -->

[notes]: https://github.com/mondeja/inkscape-braille-l18n-ext/blob/master/NOTES.md
[download-repo]: https://github.com/mondeja/inkscape-braille-l18n-ext/archive/refs/heads/master.zip
[ext-inx]: https://github.com/mondeja/inkscape-braille-l18n-ext/blob/master/text_braille_l18n.inx
[ext-py]: https://github.com/mondeja/inkscape-braille-l18n-ext/blob/master/text_braille_l18n.py

<!-- Sources -->

[en-wiki]: https://en.wikipedia.org/wiki/Braille_ASCII
[es-cbe-guide]: https://sid.usal.es/idocs/F8/FDO12069/signografiabasica.pdf
[cbe-once]: https://www.once.es/servicios-sociales/braille/comision-braille-espanola/comision-braille-espanola-cbe
[world-braille-usage]: https://1kru3o1eyt4f2w3qy21ds14w-wpengine.netdna-ssl.com/wp-content/uploads/2021/07/world-braille-usage-third-edition.pdf
