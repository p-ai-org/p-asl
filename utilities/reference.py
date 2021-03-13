LETTERS = [letter for letter in 'ABCDEFGHIKLMNOPQRSTUVWXY']

# Taken from https://www.lifeprint.com/asl101/pages-signs/classifiers/classifiers-main.htm
CLASSIFIERS = [
  'ONE',
  'THREE',
  'THREE-bent',
  'FOUR',
  'FIVE',
  'FIVE-claw',
  'A-open',
  'B-flat',
  'B-curved',
  'B-bent',
  'C',
  'C-claw',
  'C-index-and-thumb',
  'F',
  'G',
  'U',
  'H',
  'I',
  'horns',
  'ILY',
  'L',
  'L-curved',
  'O',
  'O-flat',
  'R',
  'S',
  'V',
  'V-bent',
  'X',
  'X-cocked',
  'Y'
]

def letter_to_index(letter):
  return LETTERS.index(letter)

def index_to_letter(index):
  return LETTERS[index]

def classifier_to_index(classifier):
  return CLASSIFIERS.index(classifier)

def index_to_classifier(index):
  return CLASSIFIERS[index]