#!/usr/bin/env python

from __future__ import print_function


def time_conversion(s):
    pm = s[-2:].lower() == "pm"
    replace = s[:2]
    hour = int(replace)

    if pm:
        if hour < 12:
            replace = str(hour + 12)
    else:
        if hour == 12:
            replace = "00"

    return replace + s[2:-2]
