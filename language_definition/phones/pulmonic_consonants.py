#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum, auto


class Manner(Enum):
    NASAL = auto()
    STOP = auto()
    AFFRICATE = auto()
    FRICATIVE = auto()
    APPROXIMANT = auto()
    TAP_FLAP = auto()
    TRILL = auto()
    NON_SIBILANT_AFFRICATE = auto()
    NON_SIBILANT_FRICATIVE = auto()
    LATERAL_AFFRICATE = auto()
    LATERAL_FRICATIVE = auto()
    LATERAL_APPROXIMANT = auto()
    LATERAL_TAP = auto()


OBSTRUENTS = [
    Manner.STOP,
    Manner.FRICATIVE,
    Manner.LATERAL_FRICATIVE,
    Manner.NON_SIBILANT_FRICATIVE,
    Manner.AFFRICATE,
    Manner.LATERAL_AFFRICATE,
    Manner.NON_SIBILANT_AFFRICATE,
]
SONORANTS = [
    Manner.NASAL,
    Manner.APPROXIMANT,
    Manner.TAP_FLAP,
    Manner.TRILL,
    Manner.LATERAL_APPROXIMANT,
    Manner.LATERAL_TAP,
]


class Place(Enum):
    BILABIAL = auto()
    LABIODENTAL = auto()
    LABIOVELAR = auto()
    LINGUALABIAL = auto()
    DENTAL = auto()
    ALVEOLAR = auto()
    POSTALVEOLAR = auto()
    RETROFLEX = auto()
    ALVEOLOPALATAL = auto()
    PALATAL = auto()
    VELAR = auto()
    UVULAR = auto()
    EPIGLOTTAL = auto()
    GLOTTAL = auto()
    PHARYNGEAL = auto()


