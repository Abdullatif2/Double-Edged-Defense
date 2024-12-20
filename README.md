# Double-Edged-Defense
This repository includes all supplementary material (Datasets and codes) of our paper titled "Double-Edged Defense: Thwarting Cyber Attacks and Adversarial Machine Learning in IEC61850-104 Smart Grids"

## Dataset Structure
It contains the IDS dataset designed for analyzing and identifying various types of attacks on Smart Grid (SG) systems, IEC 104. The dataset consists of multiple folders, each with specific data related to different attack vectors and scenarios.

The dataset is organized into several folders, each containing different types of data. Below is a description of each folder:

### but-iec104-i: 
Contains 7 CSV files. Six files simulate different attack scenarios while one file contains benign communication data.
DoS Attack
Injection Attack
Connection-Loss Attack
Switching Attack
Scanning Attack
Rogue Device Attack

### but-iec104-ii: 
Contains benign communication data.

### rts-iec104:
Houses traces reflecting normal SCADA network communication.

### vrt-iec104: 
Contains data from an IEC virtual testbed, including benign and malicious activities
Man-in-the-Middle (MITM) Attack
Value Change Attack
Masquerading Attack
Report-block Attack
Replay Attack
For a more detailed description of each folder, refer to Table: Description of IDS Dataset Folders.

### encs-iec104:
This folder contained 3 CSV files, one reflect normal communication, and 2 attack files.
### encs-mms:
This folder contained 2 CSV files that collects data from the IEC-MMS header, one reflect normal communication, and 1 attack file.
### gics-mms:
This folder contained 5 CSV files that collects data from the IEC-MMS header:
Normal data 
Connection loss attack 
Scanning attack 
Interruption attack

Types of Attacks
The IEC 104 data encompasses 11 distinct types of attacks:

DoS Attack (Denial of Service): Leads to potential power outages and reduced system reliability.
Injection Attack: Risks unauthorized control over SG components.
Connection-Loss Attack: Causes a lack of situational awareness and potentially cascading failures.
Switching Attack: Results in erratic device behavior.
Scanning Attack: Gives attackers insight into the SG's structure.
Rogue Device Attack: Leads to false data injection.
Man-in-the-Middle (MITM) Attack: Manipulates data and control commands.
Value Change Attack: Alters values that may result in equipment damage.
Masquerading Attack: Injects false data into the system.
Report-block Attack: Disrupts the flow of critical information.
Replay Attack: Deceives the system into making incorrect decisions.
Features in IEC 104 Header
The dataset also contains features extracted from the IEC 104 header, such as Timestamp, Relative time, Source and Destination IP addresses, Source and Destination port, etc. For more details, refer to Table: IEC 104 Dataset Features.
## Dataset Preprocessing & Labeling
1- IEC Data Preprocessing 
In this Code file, we load all the data, preprocess, and label it. After that we save the Preprocessed/labeled data into 3 CSV files (data_without_ioa.csv & data_with_ioa.csv & data_MMS.csv)

### The preprocessing of the IEC104 data includes the following tasks: 

    - Data Labeling  
    
        0: Benign Data
        1: Connection-Loss Attack
        2: DoS Attack
        3: Switching Attack
        4: Scanning Attack
        5: Rogue-device Attack
        6: Injection Attack 
        7:MITM attack
        8:Replay attack
        9:Report-block attack
        10:Value-change attack
        11:Masquerading attack
        
    - Convert Strings features to Numerical values 
        IP address
        Time Stamps
        
    - Categorical values encoding: each unique value is encoded to a corresponding integer value
        APDU format type
        u-format type
        information object address 
        
    - Clear the dataset from Null values
        All null values were replaced with the corresponding median of the feature

### The preprocessing of the IEC MMS data includes the following tasks:

- Data Labeling
  
    0: Benign Data
  
    1: Inside-Substation Attack
  
    2:Connection loss attack
  
    3:Modification attack
  
    4: Scanning Attack
  
    5: Interruption Attack
  
- Convert Strings features to Numerical values 
    IP address
    Time Stamps

- Categorical values encoding: each unique value is encoded to a corresponding integer value
    Domain Id
    Item Id

- Clear the dataset from Null values
    All null values were replaced with the corresponding median of the feature
    
