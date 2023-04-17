from UVSimBaseCode import *
import UVSimBaseCode
import sys
import mock
from io import StringIO
import pytest


def test_all():
    '''
    tests all functions
    :return:
    '''
    uvs = UVSimBaseCode.UVSim(test_bool=True)
    file_path = r"C:\Users\Sarah\Desktop\sarah\School\2023\Spring 2023\CS 2450\UVSim\TestAll1.txt"  # whatever our file path is
    uvs.GUI.set_file_name(file_path)
    our_string = uvs.GUI.input_validation(file_path).strip().split()
    uvs.GUI.process_file()
    print(uvs.memory_dict["022"])

    assert uvs.memory_dict["022"][1] == "000100"
    assert uvs.memory_dict["026"][1] == "-000442"
    assert uvs.accumulator[1] == "-000442"


def test_all_updated():
    '''
    tests all functions
    :return:
    '''
    uvs = UVSimBaseCode.UVSim(test_bool=True)
    file_path = r"C:\Users\Sarah\Desktop\sarah\School\2023\Spring 2023\CS 2450\UVSim\TestAll1Updated.txt"  # whatever our file path is
    uvs.GUI.set_file_name(file_path)
    uvs.GUI.process_file()
    print(uvs.memory_dict["022"])

    assert uvs.memory_dict["022"][1] == "000100"
    assert uvs.memory_dict["026"][1] == "-000442"
    assert uvs.accumulator[1] == "-000442"

def test_load():
    '''load a word from a specific location in memory(val) into the accumulator'''
    sim = UVSim(test_bool=True)
    # basic test
    sim.memory_dict["021"] = [True, "05005"]
    our_register = "021"
    sim.Load(sim.memory_dict[our_register])
    assert sim.accumulator[1] == "05005"

    '''test if a negative number is in the val'''
    sim = UVSim(test_bool=True)
    sim.memory_dict["020"] = [True, "-0505"]
    our_register = "020"
    sim.Load(sim.memory_dict[our_register])
    assert sim.Load(sim.memory_dict[our_register]) != "-0505"


def test_store():
    '''store a word from the accumulator into a specific location(val) in memory'''
    # basic test
    sim = UVSim(test_bool=True)
    sim.memory_dict["012"] = [True, "04321"]
    sim.accumulator = [True, "01234"]
    our_register = "012"
    sim.Store(our_register)
    assert sim.memory_dict["012"] != [True, "09999"]
    # test if given value is in memory
    sim = UVSim(True)
    sim.memory_dict["042"] = [True, "01221"]
    sim.accumulator = [True, "09999"]
    our_register = "099"
    sim.Store(our_register)
    assert sim.memory_dict["042"] != [True, "09999"]


def test_add1():
    sim = UVSim(test_bool=True)
    # empty accumulator test
    sim.memory_dict["050"] = [False, "005005"]
    our_register = "050"
    sim.Calc.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "005005"]
    # common add test
    sim.accumulator = [False, "000050"]
    sim.memory_dict["060"] = [False, "005005"]
    our_register = "060"
    sim.Calc.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "005055"]
    # test with small numbers
    sim.accumulator = [False, "000050"]
    sim.memory_dict["060"] = [False, "000005"]
    our_register = "060"
    sim.Calc.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000055"]
    # addition of a negative
    sim.accumulator = [False, "000050"]
    sim.memory_dict["060"] = [False, "-000005"]
    our_register = "060"
    sim.Calc.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000045"]


def test_add2():
    sim = UVSim(test_bool=True)
    # empty accumulator test
    sim.memory_dict["060"] = [False, "000005"]
    our_register = "060"
    sim.Calc.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000005"]
    # common add test
    sim.accumulator = [False, "000005"]
    sim.memory_dict["071"] = [False, "003005"]
    our_register = "071"
    sim.Calc.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "003010"]
    # test with small numbers
    sim.accumulator = [False, "000000"]
    sim.memory_dict["083"] = [False, "000001"]
    our_register = "083"
    sim.Calc.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000001"]
    # addition of a negative
    sim.accumulator = [False, "-000050"]
    sim.memory_dict["060"] = [False, "000005"]
    our_register = "060"
    sim.Calc.Add(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "-000045"]


