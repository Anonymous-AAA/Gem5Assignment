import m5
from m5.objects import *
from ass_caches import *
#from m5.objects.ReplacementPolicies import RandomRP,LRURP,FIFORP,MRURP


assocs=[2,4,8,512]  #512 for fully assoc
repl_policies=[RandomRP(),LRURP(),FIFORP(),MRURP()]


system=System()

system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '2GHz'
system.clk_domain.voltage_domain = VoltageDomain()

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('2048MB')]

system.cpu = X86TimingSimpleCPU()

system.membus = SystemXBar()

#no cache
# system.cpu.icache_port = system.membus.cpu_side_ports
# system.cpu.dcache_port = system.membus.cpu_side_ports

system.cpu.icache = L1ICache()
system.cpu.dcache = L1DCache()

system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)


# system.l2bus = L2XBar()

# system.cpu.icache.connectBus(system.l2bus)
# system.cpu.dcache.connectBus(system.l2bus)


# system.l2cache = L2Cache()
# system.l2cache.connectCPUSideBus(system.l2bus)
system.membus = SystemXBar()
# system.l2cache.connectMemSideBus(system.membus)


system.cpu.icache.connectBus(system.membus)
system.cpu.dcache.connectBus(system.membus)


system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports


system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports


#binary = 'tests/test-progs/hello/bin/x86/linux/hello'

#specrand (ok)
dir='/home/anonymousa/spec/benchspec/CPU2006/999.specrand/run/run_base_ref_gcc43-64bit.0000'
binary=f"{dir}/specrand_base.gcc43-64bit"

#hmmer
# dir='/home/anonymousa/spec/benchspec/CPU2006/456.hmmer/run/run_base_ref_gcc43-64bit.0000'
# binary=f"{dir}/hmmer_base.gcc43-64bit"

#sjeng
# dir='/home/anonymousa/spec/benchspec/CPU2006/458.sjeng/run/run_base_ref_gcc43-64bit.0000'
# binary=f"{dir}/sjeng_base.gcc43-64bit"



# for gem5 V21 and beyond
system.workload = SEWorkload.init_compatible(binary)

process = Process()

#specrand
process.cmd = [binary,'1255432124', '234923']



#hmmer
# process.cmd = [binary,f"{dir}/nph3.hmm", f"{dir}/swiss41"]

#sjeng
# process.cmd = [binary,f"{dir}/ref.txt"]


system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system = False, system = system)


for assoc in assocs:
    system.cpu.icache.assoc=assoc
    system.cpu.dcache.assoc=assoc
    for repl_policy in repl_policies:
        system.cpu.icache.replacement_policy=repl_policy
        system.cpu.dcache.replacement_policy=repl_policy

        m5.instantiate()

        print(f"Beginning simulation for assoc={assoc} and repl_policy={repl_policy}!")
        exit_event = m5.simulate()

        print('Exiting @ tick {} because {}'
            .format(m5.curTick(), exit_event.getCause()))
