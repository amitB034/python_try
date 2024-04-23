
from pic import Show_image

def main():
    # Show_imageクラスのインスタンスを作成
    show_image = Show_image()
    # 画像を選択し、選択されたファイルのパスを取得
    file_path = show_image.circle_pic()
    
    if not file_path:
        print("ファイルが選択されていません。")
        return

    # 貼り付ける画像のパス
    overlay_path = '/Users/amit/Downloads/megane.png'

    # 画像に顔を認識し、貼り付ける
    show_image.paste_image(overlay_path)

    # 結果を表示
    show_image.show_image()

if __name__ == "__main__":
    main()