import cv2

# Function to resize the original image to make it more suitable for ASCII
def resize_image(image, new_width=300):
    ratio = new_width / image.shape[1]
    new_height = int(image.shape[0] * ratio)
    return cv2.resize(image, (new_width, new_height))

path = "Practice\ASCII\doomer.jpg"
image = cv2.imread(path)
chars = ' .:-=+*#%@'
chars2 = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
coef = 255/(len(chars)-1)
coef2 = 255/(len(chars2)-1)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = resize_image(gray_image)
height, width = gray_image.shape
line2=""
with open('ASCII_Image.txt', 'w') as f:
    for y in range(0, height-1, 2):
        line = ""
        for x in range(0, width-1):
            brightness = gray_image[y, x]
            line += chars[len(chars) - int(gray_image[y, x] / coef) - 1]
            line2 += chars2[int(gray_image[y, x] / coef)]
        f.write(line)
        f.write('\n')
        line2+="\n"
with open('ASCII_Image_2.txt', 'w') as j:
    j.write(line2)