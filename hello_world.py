from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.resources.resource import Resource
from gem5.simulate.simulator import Simulator
from gem5.isas import ISA
from m5.objects import Cache

class L1Cache(Cache):
    assoc = 2
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20


cache_hierarchy=PrivateL1CacheHierarchy()
memory=SingleChannelDDR3_1600("1GiB")
processor=SimpleProcessor(cpu_type=CPUTypes.TIMING,num_cores=1,isa=ISA.X86)

board=SimpleBoard(clk_freq="3GHz",processor=processor,memory=memory,cache_hierarchy=cache_hierarchy)

binary=Resource("x86-hello64-static")

board.set_se_binary_workload(binary=binary)

simultator=Simulator(board=board)
simultator.run()