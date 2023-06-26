from cps337_dfa import DFA
import math

class NFA:
    current_states = None   # A list of current states
    #initialize all variable when calling the class DFA
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return

    # For a given input character, update the list of current states
    def transition_on_input(self, input_value):
        #Make initial step
        if (self.current_states == None):
            key = (self.current_state, input_value)
            self.current_states = self.transition_function[key]
        else:
            s = set()
            keys = list(self.transition_function.keys())
            sList = list(self.current_states)
            #test input for each state in current states
            for x in range(len(sList)):
                key = (sList[x], input_value)
                #case no transition for current state
                if(key not in keys):
                    self.current_states.remove(sList[x])
            #populate current_states with updated states
            for state in self.current_states:
                key = (state, input_value)
                s = s | self.transition_function[key]
            self.current_states = s
        print(' (' + str(self.current_states) + ', ' + input_value + ')')
            

    # Returns true if the NFA is currently in an accepting state; false otherwise
    def in_accept_state(self,accept_states):
        for aState in self.accept_states:
            for cState in self.current_states:
                if(cState) == aState:
                    self.current_states = None
                    return True
        self.current_states = None
        return False

    #run the given word through the NFA and return TRUE if it is accepted; FALSE otherwise
    def accept(self, word):
        for x in range(len(word)):
            c = word[x:x+1]
            self.transition_on_input(c)
        return self.in_accept_state(self.accept_states)

    #returns corresponding DFA
    def dfa(self):
        dfaStates = self.__powerSet(self.states)
        #dfaAlphabet is self.alphabet
        dfaTransitions = self.__DFAtransitions()
        #dfaStart is self.start_state
        dfaAccepts = list()
        for l in dfaStates:
            for state in l:
                for accept_state in self.accept_states:
                    if(accept_state == state):
                        dfaAccepts.append(l)
        
        return DFA(dfaStates, self.alphabet, dfaTransitions, self.start_state, dfaAccepts)

    #returns dict of transitions of equiv DFA
    def __DFAtransitions(self):
        dfaTransitions = dict()
        tBuilder = list()                              #actual states used in transitions
        tAdd = set([self.start_state])
        tBuilder.append(tAdd)                          #populate initial value
        x = 0
        loop = True
        #keep looping until the list stops building itself and idx of x would exceed the range
        while loop:
            #test all characters in alphabet
            for char in self.alphabet:
                tAdd = set()
                #test all states in current entry and see what transitions exist
                for state in tBuilder[x]:
                    key = (state, char)
                    if key in self.transition_function:
                        tAdd = tAdd | self.transition_function[key]
                #string-build for key that has multiple states
                s = ''
                for st in tBuilder[x]:
                    s += str(st)
                dfaTransitions[(s, char)] = tAdd
                #don't add duplicate states 
                if tAdd not in tBuilder:
                    tBuilder.append(tAdd)
            if(x+1 >= len(tBuilder)):
                loop = False
            else:
                x += 1
        return dfaTransitions

    #returns powerset of a list
    def __powerSet(self, states):
        size = int(math.pow(2, len(states)))
        bits = len(states)
        master = list()
        #for a given size of list, all the different possible binary strings in a length of n-bits can
        #be used as an idx to activate certain values or not in the original list to string-build and
        #ultimately create the powerset
        for x in range(1, size):
            b = self.__to_binary(x, bits)
            s = list()
            for x in range(len(b)-1, -1, -1):
                if(b[x] == 1):
                    s.append(str(states[x]))
            master.append(s)
        master.sort(key=len)
        return master 

    #returns binary number (represented in list) of a given decimal number
    #pulled from my computer organization hw1 submission    
    def __to_binary(self, n, bits):
        nCopy = n
        bNum = [0] * bits
        while(nCopy > 1):
            exp = math.floor(math.log2(nCopy))
            bNum[(bits-1)-exp] = 1
            nCopy -= math.pow(2, exp)
        if(nCopy == 1):
            bNum[bits-1] = 1

        return bNum



