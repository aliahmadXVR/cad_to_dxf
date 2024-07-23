import ezdxf
import matplotlib.pyplot as plt

def dxf_to_image(dxf_path, image_path):
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()

    fig, ax = plt.subplots()
    for entity in msp:
        if entity.dxftype() == 'LINE':
            start_point = entity.dxf.start
            end_point = entity.dxf.end
            ax.plot([start_point.x, end_point.x], [start_point.y, end_point.y], 'k-')

    ax.set_aspect('equal')
    plt.axis('off')
    plt.savefig(image_path, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

# dxf_to_image('/home/ali/test_ws/src/my_package/CADs/corner_area_cad.dxf', '/home/ali/test_ws/src/my_package/CADs/corner_area_cad.png')
dxf_to_image('/home/ali/test_ws/src/my_package/CADs/meeting_room_cad.dxf', '/home/ali/test_ws/src/my_package/CADs/meeting_room_cad.png')
