#!/usr/bin/env python
# coding=utf-8

import inkex

# ---------------------------------

# UTILITIES

# English based locales

EN_ASCII = " A1B'K2L@CIF/MSP\"E3H9O6R^DJG>NTQ,*5<-U8V.%[$+X!&;:4\\0Z7(_?W]#Y)="

# Spanish based locales

ES_NUMBERS = {
    "1": 0x2801,
    "2": 0x2803,
    "3": 0x2809,
    "4": 0x2819,
    "5": 0x2811,
    "6": 0x280B,
    "7": 0x281b,
    "8": 0x2813,
    "9": 0x280a,
    "0": 0x281a,
}

ES_LETTERS = {
    "A": 0x2801,
    "B": 0x2803,
    "C": 0x2809,
    "D": 0x2819,
    "E": 0x2811,
    "F": 0x280B,
    "G": 0x281b,
    "H": 0x2813,
    "I": 0x280a,
    "J": 0x281a,
    "K": 0x2805,
    "L": 0x2807,
    "M": 0x280d,
    "N": 0x281d,
    "Ñ": 0x283b,
    "O": 0x2815,
    "P": 0x280f,
    "Q": 0x281f,
    "R": 0x2817,
    "S": 0x280e,
    "T": 0x281e,
    "U": 0x2825,
    "V": 0x2827,
    "W": 0x283a,
    "X": 0x282d,
    "Y": 0x283d,
    "Z": 0x2835,
}

ES_SIGNS = {
    "ª": 0x2801,  # ordinal (feminine)  -> same as A
    "º": 0x2815,  # ordinal (masculine) -> same as O
    "&": 0x282f,
    ".": 0x2804,
    ",": 0x2802,
    ":": 0x2812,
    ";": 0x2806,
    "¿": 0x2822,
    "?": 0x2822,
    "¡": 0x2816,
    "!": 0x2816,
    '"': 0x2826,
    "(": 0x2823,
    ")": 0x281c,
    "-": 0x2824,
    "*": 0x2814,
    "=": 0x2836,
    "÷": 0x2832,
    "+": 0x2816,
    "@": 0x2810,
    " ": 0x2800,  # braille space
}

ES_PREFIXES = {
    chr(15): 0x2828,  # uppercase prefix: https://codepoints.net/U+000F
}

ES_ACCENT_MARKS = {
    "Á": 0x2837,
    "É": 0x282e,
    "Í": 0x280c,
    "Ó": 0x282c,
    "Ú": 0x283e,
    "Ü": 0x2833,
}

ES_COMBINATIONS = {
    # signs
    "%": (0x2838, 0x2834),
    "‰": (0x2838, 0x2834, 0x2834),  # per mile
    "©": (0x2823, 0x2828, 0x2809, 0x281c),
    "®": (0x2823, 0x2828, 0x2817, 0x281c),
    "℗": (0x2823, 0x2828, 0x280f, 0x281c),
    "🄯": (0x2823, 0x2828, 0x2807, 0x281c),
    "/": (0x2820, 0x2802),
    "\\": (0x2810, 0x2804),
    "<": (0x2810, 0x2805),
    ">": (0x2828, 0x2802),
    "|": (0x2838, 0x2807),
    "{": (0x2810, 0x2807),
    "}": (0x2838, 0x2802),
    "—": (0x2824, 0x2824),

    # currencies
    "€": (0x2838, 0x2811),
    "$": (0x2838, 0x280e),
    "¢": (0x2818, 0x2809),
    "£": (0x2810, 0x282e),
    "¥": (0x2838, 0x283d),
    "￥": (0x2838, 0x283d),
}

CA_ACCENT_MARKS = {
    "É": 0x283f,
    "Í": 0x280c,
    "Ó": 0x282a,
    "Ú": 0x283e,
    "À": 0x2837,
    "È": 0x282e,
    "Ò": 0x282c,
    "Ï": 0x283b,
    "Ü": 0x2833,
    "Ç": 0x282f,
}

# END: UTILITIES

# ---------------------------------

# LOCALE FUNCTIONS

def en_char_map(char):
    # https://en.wikipedia.org/wiki/Braille_ASCII#Braille_ASCII_values
    try:
        mapint = EN_ASCII.index(char.upper())
    except ValueError:
        return char
    return chr(mapint + 0x2800)

def es_char_map(char):
    """Spanish/Galician/Euskera chars mappers.

    Source: https://sid.usal.es/idocs/F8/FDO12069/signografiabasica.pdf
    """
    if char.isnumeric():
        # numeric prefix + number
        return "".join([chr(0x283c), chr(ES_NUMBERS[char])])
    try:
        bcharint = {
            **ES_LETTERS,
            **ES_ACCENT_MARKS,
            **ES_SIGNS,
            **ES_PREFIXES,
        }[char.upper()]
    except KeyError:
        try:
            # combinations
            return "".join([chr(num) for num in ES_COMBINATIONS[char]])
        except KeyError:
            return char
    else:
        # if uppercase, add uppercase prefix before letter
        if char.isupper():
            return "".join([chr(0x2828), chr(bcharint)])
        return chr(bcharint)

def ca_char_map(char):
    """Catalan/Valencian chars mappers. Uses the same implementation as
    Spanish but different accent marks.

    Source: https://sid.usal.es/idocs/F8/FDO12069/signografiabasica.pdf
    """
    if char.isnumeric():
        # numeric prefix + number
        return "".join([chr(0x283c), chr(ES_NUMBERS[char])])
    try:
        bcharint = {
            **ES_LETTERS,
            **CA_ACCENT_MARKS,
            **ES_SIGNS,
            **ES_PREFIXES,
        }[char.upper()]
    except KeyError:
        try:
            # combinations
            return "".join([chr(num) for num in ES_COMBINATIONS[char]])
        except KeyError:
            return char
    else:
        # if uppercase, add uppercase prefix before letter
        if char.isupper():
            return "".join([chr(0x2828), chr(bcharint)])
        return chr(bcharint)

# END: LOCALE FUNCTIONS

LOCALE_CHARMAPS = {
    "en": en_char_map,
    "es": es_char_map,
    "gl": es_char_map,  # Galician uses Spanish alphabet
    "eu": es_char_map,  # Euskera hasn't accent marks but uses Spanish alphabet
    "ca": ca_char_map,  # Catalan/Valencian
}

# ---------------------------------

# EXTENSION

class BrailleL18n(inkex.TextExtension):
    """Convert to Braille giving a localized map of replacements."""
    def add_arguments(self, pars):
        pars.add_argument(
            "-l", "--locale", type=str, dest="locale", default="en",
            choices=LOCALE_CHARMAPS.keys(),
            help="Locale to use converting to Braille.",
        )
    
    def process_chardata(self, text):
        """Replaceable chardata method for processing the text."""
        return ''.join(map(LOCALE_CHARMAPS[self.options.locale], text))

if __name__ == '__main__':
    BrailleL18n().run()
