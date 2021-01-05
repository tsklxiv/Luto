"""
    Luto - A simple, minimal todo list app

    Created by Hoang Tuan

    Version 1.0.0

    This is the source file of it.
"""

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
import random
from os import system

theme = Theme({"cmd": "italic", "content": "bold", "error": "bold red"})
cons = Console(theme=theme)
todos = []
color_list = ["red", "green", "blue", "yellow", "magenta"]
tags = {}
current_render_type = "normal"


def render(todos, tags, render_type):
    if render_type == "normal":
        for todo in todos:
            content, tag = todo
            tag_color = tags[tag]
            cons.print(f" - [content]{content}[/content]: [{tag_color}]{tag}[/{tag_color}]")
    elif render_type == "board":
        table = Table(title="Todos")
        table.add_column("Todo", justify="left", style="magenta")
        table.add_column("Tag", justify="right", style="magenta")

        for todo in todos:
            content, tag = todo
            tag_color = tags[tag]
            table.add_row(content, tag, style=tag_color)

        cons.print(table)


system("clear")
cons.print("Welcome to [red]Luto[/red]!")
cons.print("Type [cmd]help[/cmd] for help")
cons.print("And [cmd]quit[/cmd] to quit")


while True:
    cons.print("Todos:", style="bold")
    render(todos, tags, current_render_type)
    cons.print()
    ipt = cons.input(">>>")
    parts = ipt.split()
    if parts[0] == "help":
        cons.print("""
        Luto version 1.0.0

        [b]Commands[/b]:
            [cmd]add[/cmd]: Add a todo
            [cmd]delete[/cmd]: Delete a todo
            [cmd]help[/cmd]: Display this help
            [cmd]quit[/cmd] or [cmd]exit[/cmd]: Quit the program
            [cmd]delete_all[/cmd]: Delete all the todos
            [cmd]clear[/cmd]: Clear the screen.

            # [b]Further features:[/b]
                [cmd]delete_tag[/cmd]: Delete every todo that has the same tag
        """)
    elif parts[0] == "delete":
        try:
            todo_to_delete = int(parts[1])
            todos.pop(todo_to_delete)
        except Exception as e:
            cons.print(f"[error]Error: {e}[/error]")
    elif parts[0] == "quit" or parts[0] == "exit":
        break
    elif parts[0] == "clear":
        system("clear")
    elif parts[0] == "add":
        content = cons.input("Enter the content:")
        tag = cons.input("Enter tag name:")
        if tag not in tags:
            color = random.choice(color_list)
            tags[tag] = color
        todos.append((content, tag))
        cons.print("A [i]todo[/i] has been added! :smile:")
        need_to_save = True
    elif parts[0] == "delete_all":
        todos = []
        need_to_save = True
    else:
        cons.print(f"[error]Error: Invalid command: {parts[0]}[/error]")

