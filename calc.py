#!/usr/bin/env python3

###
# This module contains the calculator functions like add, subtract, multiply, divide, square, square root, and inverse.
# This app can be accessed by command line using click using command line script
###

import click


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# build a click group
@click.group()
def calc():
    pass


# add command to the group
@calc.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_command(a, b):
    # print results in colored format
    click.secho(str(add(a, b)), fg="green")


# subtract command to the group
@calc.command("subtract")
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract_command(a, b):
    # print results in colored format
    click.secho(str(subtract(a, b)), fg="red")


# multiply command to the group
@calc.command("multiply")
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply_command(a, b):
    # print results in colored format
    click.secho(str(multiply(a, b)), fg="blue")


# divide command to the group
@calc.command("divide")
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide_command(a, b):
    # print results in colored format
    click.secho(str(divide(a, b)), fg="yellow")


if __name__ == "__main__":
    calc()
