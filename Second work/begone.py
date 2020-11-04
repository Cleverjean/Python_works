import os
import shutil

try:
    shutil.rmtree('cunt')
    print('You\'re fucked!')
except FileNotFoundError:
    print('Dafuq u doin?')
