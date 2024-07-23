def parse_laser_scan(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points

laser_scan_points = parse_laser_scan('/home/ali/test_ws/src/my_package/src/laser_scan.txt')
print(laser_scan_points)
