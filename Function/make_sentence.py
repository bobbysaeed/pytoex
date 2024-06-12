# Write function make_sentence()
# that  generate all sentences where
# subject is in ["I", "You"],  verb is in ["Play", "Love"] and the object is in ["Hockey","Football"]
# and return them as a list of sentences


def make_sentence():
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey", "Football"]

    sentences = []
    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentence = f"{subject} {verb} {obj}"
                sentences.append(sentence)

    return sentences
