from cps337_nfa import NFA

states = ['q1', 'q2', 'q3', 'q4']
alphabet = ['0', '1']
transitions = {
    ('q1', '0'):  set(['q1']),
    ('q1', '1'):  set(['q1', 'q2']),
    ('q2', '1'):  set(['q3']),
    ('q2', '0'):  set(['q3']),
    ('q3', '1'):  set(['q4']),
    ('q3', '0'):  set(['q4'])
}
accept_states = ['q4']
start_state = 'q1'

n = NFA(states, alphabet, transitions, start_state, accept_states)
print(n.accept('001111'))  # Should be true
print()
print(n.accept('111011'))  # Should be false
print("\nStates")
d = n.dfa()
print(d.states)
print("\nAlphabet")
print(d.alphabet)
print("\nTransitions")
print(d.transition_function)
print("\nStart State")
print(d.start_state)
print("\nAccept States")
print(d.accept_states)
print("\nCurrent State")
print(d.current_state)