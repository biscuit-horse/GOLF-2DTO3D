# Golf Swing 3D Motion Prediction Model

## Overview
This project develops a model to capture human key points from golf swing videos and predict their 3D motion trajectories. By addressing prediction biases caused by varying camera angles, it provides advanced technical support for golf training and analysis, surpassing existing software limited to 2D analysis.

## Features
- **2D Key Point Extraction**: Utilizes **Detectron2** to process each frame of real-person golf swing videos, extracting 17 2D human key points.
- **3D Motion Prediction**: Employs the **VideoPose3D** model to map 2D key point time series data into 3D space, predicting 3D human keypoints.
- **3D Visualization**: Generates intuitive 3D skeletal motion trajectory animations by connecting predicted 3D keypoints.

## Environment
- The model is lightweight and runs efficiently on a **CPU**, requiring no specialized hardware.

## Purpose
Fills the gap in golf training tools by providing accurate 3D motion analysis, overcoming limitations of 2D-based software and enabling enhanced performance evaluation and coaching.
