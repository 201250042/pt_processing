import os
import numpy as np
import open3d as o3d


def display(filepath):
    files = os.listdir(filepath)

    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="point_cloud", height=600, width=400)
    pointcloud = o3d.geometry.PointCloud()
    to_reset = True
    vis.add_geometry(pointcloud)
    for f in files:
        pcd = o3d.io.read_point_cloud(filepath + f, format="pcd", remove_nan_points=True)
        pcd = np.asarray(pcd.points).reshape((-1, 3))
        pointcloud.points = o3d.utility.Vector3dVector(pcd)
        vis.update_geometry(pointcloud)
        if to_reset:
            vis.reset_view_point(True)
            to_reset = False
        vis.poll_events()
        vis.update_renderer()


if __name__ == "__main__":
    display("new_pcd/pcdFiles/")
