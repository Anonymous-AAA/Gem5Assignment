import os
import matplotlib.pyplot as plt

# RES_DIR="specrand"
# RES_DIR="hmmer_1bil"
RES_DIR="sjeng_1bil"
BASE_DIR=f"/home/anonymousa/gem5_sim/gem5/my_impl/proj/stats/{RES_DIR}"
# DCACHE_MISS_STAT_NAME="system.cpu.dcache.overallMisses::total"
# ICACHE_MISS_STAT_NAME="system.cpu.icache.overallMisses::total"
HOST_SECONDS="hostSeconds"
IPC="system.cpu.ipc"
SIM_SECONDS="simSeconds"
NUM_CYCLES="system.cpu.numCycles"

Parameter=NUM_CYCLES


stat_dict={}
# collected_stats={}
categories=[]
values=[]

for entry in os.listdir(BASE_DIR):
    assoc,repl_policy=entry.split('_')
    repl_policy=repl_policy[:-2]

    # if repl_policy=="MRU":
    #     continue
    
    with open(f"{BASE_DIR}/{entry}/stats.txt") as stats_file:
        stats=stats_file.readlines()
    

    for stat in stats:
        stat_arr=stat.split()
        if len(stat_arr)>1:
            stat_dict[stat_arr[0]]=stat_arr[1]

    
    # total_misses=int(stat_dict[DCACHE_MISS_STAT_NAME])+int(stat_dict[ICACHE_MISS_STAT_NAME])

    # collected_stats[f"{repl_policy}\n{'Fully Assoc' if assoc=='512'  else 'Assoc='+assoc}"]=stat_dict[Parameter]
    categories.append(f"{repl_policy}\n{'Fully Assoc' if assoc=='512'  else 'Assoc='+assoc}")
    values.append(stat_dict[Parameter])


# Extracting keys and values from the dictionary
# categories = list(collected_stats.keys())
# values = list(collected_stats.values())


# Creating the bar plot
plt.bar(categories, values,width=0.1)

# Adding title and labels
plt.title(f"Performance({Parameter}) v/s replacement policies for all associativities ({RES_DIR})")
plt.xlabel('Replacement policies for all associativities')
plt.ylabel(f"{Parameter}")

# Showing the plot
plt.show()
    