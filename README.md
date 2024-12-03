# House_Price_Prediction_MLOps

This project implements an advanced Machine Learning Operations (MLOps) pipeline for predicting house prices. It integrates traditional property features (location, size, and number of rooms) with a novel feature: **house condition**. The pipeline uses Google Cloud Platform (GCP) for data management, Apache Airflow for orchestration, and Data Version Control (DVC) for tracking data versions and model iterations.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Folder Structure](#folder-structure)
3. [Installation and Setup](#installation-and-setup)
4. [Quickstart Guide](#quickstart-guide)
5. [Data Source](#data-source)
6. [Pipeline Workflow](#pipeline-workflow)
7. [Unit Testing and Continuous Integration](#unit-testing-and-continuous-integration)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact Information](#contact-information)

---

## Project Overview

This project aims to develop an accurate, condition-aware model for predicting house prices. The model considers a variety of features and employs advanced data processing, feature engineering, and modeling techniques. Key features of this project include:

- **Data Acquisition**: Data scraping from Zillow and integration with the Ames Housing Dataset.
- **Data Preprocessing**: Cleaning, transforming, and feature engineering to enhance prediction accuracy.
- **Modeling Techniques**: Utilizes regression, tree-based models, and neural networks to compare and optimize performance.
- **CI/CD Practices**: Automated deployment and testing using GitHub Actions.
- **Model Monitoring and Maintenance**: Tracks model performance and ensures fairness in predictions over time.

### Dependencies

Key tools and services used in this project include:
- **Apache Airflow**: For orchestrating the ETL pipeline.
- **Google Cloud Platform (GCP)**: For data storage and version control.
- **DVC (Data Version Control)**: For tracking data and model versions.

## Folder Structure

```
House_Price_Prediction_MLOps/
├── Airflow/               # Contains DAGs and scripts for data pipeline orchestration.
├── Methodology/           # Provides details on model choices, data processing, and feature engineering.
├── project_dvc/           # Stores DVC configuration files for data versioning and management.
├── tests/                 # Contains unit tests and validation scripts.
├── .gitignore             # Specifies files to ignore in Git.
└── README.md              # Main project documentation.
```

## Installation and Setup

To set up the project environment:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your_username/House_Price_Prediction_MLOps.git
    cd House_Price_Prediction_MLOps
    ```

2. **Install dependencies**:
   - Use the `requirements.txt` file to install Python dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   - Add GCP credentials and other environment variables in a `.env` file (refer to the `config/` folder).
   - Initialize a GCP service account and download an SSH key if accessing data remotely.

4. **Set Up Airflow**:
   - Initialize the Airflow database and start the Airflow scheduler and web server:
   ```bash
   airflow db init
   airflow scheduler
   airflow webserver
   ```

## Quickstart Guide

1. **Load Data from Google Cloud Storage (GCS)**:
   - Our datasets are managed in GCS, with version control provided by DVC.

2. **Trigger the Airflow Pipeline**:
   - Access the Airflow web UI at `http://localhost:8080`.
   - Enable and trigger the DAGs (data acquisition, preprocessing, and model training pipelines) as needed.

3. **Monitor Data and Model Versions**:
   - Use DVC commands to track changes in data and models:
   ```bash
   dvc add data/raw/ames_housing.csv
   dvc push
   ```

## Data Source

The main dataset used is the [Ames Housing Dataset](https://www.kaggle.com/datasets/shashanknecrothapa/ames-housing-dataset), which includes details on property features. For additional feature details, refer to our [Features Explanation](https://docs.google.com/spreadsheets/d/1XL6LJVgLLU27yV7a_oh2zuqhGOI3Syg-jWpmr0Ekk14/edit?gid=0#gid=0).

## Pipeline Workflow

We use **Apache Airflow** to manage our pipeline, which includes tasks for data scraping, preprocessing, model training, and evaluation. The pipeline structure is modular, with tasks organized into distinct DAGs for each stage.

**Pipeline Overview**:

- **Data Loading and Preprocessing**: Loads raw data from GCS, validates and cleans the data.
- **Feature Engineering**: Transforms and augments data for better model performance.
- **Model Training**: Trains models using various algorithms and stores results for evaluation. [Next Stage]
- **Model Evaluation**: Assesses model performance and pushes metrics to monitoring systems. [Next Stage]

![Pipeline Diagram](https://github.com/user-attachments/assets/55121bb8-6b69-4101-ba7b-37ae5d89cab9)


## Unit Testing and Continuous Integration

We use **GitHub Actions** to perform automated unit tests on each pipeline component. When changes are pushed to the main branch, GitHub Actions runs the unit tests and provides feedback on their status.

![Unit Test](https://github.com/user-attachments/assets/74c31c68-e3ad-4c8e-ac46-17482e6718f7)

## Contributing

We welcome contributions to improve this project. Please fork the repository, make changes, and submit a pull request. Ensure that your code follows the existing style guidelines and includes tests for any new features.

## License

This project is licensed under the [].

## Contact Information

For questions or collaboration inquiries, please contact one of the team members:
- Aliya at [26aly000@gmail.com]
- Changping Chen at [champing1409@gmail.com]
- Krishna Priya Gitalaxmi at [gitakrishnapriya@gmail.com]
- Qi An at [blessanq@gmail.com]
- Ziqi Li at [zql04150415@gmail.com]
  
# Airflow Pipeline Setup and Usage

This document provides instructions for setting up, running, and troubleshooting the Airflow-based data pipeline for the **House Price Prediction MLOps** project. Apache Airflow orchestrates various ETL processes and machine learning workflows, ensuring modular, scalable, and efficient data processing.

---

## 1. Introduction

The Airflow pipeline automates the end-to-end data processing and machine learning workflow for the House Price Prediction project. Key stages in the pipeline include:
- **Data acquisition** from Google Cloud Storage (GCS)
- **Data preprocessing** (cleaning, validation, splitting)
- **Feature engineering** and **data augmentation**
- **Model training** and **evaluation**
- **Artifact storage** and version control using DVC

---

## 2. Pipeline Overview

The pipeline consists of modular DAGs (Directed Acyclic Graphs) that run specific tasks in a sequence to process data, train models, and track outputs. Each DAG is designed to operate independently, allowing for flexibility in updating and testing individual components.

### DAGs Included:
- **data_prep_dag**: Handles data loading, validation, cleaning, and splitting.
- **feature_and_augm_dag**: Performs feature engineering and data augmentation.

### Pipeline Flow Diagram:
![Pipeline Diagram](https://github.com/user-attachments/assets/a8ecfda0-bf73-4ce4-9c8c-46b162cf10a2)
![Pipeline Diagram](https://github.com/user-attachments/assets/cf91bad9-c892-41cb-9640-31a8ef25fee9)

---

## 3. Setup

### a. Prerequisites

- **Python 3.8+**
- **Apache Airflow** (version 2.x)
- **Docker** (if using Docker Compose for containerized Airflow)
- **Google Cloud SDK** (for integration with GCS and DVC)

### b. Environment Variables

To facilitate connections to GCS and manage Airflow configuration, add environment variables in a `.env` file within the `config/` folder. Key variables include:
- `GCP_PROJECT_ID`
- `GCS_BUCKET_NAME`
- `DVC_REMOTE_PATH`
- Additional Google Cloud credentials as needed

### c. Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone [REPO_URL]
   cd Airflow
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize Airflow**:
   - Set up the Airflow database, then start the scheduler and web server:
   ```bash
   airflow db init
   airflow scheduler &
   airflow webserver
   ```

4. **Docker Setup** (Optional):
   - If using Docker Compose, start Airflow services as follows:
   ```bash
   docker-compose up -d
   ```

5. **Configure DVC**:
   - Refer to the main project `README.md` for DVC setup instructions with Google Cloud.

---

## 4. Running the Pipeline

1. **Access the Airflow Web UI**:
   - Open `http://localhost:8080` in your browser to view your DAGs.

2. **Enable DAGs**:
   - In the Airflow UI, toggle the DAGs to enable them:
     - `data_prep_dag`: Manages data loading, cleaning, and splitting
     - `feature_and_augm_dag`: Conducts feature engineering and augmentation

3. **Trigger DAG Runs**:
   - Manually start a DAG run or configure a schedule in the DAG definitions as needed.

---

## 5. DAG Structure and Task Descriptions

### **data_prep_dag**
This DAG performs core data processing tasks:
- **Data Loading**: Loads raw data from GCS.
- **Data Validation**: Validates data schema and format.
- **Data Preprocessing**: Cleans missing values, encodes categorical data, and normalizes features.
- **Data Splitting**: Divides data into training, validation, and test sets.

### **feature_and_augm_dag**
This DAG is responsible for feature engineering and data augmentation:
- **Feature Engineering**: Applies transformations and extracts meaningful features.
- **Data Augmentation**: Expands the dataset using augmentation techniques to improve model robustness.

---

## 6. Troubleshooting and Common Issues

- **Airflow DAG Not Showing**: Ensure the `dags` folder is correctly set in `AIRFLOW_HOME`. Check for syntax errors in the DAG files.
- **GCS Permission Issues**: Verify that the GCP service account has access permissions to the specified GCS bucket.
- **Docker Errors**: If using Docker, confirm that the Docker daemon is running and `.env` variables are correctly configured.

---

## 7. Folder Structure (Airflow-Specific)

Here is an outline of the `Airflow` folder structure for easy reference:

```
Airflow
├── dags                   # Contains all DAG scripts
│   ├── __pycache__        # Python cache files
│   ├── data               # Data files required by DAGs
│   ├── src                # Source scripts for custom processing
│   │   ├── __init__.py
│   │   ├── data_augment.py
│   │   ├── data_prep.py
│   │   ├── data_splitting.py
│   │   ├── feature_select.py
│   │   └── label_encode.py
│   ├── __init__.py        # Initialization file for Airflow
│   ├── data_prep_dag.py   # DAG for data loading and preprocessing
│   └── feature_and_augm_dag.py  # DAG for feature engineering and augmentation
```

---

## 8. Testing and Validation

We use **GitHub Actions** to automate unit tests and validate each task within the DAGs. When changes are committed to the main branch, GitHub Actions triggers the tests and provides feedback on their results.

To run tests locally:
```bash
pytest tests/
```

![Unit Test Status](https://github.com/user-attachments/assets/74c31c68-e3ad-4c8e-ac46-17482e6718f7)

---

## 9. Resources and References

- **[Apache Airflow Documentation](https://airflow.apache.org/docs/)**: Official documentation for setting up and using Apache Airflow.
- **[Google Cloud SDK](https://cloud.google.com/sdk/docs)**: Guide for configuring GCS and managing data storage.
- **[DVC Documentation](https://dvc.org/doc)**: Guide for setting up DVC for data versioning.

# **Running MLflow UI in an Airflow Container for Experiment Tracking**
In this project, we used MLflow within an Airflow container to track our machine learning experiments. We trained three models for predicting house prices using both categorical and numerical features:

Linear Regression
Random Forest
Elastic Net
After evaluating their performance, we found that the Random Forest model provided the best results for our dataset. All training runs, metrics, and artifacts were logged and visualized through the MLflow UI, which made it easy to compare the models and select the optimal one.

This guide explains how to run the **MLflow UI** from an Airflow container in a Dockerized environment. It assumes you already have an Airflow setup running using `docker-compose` and MLflow installed in the containers via `_PIP_ADDITIONAL_REQUIREMENTS`.
![image](https://github.com/user-attachments/assets/e0e1720d-b7f7-4f88-afbb-546535b91c5d)
![image](https://github.com/user-attachments/assets/d5bee6ac-93bd-4dfa-a1b0-0d92ef9c01b9)
![image](https://github.com/user-attachments/assets/750effb5-34bf-4c72-a9d9-7fb311b043d2)

---

## **Prerequisites**

1. **Airflow Setup**: Ensure your Airflow containers are running and properly configured in the `docker-compose.yaml` file.
2. **MLflow Installed**: MLflow should be included in the `_PIP_ADDITIONAL_REQUIREMENTS` of your Airflow setup:
   ```yaml
   _PIP_ADDITIONAL_REQUIREMENTS: "mlflow pandas scikit-learn kneed google-cloud-storage"
   ```
3. **Shared Volume**: The `mlruns` directory should be mounted to `/opt/airflow/mlruns` for consistent tracking:
   ```yaml
   volumes:
     - ./mlruns:/opt/airflow/mlruns
   ```

---

## **Steps to Run MLflow UI**

### **1. Start Airflow Containers**
Start your Airflow setup:
```bash
docker-compose up -d
```

Ensure all containers are running:
```bash
docker ps
```

### **2. Access the Desired Container**
Decide which Airflow container will host the MLflow UI. Typically, this will be the **worker** or **webserver** container. Enter the container:
```bash
docker exec -it airflow-airflow-worker-1 bash
```
*(Replace `airflow-airflow-worker-1` with the name of the desired container.)*

### **3. Start the MLflow UI**
Inside the container, start the MLflow UI:
```bash
mlflow ui --backend-store-uri postgresql+psycopg2://airflow:airflow@postgres/mlflow --host 0.0.0.0
```

- **`--backend-store-uri`**: Specifies the location of the MLflow tracking directory.
- **`--host`**: Ensures the UI is accessible from outside the container.

### **4. Access the MLflow UI**
The UI will be available at:
```
http://localhost:5000
```

If port **5000** is already in use, you can specify a different port:
```bash
mlflow ui --backend-store-uri file:///opt/airflow/mlruns --host 0.0.0.0 --port 5001
```
Ensure the port is mapped in your `docker-compose.yaml`:
```yaml
ports:
  - "5001:5001"
```

---

## **Stopping the MLflow UI**

### **1. If Running in the Foreground**
Stop the process by pressing:
```
Ctrl + C
```

### **2. If Running in the Background**
Find the MLflow process ID (PID) and terminate it:
```bash
ps aux | grep 'mlflow'
kill <PID>
```

---

## **Notes**

- For modular setups, consider running the MLflow UI in a dedicated container for better scalability and separation of concerns.
- Make sure the `mlruns` directory is shared between the container running the MLflow UI and the container where Airflow logs experiments.

---

## **Troubleshooting**

1. **Cannot Access MLflow UI**:
   - Verify that port **5000** is mapped correctly in the `docker-compose.yaml`.
   - Check if another process is using port **5000**:
     ```bash
     sudo ss -tuln | grep 5000
     ```

2. **Permission Issues**:
   Ensure the `mlruns` directory has the correct permissions:
   ```bash
   chmod -R 755 ./mlruns
   ```

---

# Troubleshooting `init-db.sh` Script in Docker Compose

This guide helps you troubleshoot issues related to the execution of the `init-db.sh` script in a Docker Compose setup, specifically for initializing a PostgreSQL database.

## Common Issues and Resolutions

### 1. File Permissions
Ensure the `init-db.sh` file has executable permissions.

**Command to check permissions:**  
```bash
ls -l init-db.sh
```

Expected output:  
```bash
-rwxr-xr-x 1 user group size date init-db.sh
```

If permissions are incorrect, run:  
```bash
chmod +x init-db.sh
```

### 2. Line Endings
Ensure the script has Unix line endings. Windows-style line endings can cause syntax errors in the container.

**Convert to Unix format:**  
Install `dos2unix` (if not already installed):  
```bash
sudo apt install dos2unix
```

Run the conversion:  
```bash
dos2unix init-db.sh
```

### 3. Correct Placement in Docker Compose
Ensure the script is mounted correctly in the `docker-compose.yml` file.

Example:  
```yaml
services:
  postgres:
    volumes:
      - ./scripts/init-db.sh:/docker-entrypoint-initdb.d/init-db.sh
```

### 4. Script Debugging
If the script fails to execute, check the logs of the PostgreSQL container:  
```bash
docker logs <postgres-container-id>
```

Manually execute the script inside the container to debug errors:  
```bash
docker exec -it <postgres-container-id> bash
bash /docker-entrypoint-initdb.d/init-db.sh
```

### 5. Confirm Database Initialization
Check if the `mlflow` database was successfully created:  
```bash
docker exec -it airflow-postgres-1 psql -U airflow
\l
```

The output should list `mlflow` as one of the databases.

## Sample `init-db.sh` Script
```bash
#!/bin/bash
# Check if the database has already been initialized
if [ ! -f "/var/lib/postgresql/data/.db_initialized" ]; then
  echo "Initializing database..."
  psql -U airflow -c "CREATE DATABASE mlflow;"
  psql -U airflow -c "GRANT ALL PRIVILEGES ON DATABASE mlflow TO airflow;"
  touch /var/lib/postgresql/data/.db_initialized
else
  echo "Database already initialized."
fi
```

## Notes
- Ensure the `init-db.sh` script is idempotent to avoid issues during multiple runs.
- The `.db_initialized` file acts as a flag to ensure the database initialization runs only once.

## Contact
If you encounter further issues, consult the Docker and PostgreSQL documentation or reach out for support.


---

## Data Validation and Data Shift Detection

To ensure high-quality data processing and robust model training, the project incorporates automated **Data Validation** and **Data Shift Detection** mechanisms. These processes leverage **TensorFlow Data Validation (TFDV)** and custom Cloud Functions integrated with **Google Pub/Sub** for real-time tracking of changes to the data folder in the GCS bucket. Notifications are sent via email for critical events.

![image](https://github.com/user-attachments/assets/a4199b64-e6be-4a0c-876c-fed11986d7ba)


---

### 1. Data Validation using TFDV

We use **TensorFlow Data Validation (TFDV)** to validate the dataset during the preprocessing pipeline. TFDV automatically analyzes the dataset to detect anomalies, inconsistencies, and schema violations.

![image](https://github.com/user-attachments/assets/02c56254-e950-463e-b864-cb456579453e)


#### Key Features:
- **Schema Generation**: Defines expected feature types, value ranges, and distributions.
- **Anomaly Detection**: Identifies:
  - Missing or unexpected values.
  - Type mismatches (e.g., numerical features containing non-numeric values).
  - Distributional anomalies (e.g., significant deviations in feature distributions).
- **Statistics Comparison**: Ensures consistency with historical data by comparing feature statistics (mean, median, standard deviation).

#### Workflow:
1. During the **data preprocessing pipeline**, TFDV analyzes the dataset and validates it against the schema.
2. Anomalies detected by TFDV are logged, and an email notification is sent for critical issues.
3. If no anomalies are found, the pipeline proceeds to the next stage.

---

### 2. Data Shift Detection using Cloud Functions

To maintain model reliability, we monitor the **data folder** in the GCS bucket for changes (additions or deletions). A custom **Google Cloud Function** tracks these events in real-time and evaluates potential data drift.

![image](https://github.com/user-attachments/assets/4a57684f-d84a-411a-9841-3fc859796662)


#### Pub/Sub Integration:
- A **Pub/Sub topic** is configured to monitor the `data/` folder in the GCS bucket.
- Whenever a new file is added or an existing file is deleted, a message is published to the Pub/Sub topic, triggering the **Data Shift Detection Cloud Function**.

#### Data Drift Detection:
- The Cloud Function compares the statistics of the newly added file with a reference dataset using statistical tests:
  - **Kolmogorov-Smirnov Test**: For numerical features.
  - **Chi-Squared Test**: For categorical features.
- Drift detection logic identifies significant deviations in feature distributions, indicating potential issues with the data pipeline.

#### Workflow:
1. **File Added to GCS**: When a new file is added to the `data/` folder, the Cloud Function:
   - Downloads the new file and the reference dataset.
   - Generates feature statistics for both datasets.
   - Detects drift using statistical tests.
2. **File Deleted from GCS**: If a file is removed, the function logs the event and sends an email notification.

---

### 3. Email Notifications

The Cloud Functions and TFDV processes are configured to send email alerts for critical events:
- **Data Validation Anomalies**:
  - Schema violations (e.g., unexpected feature types).
  - Missing or out-of-range values.
    ![image](https://github.com/user-attachments/assets/8644ff1a-d9a6-4224-abe9-84382b040075)

- **Data Drift Detection**:
  - Significant drift in feature distributions.
  - Notifications include a summary of drifted features and the corresponding p-values.
    ![image](https://github.com/user-attachments/assets/2d6eac52-bbce-40bf-a9fa-98e096fe61c5)

- **File Addition/Deletion**:
  - Alerts are sent whenever files are added to or removed from the `data/` folder.

#### Email Sample:
**Subject**: Data Drift Detected in Latest File  
**Body**:
```
A data drift was detected in the file 'new_data.csv' uploaded to the GCS bucket.

Drift Summary:
- Feature: 'Lot Area'
  Test: Kolmogorov-Smirnov Test
  p-value: 0.001
  Drift Detected: True

- Feature: 'Neighborhood'
  Test: Chi-Squared Test
  p-value: 0.015
  Drift Detected: True

Please review the new data to ensure consistency with the reference dataset.
```

---

### 4. Benefits of Automation

- **Real-time Monitoring**: Tracks changes to the `data/` folder instantly, ensuring quick detection of anomalies or drift.
- **Improved Data Quality**: TFDV ensures that only validated data proceeds to the preprocessing and modeling stages.
- **Early Issue Detection**: Data drift alerts allow for proactive adjustments to maintain model performance and reliability.
- **Seamless Integration**: Leveraging Pub/Sub and Cloud Functions ensures that the system is highly scalable and fault-tolerant.

---

### 5. How to Customize

- **Pub/Sub Topic**: Modify the topic subscription in the Cloud Function to track additional folders or buckets as needed.
- **Email Recipients**: Update the email configuration to include new recipients or modify the alert formats.
- **Drift Sensitivity**: Adjust the p-value threshold in the Cloud Function to control the sensitivity of drift detection.

---

This automated pipeline ensures data consistency and enhances the reliability of the **House Price Prediction** system, enabling efficient and scalable machine learning operations.
# Methodology for House Price Prediction

This folder documents the methodology used in the House Price Prediction project, detailing the steps taken to process data, select features, and develop a robust model. The dataset used is **AmesHousing.csv**.

---

## 1. Introduction

The methodology outlined here serves as a guide to understanding the reasoning behind data processing, feature selection, and model preparation for predicting house prices. Each decision was made with the goal of improving model accuracy, interpretability, and robustness. 

For detailed data definitions, refer to this [Data Definition Document](https://docs.google.com/spreadsheets/d/1XL6LJVgLLU27yV7a_oh2zuqhGOI3Syg-jWpmr0Ekk14/edit?usp=sharing).

---

## 2. Data Processing Methods

### Overview of the Dataset
- **Dimensions**: 82 columns, 2930 rows
- **Data Types**:
  - `float64`: 11 columns
  - `int64`: 28 columns
  - `object`: 43 columns

The dataset includes a balanced mix of quantitative variables (e.g., year built, number of fireplaces) and qualitative variables (e.g., heating quality, exterior quality).

### Data Validation
We validated the dataset using information from the [Data Documentation](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt). Key steps included:
1. **Outlier Removal**: Houses with over 4000 square feet were excluded to avoid skewing the model.
2. **Data Correction**: Corrected a record where the garage build year was incorrectly listed as 2207, changing it to 2007.

### Handling Missing Values and Duplicates
- **Duplicates**: No duplicate records were identified in the dataset.
- **Missing Values**:
   - **Numerical Variables**: Handled based on variable type:
      - Filled with `0` for features like basement full bathroom and total basement square feet.
      - Used the median for continuous features like lot frontage and garage cars.
   - **Categorical Variables**: Standardized all `NA`, empty, or `None` values to "Missing" for consistency.

### Data Saving
The cleaned dataset was saved as `cleaned_data.csv` to ensure reproducibility and facilitate alternative encoding methods if needed.

---

## 3. Feature Engineering

To prepare categorical features for modeling, we applied label encoding. The encoding was customized based on feature types and scales:

1. **Handling Missing Values**: Encoded all "Missing" values as `0`.
2. **Feature Grouping and Encoding**:
   - **Quality-related Features**: Encoded on a scale from 1 to 5, ranging from Poor to Excellent, covering 10 features.
   - **Good-to-Bad Features**: Assigned values from low to high quality across 7 features.
   - **Other Features**: Encoded appropriately based on their role in modeling.

After encoding, we saved the transformed dataset as `encoding_data.csv` for modeling use.

---

## 4. Data Splitting

The processed data was split into training and test sets with an 85/15 ratio. This larger training set size enhances model learning, particularly given the limited dataset size. To maintain an unbiased evaluation, we applied data augmentation only to the training data, leaving the test set untouched as a representative sample for real-world cases.

---

## 5. Feature Selection

After data splitting, we identified relevant features for predicting SalePrice using two methods:

### *1. Correlation Analysis*
   - We focused on features with a Pearson’s r correlation coefficient of at least 0.3 with SalePrice. This threshold balances relevance with simplicity, retaining features with moderate associations without over-complicating the model.

### *2. Lasso Regression*
   - To refine feature selection further, we applied Lasso regression, using LassoCV to find the optimal regularization level. Standardized features were used to ensure consistent scaling. We set a high importance threshold of 0.1, and only one feature was removed, reinforcing the relevance of those identified in the correlation analysis.

---

## 6. Data Augmentation

The selected features were passed through the `augment_data_with_perturbations` function for data augmentation, which introduces slight variations in key features. This approach is intended to enhance model generalization by simulating small real-world changes in the data. Key augmentation parameters:

- **Perturbation Percentage**: Set at 0.02 to ensure variations remain within 2% of original feature values, maintaining data realism.
- **Augmented Records**: Generated 2000 synthetic records, balancing data diversity with computational efficiency.

---

## 7. Model Selection and Training

For model selection, we experimented with regression, tree-based models, and neural networks. **Lasso regression** and **tree-based models** were chosen for their interpretability and performance. Hyperparameters were fine-tuned to optimize performance while avoiding overfitting.

---

## 8. Evaluation Metrics

To assess model performance, we used **Root Mean Squared Error (RMSE)** and **Mean Absolute Error (MAE)**, as both metrics provide insight into prediction accuracy and error magnitudes. These metrics help in evaluating model generalization and guiding further tuning.

---

## 9. Experimentation and Results

Several experiments were conducted to evaluate feature impact and model configurations. Through these, we achieved:
- An optimal balance between accuracy and complexity.
- Improved performance using data augmentation, which increased model robustness.

---

## 10. References and Resources

- **[Data Definition Document](https://docs.google.com/spreadsheets/d/1XL6LJVgLLU27yV7a_oh2zuqhGOI3Syg-jWpmr0Ekk14/edit?usp=sharing)**
- **[Data Documentation](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)**
- **Research Papers and Resources on Data Augmentation and Feature Selection Techniques**

# Project DVC

This project uses Data Version Control (DVC) to manage datasets and track changes efficiently. Below is the directory structure and description of each component in this project.

## Directory Structure

```plaintext
project_dvc/                  # Root folder for the DVC project
├── .dvc/                      # DVC configuration folder
│   ├── config.txt             # DVC configuration file
│   └── gitignore.txt          # Git ignore settings for DVC files
├── data/                      # Data folder containing datasets and version files
│   ├── AmesHousing.csv.dvc    # DVC-tracked file for the Ames Housing dataset
│   ├── cleaned_data.csv.dvc   # DVC-tracked file for the cleaned dataset
│   ├── encoding_data.csv.dvc  # DVC-tracked file for the encoded dataset
│   ├── gitignore.txt          # Git ignore file specific to the data folder
│   └── dvcignore.txt          # DVC ignore file for excluding certain files from DVC tracking
```

## Description of Files and Folders

- **project_dvc/**: The main directory of the project where all DVC-related files are stored.
  
- **.dvc/**: Contains DVC configuration and settings files.
  - **config.txt**: Configuration file that includes the settings for DVC in this project.
  - **gitignore.txt**: Specifies files and directories that Git should ignore in the `.dvc` folder.
  
- **data/**: This folder contains the datasets used in the project, all tracked by DVC.
  - **AmesHousing.csv.dvc**: DVC-tracked file for the original Ames Housing dataset.
  - **cleaned_data.csv.dvc**: DVC-tracked file for the cleaned version of the dataset after preprocessing.
  - **encoding_data.csv.dvc**: DVC-tracked file for the dataset after encoding categorical variables.
  - **gitignore.txt**: File to specify files in the `data` folder that Git should ignore.
  - **dvcignore.txt**: File to specify files in the `data` folder that DVC should ignore.

## Usage

1. **Setting Up DVC**:
   - Ensure DVC is installed by running `pip install dvc`.
   - Initialize DVC in the project (if not already done) using `dvc init`.

2. **Adding Data Files**:
   - Place raw and processed datasets in the `data/` folder.
   - Track each dataset with DVC by running `dvc add data/<filename>`.
   - This creates `.dvc` files (e.g., `AmesHousing.csv.dvc`) that reference the version-controlled data.

3. **Using gitignore.txt and dvcignore.txt**:
   - `gitignore.txt` is used to prevent specific files in `data/` from being tracked by Git.
   - `dvcignore.txt` helps DVC to ignore files or directories in `data/` that you do not want to track.

4. **Pushing Data to Remote Storage**:
   - Configure a remote storage for DVC using `dvc remote add -d <remote-name> <remote-url>`.
   - Push the data to the remote storage with `dvc push` to back up your datasets.

5. **Pulling Data**:
   - To retrieve data from the remote storage, use `dvc pull`.

## Notes

- Ensure that both `gitignore.txt` and `dvcignore.txt` are properly configured to exclude unnecessary files from version control.
- For collaborative projects, share `.dvc` files and configuration, allowing others to reproduce your work by using `dvc pull` to fetch the data.

