import gmsh
import sys
gmsh.initialize()

lc = 0.1
a = 0.5
gmsh.model.add("ownfigure")

p = (list(map(float, input().split())))
print(p)
n=int(len(p)/2)
for i in range(n):
	gmsh.model.geo.addPoint(p[2*i+0], p[2*i+1], 0, lc, i+1)

for i in range(n-1):
	gmsh.model.geo.addLine(i+1, i+2, i+1)

gmsh.model.geo.addLine(n, 1, n)
gmsh.model.geo.addCurveLoop([i+1 for i in range(n)], 1)


gmsh.model.geo.addPoint(0, 0, 0, lc, n+1)
gmsh.model.geo.addPoint(a, 0, 0, lc, n+2)
gmsh.model.geo.addPoint(-a, 0, 0, lc, n+3)
gmsh.model.geo.addCircleArc(n+2, n+1, n+3, n+1)
gmsh.model.geo.addCircleArc(n+3, n+1, n+2, n+2)
gmsh.model.geo.addCurveLoop([n+1, n+2], 2)



gmsh.model.geo.addPlaneSurface([1,-2], 1)
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)
if '-nopopup' not in sys.argv:
	gmsh.fltk.run()
gmsh.write("ownfigure.msh") 
gmsh.finalize()
#3 3 2 2 1 5 -1 3 -2 0 0 -3
