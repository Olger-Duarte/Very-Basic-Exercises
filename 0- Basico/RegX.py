import re

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

new_filenames = []

for filename in filenames:
    change_filename = re.search("[.]hpp$", filename)
    
    if change_filename: 
        new_filenames.append(filename.replace(".hpp", ".h"))
    else:
        new_filenames.append(filename)
        
print(new_filenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

###