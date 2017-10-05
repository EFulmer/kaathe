#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""very bad thing"""

import ast
from ast import Load, Name, parse
import sys
from reverse import rev_args


EXAMPLE_BODY = """
def foo(a, b):
    return a + b
print(foo("a", "b"))
"""


class FuncTransformer(ast.NodeTransformer):

    def visit_FunctionDef(self, node):
        clobbered_node = node
        clobbered_node.decorator_list.insert(0, Name(id='rev_args', ctx=Load()))
        return ast.copy_location(clobbered_node, node)



def transform_module(module_string, fname='<string>'):
    parsed = parse(module_string)
    transformed = FuncTransformer().visit(parsed)
    ast.fix_missing_locations(transformed)
    compiled = compile(transformed, fname, 'exec')
    if fname == '<string>':
        exec(compiled)
    else:
        return compiled

def main():
    """
    Transform input .py file if provided, otherwise run simple_demo.
    Argument is assumed to be a syntactically valid Python module.
    """
    if len(sys.argv) < 2:
        transform_module(EXAMPLE_BODY)
    else:
        module = sys.argv[1]
        with open(transform_module, 'r') as f:
            transform_module(f.read(), module)


if __name__ == '__main__':
    main()