class PulmonicConsonant(Enum):
    """

    Are ignored because of diacritics (and most of the times allophones):
        - voiced and voiceless bilabial affricates
        - voiced and voiceless labiodental stop
        - voiceless labiodental approximant
        - voiceless alveolar non sibilant affricate
        - voiced alveolar non sibilant affricate
        - Voiceless postalveolar non-sibilant affricate
        - Voiced postalveolar non-sibilant affricate
        - Voiceless alveolar non-sibilant fricative
        - Voiced alveolar non-sibilant fricative
        - Voiceless postalveolar non-sibilant fricative
        - Voiced postalveolar non-sibilant fricative
        - Voiceless alveolar tap, flap and trill
        - Voiceless dental, alveolar and postalveolar lateral approximants
        - Voiced retroflex non-sibilant fricative
        - Voiced and voiceless palatal lateral fricative
        - Voiceless velar nasal
        - Voiceless velar approximant
        - Voiceless velar lateral approximant
        - Voiced uvular tap and flap, voiceless uvular trill
        - Voiced uvular lateral approximant
        -Voiced epiglottal affricate
        - Voiced epiglottal tap
    Are ignored because absent in our languages of interests
        - voiced bilabial flap
        - voiced and voiceless bilabial trill
        - lingualabials
        - Voiceless alveolar and postalveolar approximants
        - Voiceless retroflex nasal
        - Voiced retroflex non-sibilant fricative
        - Voiceless retroflex flap
        - Voiced and voicelless retroflex trill
        - Voiceless retroflex lateral affricate and fricative
        - Voiceless retroflex lateral approximant
        - voiced retroflex lateral flap
        - Voiceless palatal nasal
        - Voiceless palatal lateral affricate
        - Voiceless palatal lateral fricative
        - Voiced palatal lateral flap
        - Voiceless velar lateral affricate, Voiced velar lateral affricate
        - Voiceless velar lateral fricative
        - Voiced velar lateral fricative and tap
    """

    # = ("", False, Place., Manner., "", "\u", )
    # m_ = ("m̥", False, Place.BILABIAL, Manner.NASAL, "Voiceless bilabial nasal", None, None)
    m = (
        "m",
        True,
        Place.BILABIAL,
        Manner.NASAL,
        "Voiced bilabial nasal",
        "\u006D",
        114,
    )
    p = (
        "p",
        False,
        Place.BILABIAL,
        Manner.STOP,
        "Voiceless bilabial stop",
        "\u0070",
        101,
    )
    p_ = (
        "p:",
        False,
        Place.BILABIAL,
        Manner.STOP,
        "Voiceless bilabial stop",
        "\u0070",
        101,
    )
    b = ("b", True, Place.BILABIAL, Manner.STOP, "Voiced bilabial stop", "\u0062", 102)
    b_ = ("b:", True, Place.BILABIAL, Manner.STOP, "Voiced bilabial stop", "\u0062", 102)
    ɸ = (
        "ɸ",
        False,
        Place.BILABIAL,
        Manner.FRICATIVE,
        "Voiceless bilabial fricative",
        "\u0278",
        126,
    )
    β = (
        "β",
        True,
        Place.BILABIAL,
        Manner.FRICATIVE,
        "Voiced bilabial fricative",
        "\u03B2",
        127,
    )
    ʙ = (
        "ʙ",
        True,
        Place.BILABIAL,
        Manner.TRILL,
        "Voiced bilabial trill",
        "\u0299",
        121,
    )
    ɱ = (
        "ɱ",
        True,
        Place.LABIODENTAL,
        Manner.NASAL,
        "Voiced labiodental nasal",
        "\u0271",
        115,
    )
    bv = (
        "bv",
        True,
        Place.LABIODENTAL,
        Manner.AFFRICATE,
        "Voiced labiodental affricate",
        None,
        None,
    )
    f = (
        "f",
        False,
        Place.LABIODENTAL,
        Manner.FRICATIVE,
        "Voiceless labiodental fricative",
        "\u0066",
        128,
    )
    v = (
        "v",
        True,
        Place.LABIODENTAL,
        Manner.FRICATIVE,
        "Voiced labiodental fricative",
        "\u0076",
        129,
    )
    ʋ = (
        "ʋ",
        True,
        Place.LABIODENTAL,
        Manner.APPROXIMANT,
        "Voiced labiodental approximant",
        "\u028B",
        150,
    )
    ⱱ = (
        "ⱱ",
        True,
        Place.LABIODENTAL,
        Manner.TAP_FLAP,
        "Voiced labiodental flap",
        "\u2C71",
        184,
    )
    n_ = (
        "n:", #"n̥",
        False,
        Place.ALVEOLAR,
        Manner.NASAL,
        "Voiceless alveolar nasal",
        None,
        None,
    )
    n = (
        "n",
        True,
        Place.ALVEOLAR,
        Manner.NASAL,
        "Voiced alveolar nasal",
        "\u006E",
        116,
    )
    t = (
        "t",
        False,
        Place.ALVEOLAR,
        Manner.STOP,
        "Voiceless alveolar stop",
        "\u0074",
        103,
    )
    d = ("d", True, Place.ALVEOLAR, Manner.STOP, "Voiced alveolar stop", "\u0064", 104)
    ts = (
        "ts",
        False,
        Place.ALVEOLAR,
        Manner.AFFRICATE,
        "Voiceless alveolar sibilant affricate",
        "\u02A6",
        103.132,
    )
    dz = (
        "dz",
        True,
        Place.ALVEOLAR,
        Manner.AFFRICATE,
        "Voiced alveolar sibilant affricate",
        "\u02A3",
        104.133,
    )
    tʃ = (
        "tʃ",
        False,
        Place.POSTALVEOLAR,
        Manner.AFFRICATE,
        "Voiceless postalveolar sibilant affricate",
        "\u0074 \u0283",
        103.134,
    )
    dʒ = (
        "dʒ",
        True,
        Place.POSTALVEOLAR,
        Manner.AFFRICATE,
        "Voiced post-alveolar sibilant affricate",
        "\u0064 \u0292",
        104.135,
    )
    tθ = (
        "tθ",
        False,
        Place.DENTAL,
        Manner.NON_SIBILANT_AFFRICATE,
        "Voiceless dental non-sibilant affricate",
        None,
        None,
    )
    dð = (
        "dð",
        True,
        Place.DENTAL,
        Manner.NON_SIBILANT_AFFRICATE,
        "Voiced dental non-sibilant affricate",
        None,
        None,
    )
    s = (
        "s",
        False,
        Place.ALVEOLAR,
        Manner.FRICATIVE,
        "Voiceless alveolar sibilant",
        "\u0073",
        132,
    )
    z = (
        "z",
        True,
        Place.ALVEOLAR,
        Manner.FRICATIVE,
        "Voiced alveolar sibilant",
        "\u007A",
        133,
    )
    ʃ = (
        "ʃ",
        False,
        Place.POSTALVEOLAR,
        Manner.FRICATIVE,
        "Voiceless postalveolar fricative",
        "\u0283",
        134,
    )
    ʃ_ = (
        "ʃ:",
        False,
        Place.POSTALVEOLAR,
        Manner.FRICATIVE,
        "Voiceless postalveolar fricative",
        "\u0283",
        134,
    )
    ʒ = (
        "ʒ",
        True,
        Place.POSTALVEOLAR,
        Manner.FRICATIVE,
        "Voiced postalveolar fricative",
        "\u0292",
        135,
    )
    θ = (
        "θ",
        False,
        Place.DENTAL,
        Manner.FRICATIVE,
        "Voiceless dental fricative",
        "\u03B8",
        130,
    )
    ð = (
        "ð",
        True,
        Place.DENTAL,
        Manner.FRICATIVE,
        "Voiced dental fricative",
        "\u00F0",
        131,
    )
    ɹ = (
        "ɹ",
        True,
        Place.ALVEOLAR,
        Manner.APPROXIMANT,
        "Voiced alveolar approximant",
        "\u0279",
        151,
    )
    ɾ = (
        "ɾ",
        True,
        Place.ALVEOLAR,
        Manner.TAP_FLAP,
        "Voiced alveolar tap and flap",
        "\u027E",
        124,
    )
    r = (
        "r",
        True,
        Place.ALVEOLAR,
        Manner.TRILL,
        "Voiced alveolar trill",
        "\u0072",
        122,
    )
    tɬ = (
        "tɬ",
        False,
        Place.ALVEOLAR,
        Manner.LATERAL_AFFRICATE,
        "Voiceless alveolar lateral affricate",
        "\u0074 \u026C",
        103.148,
    )
    ƛ = (
        "tɬ",
        False,
        Place.ALVEOLAR,
        Manner.LATERAL_AFFRICATE,
        "Voiceless alveolar lateral affricate",
        "\u0074 \u026C",
        103.148,
    )
    dɮ = (
        "dɮ",
        True,
        Place.ALVEOLAR,
        Manner.LATERAL_AFFRICATE,
        "Voiced alveolar lateral affrciate",
        "\u0064 \u026E",
        104.149,
    )
    λ = (
        "dɮ",
        True,
        Place.ALVEOLAR,
        Manner.LATERAL_AFFRICATE,
        "Voiced alveolar lateral affrciate",
        "\u0064 \u026E",
        104.149,
    )
    ɬ = (
        "ɬ",
        False,
        Place.ALVEOLAR,
        Manner.LATERAL_FRICATIVE,
        "Voiceless alveolar lateral fricative",
        "\u026C",
        148,
    )
    ɮ = (
        "ɮ",
        True,
        Place.ALVEOLAR,
        Manner.LATERAL_FRICATIVE,
        "Voiced alveolar lateral fricative",
        "\u026E",
        149,
    )
    l = (
        "l",
        True,
        Place.ALVEOLAR,
        Manner.LATERAL_APPROXIMANT,
        "Voiced alveolar lateral approximant",
        "\u006C",
        155,
    )
    ɺ = (
        "ɺ",
        True,
        Place.ALVEOLAR,
        Manner.LATERAL_TAP,
        "Voiced alveolar lateral flaps",
        "\u027A",
        181,
    )
    ɳ = (
        "ɳ",
        True,
        Place.RETROFLEX,
        Manner.NASAL,
        "Voiced retroflex nasal",
        "\u0273",
        117,
    )
    ʈ = (
        "ʈ",
        False,
        Place.RETROFLEX,
        Manner.STOP,
        "Voiceless retroflex stop",
        "\u0288",
        105,
    )
    ɖ = (
        "ɖ",
        True,
        Place.RETROFLEX,
        Manner.STOP,
        "Voiced retroflex stop",
        "\u0256",
        106,
    )
    tʂ = (
        "ʈʂ",
        False,
        Place.RETROFLEX,
        Manner.AFFRICATE,
        "Voiceless retroflex affricate",
        "\u0288 \u0282",
        105.136,
    )
    ʈʂ = (
        "ʈʂ",
        False,
        Place.RETROFLEX,
        Manner.AFFRICATE,
        "Voiceless retroflex affricate",
        "\u0288 \u0282",
        105.136,
    )
    dʐ = (
        "ɖʐ",
        True,
        Place.RETROFLEX,
        Manner.AFFRICATE,
        "Voiced retroflex affricate",
        "\u0256 \u0290",
        106.137,
    )
    ɖʐ = (
        "ɖʐ",
        True,
        Place.RETROFLEX,
        Manner.AFFRICATE,
        "Voiced retroflex affricate",
        "\u0256 \u0290",
        106.137,
    )
    ʂ = (
        "ʂ",
        False,
        Place.RETROFLEX,
        Manner.FRICATIVE,
        "Voiceless retroflex fricative",
        "\u0282",
        136,
    )
    ʐ = (
        "ʐ",
        True,
        Place.RETROFLEX,
        Manner.FRICATIVE,
        "Voiced retroflex fricative",
        "\u0290",
        137,
    )
    ɻ = (
        "ɻ",
        True,
        Place.RETROFLEX,
        Manner.APPROXIMANT,
        "Voiced retroflex approximant",
        "\u027B",
        152,
    )
    ɽ = (
        "ɽ",
        True,
        Place.RETROFLEX,
        Manner.TAP_FLAP,
        "Voiced retroflex flap",
        "\u027D",
        125,
    )
    ɭ = (
        "ɭ",
        True,
        Place.RETROFLEX,
        Manner.LATERAL_APPROXIMANT,
        "Voiced retroflex lateral approximant",
        "\u026D",
        156,
    )
    ɲ = ("ɲ", True, Place.PALATAL, Manner.NASAL, "Voiced palatal nasal", "\u0272", 118)
    c = (
        "c",
        False,
        Place.PALATAL,
        Manner.STOP,
        "Voiceless palatal stop",
        "\u0063",
        107,
    )
    ɟ = ("ɟ", True, Place.PALATAL, Manner.STOP, "Voiced palatal stop", "\u025F", 108)
    dʑ = (
        "dʑ",
        True,
        Place.ALVEOLOPALATAL,
        Manner.AFFRICATE,
        "Voiced alveolo-palatal affricate",
        "\u02A5",
        216,
    )
    tɕ = (
        "tɕ",
        False,
        Place.ALVEOLOPALATAL,
        Manner.AFFRICATE,
        "Voiceless alveolo-palatal affricate",
        "\u02A8",
        215,
    )
    cɕ = (
        "tɕ",
        False,
        Place.ALVEOLOPALATAL,
        Manner.AFFRICATE,
        "Voiceless alveolo-palatal affricate",
        "\u02A8",
        215,
    )
    cç = (
        "cç",
        False,
        Place.PALATAL,
        Manner.AFFRICATE,
        "Voiceless palatal affricate",
        "\u0063 \u00E7",
        107.138,
    )
    ɟʝ = (
        "ɟʝ",
        True,
        Place.PALATAL,
        Manner.AFFRICATE,
        "Voiced palatal affricate",
        "\u025F \u029D",
        108.139,
    )
    ɕ = (
        "ɕ",
        False,
        Place.ALVEOLOPALATAL,
        Manner.FRICATIVE,
        "Voiceless alveolo-palatal sibilant fricative",
        "\u0255",
        182,
    )
    ʑ = (
        "ʑ",
        True,
        Place.ALVEOLOPALATAL,
        Manner.FRICATIVE,
        "Voiced alveolo-palatal sibilant fricative",
        "\u0291",
        183,
    )
    ç = (
        "ç",
        False,
        Place.PALATAL,
        Manner.FRICATIVE,
        "Voiceless palatal fricative",
        "\u00E7",
        138,
    )
    ʝ = (
        "ʝ",
        True,
        Place.PALATAL,
        Manner.FRICATIVE,
        "Voiced palatal fricative",
        "\u029D",
        139,
    )
    j = (
        "j",
        True,
        Place.PALATAL,
        Manner.APPROXIMANT,
        "Voiced palatal approximant",
        "\u006A",
        153,
    )
    j_ = (
        "j:",
        True,
        Place.PALATAL,
        Manner.APPROXIMANT,
        "Voiced palatal approximant",
        "\u006A",
        153,
    )
    ʎ = (
        "ʎ",
        True,
        Place.PALATAL,
        Manner.LATERAL_APPROXIMANT,
        "Voiced palatal lateral approximant",
        "\u028E",
        157,
    )
    ŋ = ("ŋ", True, Place.VELAR, Manner.NASAL, "Voiced velar nasal", "\u014B", 119)
    k = ("k", False, Place.VELAR, Manner.STOP, "Voiceless velar stop", "\u006B", 109)
    k_ = ("k:", False, Place.VELAR, Manner.STOP, "Voiceless velar stop", "\u006B", 109)
    ɡ = ("ɡ", True, Place.VELAR, Manner.STOP, "Voiced velar stop", "\u0261", 110)
    g = ("ɡ", True, Place.VELAR, Manner.STOP, "Voiced velar stop", "\u0261", 110)
    kʷ = (
        "kʷ",
        False,
        Place.LABIOVELAR,
        Manner.STOP,
        "Palatized voiceless velar stop",
        "\u006B",
        109,
    )
    ɡʷ = (
        "ɡʷ",
        True,
        Place.LABIOVELAR,
        Manner.STOP,
        "Palatized voiced velar stop",
        "\u0261",
        110,
    )
    w = (
        "w",
        True,
        Place.LABIOVELAR,
        Manner.APPROXIMANT,
        "Voiced labio-velar approximant",
        "\u0077",
        170,
    )
    kx = (
        "kx",
        False,
        Place.VELAR,
        Manner.AFFRICATE,
        "Voiceless velar affricate",
        None,
        None,
    )
    ɡɣ = (
        "ɡɣ",
        True,
        Place.VELAR,
        Manner.AFFRICATE,
        "Voiced velar affricate",
        None,
        None,
    )
    x = (
        "x",
        False,
        Place.VELAR,
        Manner.FRICATIVE,
        "Voiceless velar fricative",
        "\u0078",
        140,
    )
    ɣ = (
        "ɣ",
        True,
        Place.VELAR,
        Manner.FRICATIVE,
        "Voiced velar fricative",
        "\u0263",
        141,
    )
    ɰ = (
        "ɰ",
        True,
        Place.VELAR,
        Manner.APPROXIMANT,
        "Voiced velar approximant",
        "\u0270",
        154,
    )
    ʟ = (
        "ʟ",
        True,
        Place.VELAR,
        Manner.LATERAL_APPROXIMANT,
        "Voiced velar lateral approximant",
        "\u029F",
        158,
    )
    ɴ = ("ɴ", True, Place.UVULAR, Manner.NASAL, "Voiced uvular nasal", "\u0274", 120)
    q = ("q", False, Place.UVULAR, Manner.STOP, "Voiceless uvular stop", "\u0071", 111)
    ɢ = ("ɢ", True, Place.UVULAR, Manner.STOP, "Voiced uvular stop", "\u0262", 112)
    qχ = (
        "qχ",
        False,
        Place.UVULAR,
        Manner.AFFRICATE,
        "Voiceless uvular affricate",
        None,
        None,
    )
    χ = (
        "χ",
        False,
        Place.UVULAR,
        Manner.FRICATIVE,
        "Voiceless uvular fricative",
        "\u03C7",
        142,
    )
    ʁ = (
        "ʁ",
        True,
        Place.UVULAR,
        Manner.FRICATIVE,
        "Voiced uvular fricative",
        "\u0281",
        143,
    )
    ʀ = ("ʀ", True, Place.UVULAR, Manner.TRILL, "Voiced uvular trill", "\u0280", 123)
    ʡ = ("ʡ", None, Place.EPIGLOTTAL, Manner.STOP, "Epiglottal stop", "\u02A1", 173)
    ħ = (
        "ħ",
        False,
        Place.PHARYNGEAL,
        Manner.FRICATIVE,
        "Voiceless pharyngeal fricative",
        "\u0127",
        144,
    )
    ʕ = (
        "ʕ",
        True,
        Place.PHARYNGEAL,
        Manner.FRICATIVE,
        "Voiced pharyngeal fricative",
        "\u0295",
        145,
    )
    ʢ = (
        "ʢ",
        True,
        Place.EPIGLOTTAL,
        Manner.TRILL,
        "Voiced epiglottal stop or fricative",
        "\u02A2",
        174,
    )
    ʜ = (
        "ʜ",
        False,
        Place.EPIGLOTTAL,
        Manner.TRILL,
        "Voiceless epiglottal trill",
        "\u029C",
        172,
    )
    ʔ = ("ʔ", None, Place.GLOTTAL, Manner.STOP, "Glottal stop", "\u0294", 113)
    ʔh = (
        "ʔh",
        False,
        Place.GLOTTAL,
        Manner.AFFRICATE,
        "Voiceless glottal affricate",
        None,
        113.146,
    )
    h = (
        "h",
        False,
        Place.GLOTTAL,
        Manner.FRICATIVE,
        "Voiceless glottal fricative",
        "\u0068",
        146,
    )
    ɦ = (
        "ɦ",
        True,
        Place.GLOTTAL,
        Manner.FRICATIVE,
        "Voiced glottal fricative",
        "\u0266",
        147,
    )

    def __init__(
        self,
        IPA: str,
        voicing: bool,
        place: Place,
        manner: Manner,
        name: str,
        unicode: str,
        ipa_num: int,
    ):
        self.ipa = IPA
        self.is_voiced = voicing
        self.manner = manner
        self.place = place
        self.long_name = name
        self.unicode = unicode
        self.ipa_number = ipa_num
