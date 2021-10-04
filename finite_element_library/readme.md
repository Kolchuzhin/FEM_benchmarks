#Finite Elements

# ANSYS APDL
## The elements to do a piezoresistive (PZR) analysis in ANSYS MAPDL are:
* PLANE223, KEYOPT(1) = 101 - coupled-field 8-node quadrilateral 
* SOLID226, KEYOPT(1) = 101 - coupled-field 20-node brick 
* SOLID227, KEYOPT(1) = 101 - coupled-field 10-node tetrahedron 

## The elements for piezoelectric (PZE) analysis in ANSYS MAPDL are:
* PLANE13,  KEYOPT(1) = 7 coupled-field quadrilateral solid 
* SOLID5,   KEYOPT(1) = 0 or 3 coupled-field brick 
* SOLID98,  KEYOPT(1) = 0 or 3 coupled-field tetrahedron 
* PLANE223, KEYOPT(1) = 1001, coupled-field 8-node quadrilateral 
* SOLID226, KEYOPT(1) = 1001, coupled-field 20-node brick 
* SOLID227, KEYOPT(1) = 1001, coupled-field 10-node tetrahedron 

# The elements from CALFEM:
* soli8e == 8 node isoparametric element
