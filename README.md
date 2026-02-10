MergePose: Automated Dataset Generation for Equestrian Form Analysis
Official implementation of the MergePose data pipeline.

This repository contains the dataset generation and training logic for SARA (Smart Assistant for Riding Analysis). It features a streamlined pipeline to ingest raw equestrian footage, extract distinct horse and rider pose metrics, and fuse them into a unified YOLO-formatted dataset for fine-tuning.

🔗 Project Website / Main Repo: SARA-AI

🎥 Demo
(Place your GIF of the bounding box detection here. Even a 5-second clip of the model tracking the horse/rider creates immediate trust.)

🏗️ Architecture
The pipeline follows a modular "extraction-fusion-training" workflow designed to handle large-scale video datasets (50GB+).

Code snippet
graph LR
    A[Raw Video Dataset] --> B(DataToCSV.py)
    B --> C{MergePose Logic}
    C --> D[Raw CSV Logs]
    D --> E(CSVtoData.py)
    E --> F[YOLOv8 Formatted Data]
    F --> G(train.py)
    G --> H[Final SARA Model]
🚀 Installation
Bash
git clone https://github.com/HashemW/MergePose.git
cd MergePose
pip install ultralytics pandas opencv-python numpy
🛠️ Usage
The pipeline is designed to be executed sequentially.

1. Data Preparation
Place your raw video files in a dedicated dataset/ directory. Note: The original 50GB dataset is not included in this repository due to size constraints. See VideoSources.txt for source attribution.

2. Pose Extraction
Run the extraction script to detect Horse + Rider entities and log their coordinates to CSV.

Bash
python DataGenerationScripts/datatoCSV.py --input_dir ./dataset --output_dir ./logs
3. Format Conversion (MergePose)
Fuse the raw CSV logs into a standardized YOLOv8 training structure (images + labels).

Bash
python DataGenerationScripts/CSVtoData.py --input_dir ./logs --output_dir ./yolo_dataset
4. Model Training
Fine-tune the YOLO model on the generated dataset.

Bash
python train.py --data ./yolo_dataset/data.yaml --epochs 100
📂 Repository Structure
Plaintext
MergePose/
├── DataGenerationScripts/
│   ├── datatoCSV.py       # Entity detection & raw coordinate logging
│   └── CSVtoData.py       # Conversion logic for YOLO formatting
├── train.py               # Training entry point for the final model
├── VideoSources.txt       # Attribution for public domain footage used
└── README.md              # Documentation
📄 Citation
This work is currently under review for ICPR 2026. If you use this pipeline or methodology, please cite the paper (citation details to be updated upon acceptance).

Note on Weights: The pre-trained weights (best.pt) and the full proprietary dataset are withheld to protect intellectual property. This repository provides the complete scaffolding to reproduce the data generation process and train your own models.
