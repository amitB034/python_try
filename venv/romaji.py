# from pykakasi import kakasi

# kks = kakasi()
# word = str(input("言葉を入れて下さい:"))

# result = kks.convert(word)
# for converted_word in result:
#     print(f"{converted_word['hepburn']}", end="")

import cv2
# 画像ファイルのパス
image_path = '/Users/amit/Desktop/python_try/venv/image/photo.jpeg'
# OpenCVで画像を読み込む
image = cv2.imread(image_path)
# OpenCVの顔検出用の事前学習済み分類器のパス
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
# 事前学習済みの顔検出器を読み込む
face_cascade = cv2.CascadeClassifier(cascade_path)
# 画像をグレースケールに変換する（顔検出はグレースケール画像で行う）
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 顔を検出する
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
# 顔を囲む資格を描画する
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
# 結果を表示する
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()