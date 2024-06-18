# Assuming `dxf_lines` from the DXF parsing step
# Assuming `laser_scan_points` from the laser scan parsing step

import numpy as np
import open3d as o3d

def convert_to_point_cloud(points):
    return np.array(points)

dxf_points = []
for line in dxf_lines:
    dxf_points.append(line[0])  # Start point
    dxf_points.append(line[1])  # End point

dxf_points = convert_to_point_cloud(dxf_points)
laser_scan_points = convert_to_point_cloud(laser_scan_points)

def icp_registration(source_points, target_points):
    source = o3d.geometry.PointCloud()
    source.points = o3d.utility.Vector3dVector(source_points)
    
    target = o3d.geometry.PointCloud()
    target.points = o3d.utility.Vector3dVector(target_points)
    
    threshold = 1.0
    trans_init = np.eye(4)
    
    reg_p2p = o3d.pipelines.registration.registration_icp(
        source, target, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPoint())
    
    return reg_p2p.transformation

transformation = icp_registration(dxf_points, laser_scan_points)
print(transformation)
