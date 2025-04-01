# Facial Recognition Attendance System

🛠️ This project utilizes OpenCV and the Python library **(face_recognition)** to update attendance based on individual facial features. Additionally, it generates a daily attendance record in a .csv file. <br>
<br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="python logo"  />
<img width="12" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="30" alt="vscode logo"  />
<img width="12" />
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZslNSk4pgYd4cvWIY35bE9Hol5OvaL_xTvw&s" height="30" alt="vscode logo"  />
<img width="12" />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Microsoft_Excel_2013-2019_logo.svg/1200px-Microsoft_Excel_2013-2019_logo.svg.png" height="30" alt="vscode logo"  />

## Video Demo

🎥 Here you can find a video of the working project.

https://github.com/user-attachments/assets/cab003e3-a35c-4c28-99a7-d157996abdfc

## Deployment

To run this project first clone this repository using:

```bash
  git clone https://github.com/aka-Harsh/Facial-Recognition-Attendance.git
```

Save this repository in your system and access it, then create and activate a virtual environment:
```bash
  python -m venv venv
  venv\Scripts\activate
```

Install all the required packages:
```bash
  pip install -r requirements.txt
```

Finally run the app.py file:
```bash
  streamlit run src/app.py
```
Give your webpage camera access in order to run.

## Project Outlook

<br>

![Screenshot 2024-09-06 174525](https://github.com/user-attachments/assets/8dde86ed-80c5-41f5-a736-61a0a3419b3a)
![Screenshot 2024-09-06 174556](https://github.com/user-attachments/assets/63ad46d3-2b62-4324-8a1b-aaaaab75f617)
![Screenshot 2024-09-06 174613](https://github.com/user-attachments/assets/d7102515-cabb-4279-85a7-6c4dcfda85d9)

## FAQ
#### Are you facing this issue while installing face_recognition then perform the following steps

👇 Check your python version by using the cmd
```bash
  python --version
```
👇 Now according to your python version install the dlib file from the given repository. The dlib file for python 3.12 is provided in this repository<br>
**(eg. If my python version is 3.12 then i will install the file for version 3.12)**
[Install dlib from here](https://github.com/z-mahmud22/Dlib_Windows_Python3.x)

Paste the downloaded **.whl** file in project repository and run the following cmd
```bash 
  pip install <name of your dlib file>
```
Optional (Run this cmd if still facing issues)
```bash 
  pip install cmake
```
Install the **requirements.txt** file again and run **app.py** file
