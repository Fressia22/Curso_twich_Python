"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
 """
"""
#EXPERIMENTO 1


def l337_translate(*texts):
    #text_lenght = len(texts)
    #print(text_lenght)
    
   # for text in texts:
    #    print(text.upper())
    l337_alphabet = dict{"a":"4","e":"3","i":"1","o":"0","u":"v"}
    print(texts.translate(l337_alphabet))


l337_translate("fabrina")
"""
"""
EXPERIMENTO 2
language = input(str)
a,b,c,d,e,f = language
print(a+b+c+d+e+f)
"""
"""
#EXPERIMENTO 3
import string

intab = "aeiou"
outtab = "4310v"
trantab = string.maketrans(intab, outtab)

#l337_alphabet = {"a":"4","e":"3","i":"1","o":"0","u":"v"}
text = input(str)
print(text.translate(l337_alphabet))

"""
"""
#EXPERIMENTO 4 EXITOSO solo vertical

#l337_alphabet = {"a":"4","e":"3","i":"1","o":"0","u":"v"}
my_word = "HOLU DANIEL!"

for index in my_word:
    if index == "a" or index == "A" :
        print("4")
        continue
    if index.lower() == "e":
        print("3")
        continue
    if index.lower() == "i":
        print("1")
        continue
    if index.lower() == "o":
        print("0")
        continue
    if index.lower() == "u":
        print("v")
        continue
    else:
         print(index)


"""
"""
#EXPERIMENTO 5 EXITOSO
#my_dict = {97: 52, 101: 51, 105: 49, 111: 48, 117: 230}
#my_dict = {97: "4", 101: "3", 105: "1", 111: "0", 117: "(_)"}
my_dict = {
    97: '4',
    98: '13', 
    99: '[',
    100: ')',
    101: '3', 
    102: '|=',
    103: '&',
    104: '#',
    105: '][',
    106: ',_|',
    107: '>|',
    108: '1',
    109: 'jvi',
    110: '/\/',
    111: '<>',
    112: '|*',
    113: '<|',
    114: '/2',
    115: '2',
    116: '+',
    117: 'L|',
    118: '\|',
    119: 'vN',
    120: 'ecks',
    121: 'j',
    122: '7_',
    32: ' ',
    49: 'L',
    50: 'R',
    51: 'E',
    52: 'A',
    53: 'S',
    54: 'G',
    55: 'T',
    56: 'B',
    57: 'g',
    48: 'o'
}

txt = "Holu Daniel!!! feliz 2023"

print(txt.lower().translate(my_dict))

"""

# EXPERIMENTO 6 EXITOSO
l33t_dictionary = {
    'a': '4',
    'b': '13', 
    'c': '[',
    'd': ')',
    'e': '3', 
    'f': '|=',
    'g': '&',
    'h': '#',
    'i': '][',
    'j': ',_|',
    'k': '>|',
    'l': '1',
    'm': 'jvi',
    'n': '/\/',
    'o': '<>',
    'p': '|*',
    'q': '<|',
    'r': '/2',
    's': '2',
    't': '+',
    'u': 'L|',
    'v': '\|',
    'w': 'vN',
    'x': 'ecks',
    'y': 'j',
    'z': '7_',
    ' ': ' ',
    '1': 'L',
    '2': 'R',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'G',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'o'
}

text = input(str)
hack_lang = ''

for index in text.lower():
    if index in l33t_dictionary:
        hack_lang += l33t_dictionary[index]
        continue
    else: 
        hack_lang += index

print(hack_lang)