def test_subtract1():
    sim = UVSim(test_bool=True)
    # empty register test
    sim.accumulator = [False, "005555"]
    our_register = "050"
    sim.Calc.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "005555"]
    # common subtraction test
    sim.accumulator = [False, "000500"]
    sim.memory_dict["050"] = [False, "000045"]
    sim.Calc.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000455"]
    # subtraction of a negative
    sim.accumulator = [False, "000500"]
    sim.memory_dict["050"] = [False, "-000045"]
    sim.Calc.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000545"]


def test_subtract2():
    sim = UVSim(test_bool=True)
    # empty register test
    sim.accumulator = [False, "-003500"]
    our_register = "065"
    sim.Calc.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "-003500"]
    # common subtraction test
    sim.accumulator = [False, "005555"]
    sim.memory_dict["065"] = [False, "005556"]
    sim.Calc.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "-000001"]
    # subtraction of a negative
    sim.accumulator = [False, "000500"]
    sim.memory_dict["065"] = [False, "-005545"]
    sim.Calc.Subtract(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "006045"]


def test_multiply1():
    sim = UVSim(test_bool=True)
    # empty register test
    sim.accumulator = [False, "005555"]
    our_register = "050"
    sim.Calc.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000000"]
    # common multiplication test
    sim.accumulator = [False, "000500"]
    sim.memory_dict["050"] = [False, "000045"]
    sim.Calc.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "022500"]
    # negative multiplication
    sim.accumulator = [False, "000500"]
    sim.memory_dict["050"] = [False, "-000045"]
    sim.Calc.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "-022500"]


def test_multiply2():
    sim = UVSim(test_bool=True)
    # empty register test
    sim.accumulator = [False, "003333"]
    our_register = "070"
    sim.Calc.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000000"]
    # common multiplication test
    sim.accumulator = [False, "005000"]
    sim.memory_dict["070"] = [False, "000002"]
    sim.Calc.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "010000"]
    # negative multiplication
    sim.accumulator = [False, "-000056"]
    sim.memory_dict["070"] = [False, "000020"]
    sim.Calc.Multiply(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "-001120"]


