import os.path

from mario import generate_mario_pyramid

# Check if files exist
def test_exists():

    err = "Die Datei mario.py existiert nicht"
    assert os.path.exists('mario.py'), err

    err = "Die Datei main.py existiert nicht"
    assert os.path.exists('main.py'), err

# Checks if accepts negative values
def test_generate_negative():
    err = "Deine Funktion darf keine negativen Werte akzeptieren"
    assert generate_mario_pyramid(-1) == None, err

# Checks if accepts 0
def test_generate_zero():
    err = "Deine Funktion darf den Wert 0 nicht akzeptieren"
    assert generate_mario_pyramid(0) == None, err

# Checks pyramid with height: 1
def test_generate_one():
    err = "Deine Funktion gibt für den Wert 1 eine falsche Pyramide aus"
    assert generate_mario_pyramid(1) == '#', err

# Checks pyramid with height: 2
def test_generate_two():
    err = "Deine Funktion gibt für den Wert 2 eine falsche Pyramide aus"
    assert generate_mario_pyramid(2) == ' #\n' \
                                        '##', err

# Checks pyramid with height: 8
def test_generate_eight():
    err = "Deine Funktion gibt für den Wert 8 eine falsche Pyramide aus"
    assert generate_mario_pyramid(8) == '       #\n' \
                                        '      ##\n' \
                                        '     ###\n' \
                                        '    ####\n' \
                                        '   #####\n' \
                                        '  ######\n' \
                                        ' #######\n' \
                                        '########', err
