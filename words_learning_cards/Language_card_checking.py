# using random.choice()
import random
import sys


word_pairs = []
r2e = {}
english_words = []
russian_words = []
valid_selection = True
VERSION = 'The current version is 2022090701'
CHANGED = 'The two previous random values are not suggested to check'


def input_validating(translation_words):
    while True:
        try:
            row_input = input('Input Your selection here, please: ')
            if row_input == 'z':
                return row_input
            selected_number = int(row_input)
            print('Your choice {}'.format(translation_words[selected_number]))
        except (ValueError, ArithmeticError, IndexError):
            print('''
            It is not correct number.'
            Reenter please
            or type z for quit...
            ''')
        else:
            break
    return selected_number


def sort_list_randomly(a, b):
    c = list(zip(a, b))
    random.shuffle(c)
    a, b = zip(*c)
    return a, b


def validating_selection(source, translation):
    c = 0
    random_source = ''
    selected_word = ''
    selected_number = 0
    list_of_selected = [source[0], source[1]]
    while random_source == selected_word:
        source_list, translation_list = sort_list_randomly(source, translation)
        if c > 0:
            print('Correct! Try the next one:')
        # select random word that is not equal to 2 previous
        while True:
            random_source = random.choice(source_list)
            if random_source not in list_of_selected:
                break
        list_of_selected.pop(0)
        list_of_selected.append(random_source)
        c = c + 1
        print('''
Select number that corresponds to
the correct translation of:
{}
from list below or select z to quit
        '''.format(random_source))
        for r in translation_list:
            print('{}: {}'.format(translation_list.index(r), r.rstrip("\n")))
        # checking input till it is valid
        selected_number = input_validating(translation_list)
        if selected_number != 'z':
            selected_word = source_list[selected_number]
        else:
            break
    if selected_number != 'z':
        print('Wrong. Your choice '
              'corresponds to word {}'.format(selected_word))
    return selected_word


def main():
    # open file with pairs of words
    checked_file = open("words.txt", encoding='utf-8', mode='r')
    # create list of lines from file
    lines = checked_file.readlines()
    # close file and clean the buffer
    checked_file.close()
    # create list word_pairs
    # like [['english1', 'russian1'], ['english2', 'russian2']]
    for x in lines:
        # print(x.split(':'))
        word_pairs.append(x.split(':'))
    # Create dictionary: language1 to language 2
    e2r = dict(word_pairs)
    # Create dictionary: language2 to language 1
    for key, value in e2r.items():
        r2e[value] = key
        english_words.append(key)
        russian_words.append(value)
    ans = True
    while ans:
        print("""
        1.Check Language1 - Language2 translation
        2.Check Language2 - Language1 translation
        3.Exit/Quit
        """)
        ans = input('Input Your choice here: ')
        if ans == "1":
            validating_selection(english_words, russian_words)
        elif ans == "2":
            validating_selection(russian_words, english_words)
        elif ans == "3":
            print("\n Goodbye")
            ans = None
        else:
            print("\n Not Valid Choice. Try again please.")
    exit()


if __name__ == "__main__":
    main()
