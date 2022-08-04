# Import required libraries
import pickle
from collections import defaultdict
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import string
import translators as ts

from translate import Translator
# Reading the first dataset
df2 = pd.read_csv("dataset_1.txt", sep=",")

# Strip leading and trailing space
df2['Urdu'] = df2['Urdu'].str.strip()
df2['Roman-Urdu'] = df2['Roman-Urdu'].str.strip()


def defval(): return []


# Initalizing default dictionary
map_dict = defaultdict(defval)

# Mapping Urdu Words onto Roman Urdu words
for i in range(len(df2)):
    map_dict[df2['Roman-Urdu'][i]].append(df2['Urdu'][i])

with open('dataset_2.txt', encoding="utf8") as f:
    contents = [line.rstrip('\n') for line in f]

# Reading the second dataset
file = open('dataset_2.txt', 'r', encoding='utf-8-sig')
Lines = file.readlines()

urdu = []
roman = []

# Add even lines to the Urdu list, and odd lines to the Roman Urdu list
for i in range(len(Lines)):
    if i % 2 == 0:
        roman.append(Lines[i])
    else:
        urdu.append(Lines[i])

for i in range(len(urdu)):
    urdu[i] = urdu[i].strip()
    roman[i] = roman[i].strip().lower()

# Conversion to a Dataframe
df = pd.DataFrame({'urdu': urdu, 'roman': roman})

#nltk.download('punkt')

for i in range(len(df)):

    # Translating punctuations using built-in translate library
    roman_words = word_tokenize(df['roman'][i].translate(
        str.maketrans('', '', string.punctuation)))
    urdu_words = word_tokenize(
        df['urdu'][i].translate(str.maketrans('', '', '،۔')))

    # Check conditions for selecting the words from lists
    if len(roman_words) == len(urdu_words):
        j = 0
        for i in range(len(roman_words)):
            if len(roman_words[i]) >= 4 and len(urdu_words[j]) <= 2:
                if j < len(urdu_words)-1:
                    map_dict[roman_words[i]].append(
                        urdu_words[j] + ' ' + urdu_words[j+1])
                    j += 1
                else:
                    map_dict[roman_words[i]].append(urdu_words[j])
            else:
                map_dict[roman_words[i]].append(urdu_words[j])
            j += 1
            if j == len(urdu_words):
                break


def Roman_to_urdu(sentence):
    urdu_list=[]
    word = []   
    words=word_tokenize(sentence)
    #print(words)
    for i in range(len(words)):
        if words[i].lower() in map_dict.keys():
            #print(map_dict[words[i].lower()][0])
            urdu_list.append(map_dict[words[i].lower()][0])
        #elif words[i].lower() not in map_dict.keys():
        else:
            translator= Translator(from_lang="en",to_lang="ur")
            translation = translator.translate(words[i].lower())
            urdu_list.append(translation)
    return ' '.join(urdu_list) 


urdu_lang_dict = {'ا': ['a', 'aa', 'a'], 'ب': ['b'], 'پ': ['p'], 'ت': ['t'], 'ٹ': ['t'], 'ث': ['s'], 'ج': ['j'], 'چ': ['ch'], 'ح': ['h'], 'خ': ['kh'], 'د': ['d'], 'ڈ': ['dd'], 'ذ': ['z'], 'ر': ['r'], 'ڑ': ['rr'], 'ز': ['z'], 'ژ': ['zh'], 'س': ['s'], 'ش': ['sh'], 'ص': ['s'], 'ض': ['z'], 'ط': ['t'], 'ظ': ['z'], 'ع': [
    'a', "a'", 'o'], 'غ': ['gh'], 'ف': ['f'], 'ق': ['q'], 'ک': ['k'], 'گ': ['g'], 'ل': ['l'], 'م': ['m'], 'ن': ['n'], 'و': ['wo', 'o', 'o'], 'ہ': ['h', 'h', 'eh'], 'ھ': ['h'], 'ه': ['h'], 'ی': ['y', 'ei', 'i'], 'ئ': ['i'], 'ي': ['e'], 'ے': ['ay'], 'آ': ['aa'], 'ں': ['n'], '؟': ['?'], '،': [','], '.': ['.'], '۔': ['.']}
no_As = ['ی', 'ے', 'آ', 'ا', 'و', 'ع', 'ہ', 'ں', 'ھ', 'ئ', 'ن']
next_skippers = ['ئی']


def get_position(text, index):
    if index == 0:
        return 0
    elif index == len(text) - 1:
        return 2
    else:
        if text[index - 1] == ' ':
            return 0
        elif text[index + 1] == ' ' or text[index + 1] == '.' or text[index + 1] == '۔' or text[index + 1] == '،' or text[index + 1] == '"':
            return 2
        else:
            return 1


def urdutoroman(input_text):
    skip = False
    output_text = ""
    for i in range(len(input_text)):
        if not skip:
            char = input_text[i]
            if char in urdu_lang_dict:
                position = get_position(input_text, i)
                if len(urdu_lang_dict[char]) > 1:
                    output_text += urdu_lang_dict[char][2]
                else:
                    output_text += urdu_lang_dict[char][0]
            else:
                output_text += char
        else:
            skip = False
    return output_text


# Save the two models
with open('roman_to_urdu.pickle', 'wb') as file:
    pickle.dump(Roman_to_urdu, file)

with open('urdu_to_roman.pickle', 'wb') as file:
    pickle.dump(urdutoroman, file)


# API functions
def translateToUrdu(text):
    with open('roman_to_urdu.pickle', 'rb') as f:
        model = pickle.load(f)
        return model(text)


def translateToRoman(text):
    with open("urdu_to_roman.pickle", "rb") as f:
        model = pickle.load(f)
        return model(text)
