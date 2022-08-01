# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux_non_zero_inp(dut):
    """Test for generating non-zero values for input lines and hitting all values of select lines, 0 to 30"""
    
    
    cocotb.log.info('##### CTB: Develop your test here ########')

    inp = {}
    k = 0
    
    #while k < 32:
    for k in range(31):
        val = random.randint(1,3)
        inp[k] = val
        # print("k value:",k)
        # print("inp[key]=:",inp[k])
        #k += 1
        
        
    for i in range(31):
        sel = i 
        #sel = random.randint(0,31) 
        # input driving
        
        dut.sel.value  = sel 
        dut.inp0.value = inp[0]
        dut.inp1.value = inp[1]
        dut.inp2.value = inp[2]
        dut.inp3.value = inp[3]
        dut.inp4.value = inp[4]
        dut.inp5.value = inp[5]
        dut.inp6.value = inp[6]
        dut.inp7.value = inp[7]
        dut.inp8.value = inp[8]
        dut.inp9.value = inp[9]
        dut.inp10.value = inp[10]
        dut.inp11.value = inp[11]
        dut.inp12.value = inp[12]
        dut.inp13.value = inp[13]
        dut.inp14.value = inp[14]
        dut.inp15.value = inp[15]
        dut.inp16.value = inp[16]
        dut.inp17.value = inp[17]
        dut.inp18.value = inp[18]
        dut.inp19.value = inp[19]
        dut.inp20.value = inp[20]
        dut.inp21.value = inp[21]
        dut.inp22.value = inp[22]
        dut.inp23.value = inp[23]
        dut.inp24.value = inp[24]
        dut.inp25.value = inp[25]
        dut.inp26.value = inp[26]
        dut.inp27.value = inp[27]
        dut.inp28.value = inp[28]
        dut.inp29.value = inp[29]
        dut.inp30.value = inp[30]


        # print("select value:",sel)
        # print("value in0:",dut.inp0.value)
        # print("value in1:",dut.inp1.value)

        def muxChecker(sel,i):
            #for i in range(s):
            if(sel==i):
                result =  inp[i]
                # print("result inside if block:",result)
            else:
                result = 0
                # print("result inside else:",result)
            return result
        

        await Timer(2, units='ns')

        #assert dut.out.value == muxChecker(sel), f"Mux result is incorrect: {dut.X.value} != muxChecker(sel)"
        assert dut.out.value == muxChecker(sel,i), "Randomised test failed with: {sel} != {out}".format(
            sel=dut.sel.value, out=dut.out.value)


@cocotb.test()
async def test_mux_rand_sel_non_zer_inp(dut):
    """Test for generating non-zero values for input lines and hitting random values of select lines, 0 to 30"""
    
    
    cocotb.log.info('##### CTB: Develop your test here ########')

    inp = {}
    k = 0
    
    #while k < 32:
    for k in range(31):
        val = random.randint(0,3)
        inp[k] = val
        # print("k value:",k)
        # print("inp[key]=:",inp[k])
        #k += 1
        
        
    for i in range(100):
        sel = random.randint(0,30) 
        # input driving
        for j in range (31):
            if(sel==j):
                j=sel
            else:
                j=31

        dut.sel.value  = sel 
        dut.inp0.value = inp[0]
        dut.inp1.value = inp[1]
        dut.inp2.value = inp[2]
        dut.inp3.value = inp[3]
        dut.inp4.value = inp[4]
        dut.inp5.value = inp[5]
        dut.inp6.value = inp[6]
        dut.inp7.value = inp[7]
        dut.inp8.value = inp[8]
        dut.inp9.value = inp[9]
        dut.inp10.value = inp[10]
        dut.inp11.value = inp[11]
        dut.inp12.value = inp[12]
        dut.inp13.value = inp[13]
        dut.inp14.value = inp[14]
        dut.inp15.value = inp[15]
        dut.inp16.value = inp[16]
        dut.inp17.value = inp[17]
        dut.inp18.value = inp[18]
        dut.inp19.value = inp[19]
        dut.inp20.value = inp[20]
        dut.inp21.value = inp[21]
        dut.inp22.value = inp[22]
        dut.inp23.value = inp[23]
        dut.inp24.value = inp[24]
        dut.inp25.value = inp[25]
        dut.inp26.value = inp[26]
        dut.inp27.value = inp[27]
        dut.inp28.value = inp[28]
        dut.inp29.value = inp[29]
        dut.inp30.value = inp[30]


        # print("select value:",sel)
        # print("value in0:",dut.inp0.value)
        # print("value in1:",dut.inp1.value)

        def muxChecker(sel,j):
            #for i in range(s):
            if(sel==j):
                result =  inp[j]
                # print("result inside if block:",result)
            else:
                result = 0
                # print("result inside else:",result)
            return result
        

        await Timer(2, units='ns')

        #assert dut.out.value == muxChecker(sel), f"Mux result is incorrect: {dut.X.value} != muxChecker(sel)"
        if(j!=31):
            assert dut.out.value == muxChecker(sel,j), "Randomised test failed with: {sel} != {out}".format(
                sel=dut.sel.value, out=dut.out.value)    

    
@cocotb.test()
async def test_mux_with_zero_inp_val(dut):
    """Test for generating non-zero values for input lines and hitting all values of select lines, 0 to 30"""
    
    
    cocotb.log.info('##### CTB: Develop your test here ########')

    inp = {}
    k = 0
    
    #while k < 32:
    for k in range(31):
        val = 0
        inp[k] = val
        # print("k value:",k)
        # print("inp[key]=:",inp[k])
        #k += 1
        
        
    for i in range(31):
        sel = i 
        #sel = random.randint(0,31) 
        # input driving
        
        dut.sel.value  = sel 
        dut.inp0.value = inp[0]
        dut.inp1.value = inp[1]
        dut.inp2.value = inp[2]
        dut.inp3.value = inp[3]
        dut.inp4.value = inp[4]
        dut.inp5.value = inp[5]
        dut.inp6.value = inp[6]
        dut.inp7.value = inp[7]
        dut.inp8.value = inp[8]
        dut.inp9.value = inp[9]
        dut.inp10.value = inp[10]
        dut.inp11.value = inp[11]
        dut.inp12.value = inp[12]
        dut.inp13.value = inp[13]
        dut.inp14.value = inp[14]
        dut.inp15.value = inp[15]
        dut.inp16.value = inp[16]
        dut.inp17.value = inp[17]
        dut.inp18.value = inp[18]
        dut.inp19.value = inp[19]
        dut.inp20.value = inp[20]
        dut.inp21.value = inp[21]
        dut.inp22.value = inp[22]
        dut.inp23.value = inp[23]
        dut.inp24.value = inp[24]
        dut.inp25.value = inp[25]
        dut.inp26.value = inp[26]
        dut.inp27.value = inp[27]
        dut.inp28.value = inp[28]
        dut.inp29.value = inp[29]
        dut.inp30.value = inp[30]


        #print("select value:",sel)
        #print("value in0:",dut.inp0.value)
        #print("value in1:",dut.inp1.value)

        def muxChecker(sel,i):
            #for i in range(s):
            if(sel==i):
                result =  inp[i]
                # print("result inside if block:",result)
            else:
                result = 0
                # print("result inside else:",result)
            return result
        

        await Timer(2, units='ns')

        #assert dut.out.value == muxChecker(sel), f"Mux result is incorrect: {dut.X.value} != muxChecker(sel)"
        assert dut.out.value == muxChecker(sel,i), "Randomised test failed with: {sel} != {out}".format(
            sel=dut.sel.value, out=dut.out.value)        
