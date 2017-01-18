def color_mixer(color1, color2):
    if (color1 == 'red' or 'blue') and (color2 == 'red' or 'blue'):
        return 'Magenta'
    elif (color1 == 'yellow' or 'blue') and (color2 == 'yellow' or 'blue'):
        return 'Green'
    elif (color1 == 'yellow' or 'red') and (color2 == 'yellow' or 'red'):
        return 'Orange'

if __name__ == '__main__':
    print(color_mixer('red', 'yellow'))