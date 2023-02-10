import pytest
import UVSimBaseCode
import os
import sys
import mock
from io import StringIO

def test_add():

    

    '''
    possible example
    :return:
    '''
    '''
    example for this, what it may look like.
    uvs = UVSimBaseCode.UVSim()
    file_path = "" #whatever our file path is
    our_string = UVSimBaseCode.input_validation(file_path).strip().split()
    uvs.process_instructions(our_string)
    assert (uvs.accumulator == 4)
    
    '''

def test_Read():
    #Testing that it works with a valid input
    sim = UVSimBaseCode.UVSim()
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
    sim = UVSimBaseCode.UVSim()
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


    
