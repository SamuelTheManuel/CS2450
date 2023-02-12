import pytest
import UVSimBaseCode
import pytest
from UVSimBaseCode import *
import UVSimBaseCode
import os
import sys
import mock
from io import StringIO

def test_all():
    '''
    tests all functions
    :return:
    '''
    uvs = UVSimBaseCode.UVSim()
    file_path = r"C:\Users\Sarah\Desktop\sarah\School\2023\Spring 2023\CS 2450\UVSim\TestAll1.txt"  # whatever our file path is
    our_string = UVSimBaseCode.input_validation(file_path).strip().split()
    uvs.initiate_process(our_string)
    print(uvs.memory_dict["22"])
    assert uvs.memory_dict["22"][1] == "0100"
    assert uvs.memory_dict["26"][1] == "-0442"
    assert uvs.accumulator[1] == "-0442"

def test_load():
    '''load a word from a specific location in memory(val) into the accumulator'''
    sim = UVSim()
    #basic test
    sim.memory_dict["21"] = [True, "5005"]
    our_register = "21"
    sim.Load(sim.memory_dict[our_register])
    assert sim.accumulator[1] == "5005"

    '''test if a negative number is in the val'''
    sim = UVSim()
    sim.memory_dict["20"] = [True, "-505"]
    our_register = "20"
    sim.Load(sim.memory_dict[our_register])
    assert sim.Load(sim.memory_dict[our_register]) != "-505"


def test_store():
    '''store a word from the accumulator into a specific location(val) in memory'''
    #basic test
    sim = UVSim()
    sim.memory_dict["12"] = [True, "4321"]
    sim.accumulator = [True, "1234"]
    our_register = "12"
    sim.Store(our_register)
    assert sim.memory_dict["12"] != [True, "9999"]
    
    #test if given value is in memory
    sim = UVSim()
    sim.memory_dict["42"] = [True, "1221"]
    sim.accumulator = [True, "9999"]
    our_register = "100"
    sim.Store(our_register)
    assert sim.memory_dict["42"] != [True, "9999"]
    
def test_add1():
    sim = UVSim()
    # empty accumulator test
    sim.memory_dict["50"] = [False, "5005"]
    our_register = "50"
    sim.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "5005"]
    # common add test
    sim.accumulator = [False, "+0050"]
    sim.memory_dict["60"] = [False, "5005"]
    our_register = "60"
    sim.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "5055"]
    # test with small numbers
    sim.accumulator = [False, "+0050"]
    sim.memory_dict["60"] = [False, "0005"]
    our_register = "60"
    sim.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0055"]
    # addition of a negative
    sim.accumulator = [False, "+0050"]
    sim.memory_dict["60"] = [False, "-0005"]
    our_register = "60"
    sim.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0045"]

def test_add2():
    sim = UVSim()
    # empty accumulator test
    sim.memory_dict["60"] = [False, "0005"]
    our_register = "60"
    sim.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0005"]
    # common add test
    sim.accumulator = [False, "+0005"]
    sim.memory_dict["71"] = [False, "3005"]
    our_register = "71"
    sim.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "3010"]
    # test with small numbers
    sim.accumulator = [False, "+0000"]
    sim.memory_dict["83"] = [False, "0001"]
    our_register = "83"
    sim.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0001"]
    # addition of a negative
    sim.accumulator = [False, "-0050"]
    sim.memory_dict["60"] = [False, "+0005"]
    our_register = "60"
    sim.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "-0045"]
    

def test_subtract1():
    sim = UVSim()
    # empty register test
    sim.accumulator = [False, "5555"]
    our_register = "50"
    sim.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "5555"]
    # common subtraction test
    sim.accumulator = [False, "0500"]
    sim.memory_dict["50"] = [False, "0045"]
    sim.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0455"]
    # subtraction of a negative
    sim.accumulator = [False, "0500"]
    sim.memory_dict["50"] = [False, "-0045"]
    sim.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0545"]

