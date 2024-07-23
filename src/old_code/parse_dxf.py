import ezdxf

def parse_dxf(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()
    lines = []
    for entity in msp:
        if entity.dxftype() == 'LINE':
            start_point = entity.dxf.start
            end_point = entity.dxf.end
            lines.append((start_point, end_point))
    return lines

dxf_lines = parse_dxf('/home/ali/test_ws/src/my_package/CADs/cad1.dxf')
print(dxf_lines)
