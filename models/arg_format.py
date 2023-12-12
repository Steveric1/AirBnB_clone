#!/usr/bin/python3

import re
from shlex import split

"""arg_format - formatting argument parse to
commandline
    arg: argument parse in
"""


def arg_parse(arg):
    braces = re.search(r"\{(.*?)\}", arg)
    sqr_bracket = re.search(r"\[(.*?)\]", arg)

    if braces is None:
        if sqr_bracket is None:
            return [iterate.strip(",") for iterate in split(arg)]
        else:
            my_arg = split(arg[:sqr_bracket.span()[0]])
            ret = [iterate.strip(",") for iterate in my_arg]
            ret.append(sqr_bracket.group())
            return ret
    else:
        my_arg = split(arg[:braces.span()[0]])
        ret = [iterate.strip(",") for iterate in my_arg]
        ret.append(braces.group())
        return ret
