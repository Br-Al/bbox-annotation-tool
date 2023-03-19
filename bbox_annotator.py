import cv2
import os


def draw_rectangle(event, x, y, flags, params):
    global pt1, pt2
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        pt2 = (x, y)
        cv2.rectangle(source, pt1, pt2, (0, 255, 0), 2)
        face = source[pt1[1]:pt2[1], pt1[0]:pt2[0]]
        cv2.imwrite(os.path.join(save_face_dir, f'{image_name}{pt1[0]}{pt1[1]}{pt2[0]}{pt2[1]}.png'), face)
        mode = 'a' if os.path.exists(os.path.join(annotations_file_dir, 'annotations.txt')) else 'w'
        with open(os.path.join(annotations_file_dir, 'annotations.txt'), f'{mode}+') as f:
            f.writelines(f'{image_name} 1 {pt1[0]} {pt1[1]} {pt2[0]} {pt2[1]}\n')
        cv2.imshow('Face Annotation Tool', source)

def bbox_annotator(im_path='data/images/ai.png', save_dir='data/images/', annotations_dir='data/annotations/'):
    global source, save_face_dir, annotations_file_dir, image_name
    save_face_dir = os.path.join(save_dir)
    annotations_file_dir = os.path.join(annotations_dir)
    image_name = im_path.split('/')[-1]
    try:
        source = cv2.imread('data/images/ai.png')
    except FileNotFoundError as e:
        print('File not found ', e)
        exit()
    dummy = source.copy()
    cv2.namedWindow('Face Annotation Tool')
    cv2.setMouseCallback('Face Annotation Tool', draw_rectangle)
    k = 0

    while k != 27:
        cv2.imshow('Face Annotation Tool', source)
        cv2.putText(
            source, 
            'Select top left corner, and drag, Press ESC to exit and c to clear', 
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        ) 

        k = cv2.waitKey(20) & 0xFF
        if k == 99:
            source = dummy.copy()

    cv2.destroyAllWindows()
