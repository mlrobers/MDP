from enum import Enum
from operator import itemgetter

class MDP:

    init_value = 0

    def __init__(self, s, a, p, r, y):
        self.states = s
        self.get_actions = a
        self.reward = r
        self.transition_model = p
        self.discount = y
        self.get_successors = None
        self.is_terminal_state = None
        self.u = None
        self.u_prime = None
        self.pi = None
        self.optimal_policies = None
        self.delta = 0

    def __str__(self):
        return self.draw_grid()

    def value_iteration(self, epsilon):
        self.u = dict()
        self.u_prime = dict()
        for state in self.states:
            self.u[state] = self.init_value
            self.u_prime[state] = self.init_value
        self.delta = 0

        while True:
            self.u = dict(self.u_prime)
            self.delta = 0
            print(self.u)

            self.value_update()
            if self.discount == 0:
                d = 0
            else:
                d = epsilon * (1 - self.discount) / self.discount
            if self.delta < max(d, 0.001):
                self.update_optimal_policies()
                return self.u

    def policy_iteration(self):
        self.u = dict()
        self.pi = dict()
        for state in self.state:
            some_action = self.get_actions(state)[0]
            self.u[state] = 0
            self.pi[state] = some_action

        while True:
            self.policy_evaluation()
            changed = False
            for state in self.states:
                a = self.max_action_value(state, self.get_actions(state), self.get_successors(state))
                b = self.sum_successors_policy(self.get_successors(state))
                if a > b:
                    self.pi[state] = self.argmax(self.get_actions(state), self.get_successors(state))
                    changed = True

            if changed: break

    def max_action_value(self, state, action_list, successor_list):
        t_list = list()
        for action in action_list:
            t = 0
            for s_prime in successor_list:
                t += self.transition_model(state, action, s_prime) * self.u[s_prime]
            t_list.append(t)
        return max(t_list)

    def sum_successors_policy(self, successor_list):
        pass

    def argmax(self, action_list, successor_list):
        pass

    def value_update(self):
        for state in self.states:
            if self.is_terminal_state(state):
                self.u_prime[state] = self.reward(state)
            else:
                actions = self.get_actions(state)
                successor_states = self.get_successors(state)
                t_list = list()
                for a in actions:
                    t = 0
                    for s_prime in successor_states:
                        t += self.transition_model(state, a, s_prime) * self.u[s_prime]
                    t_list.append(t)
                max_t = max(t_list)
                self.u_prime[state] = self.reward(state) + (self.discount * max_t)

            b = abs(self.u[state] - self.u_prime[state])
            if b > self.delta:
                self.delta = b

    def policy_evaluation(self):
        for state in self.states:
            if self.is_terminal_state(state):
                self.u_prime[state] = self.reward(state)
            else:
                successor_states = self.get_successors(state)
                t = 0
                for s_prime in successor_states:
                    t += self.transition_model(state, self.pi[state], s_prime) * self.u[s_prime]
                self.u[state] = self.reward(state) + self.discount * t


    def optimal_policy(self, state):
        successor_list = self.get_successors(state)
        action_list = self.get_actions(state)
        action_value_pairs = []
        for action in action_list:
            value = 0
            for successor_state in successor_list:
                value += self.transition_model(state, action, successor_state) * self.u[successor_state]

            action_value_pairs.append((value, action))

        return max(action_value_pairs, key = itemgetter(0))[1]

    def update_optimal_policies(self):
        self.optimal_policies = dict()

        for state in self.states:
            self.optimal_policies[state] = self.optimal_policy(state)

    def draw_grid(self):
        s = str()
        max_i = 0
        max_j = 0
        for state in self.states:
            i = state[0]
            j = state[1]
            if i > max_i:
                max_i = i
            if j > max_j:
                max_j = j

        for i in range(1, max_i + 1):
            for j in range(1, max_j + 1):
                if (i, j) in self.states:
                    if self.is_terminal_state((i, j)):
                        s += str(self.reward((i, j)))
                    else:
                        optimal_action = self.optimal_policies[(i, j)]
                        if optimal_action == Direction.NORTH:
                            s += "^"
                        if optimal_action == Direction.EAST:
                            s += ">"
                        if optimal_action == Direction.SOUTH:
                            s += "v"
                        if optimal_action == Direction.WEST:
                            s += "<"
                else:
                    s += "*"
                s += "\t"
            s += "\n"

        return s


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
