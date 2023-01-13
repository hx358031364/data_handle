import albumentations as A
import cv2
import os

def preprocess(image):
    image_cv = cv2.imread(image)
    transform = A.Compose([
        A.OneOf([
            A.Blur(p=1),
            A.MedianBlur(p=1),
            A.HorizontalFlip(p=1),
            A.RandomBrightnessContrast(p=1),
            A.GaussianBlur(p=1),
        ])

    ])

    transformed = transform(image=image_cv)
    in_img = transformed["image"]
    return in_img

img_path = r'D:\data\resulet\rema\kulou'

imgs = os.listdir(img_path)
sava_path = r'D:\data\resulet\rema\kulo_aug'
for img in imgs:
    img_file = os.path.join(img_path, img)
    aug_img = preprocess(img_file)
    name = 'kulou_aug3_'+img
    cv2.imwrite(os.path.join(sava_path, name), aug_img)
