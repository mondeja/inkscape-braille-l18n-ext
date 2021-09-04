# Contributions guide

You only need Inkscape>=1.0, a posix shell and (optionally) the
[xvfb][xvfb-package] package to develop and test.

## Make changes to the code

1. Move [text_braille_l18n.inx][ext-inx] and [text_braille_l18n.py][ext-py]
 files to your user's extensions directory. If you don't know its location,
 open it from `Edit` -> `Preferences` -> `System` -> `Users extensions`.
1. Edit the code there.
1. Once edited and manually tested, move the files to this repository, it's
 time to run tests.

## Test your changes

- `sh tests/run.sh`: Run tests.

### Environment variables

Some environment variables can be defined to control the execution of tests:

- `LOCALES=en,es sh tests/run.sh`: Run tests for specified alphabets.
- `DEBUG=1 sh tests/run.sh`: Run tests showing all executed commands (mainly
 for tests script debugging).
- `GUI=1 sh tests/run.sh`: Run tests in GUI mode (showing Inkscape UI).
- `NO_COLOR=1 sh tests/run.sh`: Run tests showing differences between produced
 and expected output in black/white (by default colored output). See
 [`NO_COLOR` standard][no-color-standard].

You'll see that a folder is created under `tests/tmp/` where the output for
each locale is stored.

---

## How to add a new language?

1. Check the official established encoding specification for your language in
 the document [World Braille Usage][world-braille-usage]. Search the document
 for the language, but note that will be written in that language, so translate
 it to your language using an online translator if you can't follow it.
1. Create the option for the language in `text_braille_l18n.inx` inside
 `locale` parameter.
1. Create a function for characters mapping for the language in
 `text_braille_l18n.py`. Use other languages as reference if you don't know how
 to structure it.
1. Include that function in `LOCALE_CHARMAPS`, being the key the
 [ISO-639-1][iso-639-1] correspondent to the language.
1. Create the expected file for the locale in `tests/{locale}.expect.txt`.
1. Add the language to README [Supported alphabets][supported-alphabets-table]
 table.
1. Add a section with details about the implementation for that language in
 [NOTES.md][notes]. This is specially useful if the implementation contains
 singularities and will help future developers to maintain the code.

## Some tricks developing

- Convert Braille unicode character to hexadecimal integer representation:
 `hex(ord("⠿"))`.
- Convert hexadecimal integer representation to Braille unicode character:
 `chr(0x283f)`.
- Copy Braille unicode character from [Braille ASCII Wikipedia page][en-wiki].
 You can search by their binary representation, for example: `⠽` would be
 `101111`.

<!-- Internal links -->

[ext-inx]: https://github.com/mondeja/inkscape-braille-l18n-ext/blob/master/text_braille_l18n.inx
[ext-py]: https://github.com/mondeja/inkscape-braille-l18n-ext/blob/master/text_braille_l18n.py
[supported-alphabets-table]: https://github.com/mondeja/inkscape-braille-l18n-ext#supported-alphabets
[notes]: https://github.com/mondeja/inkscape-braille-l18n-ext/blob/master/NOTES.md

<!-- External links -->

[xvfb-package]: https://packages.debian.org/es/sid/xvfb
[no-color-standard]: https://no-color.org
[en-wiki]: https://en.wikipedia.org/wiki/Braille_ASCII
[world-braille-usage]: https://1kru3o1eyt4f2w3qy21ds14w-wpengine.netdna-ssl.com/wp-content/uploads/2021/07/world-braille-usage-third-edition.pdf
[iso-639-1]: https://en.wikipedia.org/wiki/ISO_639-1
