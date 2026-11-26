#!/usr/bin/env python3
"""Entry for make.fun bounty: The One-Line Excuse Championship

A tiny one-liner joke program. Run it and it prints the joke.
"""

JOKE = "My excuse is that I don't have an excuse. Which is, in itself, an excuse. I'm very good at this."


def tell_joke():
    """Return the one-line joke for this bounty."""
    return JOKE


def main():
    print(tell_joke())


if __name__ == "__main__":
    main()
