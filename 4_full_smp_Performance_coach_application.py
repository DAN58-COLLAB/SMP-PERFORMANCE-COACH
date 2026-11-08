import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Synthetic example records: sleep hours, water glasses, bench press (kg).
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

COACHING = {
    (True, True, True): ("Strong inputs and a strong result.", "Keep the routine consistent."),
    (True, True, False): ("Goal reached, but hydration was low.", "Pay attention to hydration tomorrow."),
    (True, False, True): ("Goal reached despite limited sleep.", "Prioritize recovery tonight."),
    (True, False, False): ("Goal reached with both inputs below target.", "Build a sustainable routine."),
    (False, True, True): ("Sleep and hydration were solid, but the goal was missed.", "Review schedule and activity load."),
    (False, True, False): ("Sleep was adequate, but hydration was low.", "Plan regular water breaks."),
    (False, False, True): ("Sleep was below target while hydration was adequate.", "Consider an earlier bedtime."),
    (False, False, False): ("Both sleep and hydration were below target.", "Work on one manageable improvement."),
}


def analyze_day(sleep_hr, water_glasses, bench_kg, day_label="Day"):
    features = np.array([[sleep_hr, water_glasses, bench_kg]])
    prediction = int(model.predict(features)[0])
    confidence = float(model.predict_proba(features)[0][prediction])
    first, second = COACHING[(bool(prediction), sleep_hr >= 7, water_glasses >= 8)]
    return {
        "label": day_label,
        "sleep_hr": sleep_hr,
        "water_glasses": water_glasses,
        "bench_kg": bench_kg,
        "hit_goal": bool(prediction),
        "confidence": confidence,
        "coaching": f"{first} {second}",
    }


if __name__ == "__main__":
    incoming_days = [
        ("Day 29", 8.0, 10, 92),
        ("Day 30", 5.5, 4, 70),
        ("Day 31", 7.2, 7, 84),
        ("Day 32", 8.5, 11, 95),
        ("Day 33", 6.1, 5, 76),
    ]
    results = [analyze_day(sleep, water, bench, label)
               for label, sleep, water, bench in incoming_days]

    print("=" * 62)
    print("SMP PERFORMANCE COACH | DAILY REPORTS")
    print("=" * 62)
    for item in results:
        outcome = "HIT GOAL" if item["hit_goal"] else "MISS GOAL"
        print(f"\n{item['label']}: {outcome} ({item['confidence']:.0%} model probability)")
        print(f"Sleep: {item['sleep_hr']}h | Water: {item['water_glasses']} glasses | Bench: {item['bench_kg']}kg")
        print(f"Coach: {item['coaching']}")

    hits = sum(item["hit_goal"] for item in results)
    print(f"\nSummary: {hits}/{len(results)} sample days predicted to hit the goal.")
