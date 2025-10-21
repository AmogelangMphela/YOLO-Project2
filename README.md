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

├── .github/                     

├── Basketball_dataset/           # Custom dataset used for training

│   ├── test/

│   ├── train/

│   └── val/

├── docker/                      

├── docs/                         

├── examples/                     

├── result/                       

├── runs/                         

├── tests/                       

├── theimages/                    # contains the image used for visualization 

├── TrainResults/                 # Detailed results and logs from training runs

│   ├── yolov5n/

|   |   |_ results                # contains the attention map for the model
|   |   | Test                   # contains results for testing
|   |   | Training                # contains training logs and results

│   ├── yolov5n(cbam-backbone)/

│   ├── ... and yolo model results structured the same as yolov5n (yolov8, yolov11, eca, etc.)

├── ultralytics/                  # Core modified Ultralytics source code

│   ├── pycache/

│   ├── assets/

│   ├── cfg/                      # Configuration files for models and data

│   │   ├── datasets/

│   │   └── models/               # YAML model configuration files

│   │       ├── v11/              #same structure as V8 directory shown below

│   │       ├── v5/              #same structure as V8 directory shown below

│   │       └── v8/

│   │           ├── yolov8-cbam.yaml      # YOLOv8 with CBAM

│   │           ├── yolov8-eca.yaml       # YOLOv8 with ECA

│   │           └── yolov8.yaml           # Baseline YOLOv8

│   ├── data/

│   ├── engine/

│   ├── hub/

│   ├── models/

│   ├── nn/                       # Custom/Modified Neural Network modules

│   │   ├── modules/              # Core modules (e.g., activation, conv, block)

│   │       ├── activation.py

│   │       ├── block.py

│   │       ├── conv.py          # ECA and CBAM defined here, Conv blocks modified here (e.g., activation, conv, block)

│   │       ├── .......

│   ├── solutions/

│   ├── tasks.py

│   ├── trackers/

│   └── utils/

├── .dockerignore

├── .gitignore

├── CITATION.cff

├── Grad-CAM.py                   # Script for visualizing model attention (e.g., Grad-CAM) 

├── LICENSE

├── mkdocs.yml

├── pyproject.toml

├── README.zh-CN.md

├── testing.py                    # Main script for running model testing

├── Training.py                   # Main script for running model training

├── verify.py

└── *.pt                          # Pre-trained or custom-trained model weights (e.g., yolov8n.pt)
