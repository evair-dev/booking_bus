from datetime import datetime


def list_id_schedules(data, schedule_id):
    return [raw for raw in data if raw["id"] == schedule_id]


def select_schedule(schedules):
    schedule_id = input("introduce the number: ")
    available_schedule = list_id_schedules(schedules, schedule_id)
    if not available_schedule:
        print("Select a valid id")
        return select_schedule(schedules)
    else:
        timer_split = str(available_schedule[0]["departure_time"]).split()
        print(f"You have select: \n"
              f"date: {timer_split[0]} \ntime: {timer_split[1]}")


def available_times(schedules):
    print("The available schedules: ")
    for time in schedules:
        timer = datetime.strptime(time["departure_time"], '%m/%d/%y %H:%M:%S')
        timer_split = str(timer).split()
        print(f"{time['id']}. date: {timer_split[0]} time: {timer_split[1]}")
