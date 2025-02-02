#STuffs: imports for Pyinstaller distribution
#Before all fix pyinstaller:
#import multiprocessing
#multiprocessing.freeze_support()
#import pywt._extensions._cwt
#import sklearn.utils._cython_blas
#import skimage.io
#import skimage.io._plugins.matplotlib_plugin
#skimage.io.use_plugin('pil', 'imread')   #这些都是编译exe所需，这里须显示调用pil的imread，而不是matplotlib的，因为我训练的时候dataloader里默认用的是pil的imread，和matplotlib的imread读取的数据分布不一样。

def night_cast():
    try:
        with open("./daylight", 'r') as f:
            light = int(f.readline())
    except:
        light = 10
    if light>_LIGHT_THRESHOLD:
        NIGHT_CAST = True
    else:
        NIGHT_CAST = False
    return NIGHT_CAST

def get_confidence(): 
    #CONFIDENCE_THRESHOLD = 0.63   #retrain with conf 0.53 to get 2.87 with old data.
    CONFIDENCE_THRESHOLD = 0.14   #retrain with conf 0.14 to get 2.87 with old data more neg.
    if night_cast():
        #CONFIDENCE_THRESHOLD = CONFIDENCE_THRESHOLD/2   #晚上的置信度是白天的一半  #will depracate in next version
        pass
    return CONFIDENCE_THRESHOLD

#Just a workaround:
################Options for object detection:
#CLASSES_6 = ['angle', 'angle_r', 'top', 'top_r', 'head']  #+1背景类别 will depracate in next version
CLASSES_4 = ['angle', 'top', 'head']    #加入晚上数据的模型已经不区分左右了

################Options for A and B:
VISUALIZATION        = False
VISUALIZATION        = True
UNVEIL               = False
UNVEIL               = True

IGNORE_5 = False
IGNORE_5 = True
_LIGHT_THRESHOLD = 20  #光线曝光时间阈值，实际值大于阈值则说明是晚上
CONFIDENCE_THRESHOLD = get_confidence()   

#定位模型
SPATIAL_IN_SEAT_MODEL = "spatial_model_both_side_finetunes/model_best.pt"   
#检测模型
MMD_CONFIG = "mmdetection/configs/car_face/cascade_rcnn_hrnetv2p_w32_20e_4_more_neg.py"
MMD_WEIGHTS = "object_detection_logs_data_both_side_finetunes/hrnet_epoch_18_287_more_neg.pth"
#白天+晚上的模型（不区分左右） will depracate in next version
#MMD_CONFIG_NIGHT = "mmdetection/configs/car_face/cascade_rcnn_hrnetv2p_w32_20e_4.py" #will depracate in next version
#MMD_WEIGHTS_NIGHT = "object_detection_logs_data_both_side_finetunes/hrnet_night_and_day.pth"  #will depracate in next version
#OBJECT_DETECTION_MODEL = "object_detection_logs_data_both_side_finetunes/csv_retinanet_full_data_465.pt"    #微调后

#################Options for threads_start:
PARALLEL_MODE = False    #单线程的threads_starts会有bug！只会调用左侧的 测试的话 请注意！  单 car_to_car_merge应该不受影响
PARALLEL_MODE = True
if PARALLEL_MODE:
    VISUALIZATION = False


##################Options for Seat merge:
NUM_OF_SEATS_PEER_CAR = 5
MERGE_METHOD = "vote"
VOTE_THRESHOLD = 2  #where >= count
CAR_TO_CAR_DIR = "/mfs/home/limengwei/car_face/shanghai_data/round2/backclear/"
#CAR_TO_CAR_DIR = "/home/user/list/"


######################MMD:
