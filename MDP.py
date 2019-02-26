class MDP:
    states = [] # list of states
    actions = None # Action function, ACTIONS(s)
    p = None # Transition Model, P(s'|s,a)
    rewards = None # Rewards function, REWARDS(s)
    discount = 1 # discount to rewards


    def __init__(self, S, A, P, R, Y):
        """

        :param S: Set of states
        :param A: ACTIONS(s)
        :param P: P(s'|s,a)
        :param R: REWARDS(s)
        :param Y: Discount
        """

        states = S
        actions = A
        p = P
        rewards = R
        discount = Y


    def get_successor_states(self, s):
        successor_states = []
        for a in self.actions(s):
            for potential_succesor in self.states:
                prob = self.p(s,a,potential_succesor)
                if prob > 0:
                    successor_states.append(potential_succesor)
        return successor_states

def value_iteration(mdp, epsilon):
    u = None
    u_prime = None
    delta = 0

    while True:
        u = u_prime
        delta = 0
        for state in mdp.states:
            actions = mdp.actions(state)
            successorStates = mdp.get_successor_states(state)
            t_list = []
            for a in actions:
                t = 0
                for s_prime in successorStates:
                    t += mdp.p(state, a, s_prime) * u[s_prime]
                t_list.append(t)
            t_sum = sum(t_list)
            u_prime[state] = mdp.rewards(state) + mdp.discount * t_sum

            if abs(u_prime[state] - u[state]) > delta:
                delta = abs(u_prime[state] - u[state])

        if delta < epsilon * (1 - mdp.discount) / mdp.discount:
            return u