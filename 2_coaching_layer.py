# A simple rule-based coaching layer. No external AI API is called.

COACHING_TEMPLATES = {
    (True, True, True): ("Strong inputs and a strong result.", "Keep the routine consistent."),
    (True, True, False): ("The goal was reached, but hydration was low.", "Pay attention to hydration tomorrow."),
    (True, False, True): ("The goal was reached despite limited sleep.", "Prioritize recovery tonight."),
    (True, False, False): ("The goal was reached with both inputs below target.", "Build a more sustainable routine."),
    (False, True, True): ("Sleep and hydration were solid, but the goal was missed.", "Review schedule and activity load."),
    (False, True, False): ("Sleep was adequate, but hydration was below target.", "Plan regular water breaks."),
    (False, False, True): ("Sleep was below target while hydration was adequate.", "Consider an earlier bedtime."),
    (False, False, False): ("Both sleep and hydration were below target.", "Work on one manageable improvement at a time."),
}


def get_coaching_message(sleep_hours, water_glasses, hit_goal):
    key = (bool(hit_goal), sleep_hours >= 7.0, water_glasses >= 8)
    first, second = COACHING_TEMPLATES[key]
    return f"{first} {second}"


if __name__ == "__main__":
    examples = [(8.0, 10, True), (5.5, 4, False), (7.5, 6, True)]
    for sleep, water, hit in examples:
        result = "HIT GOAL" if hit else "MISS GOAL"
        print(f"[{result}] Sleep: {sleep}h | Water: {water} glasses")
        print(get_coaching_message(sleep, water, hit))
        print("-" * 50)
