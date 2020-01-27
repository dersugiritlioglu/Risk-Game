# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:49:14 2020

@author: Dersu Giritlioglu
"""

# RISK GAME PROBABILITIES
# A - Attack
# D - Defence

print("\n\t%\tDEF WINS\t-\tDRAW\t-\tATT WINS")
dice = [1,2,3,4,5,6]

# 3A - 1D
a_2dead = 0
draw = 0
d_2dead = 0


for a1 in dice:
    for a2 in dice:
        for a3 in dice:
            for d1 in dice:
                a_death = 0
                d_death = 0
                a_max = max(a1,a2,a3)
                d_max = d1
                if d_max >= a_max:
                    a_death += 1
                else:
                    d_death += 1
                
                if a_death > d_death:
                    a_2dead += 1
                else:
                    d_2dead += 1

                        
print("3A - 1D: ", "{:12.2f}".format(a_2dead/6**4*100), "{:21.2f}".format(draw/6**4*100), "{:17.2f}".format(d_2dead/6**4*100))
###############################################################################

# 3A - 2D
a_2dead = 0
draw = 0
d_2dead = 0


for a1 in dice:
    for a2 in dice:
        for a3 in dice:
            for d1 in dice:
                for d2 in dice:
                    a_death = 0
                    d_death = 0
                    a_max = max(a1,a2,a3)
                    d_max = max(d1,d2)
                    if d_max >= a_max:
                        a_death += 1
                    else:
                        d_death += 1
                    a_others = [a1,a2,a3]
                    a_others.remove(a_max)
                    d_others = [d1,d2]
                    d_others.remove(d_max)
                    
                    a_max2 = max(a_others)
                    d_max2 = max(d_others)
                    if d_max2 >= a_max2:
                        a_death += 1
                    else:
                        d_death += 1
                    
                    if a_death > d_death:
                        a_2dead += 1
                    elif a_death == d_death:
                        draw += 1
                    else:
                        d_2dead += 1

                        
print("3A - 2D: ", "{:12.2f}".format(a_2dead/6**5*100), "{:21.2f}".format(draw/6**5*100), "{:17.2f}".format(d_2dead/6**5*100))
###############################################################################

                        
# 2A - 2D
a_2dead = 0
draw = 0
d_2dead = 0

for a1 in dice:
    for a2 in dice:
        for d1 in dice:
            for d2 in dice:
                a_death = 0
                d_death = 0
                a_max = max(a1,a2)
                d_max = max(d1,d2)
                if d_max >= a_max:
                    a_death += 1
                else:
                    d_death += 1
                a_others = [a1,a2]
                a_others.remove(a_max)
                d_others = [d1,d2]
                d_others.remove(d_max)
                
                a_max2 = max(a_others)
                d_max2 = max(d_others)
                if d_max2 >= a_max2:
                    a_death += 1
                else:
                    d_death += 1
                
                if a_death > d_death:
                    a_2dead += 1
                elif a_death == d_death:
                    draw += 1
                else:
                    d_2dead += 1

                        
print("2A - 2D: ", "{:12.2f}".format(a_2dead/6**4*100), "{:21.2f}".format(draw/6**4*100), "{:17.2f}".format(d_2dead/6**4*100))
                        
###############################################################################

# 2A - 1D
a_2dead = 0
draw = 0
d_2dead = 0

for a1 in dice:
    for a2 in dice:
        for d1 in dice:
            a_death = 0
            d_death = 0
            a_max = max(a1,a2)
            d_max = d1
            if d_max >= a_max:
                a_death += 1
            else:
                d_death += 1
            
            if a_death > d_death:
                a_2dead += 1
            else:
                d_2dead += 1

                        
print("2A - 1D: ", "{:12.2f}".format(a_2dead/6**3*100), "{:21.2f}".format(draw/6**3*100), "{:17.2f}".format(d_2dead/6**3*100))
                                            
###############################################################################

# 1A - 1D
a_2dead = 0
draw = 0
d_2dead = 0

for a1 in dice:
    for d1 in dice:
        a_death = 0
        d_death = 0
        a_max = a1
        d_max = d1
        if d_max >= a_max:
            a_death += 1
        else:
            d_death += 1
        
        if a_death > d_death:
            a_2dead += 1
        else:
            d_2dead += 1

                        
print("1A - 1D: ", "{:12.2f}".format(a_2dead/6**2*100), "{:21.2f}".format(draw/6**2*100), "{:17.2f}".format(d_2dead/6**2*100))
                                            
                        
                        
                        
                        
                        
                        
                        
                        