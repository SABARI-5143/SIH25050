# 🚦 Smart Traffic Vehicle Detection & Signal Control

This project uses **YOLOv8**, **OpenCV**, and **Arduino** to automatically control traffic signals based on **real-time vehicle count**.

---
## 📂 Project Structure
yolo_model/          # YOLOv8 trained model and detection code  
arduino/             # Arduino sketch for traffic signal control  
frontend/            # HTML, CSS, JavaScript files for dashboard  
opencv_scripts/      # Additional OpenCV utilities  
README.md            # This file  

---

## ⚡ Features
- 🚗 Real-time vehicle detection with **YOLOv8**
- 🔄 Dynamic traffic light timing based on vehicle density
- 🛠 Arduino controlled physical signal lights
- 🌐 Frontend dashboard to monitor live traffic status

---

## 🛠 Tech Stack
- **Python 3.12+**
- [YOLOv8 (Ultralytics)](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- **Arduino UNO / Mega**
- **HTML, CSS, JavaScript**

---

## ⚙️ How to Run

### 1️⃣ Clone the Repository
git clone https://github.com/SABARI-5143/SIH25050.git  
cd SIH25050  

### 2️⃣ Install Python Dependencies
pip install ultralytics opencv-python  

### 3️⃣ Run the Detection Script
- **Colab:** open `vehicle_detection.ipynb` and run all cells  
- **Local Python:**  
python vehicle_detection.py  

---

## 🧩 Arduino Setup
1. Open `traffic_signal.ino` in Arduino IDE  
2. Connect Arduino board and upload the code  
3. Attach LEDs or actual signal hardware as per pin configuration

---

## 🌐 Frontend
Open `frontend/index.html` in a browser to view the live dashboard.

---

## 📊 Example Output
🚦 Total vehicles detected: 35  
✅ Counts by type: {'car': 20, 'bus': 3, 'truck': 2, 'motorbike': 10}

---

## 🚀 Future Improvements
- Real-time camera feed integration
- IoT sensor support for accurate counting
- Web app deployment of dashboard

---

## 🤝 Contributing
Pull requests are welcome.  
For major changes, open an issue first to discuss what you would like to change.

---

## 📝 License
Licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

### 👨‍💻 Author
**Sabari** – [GitHub](https://github.com/SABARI-5143)
