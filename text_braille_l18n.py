#!/usr/bin/env python
# coding=utf-8

__version__ = "0.0.1"

import inkex

def en_char_map(char):
    # https://en.wikipedia.org/wiki/Braille_ASCII#Braille_ASCII_values
    try:
        mapint = ("A1B'K2L@CIF/MSP\"E3H9O6R^DJG>NTQ,"
                  "*5<-U8V.%[$+X!&;:4\\0Z7(_?W]#Y)=").index(char.upper())
    except ValueError:
        return char
    return chr(mapint + 0x2801)

def es_char_map(char):
    # https://sid.usal.es/idocs/F8/FDO12069/signografiabasica.pdf
    if char.isnumeric():
        # numeric prefix + number
        return "".join([
            chr(0x283c),
            chr({
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
            }[char]),
        ])
    try:
        bchar = chr({
            # letters
            "A": 0x2801,
            "ª": 0x2801,  # ordinal (feminine)
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
            "º": 0x2815,  # ordinal (masculine)
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
            "Á": 0x2837,
            "É": 0x282e,
            "Í": 0x280c,
            "Ó": 0x282c,
            "Ú": 0x283e,
            "Ü": 0x2833,

            # signs
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

            # prefixes
            chr(15): 0x2828,  # uppercase prefix: https://codepoints.net/U+000F
            "#": 0x283c,      # numerical prefix
        }[char.upper()])
    except KeyError:
        try:
            # combinations
            return {
                "%": chr(0x2838) + chr(0x2834),
                "‰": chr(0x2838) + chr(0x2834) + chr(0x2834),  # per mile
                "©": chr(0x2823) + chr(0x2828) + chr(0x2809) + chr(0x281c),
                "®": chr(0x2823) + chr(0x2828) + chr(0x2817) + chr(0x281c),
                "/": chr(0x2820) + chr(0x2802),
                "\\": chr(0x2810) + chr(0x2804),
                "<": chr(0x2810) + chr(0x2805),
                ">": chr(0x2828) + chr(0x2802),
                "|": chr(0x2838) + chr(0x2807),
                "{": chr(0x2810) + chr(0x2807),
                "}": chr(0x2838) + chr(0x2802),
                "—": chr(0x2824) + chr(0x2824),

                # currencies
                "€": chr(0x2838) + chr(0x2811),
                "$": chr(0x2838) + chr(0x280e),
                "¢": chr(0x2818) + chr(0x2809),
                "£": chr(0x2810) + chr(0x282e),
                "¥": chr(0x2838) + chr(0x283d),
                "￥": chr(0x2838) + chr(0x283d),
            }[char]
        except KeyError:
            return char
    else:
        # if uppercase, add uppercase prefix before letter
        return "".join([chr(0x2828) if char.isupper() else '', bchar])

LOCALE_CHARMAPS = {
    "en": en_char_map,
    "es": es_char_map,
}

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
