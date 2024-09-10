import nltk
from nltk import word_tokenize, pos_tag
from nltk.tag import RegexpTagger

patterns = [
    (r'^[Tt]he$', 'DT'),  
    (r'^[Aa]$', 'DT'),    
    (r'.*ing$', 'VBG'),   
    (r'.*ed$', 'VBD'),    
    (r'.*es$', 'VBZ'),   
    (r'.*s$', 'NNS'),    
    (r'^[A-Z][a-z]*$', 'NNP'),  
    (r'\d+', 'CD'),      
    (r'.*', 'NN')         
]

tagger = RegexpTagger(patterns)

sentence = "The cat is playing with the dogs"
words = word_tokenize(sentence)

tagged_sentence = tagger.tag(words)

print("Tagged Sentence:", tagged_sentence)
