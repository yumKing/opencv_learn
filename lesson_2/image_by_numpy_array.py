import cv2

# 修改特定像素蓝色通道的值B G R
img = cv2.imread('RandomColor.png')
print(img.item(150, 120, 0))
img.itemset((150, 120, 0), 255)
print(img.item(150, 120, 0))

# 将图像所有绿色通道的值设为0
img[:, :, 1] = 0

# 拷贝一块图像区域给另一块区域
my_roi = img[0:100, 0:100]
img[300:400, 300:400] = my_roi

# 图像的属性
print(img.shape)
print(img.size)
print(img.dtype)