def test_subtract2():
    sim = UVSim()
    # empty register test
    sim.accumulator = [False, "-3500"]
    our_register = "65"
    sim.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "-3500"]
    # common subtraction test
    sim.accumulator = [False, "5555"]
    sim.memory_dict["65"] = [False, "5556"]
    sim.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "-0001"]
    # subtraction of a negative
    sim.accumulator = [False, "0500"]
    sim.memory_dict["65"] = [False, "-5545"]
    sim.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "6045"]

def test_multiply1():
    sim = UVSim()
    # empty register test
    sim.accumulator = [False, "5555"]
    our_register = "50"
    sim.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0000"]
    # common multiplication test
    sim.accumulator = [False, "0500"]
    sim.memory_dict["50"] = [False, "0045"]
    sim.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "22500"]
    # negative multiplication
    sim.accumulator = [False, "0500"]
    sim.memory_dict["50"] = [False, "-0045"]
    sim.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "-22500"]

def test_multiply2():
    sim = UVSim()
    # empty register test
    sim.accumulator = [False, "3333"]
    our_register = "70"
    sim.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0000"]
    # common multiplication test
    sim.accumulator = [False, "5000"]
    sim.memory_dict["70"] = [False, "0002"]
    sim.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "10000"]
    # negative multiplication
    sim.accumulator = [False, "-0056"]
    sim.memory_dict["70"] = [False, "0020"]
    sim.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "-1120"]

