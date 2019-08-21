# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:36:00 2019

@author: lenovo
"""

import numpy as np
from pynput.keyboard import Key, Listener


def on_press(key):
    pass

def on_release_enter(key):
    #print('{0} release'.format(
    #    key))
    if key == Key.enter:
        # Stop listener
        return False

def print_field(field):
    print("    ",end='')
    for i in range(field.shape[1]):
        print(i," ",end='')
    print("\n")
    for i in range(field.shape[0]):
        print(i, "  ", end='')
        for j in range(field.shape[1]):
            if field[i][j] == -1:
                print(".  ", end = '')
            else:
                print(str(int(field[i][j]))+"  ", end = '')
        print()
        
def formfield(field):
    empty = 0
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if np.random.random() < sparsity:
                field[i][j] = -1
                empty += 1
    return empty

def players_pick_fields(field, pl_count, empty):
    print('Now you will pick spots from the field. Highest dice will pick first.')
    dicememo = np.zeros(pl_count)
    starting_pl_count = pl_count
    while True:
        for i in range(starting_pl_count):
            print('Player '+ str(i) + ', roll the dice (press Enter).')
            with Listener(
                    on_press=on_press,
                    on_release=on_release_enter) as listener:
                listener.join()
            dice = np.random.randint(1,7)
            dicememo[i] = dice
            print('Player '+ str(i) + ': ' + str(dice))
        if np.where(dicememo==np.max(dicememo))[0].shape[0] == 1:
            starting_player=np.where(dicememo==np.max(dicememo))[0]
            break
        else:
            starting_pl_count = np.where(dicememo==np.max(dicememo))[0].shape[0]
            # TODO: player ismi kayıyor. Bir liste yapıp whilein içindeki foru o listede döndürebilirim.
    print('Player '+ str(starting_player[0]) + ' picks first.')
        
    while empty>0:
        for pid in range(starting_player[0], starting_player[0]+pl_count):
            pid = pid%pl_count
            picked = np.random.randint(0,width*height - empty)
            filledcount = 0
            for h in range(height):
                breakflag = False
                for w in range(width):    
                    if field[h][w] == 0:
                        if filledcount == picked:
                            print("f,p:",filledcount,picked)
                            field[h][w] = pid
                            print("Player ", pid, ": ", h, ",", w)
                            breakflag = True
                            break
                        filledcount += 1
                if breakflag:
                    break
            with Listener(
                    on_press=on_press,
                    on_release=on_release_enter) as listener:
                listener.join()
        print_field(field)
        empty -= 1
        # TODO: fix this function

    print('Starting spots are set!')
        
    
global sparsity
global width
global height

width = 10
height = 10
sparsity = 0.1
#pl_count = int(input("How many players? : "))
pl_count = 3

whos_field = np.full((width,height),9)
empty = formfield(whos_field)
print_field(whos_field)
players_pick_fields(whos_field, pl_count, empty)














