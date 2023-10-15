# Double-Edged-Defense
This repository includes all supplementary material (Datasets and codes) of our paper titled "Double-Edged Defense: Thwarting Cyber Attacks and Adversarial Machine Learning in IEC61850-104 Smart Grids"
It contains the IDS dataset designed for analyzing and identifying various types of attacks on Smart Grid (SG) systems, IEC 104. The dataset consists of multiple folders, each with specific data related to different attack vectors and scenarios.
Folder Structure
The dataset is organized into several folders, each containing different types of data. Below is a description of each folder:

but-iec104-i: Contains 7 CSV files. Six files simulate different attack scenarios while one file contains benign communication data.

DoS Attack
Injection Attack
Connection-Loss Attack
Switching Attack
Scanning Attack
Rogue Device Attack
but-iec104-ii: Contains benign communication data.

rts-iec104: Houses traces reflecting normal SCADA network communication.

vrt-iec104: Contains data from an IEC virtual testbed, including benign and malicious activities.

Man-in-the-Middle (MITM) Attack
Value Change Attack
Masquerading Attack
Report-block Attack
Replay Attack
For a more detailed description of each folder, refer to Table: Description of IDS Dataset Folders.

Types of Attacks
The dataset encompasses 11 distinct types of attacks:

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
