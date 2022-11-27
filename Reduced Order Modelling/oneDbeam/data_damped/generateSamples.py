# generates the displacement data for each frame/time as a row in an output file. This can be read by a script from
# Scilab/Matlab and would return SVD for the system, which can be written to the odb as a modal data using another
# script.
from odbAccess import *
from abaqusConstants import *
from odbMaterial import *
from odbSection import *
import itertools

# Open ODB
odb = openOdb(path='Job-4.odb')

# Frames
fs = odb.steps['Step-1'].frames

# Open a file vorticity.dat in write mode
f = open('displacement.dat', 'w+')

# Open a file ns.txt in write mode
nss = open('ns.txt', 'w+')


for i in range(len(fs)):
    udict = dict([(u.nodeLabel, (u.data[0], u.data[1])) for u in fs[i].fieldOutputs['U'].values])
    us = list(itertools.chain(*udict.values()))
    ns = list(udict.keys())
    f.write('%s\n'%(str(us)[1:-1]))

f.close()
nss.write('%s\n'%(str(ns)[1:-1]))
nss.close()



