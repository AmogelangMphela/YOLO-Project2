# YOLO Modification Project: Ultralytics with Attention Mechanisms

This project is a modified implementation of the **Ultralytics YOLO** framework, focusing on integrating and evaluating different **attention mechanisms** 
(specifically CBAM and ECA) across various YOLO versions (v5, v8, v11) for object detection.

---

## Project Overview

The primary goal of this project is to:
1. **Customize** the standard YOLO architectures with modules like **CBAM (Convolutional Block Attention Module)** and **ECA (Efficient Channel Attention)**.
2. **Train** and **evaluate** these modified models on a custom dataset.
3. **Compare** the performance improvements against the baseline YOLO models.

---

## Folder Structure



The repository is organized to clearly separate configurations, training results, and the core Ultralytics source code.
The commented files are the relevant files


YOLO2-Project2/ultralytics-main/
├── Basketball_dataset/         # Custom dataset (Basketball) with train/val/test splits.
├── TrainResults/               # Repository for all training logs, metrics, and attention maps.
│   ├── yolov5n/                # e.g., Base YOLOv5-nano results
|   |   ├── results
|   |   ├── Testing
|   |   ├── Training
│   └── yolov5n(cbam-backbone)/ # e.g., YOLOv5-nano with CBAM results
├── theimages/                  # Images used for visualization and Grad-CAM outputs.
├── ultralytics/                # Core Modified Ultralytics Source
│   ├── cfg/                    # YAML configurations for models and datasets
│   └── nn/                     # Contains the attention module definitions (e.g., CBAM, ECA)
├── Training.py                 # Main script to initiate model training.
├── testing.py                  # Main script to evaluate model performance (mAP, etc.).
└── Grad-CAM.py                 # Script for visualizing model attention/feature maps.
└── *.pt                          # Pre-trained or custom-trained model weights (e.g., yolov8n.pt)
