import bpy, math

def spur(name, n, r, width, wholeDepth, topLand=0.5, bottomLand=0.5):
	m = bpy.data.meshes.new(name)
	o = bpy.data.objects.new(name, m)
	vertices = []
	faces = []
	a = 2*math.pi/n
	slopeLand = (1-topLand-bottomLand)/2
	for i in range(n):
		vertices.append((r*math.cos(a*i), r*math.sin(a*i), 0))
		vertices.append((r*math.cos(a*(i+topLand)), r*math.sin(a*(i+topLand)), 0))
		vertices.append(((r-wholeDepth)*math.cos(a*(i+topLand+slopeLand)), (r-wholeDepth)*math.sin(a*(i+topLand+slopeLand)), 0))
		vertices.append(((r-wholeDepth)*math.cos(a*(i+topLand+slopeLand+bottomLand)), (r-wholeDepth)*math.sin(a*(i+topLand+slopeLand+bottomLand)), 0))
	for i in range(4*n):
		v = vertices[i]
		vertices.append((v[0], v[1], width))
	vertices.append((0,0,0))
	vertices.append((0,0,width))
	for i in range(n-1):
		faces.append([4*i, 4*i+1, 4*n+4*i+1, 4*n+4*i]) # top land
		faces.append([4*i+1, 4*i+2, 4*n+4*i+2, 4*n+4*i+1]) # slope
		faces.append([4*i+2, 4*i+3, 4*n+4*i+3, 4*n+4*i+2]) # bottom land
		faces.append([4*i+3, 4*i+4, 4*n+4*i+4, 4*n+4*i+3]) # slope
		faces.append([4*i+3, 4*i+4, 4*i+5, 4*i+6])
		faces.append([4*n+4*i+3, 4*n+4*i+4, 4*n+4*i+5, 4*n+4*i+6])
		faces.append([4*i+3, 4*i+6, 8*n]) # slice
		faces.append([4*n+4*i+3, 4*n+4*i+6, 8*n+1])
		faces.append([4*i+2, 4*i+3, 8*n]) # slice
		faces.append([4*n+4*i+2, 4*n+4*i+3, 8*n+1])
	faces.append([4*n-4, 4*n-3, 4*n+4*n-3, 4*n+4*n-4]) # top land
	faces.append([4*n-3, 4*n-2, 4*n+4*n-2, 4*n+4*n-3]) # slope
	faces.append([4*n-2, 4*n-1, 4*n+4*n-1, 4*n+4*n-2]) # bottom land
	faces.append([4*n-1, 0, 4*n, 8*n-1]) # slope
	faces.append([0, 1, 2, 4*n-1])
	faces.append([4*n, 4*n+1, 4*n+2, 8*n-1])
	faces.append([4*(n-1)+3, 2, 8*n]) # slice
	faces.append([4*n+4*(n-1)+3, 4*n+2, 8*n+1])
	faces.append([4*(n-1)+2, 4*(n-1)+3, 8*n]) # slice
	faces.append([4*n+4*(n-1)+2, 4*n+4*(n-1)+3, 8*n+1])
	m.from_pydata(vertices, [], faces)
	bpy.data.collections.get("Collection").objects.link(o)
	bpy.context.view_layer.objects.active = o
