# generates the displacement data for each frame/time as a row in an output file. This can be read by a script from
# Scilab/Matlab and would return SVD for the system, which can be written to the odb as a modal data using another
# script.
from odbAccess import *
from abaqusConstants import *
from odbMaterial import *
from odbSection import *
import itertools

# Open ODB
odb = openOdb(path='NLPFEH_LD_NBC_01MS_T60-fluid_domain.odb')

# Frames
fs = odb.steps['flow'].frames

# Open a file vorticity.dat in write mode
f = open('velocity.dat', 'w+')

# Open a file ns.txt in write mode
nss = open('ns.txt', 'w+')


for i in range(len(fs)):
    vel = dict([(velocity.nodeLabel, velocity.data[0]) for velocity in fs[i].fieldOutputs['V'].values])
    vels = list(itertools.chain(vel.values()))
    ns = list(vel.keys())
    f.write('%s\n'%(str(vels)[1:-1]))

f.close()
nss.write('%s\n'%(str(ns)[1:-1]))
nss.close()



