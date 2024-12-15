import numpy as np

def get_joint_coordinates(frame_number, data):
    """
    提取指定帧的17个关节点坐标。
    
    参数:
    - frame_number: 帧编号（从0开始）
    - data: 包含所有帧的3D关节点坐标的NumPy数组
    
    返回:
    - 一个17x3的NumPy数组，包含指定帧的17个关节点坐标，或者None如果帧编号超出范围。
    """
    if frame_number < 0 or frame_number >= len(data):
        return None  # 帧编号超出范围
    
    return data[frame_number]

# 读取 .npy 文件
file_path = 'outputfile.npy'  # 替换为你的文件路径
data = np.load(file_path)

# 获取第10帧的关节点坐标
frame_number = 30  # 或其他你感兴趣的帧编号
joint_coordinates = get_joint_coordinates(frame_number, data)
print("Joint coordinates for frame number {}: \n{}".format(frame_number, joint_coordinates))


