#!/bin/sh

: '
  Tests for braille-l18n Inkscape extension. You must have Inkscape installed
  in order to run this script. WARNING: if braille-l18n extension files are
  found inside your user extensions directory will be overwritten by the
  development files located in this directory!

  Environment variables:

  - DEBUG: If not empty, all executed commands will be shown in the output.
  - LOCALES: Specify a set of locales to test, separated by commas. If empty,
      all locales will be tested.
  - GUI: If not empty, the tests will be executed in GUI mode, which is useful
      if you need to debug errors from the extension. If not active, exceptions
      like syntax errors in the extension will cause the Inkscape batch command
      execution to be frozen.
  - NO_COLOR: If defined, the difference between expected and produced output
      and will be shown in black/white.
'

error() {
  printf "$1" >&2
}

configure_script() {
  set -e
  if [ -n "$DEBUG" ]; then
    set -x
  fi

  if [ ! -f "text_braille_l18n.inx" ]; then
    error "You must be at the root of the directory to execute the tests.\n"
    exit 1
  fi
}

prepare_tmp_folder() {
  rm -rf tests/tmp/
  mkdir tests/tmp/
}

print_user_extensions_directory() {
  printf "$(inkscape --user-data-directory)/extensions"
}

move_extension_to_user_extensions_directory() {
  extensions_directory="$(print_user_extensions_directory)"
  rm -f "$extensions_directory/text_braille_l18n.*"
  cp text_braille_l18n.* "$extensions_directory"
}

: '
  Configure preferences.xml file so the extension braille-l18n can be
  configured to use the parameters specified for the test.

  $1 - Locale parameter.
'
configure_profile_preferences() {
  locale="$1"
  preferences_filepath="$(inkscape --user-data-directory)/preferences.xml"
  locale_pref="$(< $preferences_filepath grep -o "org.inkscape.text.braille-l18n.locale" || true)"

  # if locale preference is present
  if [ -n "$locale_pref" ]; then
    # replace value with locale passed as function argument
    sed -i -r "s/org.inkscape.text.braille-l18n.locale=\"(.+)\"/org.inkscape.text.braille-l18n.locale=\"$locale\"/g" "$preferences_filepath"
  else
    # add extension preference after 'id="extensions"' line (extensions group)
    sed -i "s/id=\"extensions\"/&\n   org.inkscape.text.braille-l18n.locale=\"$locale\"/g" "$preferences_filepath"
  fi;
}

get_locales() {
  # read all locales from inx extension file
  echo "$(< "$PWD/text_braille_l18n.inx" grep '<option value=' | cut -d'"' -f2)"
}

: '
  Extract Braille output from a produced SVG running a test using Inkscape,
  for further comparison.

  $1 - Path to the SVG file which Braille output will be extracted.
'
extract_svg_output_text() {
  < "$1" grep 'id="tspan' | cut -d'>' -f2
}

test_extension_effect() {
  locale="$1"
  svg_output_filepath="$PWD/tests/tmp/$locale.out.svg"
  txt_output_filepath="tests/tmp/$locale.out.txt"
  txt_expect_filepath="tests/$locale.expect.txt"

  printf "TEST: locale=$locale\n"

  # if test file doesn't exists
  if [ ! -f "$txt_expect_filepath" ]; then
    error "File '$txt_expect_filepath' was expected to exist but not found!\n\n"
    printf "1" > "tests/tmp/exitcode"
    return 0
  fi;

  # configure parameters for extension
  configure_profile_preferences "$locale"

  # Xvfb command used
  xvfb_command="xvfb-run --auto-servernum"
  if [ -n "$GUI" ]; then
    xvfb_command=""
  fi

  # run extension using inkscape in headless mode with Xvfb
  $xvfb_command inkscape \
    --batch-process \
    --export-plain-svg \
    --vacuum-defs \
    --actions="select-by-element:text;
org.inkscape.text.braille-l18n.noprefs;
export-filename:$svg_output_filepath;
export-do;" \
    tests/input.svg

  # extract braille output from produced SVG and save in other file
  extract_svg_output_text "$svg_output_filepath" > "$txt_output_filepath"

  if ! diff --brief "$txt_output_filepath" "$txt_expect_filepath"; then
    printf "<: $txt_output_filepath\n>: $txt_expect_filepath\n"

    # set ouput color format
    color_option="--color"
    if [ -n "$NO_COLOR" ]; then
      color_option=""
    fi

    # ignore error (or file exits due to 'set -e')
    diff $color_option "$txt_output_filepath" "$txt_expect_filepath" || true
    printf "\n"
    printf "1" > "tests/tmp/exitcode"
  else
    printf "\n"
  fi
}

run_tests() {
  get_locales | tr ' ' '\n' | while read locale; do
    # filter locales if 'LOCALE' environment variable is specified
    if [ -n "$LOCALES" ] && [ -z "$(printf "$LOCALES" | grep -o "$locale")" ]; then
      continue
    fi
    test_extension_effect "$locale"
  done
}

cleanup_and_exit() {
  if [ -f "tests/tmp/exitcode" ]; then
    exitcode="$(cat tests/tmp/exitcode)"
    rm tests/tmp/exitcode
  else
    exitcode=0
  fi
  exit $exitcode
}

main() {
  configure_script
  prepare_tmp_folder
  move_extension_to_user_extensions_directory
  run_tests
  cleanup_and_exit
}

main
