# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    queue = []
  


# queue.append('b')
# queue.append('c')
  
# print("Initial queue")
# print(queue)
  
# # Removing elements from the queue
# print("\nElements dequeued from queue")
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    queue.append(dut.inp_bit.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1

    def seqChecker():
            if():
                result =  inp[i]
                print("result inside if block:",result)
        

        await Timer(2, units='ns')
        assert dut.seq_seen.value == seqChecker(sel,i), "Randomised test failed with: {sel} != {out}".format(
            sel=dut.sel.value, out=dut.out.value)    
