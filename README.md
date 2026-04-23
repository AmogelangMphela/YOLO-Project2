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

## 📁 Folder Structure

The repository is organized to clearly separate configurations, training results, and the core Ultralytics source code.

```bash
YOLO2-Project2/
└── ultralytics-main/
    ├── Basketball_dataset/          # Custom dataset (train/val/test splits)
    │
    ├── TrainResults/                # Training outputs, logs, visualizations
    │   ├── yolov5n/                 # Baseline YOLOv5-nano
    │   │   ├── Training/            # Logs, checkpoints, configs
    │   │   ├── Test/                # Evaluation outputs
    │   │   └── _results/            # Grad-CAM heatmaps
    │   │
    │   └── yolov5n_cbam_backbone/   # Modified model results
    │       └── ...
    │
    ├── theimages/                   # Grad-CAM & visualization images
    │
    ├── ultralytics/                 # Modified Ultralytics source
    │   ├── cfg/
    │   │   └── models/
    │   │       ├── v5/
    │   │       ├── v8/
    │   │       │   ├── yolov8.yaml
    │   │       │   ├── yolov8-cbam.yaml
    │   │       │   └── yolov8-eca.yaml
    │   │       └── v11/
    │   │
    │   └── nn/
    │       └── modules/
    │           └── conv.py          # CBAM, ECA, modified conv blocks
    │
    ├── Training.py                 # Training script
    ├── testing.py                  # Evaluation script (mAP, metrics)
    └── Grad-CAM.py                 # Attention visualization
