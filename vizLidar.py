import numpy as np
import open3d as o3d
import pptk

# P = np.random.rand(100,3)
# v = pptk.viewer(P)

def main():
    pcd = o3d.io.read_point_cloud("data/sets/nuscenes/samples/RADAR_FRONT/n008-2018-08-01-15-16-36-0400__RADAR_FRONT__1533151608521984.pcd") # Read the point cloud
    draw_geometries([pcd]) # Visualize the point cloud
    xyz_load = np.asarray(pcd_load.points)
    print('xyz_load')
    print(xyz_load)
if __name__ == "__main__":
    main()
