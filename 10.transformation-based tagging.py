transformation_rule = ('NN', 'VB', 'is')  
def initial_tagging(sentence):
    words = sentence.split()
    return [(word, 'NN') for word in words]  

def apply_transformation_rule(tagged_sentence):
    for i in range(1, len(tagged_sentence)):
        word, tag = tagged_sentence[i]
        prev_word, _ = tagged_sentence[i - 1]

        if tag == transformation_rule[0] and prev_word == transformation_rule[2]:
            tagged_sentence[i] = (word, transformation_rule[1])
    return tagged_sentence

sentence = "The cat is playing"

tagged_sentence = initial_tagging(sentence)
print("Initial Tagged Sentence:", tagged_sentence)

refined_tagged_sentence = apply_transformation_rule(tagged_sentence)
print("Refined Tagged Sentence:", refined_tagged_sentence)
