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
                print("x  ", end = '')
            else:
                if field[i][j] == -2:
                    print(".  ", end = '')
                else:
                    print(str(int(field[i][j]))+"  ", end = '')
        print()
        
def formfield(field):
    empty = []
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if np.random.random() < sparsity:
                field[i][j] = -1
            else:    
                empty.append((i,j))
    return empty

def players_pick_fields(field, pl_count, empty, need_press):
    print('Now you will pick spots from the field. Dots are the places you can select,\
         x\'s represent the sea, so noone can take them. Highest dice will pick first.\n')
    dicememo = np.zeros(pl_count)
    starting_pl_count = list(range(pl_count))
    while True:
        for i in starting_pl_count:
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
            #starting_pl_count = np.where(dicememo==np.max(dicememo))[0].shape[0]
            starting_pl_count = list(np.where(dicememo==np.max(dicememo))[0])
            # TODO: PROBABLY DONE... player ismi kayıyor. Bir liste yapıp whilein içindeki foru o listede döndürebilirim.
    print('Player '+ str(starting_player[0]) + ' picks first.')
    with Listener(
            on_press=on_press,
            on_release=on_release_enter) as listener:
        listener.join()

    while len(empty)>0:
        # start from the starting player
        # the other dices mean nothing. Order will be clockwise (in this case,
        # increasing order).
        for pid in range(starting_player[0], starting_player[0]+pl_count):
            pid = pid%pl_count
            if len(empty) == 0:
                break
            picked = np.random.randint(len(empty))
            h,w = empty[picked]
            empty.remove((h,w))
            field[h][w] = pid
            if need_press:
                print("Player ", pid, ": ", h, ",", w)
                print_field(field)
            if len(empty)>0 and need_press:
                with Listener(
                        on_press=on_press,
                        on_release=on_release_enter) as listener:
                    listener.join()

    print('Starting spots are set!')
    print_field(field)
        
    
global sparsity
global width
global height

width = 10
height = 10
sparsity = 0.4
#pl_count = int(input("How many players? : "))
pl_count = 3

whos_field = np.full((width,height),-2) # -2 indicated not selected yet in the field representation.
empty = formfield(whos_field)
print_field(whos_field)
need_press = False
players_pick_fields(whos_field, pl_count, empty, need_press)














