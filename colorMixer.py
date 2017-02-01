def color_mixer(color1, color2):
    if (color1 == 'red' or color1 == 'blue') and (color2 == 'red' or color2 == 'blue'):
        return 'Magenta'
    elif (color1 == 'yellow' or color1 == 'blue') and (color2 == 'yellow' or color2 == 'blue'):
        return 'Green'
    elif (color1 == 'yellow' or color1 == 'red') and (color2 == 'yellow' or color2 == 'red'):
        return 'Orange'

print(color_mixer(color1='yellow', color2='red'))
print(color_mixer(color1='red', color2='red'))
print(color_mixer(color1='yellow', color2='blue'))
