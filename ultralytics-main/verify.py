from ultralytics import YOLO

model = YOLO("TrainResults/yolov8n(cbam-neck)/train/weights/best.pt")

model.info(detailed=True)