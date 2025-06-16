# 🔺 Triangle Congruence Visualizer

An educational web app built with Python and Flask to help students visually explore triangle congruence (SSS, SAS, ASA, and more) using coordinate geometry. Designed for interactive learning and ideal for math classrooms or self-study.
This is a Flask-based educational web app that dynamically visualizes step-by-step triangle congruence proofs (SSS, SAS, ASA, etc.) using coordinate geometry. It’s designed for students, educators, and enthusiasts who want to understand triangle congruence through plotted diagrams and coordinate-based logic.

## 🚀 Live Demo

[![Live Demo](https://img.shields.io/badge/Live_App-Click_Here-green)](https://jagdevsinghdosanjh.pythonanywhere.com)

> _Hosted on [PythonAnywhere](https://www.pythonanywhere.com)_  
> _**Creator:** Jagdev Singh Dosanjh
https://www.dosanjhpubsasr.org

https://www.physicsbyjsd.org

---
## ✨ Features

- 📐 Step-by-step generation of triangle congruence visuals
- 🧮 Built-in use of distance & slope formulas for SSS/SAS/ASA
- 📊 Generated `.png` diagrams rendered in-browser via Flask
- 📁 Auto-save diagrams in `/static` for reuse or printing
- 🧠 Designed for secondary-level geometry learners
    - Visual demonstration of triangle congruence on a coordinate plane
    - Generates `.png` plots using Matplotlib
    - Images rendered dynamically and served via Flask
    - Fully compatible with [PythonAnywhere](https://www.pythonanywhere.com)
    - Easily extendable for slope, distance, and reflection activities
---

## 🏗️ Project Structure

triangle_app/ │ ├── app.py # Main Flask application with diagram generator ├── static/ # Stores generated images like step_1.png │ └── step_1.png ├── templates/ │ └── index.html # Displays all steps visually └── README.md

## 🚀 Getting Started

1. **Clone the repository or upload files:**

   ```bash
   git clone https://github.com/yourusername/triangle-congruence-visualizer.git
   cd triangle-congruence-visualizer
## 🚀 Install Requirements
pip install flask matplotlib
## 🚀 Run the APP Locally
flask run 
and
Open
 http://localhost:5000 
 in your browser.

## Deployment on PythonAnywhere
Upload the project via the Files tab

Ensure app.py is your Flask entry point

Place generated images inside /static/

Reload from the Web tab and enjoy!

## Educational Use
Perfect for:

Demonstrating triangle congruence rules in Class 9 math

Helping students visualize slope and distance relationships

Creating math content with a geometric and programming twist

📌 To Do
Add dropdown to switch between SSS / SAS / ASA modes

Include distance and slope labels on diagrams

Option to export visuals into a printable PDF worksheet

📸 Sample Screenshot

👨‍🏫 Created By
Jagdev Singh Dosanjh Dedicated educator bridging geometry and real-world computing using Python + Flask.

Let me know if you'd like to tailor this README for GitHub Pages, add licensing information, or even embed a live app demo badge. Onward to geometry greatness! 🔷📐🌐  
