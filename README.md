🏋️ SMP Performance Coach

A Python-based machine learning project that combines a Random Forest classifier with a rule-based coaching system to analyse sample fitness data and generate coaching feedback.

The project demonstrates how machine learning predictions can be combined with simple Python logic to produce readable reports.

🚀 What the Project Does

The application:

Accepts sample fitness inputs, including sleep, water intake and bench-press data.

Uses a Random Forest classifier to predict an illustrative daily step-goal outcome.

Generates rule-based coaching messages.

Processes multiple sample records.

Produces individual reports and a final summary.

🛠️ Technologies Used

Python

NumPy

Scikit-learn

Random Forest Classification

Rule-based logic

📁 Project Structure

File

Purpose

1_train_classifier.py

Trains and evaluates the classifier

2_coaching_layer.py

Creates rule-based coaching messages

3_classifier_+_coaching_in_one_function.py

Combines prediction and coaching

4_full_smp_Performance_coach_application.py

Runs the complete sample application

⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/DanOdhiambo5/SMP-PERFORMANCE-COACH.git
```

2. Enter the project folder

```bash
cd SMP-PERFORMANCE-COACH
```

3. Create a virtual environment

```bash
python -m venv .venv
```

4. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

▶️ Run the Application

```bash
python "4_full_smp_Performance_coach_application.py"
```

🎯 Learning Objectives

This project demonstrates practical understanding of:

Python data handling

NumPy arrays

Machine learning fundamentals

Training and testing a classifier

Rule-based decision making

Functions and application structure

Processing multiple records and generating reports

⚠️ Project Limitations

This is an educational prototype. Its 28-row dataset and labels are synthetic and illustrative.

The model has not been validated for real-world fitness, health or medical decisions. Its predictions should not be treated as professional advice or evidence of actual performance.

👨‍💻 Author

Dan58

Learning Python, machine learning and software development through practical projects.
