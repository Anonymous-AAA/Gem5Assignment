import os
import matplotlib.pyplot as plt

RES_DIR="specrand"
# RES_DIR="hmmer_1bil"
BASE_DIR=f"/home/anonymousa/gem5_sim/gem5/my_impl/proj/stats/{RES_DIR}"
DCACHE_MISS_STAT_NAME="system.cpu.dcache.overallMisses::total"
ICACHE_MISS_STAT_NAME="system.cpu.icache.overallMisses::total"


stat_dict={}
misses={}

for entry in os.listdir(BASE_DIR):
    assoc,repl_policy=entry.split('_')
    repl_policy=repl_policy[:-2]

    if repl_policy=="MRU":
        continue
    
    with open(f"{BASE_DIR}/{entry}/stats.txt") as stats_file:
        stats=stats_file.readlines()
    

    for stat in stats:
        stat_arr=stat.split()
        if len(stat_arr)>1:
            stat_dict[stat_arr[0]]=stat_arr[1]

    
    total_misses=int(stat_dict[DCACHE_MISS_STAT_NAME])+int(stat_dict[ICACHE_MISS_STAT_NAME])

    misses[f"{repl_policy}\nAssoc={assoc}"]=total_misses



# Extracting keys and values from the dictionary
categories = list(misses.keys())
values = list(misses.values())

# Creating the bar plot
plt.bar(categories, values,width=0.1)

# Adding title and labels
plt.title('Cache misses v/s replacement policies for all associativities')
plt.xlabel('Replacement policies for all associativities')
plt.ylabel('Cache misses')

# Showing the plot
plt.show()
    