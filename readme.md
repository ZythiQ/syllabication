### Overview

This program splits words into syllables using weird greedy algorithms. Currently, only consonant splitting is implemented. This will be expanded into root-based and MOP splitting later on.

### Setup / Requirements

```bash
pip install nltk
```

### Commands

Run the script to split one or more words into syllables.

```bash
python syllabicate.py WORD [WORD...] [options]
```

##### Options:

`-c`, `--count`: Show the syllable count for each word.

`-s`, ``--separator``: Custom separator between syllables (default: ' • ')

`-f`, `--format`: Output format (text or json, default: text)

`-o`, `--output-file`: Write the results to a file instead of the terminal.

##### Examples:

```bash
python syllabicate.py syzygium paniculatum -c
```

```bash
python syllabicate.py abbreviation american abliterate -s ', '
```

```bash
python syllabicate.py -o syllables.txt -f text # Use the NLTK word corpus and output a file.
```

### Notes

- Consonant based splitting is BAD with vowel diphthongs like in: `January`
- Not sure what prompted this project, but I'm determined to get a decent syllabicator.
- I am aware of the consonant splitting bug where double-letters are treated as a disputed consonant. Too lazy to fix that, but will later.
