def color_mixer(color1, color2):
    if (color1 == 'red' or 'blue')) and (color2 == ('red' or 'blue')):
        return 'Magenta'
    elif (color1 == ('yellow' or 'blue')) and (color2 == ('yellow' or 'blue')):
        return 'Green'
    elif (color1 == ('yellow' or 'red')) and (color2 == ('yellow' or 'red')):
        return 'Orange'

print(color_mixer(color1='yellow', color2='red'))
print(color_mixer(color1='red', color2='red'))
print(color_mixer(color1='yellow', color2='blue'))
