import os.path

from mario import generate_mario_pyramid

# Check if files exist
def test_exists():
    assert os.path.exists('mario.py')
    assert os.path.exists('main.py')

# Checks if accepts negative values
def test_generate_negative():
    assert generate_mario_pyramid(-1) == None

# Checks if accepts 0
def test_generate_zero():
    assert generate_mario_pyramid(0) == None

# Checks pyramid with height: 1
def test_generate_one():
    assert generate_mario_pyramid(1) == '#'

# Checks pyramid with height: 2
def test_generate_two():
    assert generate_mario_pyramid(2) == ' #\n' \
                                        '##'

# Checks pyramid with height: 8
def test_generate_eight():
    assert generate_mario_pyramid(8) == '       #\n' \
                                        '      ##\n' \
                                        '     ###\n' \
                                        '    ####\n' \
                                        '   #####\n' \
                                        '  ######\n' \
                                        ' #######\n' \
                                        '########'
