import cv2
import numpy as np
import os


def greyScale(image, dir_name):
    # Perform some basic operations
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dir_name += "_grey.jpg"

    # Save the processed image
    cv2.imwrite(dir_name, gray_image)


def santuration(image, dir_name):
    # Specify the saturation factor (e.g., 1.5 for increased saturation)
    saturation_factor = 1.5
    dir_name += "_sature.jpg"

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Scale the saturation channel
    hsv_image[:, :, 1] = np.clip(
        hsv_image[:, :, 1] * saturation_factor, 0, 255).astype(np.uint8)

    # Convert the image back to the BGR color space
    saturated_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(dir_name, saturated_image)


def edgeDetection(image, dir_name):
    dir_name += "_edge.jpg"
    # Convert to graycsale for better pixel light intensity detection
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100,
                      threshold2=200)
    cv2.imwrite(dir_name, edges)


def gaussianBlurr(image, dir_name):
    dir_name += "_blurr.jpg"
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    denoised = cv2.GaussianBlur(image, (3, 3), 0)
    cv2.imwrite(dir_name, denoised)


def generate(dir_name, dir_choose, range_end, extension):
    generated_dir = f"{dir_name}_generated/"
    os.makedirs(generated_dir, exist_ok=True)

    for i in range(0, range_end):
        name_file = i
        image = cv2.imread(f"./{dir_choose}/{name_file}{extension}")
        save_dir = f"{generated_dir}{i}"
        santuration(image, save_dir)
        greyScale(image, save_dir)
        gaussianBlurr(image, save_dir)
        edgeDetection(image, save_dir)


if __name__ == "__main__":
    print("Catatan :\n Harap membuat folder baru didirektori ini untuk mengenerate data")
    print(" Harap memberi nama gambar didalam foldernya nomor dari 0 hingga banyak data")
    print(" Harap menggunakan extensi gambar 1 jenis saja pada gambar didalam direktori (.jpg/.jpeg/.png)")
    os.system('pause')

    # Read an image from file
    dir_path = "./"
    files_dir = [
        f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))
    ]
    valid_ext = [".jpg", ".jpeg", ".png"]

    # Optimize the dir name choose with your device dir path
    dir_name = "./batik-image-processing/"
    dir_choose = ""
    range_end = 0
    extension = ""
    try_again = 0
    while True:
        while True:
            os.system('cls')
            for data in files_dir:
                print(data)
            dir_choose = input(
                "Masukkan nama folder yang datanya akan digenerate : ")
            if dir_choose in files_dir:
                while True:
                    range_end = int(
                        input("Masukkan jumlah image pada foldernya : "))
                    extension = input(
                        "Pilih salah satu (.jpg/.jpeg/.png)\nMasukkan jenis extension dari gambar didalam folder : ")
                    extension = extension.lower()
                    if range_end > 0 and extension in valid_ext:
                        break
                    else:
                        print(
                            "Mohon pastikan jumlah image lebih dari 0 dan gunakan extension gambar yang valid")
                        os.system('pause')
                break
            else:
                print("Pilih nama folder dengan benar!")
                os.system('pause')
        dir_name += dir_choose
        generate(dir_name, dir_choose, range_end, extension)
        print(
            f"Data berhasil di generate disimpan pada folder {dir_choose}_generated")
        while True:
            try_again = int(input(
                "Apakah anda ingin mengenerate data lagi?\n 1.Iya\n 2.Tidak\nPilihan anda : "))
            if try_again == 1:
                break
            elif try_again == 2:
                exit()
            else:
                print("Pilihan tidak valid. Masukkan 1 atau 2.")
                os.system('pause')
