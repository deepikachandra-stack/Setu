import json

def load_processes():
    with open("data/processes.json", "r", encoding="utf-8") as file:
        return json.load(file)

def get_process(service):
    processes = load_processes()
    service = service.lower().strip()

    if service in processes:
        return processes[service]

    for process in processes.values():
        if process["name"].lower() == service:
            return process

    return None