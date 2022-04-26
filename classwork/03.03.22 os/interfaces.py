import os
import netifaces

def interfaces():
    print(netifaces.interfaces())
    open('~/bash_history')