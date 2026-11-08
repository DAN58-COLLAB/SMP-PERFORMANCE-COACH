# SMP Performance Coach

A command-line learning prototype that combines a Random Forest classifier with rule-based coaching messages. It uses sleep, water and bench-press inputs to predict an illustrative daily step-goal outcome and produce a batch report.

## Project files
- `1_train_classifier.py` — trains and evaluates a small classifier.
- `2_coaching_layer.py` — demonstrates rule-based coaching templates.
- `3_classifier_+_coaching_in_one_function.py` — combines prediction and coaching.
- `4_full_smp_Performance_coach_application.py` — runs a batch of sample days and prints individual and summary reports.

## Requirements
Python 3.9+, NumPy and scikit-learn.

## Run

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python "4_full_smp_Performance_coach_application.py"
```

## Learning objectives
- Prepare feature arrays and labels
- Split sample data into training and test sets
- Train a Random Forest classifier
- Combine model output with readable rule-based feedback
- Process multiple records and summarize results

## Important limitations
The 28-row dataset and labels are synthetic and illustrative. The model is not validated for health, fitness or medical decisions. Its probability output is not evidence of real-world accuracy. Coaching messages are fixed templates, not individualized professional advice.
