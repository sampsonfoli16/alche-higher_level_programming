#!/usr/bin/python3
"""Text indentation: add two new lines after ., ? and : characters.

Function `text_indentation(text)` prints text with two new lines after each
occurrence of '.', '?' or ':' while removing extra spaces at the start of
lines.
"""


def text_indentation(text):
    """Print text with two newlines after '.', '?' and ':' characters.

    Raises TypeError if `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    separators = {'.', '?', ':'}
    result = ''
    i = 0
    length = len(text)

    while i < length:
        char = text[i]
        result += char
        if char in separators:
            result += '\n\n'
            i += 1
            # skip any spaces following the separator
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1

    result = result.rstrip('\n')

    # Print each line stripped of leading/trailing spaces
    for line in result.split('\n'):
        print(line.strip())
