#binary
import open3d as o3d
import numpy as np
import numpy as np
import mayavi.mlab
def read_pcd(file_path1):
    pcd = o3d.io.read_point_cloud(file_path1)
    #pcd2 = o3d.io.read_point_cloud(file_path2)

    print(np.asarray(pcd.points))

    #print(np.asarray(pcd2.points))
    #colors = np.asarray(pcd.colors) * 255

    pointcloud = np.asarray(pcd.points)
    #pointcloud2 = np.asarray(pcd2.points)

    print(pointcloud.shape)

    #print(pointcloud2.shape)
    x = pointcloud[:, 0]  # x position of point
    xmin = np.amin(x, axis=0)
    xmax = np.amax(x, axis=0 )
    y = pointcloud[:, 1]  # y position of point
    ymin = np.amin(y, axis=0)
    ymax = np.amax(y, axis=0)
    z = pointcloud[:, 2]  # z position of point
    zmin = np.amin(z, axis=0)
    zmax = np.amax(z, axis=0)
    print(xmin,xmax,ymin,ymax,zmin,zmax)
    d = np.sqrt(x ** 2 + y ** 2)  # Map Distance from sensor
    vals = 'height'
    if vals == "height":
        col = z
    else:
        col = d
    fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(640, 500))
    mayavi.mlab.points3d(x, y, z,
                         col,  # Values used for Color
                         mode="point",
                         # 灰度图的伪彩映射
                         colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                         # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                         figure=fig,
                         )
    # 绘制原点
    mayavi.mlab.points3d(0, 0, 0, color=(1, 1, 1), mode="sphere",scale_factor=0.2)
    # 绘制坐标
    axes = np.array(
        [[20.0, 0.0, 0.0, 0.0], [0.0, 20.0, 0.0, 0.0], [0.0, 0.0, 20.0, 0.0]],
        dtype=np.float64,
    )
    #x轴
    mayavi.mlab.plot3d(
        [0, axes[0, 0]],
        [0, axes[0, 1]],
        [0, axes[0, 2]],
        color=(1, 0, 0),
        tube_radius=None,
        figure=fig,
    )
    #y轴
    mayavi.mlab.plot3d(
        [0, axes[1, 0]],
        [0, axes[1, 1]],
        [0, axes[1, 2]],
        color=(0, 1, 0),
        tube_radius=None,
        figure=fig,
    )
    #z轴
    mayavi.mlab.plot3d(
        [0, axes[2, 0]],
        [0, axes[2, 1]],
        [0, axes[2, 2]],
        color=(0, 0, 1),
        tube_radius=None,
        figure=fig,
    )
    mayavi.mlab.show()

if __name__ == '__main__':
#mayavi显示点云
    read_pcd("new_pcd/pcdFiles/1715866938091591.pcd")
