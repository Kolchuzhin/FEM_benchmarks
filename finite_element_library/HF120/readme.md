## HF120,1 3-D High-Frequency Brick Solid, 1ST ORDER

HF120 is a high-frequency brick element which models 3-D electromagnetic fields and waves governed by the full set of Maxwell's equations in linear media.
It is based on a full-wave formulation of Maxwell's equations in terms of the time-harmonic electric field E (exponent jωt dependence assumed).

Size:
 * Lx=1.0*um
 * Ly=2.0*um
 * Lz=1.0*um

FREQUENCY=1E9 Hz

The first order element has one AX DOF on each edge. 
The first order hexahedral element has a total of 12 AX DOFs.





* HF120element.mac:      MAPDL macros

* HF120element.dat:	     [12x12] stiffness matrix of HF120 element into Harwell-Boeing format 
* HF120element.mapping:  node mapping




<!--
!      	            z    W
!       P  o-------------X-----------o O
!         /         ^               /|
!      X x          |    y      V  x |
!       /         U |   /         /  x A
!    M o------------x------------o N |
!      |            | /          |   |
!      |            |/           |   o K
!    Y x            *------------x--/--  x
!      |                       Z | /
!      |                         |/
!    I o-----------x-------------o J
!                  Q
!
!                   ASCII-Schematic of the problem
!
! Nodes I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B
-->
