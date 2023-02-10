import pytest
import UVSimBaseCode
import pytest
from UVSimBaseCode import *
import UVSimBaseCode
import os
import sys
import mock
from io import StringIO

def test_add():
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
    

def test_subtract():
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

def test_multiply():
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
    
def test_divide():
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
    assert result == "REGISTER 0: +1234"
    assert captured_output.getvalue() == "REGISTER 0: +1234\n"
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
    assert uvs.accumulator == "4204"


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

    assert uvs.memory_dict["50"][1] == "3303"
    assert uvs.accumulator == "3963600"



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
    assert uvs.accumulator == "-2439"


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
    assert uvs.accumulator == "-2439"

