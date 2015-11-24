"""
A lisp REPL

"""

from utils import *


def parse(tokens):
    """
    Converts a list of tokens into an abstract syntax tree

    """

    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')

    token = tokens.pop(0)
    if token == '(':
        expr = []
        while tokens[0] != ')':
            expr.append(parse(tokens))
        tokens.pop(0) # pop off ')'
        return expr

    elif token == ')':
        raise SyntaxError('unexpected ")"')

    else:
        return fmt(token)


class REPL:

    def __init__(self, env):
        """
        A toy Read-Evaluate-Print-Loop

        """

        self.env = env

    def __call__(self, x):
        """
        Evaluate an expression in the given environment

        """

        if isinstance(x, str):
            return self.env[x]

        elif not isinstance(x, list):
            return x

        # conditionals
        elif x[0] == 'if':
            _, test, then, otherwise = x
            expr = then if self(test) else otherwise
            return self(expr)

        # store variable in memory
        elif x[0] == 'define':
            _, var, expr = x
            value = self(expr)
            self.env[var] = value
            return 'Stored {} = {}'.format(var, value)

        # function call
        else:
            operator = self(x[0])
            args = [self(arg) for arg in x[1:]]
            return operator(*args)

    def run(self, prompt='\n$ '):

        try:
            while True:
                text = input(prompt)
                program = parse(tokenize(text))
                response = self(program)
                print('> {}'.format(response))

        except KeyboardInterrupt:
            print('\nGoodbye!')


if __name__ == '__main__':

    env = standard_env()
    REPL(env).run()
