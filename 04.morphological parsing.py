class MorphologicalParser:
    def __init__(self):
        self.states = ['SINGULAR', 'PLURAL']
        self.initial_state = 'SINGULAR'
        self.final_states = ['PLURAL']
        self.transitions = {
            'SINGULAR': {'+s': 'PLURAL', '+es': 'PLURAL', '+ies': 'PLURAL'},
            'PLURAL': {}
        }

    def parse(self, word):
        current_state = self.initial_state
        for suffix in self.transitions[current_state]:
            if word.endswith(suffix):
                current_state = self.transitions[current_state][suffix]
                word = word[:-len(suffix)]
        return word + 's' if current_state == 'PLURAL' else word

parser = MorphologicalParser()
print(parser.parse('cat'))  # cats
print(parser.parse('bus'))  # buses
print(parser.parse('city'))  # cities
