'''
There is n number of houses where each house will have energy and coin
Entering the house can happen only in sequence
can pick either energy or coin
what is the maximum number of coins can collect?
'''

import functools

init_energy = 2
energy = [1,3,1,1]
coin = [2,1,1,3]

def energy_or_coin(num,index):
    result = 'energy'
    if len(coin[index+1:len(energy)]) < num: return 'coin'
    for int_coins in sorted(coin[(index+1):len(coin)])[::-1][0:num]:
        if coin[index] >= int_coins:
            result = 'coin'
            break
    else:
        if index == len(coin)-1: return 'coin'
    return result
        

def max_sum(num,lst_energy):
    if len(lst_energy) < num: num = len(lst_energy)
    result = functools.reduce( lambda x, y: x+y, sorted(lst_energy)[::-1][0:num])
    return result

total_energy = total1_energy = init_energy
total_max = max_sum(total_energy,coin)
total_coin = 0
for index,single_energy in enumerate(energy):

    resp = energy_or_coin(total1_energy + single_energy - 1, index)
    if resp == 'coin':
        if index == len(coin)-1:
            total_coin += coin[index]
        elif total1_energy - 1 == 0:
            total1_energy = total1_energy + single_energy - 1
        else:
            total1_energy = total1_energy - 1
            total_coin += coin[index]
    else:
        total1_energy = total1_energy + single_energy - 1
       
    
    total_energy = total_energy + single_energy - 1
    if coin[index+1:len(energy)]:
        tmp_total = max_sum(total_energy, coin[index+1:len(energy)])
    if total_max < tmp_total: total_max = tmp_total
    
print ("Final output: %s or %s" %(total_max,total_coin)) 
    
