
from pic import Show_image

def main():
    show_image = Show_image()
    file_path = show_image.circle_pic()
    
    if not file_path:
        print("ファイルが選択されていません。")
        return

    overlay_path = '/Users/amit/Downloads/megane.png'

    show_image.paste_image(overlay_path)
    print(5)
    show_image.show_image()

if __name__ == "__main__":
    main()