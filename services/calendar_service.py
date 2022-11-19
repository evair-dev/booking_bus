def available_schedule_by_bus(bus_id, data):
    return [raw for raw in data if raw["bus_id"] == bus_id]



