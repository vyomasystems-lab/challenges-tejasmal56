# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer
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
    # await RisingEdge(dut.clk)
    queue.append(dut.inp_bit.value)
    print("queue inside if block:",queue)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    queue.append(dut.inp_bit.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    queue.append(dut.inp_bit.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    queue.append(dut.inp_bit.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    queue.append(dut.inp_bit.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 0
    queue.append(dut.inp_bit.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    queue.append(dut.inp_bit.value)
    await RisingEdge(dut.clk)
    dut.inp_bit.value = 1
    queue.append(dut.inp_bit.value)
    print("queue inside if block:",queue)

    # def seqChecker(queue):
    #     result = []
    #     if(queue==1011):
    #         result[0] =  queue.pop(0)
    #         result[1] =  queue.pop(0)
    #         result[2] =  queue.pop(0)
    #         result[3] =  queue.pop(0)
    #         print("result inside if block:",result)
    #     return result
    def seqChecker(queue):
        # result = []
        if(queue==1011):
            # result[0] =  queue.pop(0)
            # result[1] =  queue.pop(0)
            # result[2] =  queue.pop(0)
            # result[3] =  queue.pop(0)
            result = 1
   
            print("result inside if block:",result)
        return result    

    # await Timer(2, units='ns')
    # await RisingEdge(dut.clk)
    # assert dut.seq_seen.value == seqChecker(queue), "Randomised test failed with: {seq_seen} != {1011}".format(
    #     seq_seen=dut.seq_seen.value, inp_bit=dut.inp_bit.value)  


    
    await RisingEdge(dut.clk)
    assert dut.seq_seen.value == seqChecker(queue), "Randomised test failed with: {seq_seen} != {1011}".format(
        seq_seen=dut.seq_seen.value, inp_bit=dut.inp_bit.value)    