## Processed Datasets:
The datasets can be downloaded from this link: 1- https://drive.google.com/file/d/1RKUzY9lmOzwU8ifQoJ4Q7cWRqcRO6PeM/view?usp=drive_link, https://drive.google.com/file/d/18XclVyqsJX9mkOCKd7zEsdQCndeENunH/view?usp=drive_link
2- https://drive.google.com/file/d/18XclVyqsJX9mkOCKd7zEsdQCndeENunH/view?usp=sharing
## Adversarial Training for Robust Model
### 1- LTSM.ipynb

In this Code file, We experimented with the use of LTSM on the preprocessed dataset. The results were very bad, Hence we didn't use it in our methodology. 


### 2- MLP-IEC_without_IOA

In this code file, we used the generated CSV File from the IEC Data Preprocessing & Labeling Code. Specifically, we used "data_without_ioa.csv". 
The Steps performed in this code include: 
- Data Loading
- Data Sampling (30,000 Samples per Class, Total: 6 Classes) 
- Min-MAx Normalization  
- Model Training 
- Model Testing 

Result: The model was able to achieve 98% Accuracy 

### 3- MLP-IEC_with_IOA

In this code file, we used the generated CSV File from the IEC Data Preprocessing & Labeling Code. Specifically, we used "data_without_ioa.csv". 
The Steps performed in this code include: 
- Data Loading
- Data Sampling (2000 Samples per Class, Total: 7 Classes)
- Min-MAx Normalization  
- Model Training 
- Model Testing 

Result: The model was able to achieve only 89% Accuracy due to the huge data imbalance between classes 

### 4- MLP-IEC104_All_merged_All_data

In this code file, we used the generated CSV File from the IEC Data Preprocessing & Labeling Code. Specifically, we used "data_without_ioa.csv" & "data_with_ioa.csv". 
The main goal of this file is to train a multiclass model that can differniate between 11 Classes (The model was trained on both the benign and attack samples togther)

The Steps performed in this code include: 
- Data Loading
- Remove the IOA and other irrelevant feature 
- Merge All data in one Dataframe
- Data Sampling (2000 Samples per class , Total: 12 Classes)
- Min-MAx Normalization  
- Model Training 
- Model Testing 

Result: The model was able to achieve only 95% Accuracy


### 5- MLP-IEC104_All_merged_All_data-Binary_adv (1st Layer of the Hierarchical Model) 

In this code file, we used the generated CSV File from the IEC Data Preprocessing & Labeling Code. Specifically, we used "data_without_ioa.csv" & "data_with_ioa.csv". 
The main goal of this file is to train the binary model and test/enhance its robustness against Adversarial attacks. (The model was trained on both the benign and attack samples togther)

The Steps performed in this code include: 
- Data Loading
- Remove the IOA and other irrelevant feature
- Merge All data in one Dataframe
- Unify the Label for all attack samples since this is a binary classification 
- Data Sampling (200,000 Samples per class , Total: 2 Classes)
- Min-MAx Normalization  
- Model Training 
- Model Testing (100% without Applying any adversarial attack)
- Save the trained Model
- Generate Adversarial Samples using (FGSM/PGD/ Carlini & Wagner) attacks
- Examine the impact of each attack on the trained model performance 

Result: The model Achieved 100% accuracy and maintained the same accuracy even when applying attacks like (FGSM/PGD/ Carlini & Wagner)

### 6- MLP-IEC104_All_merged_All_data_adv (2nd Layer of the Hierarchical Model) 

In this code file, we used the generated CSV File from the IEC Data Preprocessing & Labeling Code. Specifically, we used "data_without_ioa.csv" & "data_with_ioa.csv". 
The main goal of this file is to train the attack model and test/enhance its robustness against Adversarial attacks. (The model was trained on the attack samples only)

The Steps performed in this code include: 

- Data Loading
- Remove the IOA and other irrelevant feature
- Merge All data in one Dataframe
- Remove all benign Samples to train the attack model 
- Data Sampling (10,000 Samples for class 1 & 4 and 5000 Samples for remaining classes, Total: 11 Classes)
- Min-MAx Normalization  
- Model Training 
- Model Testing (99.9% without Applying any adversarial attack)
- Save the trained Model
- Generate Adversarial Samples using (FGSM/PGD/ Carlini & Wagner) attacks
- Examine the impact of each attack on the trained model performance 
- Perform Defensive Distillation & Adversarial Training to increase model resiliency againest the attacks
- Test Model accuracy after distillation 

Result: You Can Refer to Table Defensive Distillation effect on Model Accuracy for the detailed results
