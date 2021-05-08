import gmsh
import sys

gmsh.initialize()

gmsh.model.add("t3")
a=0.5
lc = 0.1
gmsh.model.geo.addPoint(2, 0, 0, lc, 1)
gmsh.model.geo.addPoint(0, 3, 0, lc, 2)
gmsh.model.geo.addPoint(-2, 0, 0, lc, 3)
gmsh.model.geo.addPoint(0, -3, 0, lc, 4)
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(3, 2, 2)
gmsh.model.geo.addLine(3, 4, 3)
gmsh.model.geo.addLine(4, 1, 4)
gmsh.model.geo.addCurveLoop([4, 1, -2, 3], 1)

gmsh.model.geo.addPoint(0, 0, 0, lc, 7)
gmsh.model.geo.addPoint(a, 0, 0, lc, 5)
gmsh.model.geo.addPoint(-a, 0, 0, lc, 6)
gmsh.model.geo.addCircleArc(5, 7, 6, 5)
gmsh.model.geo.addCircleArc(6, 7, 5, 6)
gmsh.model.geo.addCurveLoop([5, 6], 2)

gmsh.model.geo.addPlaneSurface([1, -2], 1)

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(2)

gmsh.write("t3.msh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
