
🎨 Air Canvas – Virtual Drawing Using Hand Gestures

Air Canvas is a computer vision–based virtual drawing application that allows users to draw on a digital canvas without touching any physical surface.
Using hand gesture recognition, the system tracks finger movements in real time and renders drawings directly on the screen.

This project demonstrates the practical application of OpenCV, MediaPipe, and real-time gesture tracking in Human–Computer Interaction (HCI).

---

🚀 Features

✋ Real-time hand and finger tracking

🖌️ Draw in the air using finger movements

🎨 Multiple drawing colors

🧼 Clear canvas using gesture/action

📷 Works with standard webcam

⚡ Low-latency real-time performance

---

🛠️ Technologies Used

Python

OpenCV – video capture & drawing

MediaPipe – hand landmark detection

NumPy – array and coordinate handling

Webcam – real-time input device

---

📂 Project Structure

air-canvas-main/
│
├── air_canvas.py          # Main application file
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignored files & folders
└── assets/                # (Optional) screenshots / demo images
---

⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Deepika-shree/Air-Canvas.git
cd air-canvas-main

2️⃣ Create a Virtual Environment

python -m venv .venv

Activate it:

Windows
.venv\Scripts\activate

Linux / macOS
source .venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt
---

▶️ How to Run

python air_canvas.py

Ensure your webcam is connected and accessible.
---

🧠 How It Works

1. Webcam captures live video frames


2. MediaPipe detects hand landmarks


3. Index finger tip position is tracked


4. Finger movement is mapped to drawing strokes


5. OpenCV renders the strokes on a virtual canvas

---

📌 Use Cases

Touchless drawing applications

Interactive smart boards

Gesture-based user interfaces

AR/VR interaction prototypes

Educational demonstrations
---

🧪 Future Enhancements

Save drawings as image files

Gesture-based color selection

Multi-hand support

Shape recognition

GUI controls for tools
---

👩‍💻 Author

Deepika Shree
Computer Science & Engineering
GitHub: Deepika-shree
---

⭐ Acknowledgements

Google MediaPipe

OpenCV community

Python open-source ecosystem
---

📜 License

This project is for educational and learning purposes.
---
