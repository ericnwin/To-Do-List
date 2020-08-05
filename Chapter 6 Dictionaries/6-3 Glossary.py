'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
'''

glossary = {'print':'allows you to output parameters',
    'str':'allows you to convert a datatype to a string',
    '.strip()':'allows you to remove the whitespace from a variable on both sides',
    '.title()':'allows for the first letter in each word to be capitalized',
    '.item()':'creates an easy to read key-value pair',
    }
for key in glossary:
    print(key,'\n', glossary[key])

# method book used
for function, explanation in glossary.items():
    print(f'{function}:{explanation}\n')

# can use set() to create a list w/ only unique entries
