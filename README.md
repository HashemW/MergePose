# MergePose: Automated Dataset Generation for Equestrian Form Analysis

![Status](https://img.shields.io/badge/Status-Under_Review-yellow)
![Conference](https://img.shields.io/badge/Submitted_to-ICPR_2026-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![YOLO](https://img.shields.io/badge/Model-YOLOv8-orange)

**Official implementation of the MergePose data pipeline.**

This repository contains the dataset generation and training logic for horse and rider pose detection. It features a streamlined pipeline to ingest raw equestrian footage, extract distinct horse and rider pose metrics, and fuse them into a unified YOLO-formatted dataset for fine-tuning.

---

## 👥 Authors

**Hashem Wahed**, **Mohammad Nayeem Teli**
*Submitted to the International Conference on Pattern Recognition (ICPR), 2026.*

---

## 🏗️ Pipeline Architecture

The pipeline follows a modular "extraction-fusion-training" workflow designed to handle large-scale video datasets (50GB+).

<img width="1328" height="397" alt="image" src="https://github.com/user-attachments/assets/51d5d86b-364d-4a79-a039-d45ce83adf65" />

---

Here is the revised **Installation** section. I updated it to explicitly warn users about the DeepLabCut (DLC) complexity and recommended using **Conda**, which is the standard "safe" way to handle DLC's fragile dependency tree.

You can replace the previous "Installation" section with this:

```markdown
## ⚙️ Installation & Environment Setup

**⚠️ Prerequisite Warning:**
This pipeline integrates **DeepLabCut (DLC)** with **YOLO**. Installing DeepLabCut can be complex due to specific version dependencies (especially for GPU support). We **strongly recommend** using **Anaconda** or **Miniconda** to isolate the environment.

### 1. Create a Conda Environment
Start with a clean Python 3.8+ environment to avoid conflicts.
```bash
conda create -n mergepose python=3.8
conda activate mergepose

```

### 2. Install DeepLabCut

*Note: DLC installation varies significantly by OS and GPU availability. If the standard command fails, please refer to the [official DeepLabCut installation guide](https://deeplabcut.github.io/DeepLabCut/docs/installation.html).*

```bash
# Standard installation (may require system-specific dependencies)
pip install "deeplabcut[gui]"

# OR (Recommended for ALL users):
# Follow the official DLC guide to install via their provided conda YAML file.

#NOTE:
# DeepLabCut model names and properties differ between version 3.0 and 2.3. The version used in the official
# MergePose implementation was 2.3. However, you may try any that you want!
```

### 3. Install YOLO & Utilities

Once DeepLabCut is successfully installed and running, install the remaining pipeline dependencies:

```bash
pip install ultralytics pandas opencv-python numpy

```

### 4. Verification

Run this quick check to ensure both libraries are communicating correctly:

```bash
python -c "import ultralytics; import deeplabcut; print('✅ Environment Ready!')"

```

---

## 🛠️ Usage

The pipeline is designed to be executed sequentially to process raw video into a trainable model.

### 1. Data Preparation

Place your raw video files in a dedicated `dataset/` directory.
*(Note: The original 112GB dataset is not included in this repository due to size constraints. See `VideoSources.txt` for source attribution.)*

### 2. Pose Extraction (Data Generation)

Run the extraction script to detect Horse + Rider entities and log their coordinates to CSV.

```bash
python DataGenerationScripts/CSVProducer.py

```

### 3. Format Conversion

Fuse the raw CSV logs into a standardized YOLOv8 training structure (images + labels).

```bash
python DataGenerationScripts/CSVtoData.py

```

### 4. Model Training

Fine-tune the YOLO model on the generated dataset.

```bash
python train.py --epochs 100

```

---

## 📂 Repository Structure

```text
MergePose/
├── DataGenerationScripts/
│   ├── datatoCSV.py       # Entity detection & raw coordinate logging
│   └── CSVtoData.py       # Conversion logic for YOLO formatting
├── train.py               # Training entry point for the final model
├── VideoSources.txt       # Attribution for public domain footage used
└── README.md              # Documentation

```

---

## ⚠️ Note on Weights & Data

The pre-trained weights (`best.pt`) and the full proprietary dataset are withheld to protect intellectual property and commercial viability. This repository provides the complete scaffolding to reproduce the data generation process and train your own models using the **MergePose** methodology.
