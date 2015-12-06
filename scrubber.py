#INPUT SAMPLE:
# The first argument is a source strings and the characters that need to be scrubbed.

def scrubber(sentence, letters):

    new_sentence = list(sentence

    for letter in letters:
        for i, char in enumerate(sentence):
            if letter == char:
                new_sentence[i]=""
    print ''.join(new_sentence)

scrubber("hello world", "def")