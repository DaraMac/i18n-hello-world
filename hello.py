#!/usr/bin/env python3

import gettext

gettext.install(domain="hello", localedir="locales")

def hello():
    print(_("Hello World"))

if __name__ == "__main__":
    hello()
