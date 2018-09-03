import matplotlib.pyplot as plt
from skimage import io

filename_main = 'USF4_Logo.bmp'
filename_background = 'vingadores.jpg'

img_main = io.imread(filename_main)
img_background = io.imread(filename_background)
img_out = img_main.copy()

rows, cols, dim = img_main.shape

background_color = img_main[0, 0]

x = round(img_background.shape[0] / 2) - round(img_main.shape[0] / 2)
y = round(img_background.shape[1] / 2) - round(img_main.shape[1] / 2)

for i in range(rows):
    for j in range(cols):
        if set(background_color == img_out[i, j]) == {True}:
            img_out[i, j] = img_background[i + x, j + y]

plt.figure('InMain')
io.imshow(img_main)
plt.figure('InBackground')
io.imshow(img_background)
plt.figure('Out')
io.imshow(img_out)

io.show()
