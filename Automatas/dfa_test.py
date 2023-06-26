from cps337_dfa import DFA

states = ['q0', 'q1', 'q2', 'q3']
alphabet = ['a', 'b']
transitions = {
    ('q0', 'a'):  'q1',
    ('q0', 'b'):  'q0',
    ('q1', 'a'):  'q1',
    ('q1', 'b'):  'q2',
    ('q2', 'a'):  'q3',
    ('q2', 'b'):  'q0',
    ('q3', 'a'):  'q3',
    ('q3', 'b'):  'q3'
}
accept_states = ['q3']
start_state = 'q0'

d = DFA(states, alphabet, transitions, start_state, accept_states)
print(d.accept("abb"))   # Should be false
print(d.accept("bbabab"))  # Should be true
