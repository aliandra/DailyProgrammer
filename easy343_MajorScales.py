def getMajorScale(major):
    """
    Return major scale.

    The notes in a major scale are the notes that are 0, 2, 4, 5, 7, 9,
    and 11 semitones above the note that the scale is named after.
    """
    chromatic_scale = [
        'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    ]
    major_index = chromatic_scale.index(major)
    chromatic_scale = (chromatic_scale[major_index:] +
                       chromatic_scale[:major_index])
    index = [0, 2, 4, 5, 7, 9, 11]
    major_scale = []
    for i in index:
        major_scale.append(chromatic_scale[i])
    return major_scale


def note(major, solfege):
    """
    Return the solfège note of the major scale.
    """
    major_scale = getMajorScale(major)
    note_name = {
        "Do": 0, "Re": 1, "Mi": 2, "Fa": 3, "So": 4, "La": 5, "Ti": 6
    }
    return major_scale[note_name[solfege]]


def test():
    assert note("C", "Do") == "C"
    assert note("C", "Re") == "D"
    assert note("C", "Mi") == "E"
    assert note("D", "Mi") == "F#"
    assert note("A#", "Fa") == "D#"
    print("All tests passed")


test()


''' Favorite Response:

def get_note(scale, solfege):
    chromatic_scale = [
        'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
    ]
    major_scale = {
        'Do': 0, 'Re': 2, 'Mi': 4, 'Fa': 5, 'So': 7, 'La': 9, 'Ti': 11
    }
    print(chromatic_scale[(chromatic_scale.index(scale) +
          major_scale[solfege]) % len(chromatic_scale)])
'''
