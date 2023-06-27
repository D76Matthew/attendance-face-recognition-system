# attendance-face-recognition-system
A simple Attendance Face Recognition system using Python

Data can be cast using streamlit_app.py and kept by csv_msql_attendance.py

## Library

you could install it in Python using the `pip` command

### cv2
`pip install opencv-python`

### face_recognition
`pip install face-recognition`

### numoy
`pip install numpy`

### pandas
`pip install pandas`

### mysql.connector
`pip install mysql-connector-python`

### streamlit
`pip install streamlit`

### streamlit-autorefresh
`pip install streamlit-autorefresh`

## Codes, csv, and folders

the code consists of:

- locate_face: locate face from the image
- testing-face-recog: testing face name from image files name
- attendances-system-0.5: testing face recognition with images from folder images
- attendance-system: implement face recognition for attendance which recorded in csv files
- csv_mysql_attendance: simple code to send csv data to SQL 
- streamlit_app: simple code to send csv data to cast to the website via streamlit

csv:

- Attendance.csv
- Attendance-inout.csv: updated csv file which add check-in and check-out

Folders:

- Images: images of people you want to use for face recognition
- face_recognition_models-master: master models for face recognition

## Future Update

- make into android apk 
- Automated update csv to SQL data
- Connect with microcontrollers (ESP32)

## Important info

to make into .exe use command

`pip install pyinstaller`

`pyinstaller --onefile --windowed --collect-data=face_recognition_models myscript.py`

change myscript.py to script name



