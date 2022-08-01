# MUX Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

GITPOD ID: https://vyomasystem-challengest-rwgmezlragt.ws-us54.gitpod.io/

## Verification Environment

The test drives inputs to the Design Under Test (mux module here) which takes in 2-bit inputs inp0-inp30 and selects a particular input based on the select line value

The values are assigned to the input ports inp0-inp30 with values 0-3(2bits) and select line input with values 0-30(5bits)
```
dut.inp0.value = inp[0]
.
.
.
dut.inp30.value = inp[30]
```

The assert statement is used for comparing the mux's ouput to the expected value, the expected value is coded inside a function called the muxChecker.

The following error is seen:
```
assert dut.out.value == muxChecker(sel,i), "test failed with: {sel!=i} != {out}".format(
            AssertionError: Mux result is incorrect: if(sel==1), expected value(out)=inp[1]={0,1,2,3})
```
## Test Scenario 1 **(Important)**
- Test Inputs: inp0-inp30 = {1,2,3} , sel = 0-30//non-zero values
- Expected Output: 
  Ex:
  if(sel=1)
  out= inp[1] //i.e, non-zero values{1,2,3} 

  ## Test Scenario 2 **(Important)**
- Test Inputs: inp0-inp30 = {0,1,2,3} , sel = 0-30, random values for sel and inp0-30 //randomly repeated for different values
- Expected Output: 
  Ex:
  if(sel=1)
  out= inp[1] 

  Similarly check for all the inputs values of sel signal {0 - 30}values
- 1. Observed Output in the DUT dut.out is not equal to inp12 when sel='d12
- 2. Observed Output in the DUT dut.out is not equal to inp30 when sel='d30

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, see the following

```
 case(sel)
      5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12; =====> BUG_1 sel='d12 ('b01100)not available instead it is 'd13('b01101)
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
                              ====> BUG_2 //inp30 not assigned
      default: out = 0;
    endcase
  end
```


## Design Fix
Updating the design and re-running the test makes the test pass.

Fail Test snap :(https://imgur.com/BqL6Mo4)
Pass Test Snap: (https://imgur.com/gqwGSZc)

The updated design is checked in as mux_fix.v

## Verification Strategy
Directed Test:non-zero of inp values for all select value as default is set as 0, so we can easily find out if there any problem with the select case and assigned input case.
Random Test: randomly generate all input values including zero input values for different select values. For further scenarios with randomly generated zer and non-zero values.

## Is the verification complete ?
Yes
