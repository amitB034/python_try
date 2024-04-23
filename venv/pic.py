# from pykakasi import kakasi

# kks = kakasi()
# word = str(input("言葉を入れて下さい:"))

# result = kks.convert(word)
# for converted_word in result:
#     print(f"{converted_word['hepburn']}", end="")


from tkinter import filedialog
import cv2

class Show_image():

    def __init__(self):
        self.faces = []

    def circle_pic(self):
        # ファイル選択ダイアログを表示して画像ファイルを選択
        file_path = filedialog.askopenfilename(title="画像ファイルを選択",
                                               filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpeg"), ("All files", "*.*")])
        if not file_path:
            return None
        # OpenCVで画像を読み込む
        self.image = cv2.imread(file_path)
        # OpenCVの顔検出用の事前学習済み分類器のパス
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        # 事前学習済みの顔検出器を読み込む
        face_cascade = cv2.CascadeClassifier(cascade_path)
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        return file_path

    def paste_image(self, overlay_path):
        overlay_image = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)

        for (x, y, w, h) in self.faces:
            overlay_image = cv2.resize(overlay_image, (w, h))
            roi = self.image[y:y+h, x:x+w]
            for i in range(overlay_image.shape[0]):
                for j in range(overlay_image.shape[1]):
                    if overlay_image[i, j][3] != 0:
                        roi[i, j] = overlay_image[i, j][:3]

    def show_image(self):
        cv2.imshow("Result", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()