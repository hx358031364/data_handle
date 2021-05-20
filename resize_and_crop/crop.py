from PIL import Image
import os
# from keras.preprocessing.image import ImageDataGenerator
# from keras.models import load_model
# import numpy as np
# import os
# import keras.backend as K
# import shutil
# import cv2
# import keras
# import numpy as np
# from tensorflow.keras.preprocessing import image
from PIL import ImageFile
# from keras.models import load_model
# import keras
ImageFile.LOAD_TRUNCATED_IMAGES = True
# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
# os.environ['CUDA_VISIBLE_DEVICES'] = "7"
from tqdm import tqdm

save_path = "/home/huangxin/work/testcode/ImageClassification-PyTorch-master/crop_test_data/12/"
fileList = os.listdir(r"/home/huangxin/disk2/crop_test_data_not/12/")
count = len(fileList)
# print(fileList)
for i,file in enumerate(tqdm(fileList)):
    try:
        im = Image.open("/home/huangxin/disk2/crop_test_data_not/12/{}".format(file))
        if im.mode == "P" or "LA":
            im = im.convert('RGB')
        print(im.size)
        kuan = im.size[0]
        gao = im.size[1]
        if gao < kuan:
            # region_l = im.crop([0,0,gao,gao])
            # region_l.save("{}/{}.jpg".format(test_path,i))

            region_m = im.crop([((kuan/2)-(gao/2)),0,((kuan/2)+(gao/2)),gao])
            region_m.save("{}/{}".format(save_path,file))

            # region_r = im.crop([(kuan-gao),0,kuan,gao])
            # region_r.save("{}/{}.jpg".format(test_path,i+2*count))
        else:
            # region_l = im.crop([0,0,kuan,kuan])
            # region_l.save("{}/{}.jpg".format(test_path,i+3*count))

            region_m = im.crop([0,((gao/2)-(kuan/2)),kuan,((gao/2)+(kuan/2))])
            region_m.save("{}/{}".format(save_path,file))
    except:
        print("/home/huangxin/disk2/crop_test_data_not/12/{}".format(file))
        # region_r = im.crop([0,(gao-kuan),kuan,gao])
        # region_r.save("{}/{}.jpg".format(test_path,i+5*count))
    # elif gao >kuan:
    #     region_r = im.crop([0,0,kuan,kuan])
    #     region_f.save("{}a/{}.jpg".format(test_path,i+20))

# def getPrecision(y_true, y_pred):
#     TP = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))#TP
#     N = (-1)*K.sum(K.round(K.clip(y_true-K.ones_like(y_true), -1, 0)))#N
#     TN=K.sum(K.round(K.clip((y_true-K.ones_like(y_true))*(y_pred-K.ones_like(y_pred)), 0, 1)))#TN
#     FP=N-TN
#     precision = TP / (TP + FP + K.epsilon())#TT/P
#     return precision

# def getRecall(y_true, y_pred):
#     TP = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))#TP
#     P=K.sum(K.round(K.clip(y_true, 0, 1)))
#     FN = P-TP #FN=P-TP
#     recall = TP / (TP + FN + K.epsilon())#TP/(TP+FN)
#     return recall
# model = load_model('17_weights4.0.h5', custom_objects={'relu6': keras.layers.ReLU(6.), 'DepthwiseConv2D': keras.layers.DepthwiseConv2D,'getRecall':getRecall,'getPrecision':getPrecision})

# dic = {0:'10map',1:'11controlled knife',2:'12firearms and ammunition',3:'13warship',4:'14tank',5:'15military aircraft',6:'16guided missile',7:'17Normal',
#            8:'1bedin',9:'2blood',10:'3ruins_train',11:'4Crisis event',12:'5Chinese national flag',13:'6Public inspection vehicles',14:'7fire fighting truck',
#            15:'8ambulance',16:'9policeman uniform'}

# # test_path = "./img/"
# test_datagen = ImageDataGenerator(rescale=1./255)
# print(test_datagen)
# # test_generator = test_datagen.flow_from_directory(test_path, target_size=(224, 224),classes=dic,batch_size=2,class_mode='categorical', shuffle=False,)
# print("1")

# test_generator = test_datagen.flow_from_directory(
#     test_path,
#     target_size=(311, 311),
#     batch_size=16,
#     class_mode='categorical',
#     shuffle=False)

# pred = model.predict_generator(test_generator, steps=None, max_queue_size=10, workers=1, use_multiprocessing=False, verbose=0)
# print("1")

# predicted_class_indices = np.argmax(pred, axis=1)

# test_generators = []
# for i in test_generator.filenames:
#     test_generators.append(i)

# for i,key in enumerate(tqdm(predicted_class_indices)):
    
#     test_generator = test_generators[i].split('\\')
#     test_generator = '/'.join(test_generator)
#     img = cv2.imread(test_path+'/'+test_generator)
#     if key == 0:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 1:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 2:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 3:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 4:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 5:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 6:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 7:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 8:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 9:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 10:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 11:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 12:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 13:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 14:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 15:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)
#     if key == 16:
#         if pred[i][key] >= 0.7:
#             cv2.imwrite('./img/{}/{}.jpg'.format(dic[key],pred[i][key]),img)

