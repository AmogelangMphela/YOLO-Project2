import torch
import torch.nn as nn
import torch.nn.functional as F
from ultralytics import YOLO
from ultralytics.nn.modules import C3k2 as OriginalC3k2


# ------------------------
# Load YOLOv11 model
# ------------------------
model = YOLO("ultralytics/cfg/models/v5/yolov5.yaml")
model = model.load("yolov5nu.pt")

#model.load("yolov5nu.pt")


model.train( 
    data="Basketball_dataset/data.yaml", 
    epochs=50, 
    imgsz=640, 
    batch=16, 
    project="TrainResults/yolov5n",
    patience=10,
    save_period = 10,
    mixup = 0.1,
    fliplr = 0.2,
    cutmix = 0.1
    )


# ------------------------
# Load YOLOv11n CBAM model
# ------------------------
model = YOLO("ultralytics/cfg/models/11/yolov5-cbam.yaml")
model = model.load("yolov5nu.pt")

#model.load("yolov5nu.pt")


model.train( 
    data="Basketball_dataset/data.yaml", 
    epochs=50, 
    imgsz=640, 
    batch=16, 
    project="TrainResults/yolov5n(cbam-backbone)",
    patience=10,
    save_period = 10,
    mixup = 0.1,
    fliplr = 0.2,
    cutmix = 0.1
    )


# ------------------------
# Load YOLOv11n ECA model
# ------------------------
model = YOLO("ultralytics/cfg/models/11/yolov5-eca.yaml")
model = model.load("yolov5nu.pt")

#model.load("yolov5nu.pt")


model.train( 
    data="Basketball_dataset/data.yaml", 
    epochs=50, 
    imgsz=640, 
    batch=16, 
    project="TrainResults/yolov5n(eca-backbone)",
    patience=10,
    save_period = 10,
    mixup = 0.1,
    fliplr = 0.2,
    cutmix = 0.1
    )

