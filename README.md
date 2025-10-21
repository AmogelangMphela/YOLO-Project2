# YOLO Modification Project: Ultralytics with Attention Mechanisms

This project is a modified implementation of the **Ultralytics YOLO** framework, focusing on integrating and evaluating different **attention mechanisms** 
(specifically CBAM and ECA) across various YOLO versions (v5, v8, v11) for object detection.

---

## Project Overview ()

The primary goal of this project is to:
1. **Customize** the standard YOLO architectures with modules like **CBAM (Convolutional Block Attention Module)** and **ECA (Efficient Channel Attention)**.
2. **Train** and **evaluate** these modified models on a custom dataset.
3. **Compare** the performance improvements against the baseline YOLO models.

---

## Folder Structure (Please open the README.md file file structure is better organize in the file)



The repository is organized to clearly separate configurations, training results, and the core Ultralytics source code.
The commented files are the relevant files


YOLO2-Project2/ultralytics-main/

├── Basketball_dataset/         # Custom dataset (Basketball) with train/val/test splits.

├── TrainResults/               # Repository for all training logs, metrics, and attention maps.

│   ├── yolov5n/                # e.g., Base YOLOv5-nano results

│   │   ├── _results            # Grad-CAM heatmap

│   │   ├── Test                # Contains the output files from running testing.py.

│   │   └── Training            # Contains logs, model checkpoints, and config files from Training.py.

│   └── yolov5n(cbam-backbone)/ # other modesl YOLOv8, YOLOv11 also found in the same directory as YOLOv5

├── theimages/                  # Images used for visualization and Grad-CAM outputs.

├── ultralytics/                # Core Modified Ultralytics Source

│   ├── cfg/                    # YAML configurations for models and datasets

│   │   └── models/             # Model architecture definitions

│   │       ├── v11/            #Structure the same as v8 shown below

│   │       ├── v5/             #Structure the same as v8 shown below

│   │       └── v8/

│   │           ├── yolov8-cbam.yaml # YOLOv8 configuration with CBAM integrated.

│   │           ├── yolov8-eca.yaml  # YOLOv8 configuration with ECA integrated.

│   │           └── yolov8.yaml      # Baseline YOLOv8 configuration.

│   └── nn/                     # Contains the attention module definitions (e.g., CBAM, ECA)

│   │   ├── modules/

│   │           ├── conv.py      # The ECA and CBAM modules are defined here the original and modified conv blocks are also here

├── Training.py                 # Main script to initiate model training.

├── testing.py                  # Main script to evaluate model performance (mAP, etc.).

└── Grad-CAM.py                 # Script for visualizing model attention/feature maps.
