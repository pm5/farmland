#!/usr/bin/env python

mappings = {
        'Cr': lambda x: x * 17.53 + 31.76,
        'Ni': lambda x: x * 4.82 + 17.78,
        'Zn': lambda x: x * 2.56 + 87.11,
        'Cu': lambda x: x * 2.03 + 9.89,
        'Pb': lambda x: x * 2.96 + 5.02,
        'Cd': lambda x: x * 1.46 + 0.03,
        }

standards = {
        'As': 60,   # PPM
        'Cd': 5,    # for food; 20 for normal use
        'Cr': 250,
        'Cu': 200,  # for food; 400 for normal use
        'Hg': 5,    # for food; 20 for normal use
        'Ni': 200,
        'Pb': 500,  # for food; 2000 for normal use
        'Zn': 600,  # for food; 2000 for normal use
        }
