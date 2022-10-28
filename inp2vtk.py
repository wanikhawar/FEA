# Script to convert inp file to vtk file

inp = open('LPEH_coexec-domain.inp', 'r')
vtk = open('LPEH_coexec-domain.vtk', 'w')

vtk.write("# vtk DataFile Version 3.0\n")
vtk.write("Mesh Data Information\n")
vtk.write("ASCII\n")
vtk.write("DATASET UNSTRUCTURED_GRID\n\n")

# READ DATA FROM INP FILE
lines = inp.readlines()

# CREATING A LIST OF COORDINATES
nodal_data = []

nodal_flag = False
for i in range(len(lines)):
    if nodal_flag:
        nodal_data.append(lines[i])
    if lines[i] == '*Node\n':
        nodal_flag = True
    if lines[i] == '*Element, type=FC3D8\n':
        nodal_flag = False
        nodal_data.remove('*Element, type=FC3D8\n')

nodes = []
for node in nodal_data:
    nodes.append(node.replace(' ', '').replace('\n', '').split(','))

# CONVERT NODAL INDEX TO INT AND NODAL DATA TO FLOAT
for node in nodes:
    node[0] = int(node[0])
    node[1] = float(node[1])
    node[2] = float(node[2])
    node[3] = float(node[3])


num_nodes = len(nodes)
vtk.write("POINTS {} float\n".format(num_nodes))

for node in nodes:
    vtk.write("{0:.7f} {1:.7f} {2:.7f}\n".format(node[1], node[2], node[3]))

# CONNECTIVITY
conn_data = []

conn_flag = False
for i in range(len(lines)):
    if conn_flag:
        conn_data.append(lines[i])
    if lines[i] == '*Element, type=FC3D8\n':
        conn_flag = True
    if lines[i] == '*Nset, nset=Set-1, generate\n':
        conn_flag = False
        conn_data.remove('*Nset, nset=Set-1, generate\n')

elements = []
for connectivity in conn_data:
    elements.append(connectivity.replace(' ', '').replace('\n', '').split(','))

num_elem = len(elements)
vtk.write("\nCELLS {0} {1}\n".format(num_elem, num_elem * 9))

# SUBTRACT ONE FROM EACH NODE NUMBER TO START THE NUMBERING FROM ZERO
for element in elements:
    vtk.write("8 {0} {1} {2} {3} {4} {5} {6} {7}\n".format(eval(element[1])-1, eval(element[2])-1, eval(element[3])-1, eval(element[4])-1, eval(element[5])-1,
                                                           eval(element[6])-1, eval(element[7])-1, eval(element[8])-1))

vtk.write('\n')
vtk.write("CELL_TYPES {}\n".format(num_elem))
for i in range(len(elements)):
    vtk.write("12\n")

vtk.write('\nPOINT_DATA {}\n'.format(num_nodes))
vtk.write('SCALARS scalars float 1\n')
vtk.write('LOOKUP_TABLE default\n')

for i in range(num_nodes):
    vtk.write(str(i+1) + '\n')

vtk.close()
inp.close()
