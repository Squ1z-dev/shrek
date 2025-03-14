import cv2
import os

face_dir = "hear_faces"
detect_dir = "haar_detected"
path = os.path.dirname(__file__)

def create_dir():
    dirs = [face_dir, detect_dir]
    for dir in dirs:
        dir = os.path.join(path, dir)
        if not os.path.exists(dir):
            os.makedirs(dir)

def get_images(path):
    exts = [".jpg", ".png"]
    images = []
    for img in os.listdir(path):
        ext = os.path.splitext(img)[1]
        if ext.lower() not in exts:
            continue
        images.append(os.path.join(path, img))
    if images:
        create_dir()
    return images

def haar_Detection(image):
    img_path = os.path.join(image)
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=3, minSize=(40, 40))

    print(f"[INFO] Found {len(faces)} Faces")

    if len(faces):
        i = 0
        copy_img = img.copy()

        base = os.path.split(image)[-1]
        name = os.path.splitext(base)[0]

        for (x,y,w,h) in faces:
            roi_color = img[y: y + h, x: x + w]
            resized_img = cv2.resize(roi_color, (64, 64))
            cv2.imwrite(os.path.join(path, face_dir, str(i) + "_" + name + "_detect.jpg"), resized_img)
            cv2.rectangle(copy_img, (x, y), (x + w, y + h), (255, 242, 0), 2)
            i += 1

        cv2.imwrite(os.path.join(path, detect_dir, name + "_detect_face.jpg"), copy_img)
        return copy_img

def show_img(img_path):
    cv2.imshow("Image", img_path)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    path = "Images"
    images = get_images(path)
    print(images)

    for image in images:
        img = haar_Detection(image)
        show_img(img)