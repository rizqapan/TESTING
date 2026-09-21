# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: TaskBazaar
import re

def tokenize_expression(expr):
    """Tokenize a simple arithmetic expression into a list of tokens."""
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        if expr[i] in '()+*-':
            tokens.append(('OP', expr[i]))
            i += 1
        elif expr[i].isdigit() or (expr[i] == '-' and i + 1 < len(expr) and (expr[i + 1].isdigit() or expr[i + 1] == '(')):
            start = i
            if expr[i] == '-':
                i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                i += 1
            tokens.append(('NUM', expr[start:i]))
        else:
            i += 1
    return tokens
