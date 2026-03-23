# ✋ GestureSense AI

> A real-time AI-powered hand gesture recognition system that enables touchless human-computer interaction using a webcam.

---

## 🚧 Project Status

⚡ This project is **actively under development**.  
We are continuously enhancing:
- Gesture accuracy and robustness  
- Real-time performance  
- AI-based gesture understanding  
- Integration with real-world control systems  

---

## 📌 Problem Statement

Current human-computer interaction methods rely heavily on:

- Keyboard ⌨️  
- Mouse 🖱️  
- Touchscreens 📱  

These methods are:

- Not intuitive in many scenarios  
- Not accessible for all users  
- Not suitable for touchless environments  

There is a growing demand for **natural, contact-free interaction systems**, especially in:

- Healthcare 🏥  
- Smart environments 🏠  
- AR/VR systems 🕶️  
- Assistive technologies ♿  

---

## 💡 Solution

GestureSense AI provides a **real-time hand gesture recognition system** using a webcam.

- Detects hand landmarks using AI  
- Interprets gestures using machine learning  
- Displays results instantly on screen  
- Can be extended to control systems and devices  

It transforms human gestures into **digital commands**.

---

## ⚙️ Features

- 📷 Real-time webcam-based gesture detection  
- ✋ Hand tracking using 21 landmark points  
- 🧠 Machine learning-based gesture classification  
- ⚡ Instant gesture prediction and display  
- 📊 Custom dataset generation pipeline  
- 🔄 Model retraining with new data  
- 🧪 Scalable architecture for advanced AI integration  

---

## 🚀 Advanced Features (In Progress)

- 🖱️ Gesture-based mouse control  
- 🔊 Volume control using hand gestures  
- 🎞️ Presentation (PPT) control  
- 🧏 Sign language recognition (A–Z)  
- 🧠 Dynamic gesture recognition (motion-based)  
- 🤖 Deep learning models (CNN / LSTM)  
- 🌐 Web-based gesture interface  

---

## 🧠 How It Works

1. Capture webcam input  
2. Detect hand using MediaPipe  
3. Extract 21 landmark coordinates  
4. Convert landmarks into feature vector  
5. Predict gesture using ML model  
6. Display result in real-time  


---

## 🛠️ Tech Stack

**Computer Vision**
- OpenCV  

**Hand Tracking**
- MediaPipe  

**Machine Learning**
- Scikit-learn (Random Forest)  

**Data Processing**
- NumPy, Pandas  

---

## 🚀 Installation

▶️ Usage

1. Collect Dataset
python collect_data.py

2. Train Model
python train_model.py

3. Run Gesture Recognition
python predict_gesture.py

Press q to exit.

🎯 Results / Output

Users get:

Real-time gesture recognition
Instant on-screen feedback
Custom gesture prediction
Fast and responsive system

📌 Applications

🖥️ Touchless computer interaction
🧏 Sign language communication
🏥 Hygiene-sensitive environments
🎮 Gaming & AR/VR interaction
🤖 Robotics and automation

⚠️ Limitations

Recognizes only trained gestures
Accuracy depends on dataset quality
Sensitive to lighting and hand position
Currently supports static gestures only

🔮 Future Improvements

🤖 AI-based gesture understanding (deep learning)
📈 Improved accuracy with large datasets
🧾 Full sign language interpreter
📱 Mobile application integration
🌐 Browser-based gesture control
🧠 Personalized gesture models

🚀 Vision

To create a natural, intuitive, and touchless interaction system where humans communicate with machines using gestures alone.

👤 Author

Shashank Chetty
GitHub: https://github.com/shashankchetty2005-code