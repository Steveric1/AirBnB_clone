#!/usr/bin/env  bash


class Name:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def  print_args(self):
        print(f"{self.args}")

    def print_kwargs(self):
        print(f"{self.kwargs}")

name = Name(1, 2, 3, 4, 5, 6, name="Eric", age=22)
name.print_args()
name.print_kwargs()
