import open3d as o3d
import numpy as np


def binary_to_ascii(pcd_name):
    # 读取binary格式的PCD文件
    pcd = o3d.io.read_point_cloud(pcd_name, format="pcd", remove_nan_points=True)
    print(pcd)

    # 将点云从binary格式转换为ASCII格式
    o3d.io.write_point_cloud(pcd_name.rsplit('.', 1)[0] + "_ascii.pcd", pcd, write_ascii=True)


def read_display_pcd_pc(path):
    pcd = o3d.io.read_point_cloud(path, format='pcd', remove_nan_points=True)
    # print(type(pcd))
    # 设置点云颜色 只能是0 1 如[1,0,0]代表红色为既r
    # pcd.paint_uniform_color([0, 1, 0])
    # 创建窗口对象
    vis = o3d.visualization.Visualizer()
    # 创建窗口，设置窗口标题
    vis.create_window(window_name="point_cloud")
    # 设置点云渲染参数
    opt = vis.get_render_option()
    # 设置背景色（这里为黑色）
    opt.background_color = np.array([255, 255, 255])
    # 设置渲染点的大小
    opt.point_size = 1.0
    # 添加点云
    vis.add_geometry(pcd)
    vis.run()


if __name__ == '__main__':
    # binary_to_ascii("1715398826.481128685.pcd")
    read_display_pcd_pc("new_pcd/pcdFiles/1715866938091591.pcd")
