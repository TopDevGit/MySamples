from wordfreq import tokenize
from wordfreq.preprocess import preprocess_text


def test_transliteration():
    # "Well, there's a lot of things you do not understand."
    # (from somewhere in OpenSubtitles
    assert tokenize("Па, има ту много ствари које не схваташ.", "sr") == [
        "pa",
        "ima",
        "tu",
        "mnogo",
        "stvari",
        "koje",
        "ne",
        "shvataš",
    ]
    assert tokenize("Pa, ima tu mnogo stvari koje ne shvataš.", "sr") == [
        "pa",
        "ima",
        "tu",
        "mnogo",
        "stvari",
        "koje",
        "ne",
        "shvataš",
    ]

    # I don't have examples of complete sentences in Azerbaijani that are
    # naturally in Cyrillic, because it turns out everyone writes Azerbaijani
    # in Latin letters on the Internet, _except_ sometimes for Wiktionary.
    # So here are some individual words.

    # 'library' in Azerbaijani Cyrillic
    assert preprocess_text("китабхана", "az") == "kitabxana"
    assert preprocess_text("КИТАБХАНА", "az") == "kitabxana"
    assert preprocess_text("KİTABXANA", "az") == "kitabxana"

    # 'scream' in Azerbaijani Cyrillic
    assert preprocess_text("бағырты", "az") == "bağırtı"
    assert preprocess_text("БАҒЫРТЫ", "az") == "bağırtı"
    assert preprocess_text("BAĞIRTI", "az") == "bağırtı"


def test_actually_russian():
    # This looks mostly like Serbian, but was probably actually Russian.
    # In Russian, Google Translate says it means:
    # "a hundred out of a hundred, boys!"
    #
    # We make sure to handle this case so we don't end up with a mixed-script
    # word like "pacanы".

    assert tokenize("сто из ста, пацаны!", "sr") == ["sto", "iz", "sta", "pacany"]
    assert tokenize("культуры", "sr") == ["kul'tury"]


def test_alternate_codes():
    # Try language codes for Serbo-Croatian that have been split, and now
    # are canonically mapped to Serbian
    assert tokenize("культуры", "sh") == ["kul'tury"]
    assert tokenize("культуры", "hbs") == ["kul'tury"]
