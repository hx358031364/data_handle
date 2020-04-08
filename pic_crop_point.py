from skimage import io
import matplotlib.pyplot as plt
import os
path = 'D:\\data\\11\\流血 - Google 搜索_files\\'
listdir = os.listdir(path)
number = 0
for jpe_file in listdir:
    img_data = io.imread(jpe_file)# 图片路径
    io.imshow(img_data)
    plt.show()
    """
    中心裁剪任意尺寸的图片（以中心为原点）
    """
    slice_height,slice_width,_ = img_data.shape

    # 如果宽度大于高度，截取宽度
    if slice_width > slice_height:
        width_crop = (slice_width - slice_height) // 2
        if width_crop >= 0:
            # img_data_0 = img_data[:, 0:slice_height, :]
            img_data_1 = img_data[:, width_crop:-width_crop, :]
            # img_data_2 = img_data[:, -slice_height:, :]

        # io.imsave('./0.jpg',img_data_0)
        io.imsave('D://data/11/a/'+number+'.jpg',img_data_1)
        # io.imsave('./2.jpg',img_data_2)
    elif slice_width < slice_height:
        slice_height = (slice_height - slice_width) // 2
        if slice_height >= 0:
            img_data_0 = img_data[:slice_width, :, :]
            img_data_1 = img_data[slice_height:-slice_height, :, :]
            img_data_2 = img_data[-slice_width:, :, :]
        # io.imsave('./0.jpg',img_data_0)
        io.imsave('D://data/11/a/'+number+'.jpg',img_data_1)
        # io.imsave('./2.jpg',img_data_2)
    elif slice_width == slice_height:
        io.imsave('D://data/11/a/'+number+'.jpg',img_data)