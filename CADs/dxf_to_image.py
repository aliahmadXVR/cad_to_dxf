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

    # Set the figure size for high resolution (1080p)
    fig.set_size_inches(19.2, 10.8)  # 1920x1080 divided by 100 dpi

    plt.savefig(image_path, bbox_inches='tight', pad_inches=0, dpi=100)
    plt.close(fig)

# Example usage
dxf_to_image('/home/ali/test_ws/src/my_package/CADs/meeting_room_cad.dxf', '/home/ali/test_ws/src/my_package/CADs/meeting_room_cad_h.png')
