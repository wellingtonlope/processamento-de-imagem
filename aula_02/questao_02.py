import matplotlib.pyplot as plt
from skimage import io
import histograma

filename = 'pout.tif'
img = io.imread(filename)

hist = histograma.imEqHistWithCut(img, 0.3)

plt.figure('n_k')
plt.bar(range(256), hist.im_h)

plt.figure('pr_rk')
plt.bar(range(256), hist.im_hn)

plt.figure('out_n_k')
plt.bar(range(256), hist.im_hEq)

plt.figure('out_pr_rk')
plt.bar(range(256), hist.im_hCut)

plt.figure('img')
io.imshow(hist.img)

plt.figure('out_img')
io.imshow(hist.img_out)

io.show()
