#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class Backness(Enum):
    FRONT = 1
    NEAR_FRONT = 1.5
    CENTRAL = 2
    NEAR_BACK = 2.5
    BACK = 3


class Height(Enum):
    CLOSE = 0
    NEAR_CLOSE = 0.3
    CLOSE_MID = 0.6
    MID = 1
    OPEN_MID = 1.3
    NEAR_OPEN = 1.6
    OPEN = 2


class Vowel(Enum):
    i = (
        "i",
        False,
        Backness.FRONT,
        Height.CLOSE,
        False,
        "Close front unrounded vowel",
        "\u0069",
        301,
    )
    y = (
        "y",
        True,
        Backness.FRONT,
        Height.CLOSE,
        False,
        "Close front rounded vowel",
        "\u0079",
        309,
    )
    e = (
        "e",
        False,
        Backness.FRONT,
        Height.CLOSE_MID,
        False,
        "Close-mid front unrounded vowel",
        "\u0065",
        302,
    )
    ø = (
        "ø",
        True,
        Backness.FRONT,
        Height.CLOSE_MID,
        False,
        "Close-mid front rounded vowel",
        "\u00F8",
        310,
    )
    #    ø = ("ø", True, Backness.FRONT, Height.MID, False, "mid front rounded vowel") - no dedicated IPA symbol
    ɛ = (
        "ɛ",
        False,
        Backness.FRONT,
        Height.OPEN_MID,
        False,
        "Open-mid front unrounded vowel",
        "\u025B",
        303,
    )
    œ = (
        "œ",
        True,
        Backness.FRONT,
        Height.OPEN_MID,
        False,
        "Open-mid front rounded vowel",
        "\u0153",
        311,
    )
    æ = (
        "æ",
        False,
        Backness.FRONT,
        Height.NEAR_OPEN,
        False,
        "Near-open front unrounded vowel",
        "\u00E6",
        325,
    )
    a = (
        "a",
        False,
        Backness.FRONT,
        Height.OPEN,
        False,
        "Open front unrounded vowel",
        "\u0061",
        304,
    )
    ɶ = (
        "ɶ",
        True,
        Backness.FRONT,
        Height.OPEN,
        False,
        "Open front rounded vowel",
        "\u0276",
        312,
    )
    ɪ = (
        "ɪ",
        False,
        Backness.NEAR_FRONT,
        Height.NEAR_CLOSE,
        False,
        "Near-close front unrounded vowel",
        "\u026A",
        319,
    )
    ʏ = (
        "ʏ",
        True,
        Backness.NEAR_FRONT,
        Height.NEAR_CLOSE,
        False,
        "Near-close front rounded vowel",
        "\u028F",
        320,
    )
    ɨ = (
        "ɨ",
        False,
        Backness.CENTRAL,
        Height.CLOSE,
        False,
        "Close central unrounded vowel",
        "\u0268",
        317,
    )
    ʉ = (
        "ʉ",
        True,
        Backness.CENTRAL,
        Height.CLOSE,
        False,
        "Close central rounded vowel",
        "\u0289",
        316,
    )
    ɘ = (
        "ɘ",
        False,
        Backness.CENTRAL,
        Height.CLOSE_MID,
        False,
        "Close-mid central unrounded vowel",
        "\u0258",
        397,
    )
    ɵ = (
        "ɵ",
        True,
        Backness.CENTRAL,
        Height.CLOSE_MID,
        False,
        "Close-mid central rounded vowel",
        "\u0275",
        323,
    )
    ə = (
        "ə",
        None,
        Backness.CENTRAL,
        Height.MID,
        False,
        "mid central vowel",
        "\u0259",
        322,
    )  # schwa
    ɜ = (
        "ɜ",
        False,
        Backness.CENTRAL,
        Height.OPEN_MID,
        False,
        "Open-mid central unrounded vowel",
        "\u025C",
        326,
    )
    ɞ = (
        "ɞ",
        True,
        Backness.CENTRAL,
        Height.OPEN_MID,
        False,
        "Open-mid central rounded vowel",
        "\u025E",
        395,
    )
    ɐ = (
        "ɐ",
        None,
        Backness.CENTRAL,
        Height.NEAR_OPEN,
        False,
        "Near-open central vowel",
        "\u0250",
        324,
    )
    #   a = ("a", False, Backness.CENTRAL, Height.OPEN, False, "Open central unrounded vowel", ) - no dedicated IPA symbol
    ʊ = (
        "ʊ",
        True,
        Backness.NEAR_BACK,
        Height.NEAR_CLOSE,
        False,
        "Near-close back rounded vowel",
        "\u028A",
        321,
    )
    ɯ = (
        "ɯ",
        False,
        Backness.BACK,
        Height.CLOSE,
        False,
        "Close back unrounded vowel",
        "\u026F",
        316,
    )
    u = (
        "u",
        True,
        Backness.BACK,
        Height.CLOSE,
        False,
        "Close back rounded vowel",
        "\u0075",
        308,
    )
    ɤ = (
        "ɤ",
        False,
        Backness.BACK,
        Height.CLOSE_MID,
        False,
        "Close-mid back unrounded vowel",
        "\u0264",
        315,
    )
    o = (
        "o",
        True,
        Backness.BACK,
        Height.CLOSE_MID,
        False,
        "Close-mid back rounded vowel",
        "\u006F",
        307,
    )
    #   o  = ("o", True, Backness.BACK, Height.MID, False, "Mid back rounded vowel", "\u") - no dedicated IPA symbol
    ʌ = (
        "ʌ",
        False,
        Backness.BACK,
        Height.OPEN_MID,
        False,
        "Open-mid back unrounded vowel",
        "\u028C",
        314,
    )
    ɔ = (
        "ɔ",
        True,
        Backness.BACK,
        Height.OPEN_MID,
        False,
        "Open-mid back rounded vowel",
        "\u0254",
        306,
    )
    ɑ = (
        "ɑ",
        False,
        Backness.BACK,
        Height.OPEN,
        False,
        "Open back unrounded vowel",
        "\u0251",
        305,
    )
    ɒ = (
        "ɒ",
        True,
        Backness.BACK,
        Height.OPEN,
        False,
        "Open back rounded vowel",
        "\u0252",
        313,
    )
    i_ = (
        "i:",
        False,
        Backness.FRONT,
        Height.CLOSE,
        True,
        "Close front unrounded vowel",
        "\u0069",
        301,
    )
    y_ = (
        "y:",
        True,
        Backness.FRONT,
        Height.CLOSE,
        True,
        "Close front rounded vowel",
        "\u0079",
        309,
    )
    e_ = (
        "e:",
        False,
        Backness.FRONT,
        Height.CLOSE_MID,
        True,
        "Close-mid front unrounded vowel",
        "\u0065",
        302,
    )
    ø_ = (
        "ø:",
        True,
        Backness.FRONT,
        Height.CLOSE_MID,
        True,
        "Close-mid front rounded vowel",
        "\u00F8",
        310,
    )
    #    _ø = ("ø:", True, Backness.FRONT, Height.MID, False, "mid front rounded vowel") - no dedicated IPA symbol
    ɛ_ = (
        "ɛ:",
        False,
        Backness.FRONT,
        Height.OPEN_MID,
        True,
        "Open-mid front unrounded vowel",
        "\u025B",
        303,
    )
    œ_ = (
        "œ:",
        True,
        Backness.FRONT,
        Height.OPEN_MID,
        True,
        "Open-mid front rounded vowel",
        "\u0153",
        311,
    )
    æ_ = (
        "æ:",
        False,
        Backness.FRONT,
        Height.NEAR_OPEN,
        True,
        "Near-open front unrounded vowel",
        "\u00E6",
        325,
    )
    a_ = (
        "a:",
        False,
        Backness.FRONT,
        Height.OPEN,
        True,
        "Open front unrounded vowel",
        "\u0061",
        304,
    )
    ɶ_ = (
        "ɶ:",
        True,
        Backness.FRONT,
        Height.OPEN,
        True,
        "Open front rounded vowel",
        "\u0276",
        312,
    )
    ɪ_ = (
        "ɪ:",
        False,
        Backness.NEAR_FRONT,
        Height.NEAR_CLOSE,
        True,
        "Near-close front unrounded vowel",
        "\u026A",
        319,
    )
    ʏ_ = (
        "ʏ:",
        True,
        Backness.NEAR_FRONT,
        Height.NEAR_CLOSE,
        True,
        "Near-close front rounded vowel",
        "\u028F",
        320,
    )
    ɨ_ = (
        "ɨ:",
        False,
        Backness.CENTRAL,
        Height.CLOSE,
        True,
        "Close central unrounded vowel",
        "\u0268",
        317,
    )
    ʉ_ = (
        "ʉ:",
        True,
        Backness.CENTRAL,
        Height.CLOSE,
        True,
        "Close central rounded vowel",
        "\u0289",
        316,
    )
    ɘ_ = (
        "ɘ:",
        False,
        Backness.CENTRAL,
        Height.CLOSE_MID,
        True,
        "Close-mid central unrounded vowel",
        "\u0258",
        397,
    )
    ɵ_ = (
        "ɵ:",
        True,
        Backness.CENTRAL,
        Height.CLOSE_MID,
        True,
        "Close-mid central rounded vowel",
        "\u0275",
        323,
    )
    ə_ = (
        "ə:",
        None,
        Backness.CENTRAL,
        Height.MID,
        True,
        "mid central vowel",
        "\u0259",
        322,
    )  # schwa
    ɜ_ = (
        "ɜ:",
        False,
        Backness.CENTRAL,
        Height.OPEN_MID,
        True,
        "Open-mid central unrounded vowel",
        "\u025C",
        326,
    )
    ɞ_ = (
        "ɞ:",
        True,
        Backness.CENTRAL,
        Height.OPEN_MID,
        True,
        "Open-mid central rounded vowel",
        "\u025E",
        395,
    )
    ɐ_ = (
        "ɐ:",
        None,
        Backness.CENTRAL,
        Height.NEAR_OPEN,
        True,
        "Near-open central vowel",
        "\u0250",
        324,
    )
    #   a_ = ("a:", False, Backness.CENTRAL, Height.OPEN, True, "Open central unrounded vowel", ) - no dedicated IPA symbol
    ʊ_ = (
        "ʊ:",
        True,
        Backness.NEAR_BACK,
        Height.NEAR_CLOSE,
        True,
        "Near-close back rounded vowel",
        "\u028A",
        321,
    )
    ɯ_ = (
        "ɯ:",
        False,
        Backness.BACK,
        Height.CLOSE,
        True,
        "Close back unrounded vowel",
        "\u026F",
        316,
    )
    u_ = (
        "u:",
        True,
        Backness.BACK,
        Height.CLOSE,
        True,
        "Close back rounded vowel",
        "\u0075",
        308,
    )
    ɤ_ = (
        "ɤ:",
        False,
        Backness.BACK,
        Height.CLOSE_MID,
        True,
        "Close-mid back unrounded vowel",
        "\u0264",
        315,
    )
    o_ = (
        "o:",
        True,
        Backness.BACK,
        Height.CLOSE_MID,
        True,
        "Close-mid back rounded vowel",
        "\u006F",
        307,
    )
    #   o_  = ("o:", True, Backness.BACK, Height.MID, True, "Mid back rounded vowel", "\u") - no dedicated IPA symbol
    ʌ_ = (
        "ʌ:",
        False,
        Backness.BACK,
        Height.OPEN_MID,
        True,
        "Open-mid back unrounded vowel",
        "\u028C",
        314,
    )
    ɔ_ = (
        "ɔ:",
        True,
        Backness.BACK,
        Height.OPEN_MID,
        True,
        "Open-mid back rounded vowel",
        "\u0254",
        306,
    )
    ɑ_ = (
        "ɑ:",
        False,
        Backness.BACK,
        Height.OPEN,
        True,
        "Open back unrounded vowel",
        "\u0251",
        305,
    )
    ɒ_ = (
        "ɒ:",
        True,
        Backness.BACK,
        Height.OPEN,
        True,
        "Open back rounded vowel",
        "\u0252",
        313,
    )

    def __init__(
        self,
        IPA: str,
        rounding: bool,
        backness: Backness,
        height: Height,
        long: bool,
        name: str,
        unicode: str,
        ipa_num: int,
    ):
        self.ipa = IPA
        self.is_round = rounding
        self.backness = backness
        self.height = height
        self.is_long = long
        self.long_name = name
        self.unicode = unicode
        self.ipa_number = ipa_num
