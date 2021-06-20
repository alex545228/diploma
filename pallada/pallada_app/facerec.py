import os
# import dlib
from skimage import io
from scipy.spatial import distance
from pathlib import Path
import pickle
from apiboost.Detect import faceRec as rec
from apiboost.Detect import Verify
from os.path import basename

BASE_DIR = Path(__file__).resolve().parent.parent

len = 0


# алгоритмы
def descript_all(path_to_photos):
    """
    дескриптер по папке с фото
    """
    try:
        face_descriptors = []
        faces = os.listdir(path_to_photos)  # адрес папки с лицами
        for i in faces:
            face_descriptors.append(descript(i, path_to_photos))
    # with open('face_db.pickle', 'wb') as fout:
    # pickle.dump(res, fout)
    except Exception:
        res = None
    res = face_descriptors
    return res


# def path_to_media():
#     path_to_media = os.path.join(BASE_DIR, 'media')
#     return path_to_media
# def descriptors():
#     descriptors = descript_all(path_to_media_simples)
#     return descriptors
# def path_to_media_simples():
#     path_to_media_simples = os.path.join(path_to_media(), 'simples')
#     return path_to_media_simples

class FaceRec:
    # def __init__(self, ):
    #
    # self.sp =
    # dlib.shape_predictor(
    # os.path.join(BASE_DIR, 'DLIB', 'shape_predictor_68_face_landmarks.dat')
    # )
    # self.facerec = dlib.face_recognition_model_v1(
    # os.path.join(BASE_DIR, 'DLIB', 'dlib_face_recognition_resnet_model_v1.dat')
    # )
    # self.detector = dlib.get_frontal_face_detector()
    # path_to_media = os.path.join(BASE_DIR, 'media')
    # path_to_media_simples = os.path.join(path_to_media, 'simples')
    # descriptors = descript_all(path_to_media_simples)

    def recognize(self, photo):
        path_to_media = os.path.join(BASE_DIR, 'media')
        path_to_media_simples = os.path.join(path_to_media, 'simples')
        descriptors = descript_all(path_to_media_simples)
        """
            идентификатор находит матрицу из базы с самым близким расстоянием
            название фото, путь к фото для распозн., алгоритмы из коробки, бд деструкторов,
            """
        main_descriptor = descript(photo, path_to_media)
        similarFace = 0
        temp = 0
        for i in descriptors:
            # distances.append(distance.euclidean(main_descriptor, i))
            similarFace = Verify(main_descriptor, i)
            if similarFace != 0:
                targetID = []
                targetID = os.listdir(path_to_media_simples)
                id_ = os.path.splitext(targetID[temp])[0]
                print("Succes")
                return id_
                break
            temp += 1



        # min_dist = min(distances)

            # id_ = None
             # if similarFace == 0:
            #     return id_
        # faces = os.listdir(path_to_media_simples)
        # for i in faces:
        #     target =
        #     print(target)
        #     print('this is target')
        #     print (temp)
        #     print('this is temp')
        #     if target == temp:
        #         print ('this is i')
        #         print(i)
        #         temp = i


def descript(photo, path):
    """
    дескриптер преобразует фото в матрицу
    название фото, путь к папке с фото, алгоритмы из коробки
    """

    img = open(os.path.join(path, photo), 'r+b')
    dets_webcam = rec(img)
    return dets_webcam

# dets_webcam = self.detector(img)

# shape_name = None
# for k, d in enumerate(dets_webcam):
# shape_name = self.sp(img, d)
# res_descriptor = self.facerec.compute_face_descriptor(img, shape_name)
# except Exception:
# res_descriptor = None
# return res_descriptor

# def descript_all(path_to_photos):
#     """
#     дескриптер по папке с фото
#     """
#     try:
#         face_descriptors = []
#         faces = os.listdir(path_to_photos)  # адрес папки с лицами
#         for i in faces:
#             face_descriptors.append(descript(i, path_to_photos))
#     # with open('face_db.pickle', 'wb') as fout:
#     # pickle.dump(res, fout)
#     except Exception:
#         res = None
#
#     return res


# def recognize(self, photo):
#
# if min_dist > 0.6 and len(self.descriptors) == 1:
# id_ = None
# elif min_dist <= 0.6 and len(self.descriptors) > 1:
# id_ = faces[distances.index(min_dist)][:-4] # точно
# elif min_dist > 0.6 and len(self.descriptors) > 1:
# id_ = faces[distances.index(min_dist)][:-4] # неточно
# return id_
# faces = os.listdir(self.path_to_media_simples)

# path_to_media = os.path.join(BASE_DIR, 'media')
# path_to_media_simples = os.path.join(path_to_media, 'simples')
# rec = FaceRec()
# _all = rec.descript_all(path_to_media_simples)
# print(rec.recognize('photo_2020-11-07_08-19-16.jpg'))
