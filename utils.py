"""
Utilities

"""
import math, operator as op

__all__ = ['replace_chars', 'tokenize', 'standard_env', 'fmt']


def replace_chars(text, replacements):

    for fromchar, tochar in replacements:
        text = text.replace(fromchar, tochar)

    return text


def tokenize(text):
    return replace_chars(text, [('(', ' ( '), (')', ' ) ')]).split()


def fmt(symbol):

    try:
        return float(symbol)

    except ValueError:
        return symbol


def standard_env():

    env = dict()

    env.update(vars(math))
    env.update({
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
        '/': op.truediv,
        '>': op.gt,
        '<': op.lt,
        '>=': op.ge,
        '<=': op.le,
        '=': op.eq,
        '^': op.pow,
    })

    return env
