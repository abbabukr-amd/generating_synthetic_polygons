from datetime import datetime

# Rows of rectangles
M = 10
# Columns of rectangles
N = 20

# Layer 0 initial center
center_x = 15000  
center_y = 15000  
# Dimension of each rectangle layer 0
width0 = 4000  
height0 = 3000   
# Dimension of each rectangle layer 1
width1 = 3000     
height1 = 2000    
# offset between layer 0 rectangles
offset_00_x = 6000   
offset_00_y = 5000  
# offset between layer 0 rectangles
offset_01_x = 1600
offset_01_y = -1400   


# Calculate half width and height for center positioning
half_width0 = width0 // 2
half_height0 = height0 // 2
half_width1 = width1 // 2
half_height1 = height1 // 2

# Get the current date and time
current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

# Create the content for the file
content = f"""HEADER 600 
BGNLIB {current_time} {current_time} 
LIBNAME LIB
UNITS 0.001 1e-09 

BGNSTR {current_time} {current_time} 
STRNAME RECTANGLES_ARRAY

"""

# Create MxN rectangles for layer 0 and layer 1
for i in range(M):  
    for j in range(N): 
        # Calculate offsets for layer 0
        layer0_x = center_x + j * offset_00_x
        layer0_y = center_y + i * offset_00_y

        # Layer 0 Boundary
        content += f"""BOUNDARY 
LAYER 0 
DATATYPE 0 
XY
{int(layer0_x - half_width0)}: {int(layer0_y - half_height0)}
{int(layer0_x - half_width0)}: {int(layer0_y + half_height0)}
{int(layer0_x + half_width0)}: {int(layer0_y + half_height0)}
{int(layer0_x + half_width0)}: {int(layer0_y - half_height0)}
ENDEL 

"""

        # Layer 1 Boundary with the same offset
        layer1_x = layer0_x + offset_01_x
        layer1_y = layer0_y + offset_01_y
        content += f"""BOUNDARY 
LAYER 1 
DATATYPE 0 
XY
{int(layer1_x - half_width1)}: {int(layer1_y - half_height1)}
{int(layer1_x - half_width1)}: {int(layer1_y + half_height1)}
{int(layer1_x + half_width1)}: {int(layer1_y + half_height1)}
{int(layer1_x + half_width1)}: {int(layer1_y - half_height1)}
ENDEL 

"""

content += """ENDSTR
ENDLIB
"""

# Write the content to a file
filename = f"rectangles_{M}x{N}_layout.txt"
with open(filename, "w") as file:
    file.write(content)

print(f"File '{filename}' generated successfully.")