def test_divide1():
    sim = UVSim(test_bool=True)
    # divide by zero test
    assert sim.Calc.Divide("000000") == "Divide by zero error"
    # empty accumulator test
    our_register = "050"
    sim.memory_dict["050"] = [False, "005555"]
    sim.Calc.Divide(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000000"]
    # common division test
    sim.accumulator = [False, "000500"]
    sim.memory_dict["050"] = [False, "000045"]
    sim.Calc.Divide(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000011"]


def test_divide2():
    sim = UVSim(test_bool=True)
    # divide by zero test
    our_register = "080"
    assert sim.Calc.Divide(sim.memory_dict[our_register][1]) == "Divide by zero error"
    # empty accumulator test
    sim.memory_dict["080"] = [False, "009555"]
    sim.Calc.Divide(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000000"]
    # common division test
    sim.accumulator = [False, "005555"]
    sim.memory_dict["080"] = [False, "001111"]
    sim.Calc.Divide(sim.memory_dict[our_register][1])
    assert sim.accumulator == [False, "000005"]


def test_Read():
    # Testing that it works with a valid input
    sim = UVSim(test_bool=True)
    with mock.patch("builtins.input", return_value="012345"):
        result = sim.GUI.Read(0)
        assert result == [False, "012345"]
        assert sim.memory_dict[0] == [False, "012345"]
    # Testing that it works with an invaild input
    with mock.patch("builtins.input", side_effect=["abcdef", "456789"]):
        result = sim.GUI.Read(0)
        assert sim.memory_dict[0] == [False, "456789"]
    # Testing what happens when the number does not have 4 digits
    with mock.patch("builtins.input", side_effect=["123", "136969"]):
        result = sim.GUI.Read(0)
        assert result == [False, "136969"]
        assert sim.memory_dict[0] == [False, "136969"]


def test_Write():
    # Testing that it works on a vaild register
    sim = UVSim(test_bool=True)
    sim.memory_dict = {0: [True, "123456"]}
    captured_output = StringIO()
    sys.stdout = captured_output
    result = sim.GUI.Write(0)
    sys.stdout = sys.__stdout__
    assert result == {'123456'}
    assert captured_output.getvalue() == "123456\n"
    # Testing that it does not work with an invalid input
    captured_output = StringIO()
    sys.stdout = captured_output
    result = sim.GUI.Write(1)
    sys.stdout = sys.__stdout__
    assert result == None
    assert captured_output.getvalue() == ""


def test_branch1(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2003\n")
        f.write("+2110\n")
        f.write("+4010\n")
        f.write("+0304\n")
        f.write("+1200")

    with b.open() as f:
        content = f.read()
        # check for all the contents
        assert content == "+2003\n+2110\n+4010\n+0304\n+1200"

    uvs = UVSim(test_bool=True)
    uvs.GUI.set_file_name(b)
    uvs.GUI.process_file()
    assert uvs.memory_dict["010"][1] == "000304"
    assert uvs.accumulator[1] == "000304"


def test_branch2(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2004\n")
        f.write("+2150\n")
        f.write("+4050\n")
        f.write("+1200\n")
        f.write("+0303")

    with b.open() as f:
        content = f.read()
        # check for all the contents
        assert content == "+2004\n+2150\n+4050\n+1200\n+0303"

    uvs = UVSim(test_bool=True)
    uvs.GUI.set_file_name(b)
    uvs.GUI.process_file()

    print(uvs.memory_dict["050"])
    assert uvs.memory_dict["050"][1] == "000303"
    assert uvs.accumulator[1] == "000303"


def test_branch_neg1(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2005\n")
        f.write("+2160\n")
        f.write("+2006\n")
        f.write("+3107\n")
        f.write("+4160\n")
        f.write("+0300\n")
        f.write("+1234\n")
        f.write("+5678\n")

    with b.open() as f:
        content = f.read()
        # check for all the contents
        assert content == "+2005\n+2160\n+2006\n+3107\n+4160\n+0300\n+1234\n+5678\n"

    uvs = UVSim(test_bool=True)
    uvs.GUI.set_file_name(b)
    uvs.GUI.process_file()

    assert uvs.memory_dict["060"][1] == "000300"
    assert uvs.accumulator[1] == "-004444"


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
        f.write("-3000\n")

    with b.open() as f:
        content = f.read()
        # check for all the contents
        assert content == "+2008\n+2170\n+2005\n+3106\n+4170\n+5678\n+1234\n+4300\n-3000\n"

    uvs = UVSim(test_bool=True)
    uvs.GUI.set_file_name(b)
    uvs.GUI.process_file()

    assert uvs.memory_dict["070"][1] == "003000"
    assert uvs.accumulator[1] == "004444"


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
        # check for all the contents
        assert content == "+2005\n+2160\n+2006\n+3107\n+4260\n+3000\n+1234\n+1234\n"

    uvs = UVSim(test_bool=True)
    our_string = content.strip().split()
    uvs.initiate_process(our_string)

    assert uvs.memory_dict["006"][1] == "001234"
    assert uvs.accumulator[1] == "002005"


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
        f.write("-3000\n")

    with b.open() as f:
        content = f.read()
        # check for all the contents
        assert content == "+2008\n+2170\n+2005\n+3106\n+4270\n+1234\n+1233\n+4300\n-3000\n"

    uvs = UVSim(test_bool=True)
    uvs.GUI.set_file_name(b)
    uvs.GUI.process_file()

    assert uvs.memory_dict["070"][1] == "003000"
    assert uvs.accumulator[1] == "000001"


def test_branch_halt1(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+4300\n")
        f.write("+3002\n")
        f.write("+2100\n")
        f.write("+0000\n")

    with b.open() as f:
        content = f.read()
        # check for all the contents
        assert content == "+4300\n+3002\n+2100\n+0000\n"

    uvs = UVSim(test_bool=True)
    uvs.GUI.set_file_name(b)
    uvs.GUI.process_file()

    assert uvs.memory_dict["002"][1] == "021000"
    assert uvs.accumulator[1] == "000000"


def test_branch_halt2(tmpdir):
    b = tmpdir.join("test_branch1.txt")
    with b.open('w') as f:
        f.write("+2004\n")
        f.write("+4300\n")
        f.write("-2005\n")
        f.write("+1234\n")
        f.write("+5678\n")

    with b.open() as f:
        content = f.read()
        # check for all the contents
        assert content == "+2004\n+4300\n-2005\n+1234\n+5678\n"

    uvs = UVSim(test_bool=True)
    uvs.GUI.set_file_name(b)
    uvs.GUI.process_file()

    assert uvs.memory_dict["002"][1] == "002005"
    assert uvs.accumulator[1] == "005678"
