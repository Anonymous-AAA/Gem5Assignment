from m5.objects import Cache,WriteAllocator
from m5.objects.ReplacementPolicies import RandomRP,LRURP,FIFORP,MRURP


# class WriteAllocatorBlkSize(WriteAllocator):
#     block_size=128

class L1Cache(Cache):
    #assoc = 2
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20
    size = '64kB'
    #replacement_policy=RandomRP()
    # write_allocator=WriteAllocatorBlkSize()

    def connectCPU(self, cpu):
        # need to define this in a base class!
        raise NotImplementedError

    def connectBus(self, bus):
        self.mem_side = bus.cpu_side_ports


class L1ICache(L1Cache):

    def connectCPU(self, cpu):
        self.cpu_side = cpu.icache_port


class L1DCache(L1Cache):

    def connectCPU(self, cpu):
        self.cpu_side = cpu.dcache_port


# class L2Cache(Cache):
#     size = '256kB'
#     assoc = 8
#     tag_latency = 20
#     data_latency = 20
#     response_latency = 20
#     mshrs = 20
#     tgts_per_mshr = 12

#     def connectCPUSideBus(self, bus):
#         self.cpu_side = bus.mem_side_ports

#     def connectMemSideBus(self, bus):
#         self.mem_side = bus.cpu_side_ports
