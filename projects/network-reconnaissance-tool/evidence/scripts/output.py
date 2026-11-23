import json

def save_deterministic_json(data: dict, filepath: str) -> None:
    # Sort results by IP address for deterministic output
    if "results" in data:
        data["results"] = sorted(data["results"], key=lambda x: x["ip"])
        
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)