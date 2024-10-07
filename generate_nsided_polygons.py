from datetime import datetime
import numpy as np

# Rows of polygons
L = 2
# Columns of polygons
M = 2
# Number of polygon sides
N = 32

# Layer 0 initial center
center_x = 15000  
center_y = 15000  
# Dimension of each polygon layer 0
width0 = 4000  
height0 = 3000   
# Dimension of each polygon layer 1
width1 = 3000     
height1 = 2000    
# Offset between layer 0 polygons
offset_00_x = 10000   
offset_00_y = 8000  
# Offset between layer 1 polygons
offset_01_x = 2800
offset_01_y = -2000   

# Get the current date and time
current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

# Create the content for the file
content = f"""HEADER 600 
BGNLIB {current_time} {current_time} 
LIBNAME LIB
UNITS 0.001 1e-09 

BGNSTR {current_time} {current_time} 
STRNAME POLYGONS_ARRAY

"""

# Structure to hold polygons
polygons = []

# Create MxN polygons for layer 0 and layer 1
for i in range(L):  
    for j in range(M): 

        layer0_x = center_x + j * offset_00_x
        layer0_y = center_y + i * offset_00_y

        # Generate N+1 points
        start_theta = np.pi / N
        end_theta = start_theta + 2 * np.pi
        theta = np.linspace(start_theta, end_theta, N+1) 

        # Calculate the x and y coordinates
        a = width0 / 2 * np.sqrt(2)
        b = height0 / 2 * np.sqrt(2)
        layer0_coords = [(round(a * np.cos(t) + layer0_x), round(b * np.sin(t) + layer0_y)) for t in theta]
        polygons.append({'layer': 0, 'coordinates': layer0_coords})

        # Store Layer 1 Boundary coordinates
        layer1_coords = [(round(a * np.cos(t) + layer0_x + offset_01_x), round(b * np.sin(t) + layer0_y + offset_01_y)) for t in theta]
        polygons.append({'layer': 1, 'coordinates': layer1_coords})

# Generate the content based on the stored polygons
for poly in polygons:
    layer = poly['layer']
    coords = poly['coordinates']
    content += f"""BOUNDARY 
LAYER {layer} 
DATATYPE 0 
XY
"""
    for x, y in coords:
        content += f"{int(x)}: {int(y)}\n"
    content += "ENDEL \n\n"

content += """ENDSTR
ENDLIB
"""

# Write the content to a file
filename = f"polygons_{N}sided_{L}x{M}_layout.txt"
with open(filename, "w") as file:
    file.write(content)

print(f"File '{filename}' generated successfully.")
