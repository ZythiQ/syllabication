from consonant_splitting import ConsonantSplitter
from nltk.corpus import words
import argparse, json


def main():
    splitter = ConsonantSplitter()

    parser = argparse.ArgumentParser(description='Split words into syllables.')
    parser.add_argument('words', nargs='*', help='Words to syllabicate.')

    parser.add_argument('-s', '--separator', default=' • ', help='Separator between syllables (default: " • ").')
    parser.add_argument('-c', '--count', action='store_true', help='Show syllable count for each word.')

    parser.add_argument('-f', '--format', choices=['text', 'json'], default='text', help='Output format (text or json).')
    parser.add_argument('-o', '--output-file', help='Output file for results.')
    args = parser.parse_args()
    
    # Process:
    word_list = args.words if args.words else list(set([w.lower() for w in words.words() if w.isalpha()]))
    text_res, json_res = [], {}
    
    for word in word_list:
        syllables = splitter.syllabicate(word)
        formatted = args.separator.join(syllables)
        
        if args.format == 'text':
            if args.count:
                formatted += f' ({len(syllables)})'
            text_res.append(f'{word}: {formatted}')

        else:
            json_res[word] = {
                'syllables': syllables,
                'count': len(syllables)
            }
    
    # Output results:
    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as file:
            if args.format == 'text':
                for line in text_res:
                    file.write(line + '\n')

            else:
                json.dump(json_res, file, indent=2)

    else:
        if args.format == 'text':
            for line in text_res:
                print(line)

        else:
            print(json.dumps(json_res, indent=2))
        print()


if __name__ == '__main__':
    main()
