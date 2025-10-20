from ultralytics import YOLO

#Test for yolov5n
print('Results for YOLOv5n')
model  = YOLO("TrainResults/yolov5n/train/weights/best.pt")
results = model.val(data = "Basketball_dataset/data.yaml", split = "test", project = "TrainResults/yolov5n/Test")
print(results.results_dict)
print("\n")

#Test for yolov8n
print('Results for YOLOv8n')
model  = YOLO("TrainResults/yolov8n/train/weights/best.pt")
results = model.val(data = "Basketball_dataset/data.yaml", split = "test", project = "TrainResults/yolov8n/Test")
print(results.results_dict)
print("\n")

#Test for yolov11n
print('Results for YOLOv11n')
model  = YOLO("TrainResults/yolov11n/train/weights/best.pt")
results = model.val(data = "Basketball_dataset/data.yaml", split = "test", project = "TrainResults/yolov11n/Test")
print(results.results_dict)
print("\n")

#Test for yolov5n (cbam-backbone)
print('Results for YOLOv5n(cbam-backbone)')
model  = YOLO("TrainResults/yolov5n(cbam-backbone)/train/weights/best.pt")
results = model.val(data = "Basketball_dataset/data.yaml", split = "test", project = "TrainResults/yolov5n(cbam-backbone)/Test")
print(results.results_dict)
print("\n")

#Test for yolov8n (cbam-backbone)
print('Results for YOLOv8n(cbam-backbone)')
model  = YOLO("TrainResults/yolov8n(cbam-backbone)/train/weights/best.pt")
results = model.val(data = "Basketball_dataset/data.yaml", split = "test", project = "TrainResults/yolov8n(cbam-backbone)/Test")
print(results.results_dict)
print("\n")

#Test for yolov11n (cbam-backbone)
print('Results for YOLOv11n(cbam-backbone)')
model  = YOLO("TrainResults/yolov11n(cbam-backbone)/train/weights/best.pt")
results = model.val(data = "Basketball_dataset/data.yaml", split = "test", project = "TrainResults/yolov11n(cbam-backbone)/Test")
print(results.results_dict)
print("\n")


#Test for yolov5n (eca-backbone)
print('Results for YOLOv5n(eca-backbone)')
model  = YOLO("TrainResults/yolov5n(eca-backbone)/train/weights/best.pt")
results = model.val(data = "Basketball_dataset/data.yaml", split = "test", project = "TrainResults/yolov5n(eca-backbone)/Test")
print(results.results_dict)
print("\n")

#Test for yolov8n (eca-backbone)
print('Results for YOLOv8n(eca-backbone)')
model  = YOLO("TrainResults/yolov8n(eca-backbone)/train/weights/best.pt")
results = model.val(data = "Basketball_dataset/data.yaml", split = "test", project = "TrainResults/yolov8n(eca-backbone)/Test")
print(results.results_dict)
print("\n")

#Test for yolov11n (eca-backbone)
print('Results for YOLOv11n(eca-backbone)')
model  = YOLO("TrainResults/yolov11n(eca-backbone)/train/weights/best.pt")
results = model.val(data = "Basketball_dataset/data.yaml", split = "test", project = "TrainResults/yolov11n(eca-backbone)/Test")
print(results.results_dict)
print("\n")