def test_divide1():
    sim = UVSim()
    # divide by zero test
    assert sim.Divide("0000") == "Divide by zero error"
    # empty accumulator test
    our_register = "50"
    sim.memory_dict["50"] = [False, "5555"]
    sim.Divide(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0000"]
    # common division test
    sim.accumulator = [False, "0500"]
    sim.memory_dict["50"] = [False, "0045"]
    sim.Divide(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0011"]

def test_divide2():
    sim = UVSim()
    # divide by zero test
    our_register = "80"
    assert sim.Divide(sim.memory_dict[our_register][1]) == "Divide by zero error"
    # empty accumulator test
    sim.memory_dict["80"] = [False, "9555"]
    sim.Divide(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0000"]
    # common division test
    sim.accumulator = [False, "5555"]
    sim.memory_dict["80"] = [False, "1111"]
    sim.Divide(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "0005"]

def test_Read():
    #Testing that it works with a valid input
    sim = UVSim()
    with mock.patch("builtins.input", return_value="1234"):
        result = sim.Read(0)
        assert result == [False, "1234"]
        assert sim.memory_dict[0] == [False, "1234"]
    #Testing that it works with an invaild input
    with mock.patch("builtins.input", side_effect=["abcd", "5678"]):
        result = sim.Read(0)
        assert result == [False, "5678"]
        assert sim.memory_dict[0] == [False, "5678"]
    #Testing what happens when the number does not have 4 digits
    with mock.patch("builtins.input", side_effect=["123", "5678"]):
        result = sim.Read(0)
        assert result == [False, "5678"]
        assert sim.memory_dict[0] == [False, "5678"]

def test_Write():
    #Testing that it works on a vaild register
    sim = UVSim()
    sim.memory_dict = {0: [True, "1234"]}
    captured_output = StringIO()
    sys.stdout = captured_output
    result = sim.Write(0)
    sys.stdout = sys.__stdout__
    assert result == {'1234'}
    assert captured_output.getvalue() == "1234\n"
    #Testing that it does not work with an invalid input
    captured_output = StringIO()
    sys.stdout = captured_output
    result = sim.Write(1)
    sys.stdout = sys.__stdout__
    assert result == None
    assert captured_output.getvalue() == ""




def test_branch1(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2003\n")
        f.write("+2110\n")
        f.write("+4010\n")
        f.write("+3004\n")
        f.write("+1200")

    with b.open() as f:
        content = f.read()
        #check for all the contents
        assert content == "+2003\n+2110\n+4010\n+3004\n+1200"

    uvs = UVSim()
    our_string = content.strip().split()
    uvs.initiate_process(our_string)

    assert uvs.memory_dict["10"][1] == "3004"
    assert uvs.accumulator == [False,"4204"]


def test_branch2(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2004\n")
        f.write("+2150\n")
        f.write("+4050\n")
        f.write("+1200\n")
        f.write("+3303")

    with b.open() as f:
        content = f.read()
        #check for all the contents
        assert content == "+2004\n+2150\n+4050\n+1200\n+3303"

    uvs = UVSim()
    our_string = content.strip().split()
    uvs.initiate_process(our_string)

    print(uvs.memory_dict["50"])
    assert uvs.memory_dict["50"][1] == "3303"
    assert uvs.accumulator == [False,"3963600"]



def test_branch_neg1(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2005\n")
        f.write("+2160\n")
        f.write("+2006\n")
        f.write("+3107\n")
        f.write("+4160\n")
        f.write("+3000\n")
        f.write("+1234\n")
        f.write("+5678\n")


    with b.open() as f:
        content = f.read()
        #check for all the contents
        assert content == "+2005\n+2160\n+2006\n+3107\n+4160\n+3000\n+1234\n+5678\n"

    uvs = UVSim()
    our_string = content.strip().split()
    uvs.initiate_process(our_string)

    assert uvs.memory_dict["60"][1] == "3000"
    assert uvs.accumulator[1] == "-2439"


def test_branch_neg2(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2008\n")
        f.write("+2170\n")
        f.write("+2005\n")
        f.write("+3106\n")
        f.write("+4170\n")
        f.write("+5678\n")
        f.write("+1234\n")
        f.write("+4300\n")
        f.write("+3000\n")


    with b.open() as f:
        content = f.read()
        #check for all the contents
        assert content == "+2008\n+2170\n+2005\n+3106\n+4170\n+5678\n+1234\n+4300\n+3000\n"

    uvs = UVSim()
    our_string = content.strip().split()
    uvs.initiate_process(our_string)

    assert uvs.memory_dict["70"][1] == "3000"
    assert uvs.accumulator[1] == "4444"



def test_branch_zero1(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2005\n")
        f.write("+2160\n")
        f.write("+2006\n")
        f.write("+3107\n")
        f.write("+4260\n")
        f.write("+3000\n")
        f.write("+1234\n")
        f.write("+1234\n")


    with b.open() as f:
        content = f.read()
        #check for all the contents
        assert content == "+2005\n+2160\n+2006\n+3107\n+4260\n+3000\n+1234\n+1234\n"

    uvs = UVSim()
    our_string = content.strip().split()
    uvs.initiate_process(our_string)

    assert uvs.memory_dict["06"][1] == "1234"
    assert uvs.accumulator[1] == "2005"


def test_branch_zero1(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2008\n")
        f.write("+2170\n")
        f.write("+2005\n")
        f.write("+3106\n")
        f.write("+4270\n")
        f.write("+1234\n")
        f.write("+1233\n")
        f.write("+4300\n")
        f.write("+3000\n")


    with b.open() as f:
        content = f.read()
        #check for all the contents
        assert content == "+2008\n+2170\n+2005\n+3106\n+4270\n+1234\n+1233\n+4300\n+3000\n"

    uvs = UVSim()
    our_string = content.strip().split()
    uvs.initiate_process(our_string)

    assert uvs.memory_dict["70"][1] == "3000"
    assert uvs.accumulator[1] == "0001"


def test_branch_halt1(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+4300\n")
        f.write("+3002\n")
        f.write("+2100\n")
        f.write("+0000\n")


    with b.open() as f:
        content = f.read()
        #check for all the contents
        assert content == "+4300\n+3002\n+2100\n+0000\n"

    uvs = UVSim()
    our_string = content.strip().split()
    uvs.initiate_process(our_string)

    assert uvs.memory_dict["02"][1] == "2100"
    assert uvs.accumulator[1] == "0000"


def test_branch_halt2(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2004\n")
        f.write("+4300\n")
        f.write("+2005\n")
        f.write("+1234\n")
        f.write("+5678\n")


    with b.open() as f:
        content = f.read()
        #check for all the contents
        assert content == "+2004\n+4300\n+2005\n+1234\n+5678\n"
        

    uvs = UVSim()
    our_string = content.strip().split()
    uvs.initiate_process(our_string)

    assert uvs.memory_dict["02"][1] == "2005"
    assert uvs.accumulator[1] == "5678"
