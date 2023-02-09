import pytest
import UVSimBaseCode
def main():
    '''
    Call your tests here
    :return:
    '''
    test_add()


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


if __name__ == '__main__':
    main()
