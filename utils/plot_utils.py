import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plot_img_with_patches(im, faces, eyes=None):
    _, ax = plt.subplots()
    ax.axis('off')
    ax.imshow(im, cmap='gray')
    
    rectangles = []
    for face in faces:
        rectangles.append(
            patches.Rectangle((face[0], face[1]), face[2], face[3],
                              linewidth=1, edgecolor='r', facecolor='none')
        )

    if eyes is not None:
        for eye in eyes:
            rectangles.append(
                patches.Rectangle((eye[0], eye[1]), eye[2], eye[3],
                                  linewidth=1, edgecolor='r', facecolor='none')
            )
    for rectangle in rectangles:
        ax.add_patch(rectangle)
    plt.show()