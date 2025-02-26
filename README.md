# YouTube Video Downloader

## About
My Name is **Zaid Alam** | Fullstack Developer

This Python project uses the `pytube` library to download YouTube videos. With this script, you can easily download YouTube videos in the highest quality.

## 📌 Features
- Download videos in the highest resolution.
- Use CLI (Command Line Interface) for downloading.
- Option to save videos in a specific folder.

---

## 🚀 Installation Guide

### **Step 1: Install Python**
This script requires **Python 3.7+** to run.
If Python is not installed, download it from the [official Python website](https://www.python.org/downloads/).

To verify Python installation, run:
```bash
python --version
```

### **Step 2: Clone this Project**
Use the following command to clone this repository from GitHub:
```bash
git clone https://github.com/zaidalam29/youtube-videos-dowloader.git
```
Then, navigate to the project folder:
```bash
cd youtube-videos-dowloader
```

### **Step 3: Install Dependencies**
Run the following command to install the required Python packages:
```bash
pip install -r requirements.txt
```
If you encounter any errors related to `pytube`, update it manually:
```bash
pip install --upgrade pytube
```

---

## 📥 How to Use

### **Download a video using CLI**
Run the following command to download a YouTube video:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID"
```
By default, the video will be saved in the **current folder**.

To save the video in a specific folder:
```bash
python youtube_downloader.py "https://www.youtube.com/watch?v=VIDEO_ID" --path "D:/MyVideos"
```

---

## 🛠 Troubleshooting

### **1️⃣ If `pytube` throws an error**
```bash
pip install --upgrade pytube
```
Or:
```bash
pip uninstall pytube
pip install git+https://github.com/pytube/pytube.git
```

### **2️⃣ If you get `403 Forbidden` error**
Due to YouTube policies, some videos may not be downloadable. To resolve this:
- Use a VPN/Proxy.
- Run the script with `use_oauth=True` and `allow_oauth_cache=True`.

---

## 🤝 Contributing
If you want to improve this project:
1. **Fork** this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'New feature added'`).
4. Push your branch (`git push origin feature-branch`).
5. Submit a **Pull Request**.

---

## 📄 License
This project is licensed under the **MIT License**.

