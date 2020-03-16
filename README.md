# blender_gear
Python script to create a mesh in Blender shaped like a gear

To create a gear, call the spur function:

spur(name, n, r, width, wholeDepth, topLand=0.5, bottomLand=0.5)
name: string: the name of the Blender object
n: integer: the number of teeth the gear has
r: positive real number: the radius of the gear, from the center to the topland
width: positive real number: the thickness of the gear
wholeDepth: the difference in height from the topland to the bottomland

topLand and bottomLand: If we define the distance from one point on a tooth to the analogous point on an adjacent tooth to be 
one period, then topLand and bottomLand measure the length of the topland and bottomlands respectively relative to the period. 
Leave the values at 0.5 and the teeth will be straight. If they add to less than 1, the teeth will be sloped.
