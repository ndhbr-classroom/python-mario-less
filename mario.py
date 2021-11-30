# Generate Mario like Pyramid
def generate_mario_pyramid(height):
    pyramid = ''

    # Check for individual numbers
    if (height <= 0 or height > 8):
        return

    # Generate
    for i in range(height):
        # Loop to add spaces
        for k in range(height - i, 1, -1):
            pyramid += ' '
        # Loop to add hashes
        for j in range(0, i+1, 1):
            pyramid += '#'
        
        if (i < height - 1):
            pyramid += '\n'

    # Print result
    return pyramid