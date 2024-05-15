import numpy as np

colemak = "1234567890-=qwfpgjluy;[]\\arstdhneio\'zxcvbkm,./"

qwerty = "1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./"

dvorak = "1234567890[]\',.pyfgcrl/=\\aoeuidhtns-;qjkxbmwvz"

uppercase_colemak = "!@#$%^&*()_+QWFPGJLUY:\{\}|ARSTDHNEIO\"ZXCVBKM<>?"

uppercase_qwerty = "!@#$%^&*()_+QWERTYUIOP\{\}|ASDFGHJKL:\"ZXCVBNM<>?"

uppercase_dvorak = "!@#$%^&*()\{\}\"<>PYFGCRL?+|AOEUIDHTNS_:QJKXBMWVZ"

# Define a function that maps each character from QWERTY to Colemak
def map_char(char, input_layout, output_layout):
    if char in input_layout:
        return output_layout[input_layout.index(char)]
    else:
        return char
    
# Convert input string to a numpy array of characters
input_string = input("What is your input string? ")
input_array = np.array(list(input_string))

layout_dict = {
    'c': colemak,
    'q': qwerty,
    'd': dvorak,
    'uc': uppercase_colemak,
    'uq': uppercase_qwerty,
    'ud': uppercase_dvorak
}

str_layout_dict = {
    'c': 'Colemak',
    'q': 'QWERTY',
    'd': 'Dvorak',
    'uc': 'Uppercase Colemak',
    'uq': 'Uppercase QWERTY',
    'ud': 'Uppercase Dvorak'
}

input_layout_code = input("\nWhat input layout?\nc for Colemak\nq for QWERTY\nd for Dvorak\nuc for Uppercase Colemak\nuq for Uppercase QWERTY\nud for Uppercase Dvorak\n\n")

while not input_layout_code in layout_dict:
    print("\nInvalid input layout code. Please choose a valid option.")
    input_layout_code = input("What input layout?\nc for Colemak\nq for QWERTY\nd for Dvorak\nuc for Uppercase Colemak\nuq for Uppercase QWERTY\nud for Uppercase Dvorak\n\n")
    
selected_input_layout = str_layout_dict[input_layout_code]
print(f"\nSelected input layout: {selected_input_layout}")

output_layout_code = input("\nWhat output layout?\nc for colemak\nq for qwerty\nd for dvorak\nuc for uppercase colemak\nuq for uppercase qwerty\nud for uppercase dvorak\n\n")

while not output_layout_code in layout_dict:
    print("\nInvalid input layout code. Please choose a valid option.")
    output_layout_code = input("What output layout?\nc for colemak\nq for qwerty\nd for dvorak\nuc for uppercase colemak\nuq for uppercase qwerty\nud for uppercase dvorak\n\n")

    
selected_output_layout = str_layout_dict[output_layout_code]
print(f"\nSelected output layout: {selected_output_layout}")

input_layout = layout_dict[input_layout_code]
output_layout = layout_dict[output_layout_code]

# Vectorize the function and apply it to the input array
vectorized_map_char = np.vectorize(map_char)
output_array = vectorized_map_char(input_array, input_layout, output_layout)

# Convert the output array back to a string
output_string = ''.join(output_array.tolist())

print("\n" + output_string)