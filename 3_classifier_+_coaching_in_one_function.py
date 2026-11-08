import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.array([
    [6.5, 6, 80], [7.2, 8, 85], [5.8, 5, 75], [8.0, 10, 90],
    [7.5, 9, 88], [6.0, 6, 78], [7.8, 8, 86], [8.2, 10, 92],
    [5.5, 4, 70], [7.0, 7, 82], [6.8, 8, 84], [8.5, 11, 95],
    [7.3, 9, 89], [6.2, 6, 76], [7.9, 10, 91], [5.9, 5, 73],
    [8.1, 11, 93], [7.4, 8, 87], [6.7, 7, 83], [8.3, 10, 94],
    [5.6, 4, 71], [7.1, 8, 85], [8.0, 9, 90], [6.4, 6, 77],
    [7.6, 9, 88], [8.4, 11, 96], [6.3, 7, 79], [7.7, 10, 91],
])
y = np.array([0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1])

X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

TEMPLATES = {
    (True, True, True): "Strong inputs and a strong result. Keep the routine consistent.",
    (True, True, False): "Goal reached, but hydration was low. Pay attention to hydration tomorrow.",
    (True, False, True): "Goal reached despite limited sleep. Prioritize recovery tonight.",
    (True, False, False): "Goal reached with both inputs below target. Build a sustainable routine.",
    (False, True, True): "Sleep and hydration were solid, but the goal was missed. Review schedule and load.",
    (False, True, False): "Sleep was adequate, but hydration was low. Plan regular water breaks.",
    (False, False, True): "Sleep was below target. Consider an earlier bedtime.",
    (False, False, False): "Both inputs were below target. Work on one manageable improvement.",
}


def analyze_day(sleep_hr, water_glasses, bench_kg):
    features = np.array([[sleep_hr, water_glasses, bench_kg]])
    prediction = int(model.predict(features)[0])
    probabilities = model.predict_proba(features)[0]
    return {
        "hit_goal": bool(prediction),
        "confidence": float(probabilities[prediction]),
        "coaching": TEMPLATES[(bool(prediction), sleep_hr >= 7, water_glasses >= 8)],
    }


if __name__ == "__main__":
    for sample in [(8.0, 10, 92), (5.5, 4, 70), (7.2, 7, 84)]:
        print(analyze_day(*sample))
