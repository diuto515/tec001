import re

def is_hex_color(s):
    return (re.fullmatch(r'#[0-9a-fA-F]{6}', s))


print(is_hex_color("#FF57784"))  
print(is_hex_color("#848f5702"))   
print(is_hex_color("#a1B292"))