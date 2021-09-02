# Contributions guide

You only need Inkscape>=1.0, [xvfb][xvfb-package] and a posix shell to develop
and test.

## Make changes to the code

1. Move [text_braille_l18n.inx][ext-inx] and [text_braille_l18n.py][ext-py]
 files to your user's extensions directory. If you don't know its location,
 open it from `Edit` -> `Preferences` -> `System` -> `Users extensions`.
1. Edit the code there.
1. Once edited and manually tested, move the files to this repository, it's
 time to run tests.

## Test your changes

- `sh tests/run.sh`: Run tests.
- `DEBUG=1 sh tests/run.sh`: Run tests showing all executed commands (mainly
 for tests script debugging).

You'll see that a folder is created under `tests/tmp/` where the output for
every locale is stored.

[xvfb]: https://packages.debian.org/es/sid/xvfb
[ext-inx]: https://github.com/mondeja/inkscape-braille-l18n-ext/blob/master/text_braille_l18n.inx
[ext-py]: https://github.com/mondeja/inkscape-braille-l18n-ext/blob/master/text_braille_l18n.py
