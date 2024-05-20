import pcl
import json


def pcd_to_json(pcd_file, json_file):
    # 读取PCD文件
    cloud = pcl.load(pcd_file)

    # 获取点云数据
    points = cloud.to_array()

    # 将点云数据转换为JSON格式
    data = {
        "points": points.tolist()
    }

    # 将数据写入JSON文件
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    # 输入PCD文件路径和输出JSON文件路径
    pcd_file = "input.pcd"
    json_file = "output.json"

    # 转换PCD文件为JSON数据并写入新文件
    pcd_to_json(pcd_file, json_file)