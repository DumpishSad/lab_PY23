# TODO решите задачу
import json
def task() -> float:
    with open('input.json', 'r') as f:
        data = json.load(f)
    mult = [f['score'] * f['weight'] for f in data]
    return round(sum(mult), 3)

print(task())
