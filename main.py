import json

from services.booking_service import available_times, select_schedule
from services.calendar_service import available_schedule_by_bus
from services.utils import show_available_buses, choose_the_bus_to_take, close_program


def read_initial_information():
    f = open('initial_data.json')
    data_raw = json.load(f)

    return data_raw


def menu():
    print("1. Booking a bus\n"
          "2. Payments \n"
          "3. Show your payments \n"
          "Write exist or 0 if you want to exit to the program")
    option = input(">>")
    return option


def book_bus():
    data = read_initial_information()
    show_available_buses(data["buses"])
    bus_id = choose_the_bus_to_take(data["buses"])
    schedules = available_schedule_by_bus(bus_id, data["available_schedule"])
    available_times(schedules)
    select_schedule(schedules)


def payments():
    print("estas en payments")
    pass


def show():
    print("estas en payments")
    pass


if __name__ == "__main__":
    print("------ Welcome to Spicy bus ------")

    while True:
        option_selected = "0"
        while option_selected not in ["1", "2", "3"]:
            option_selected = close_program(menu())
        if option_selected == "1":
            book_bus()
        elif option_selected == "2":
            payments()
        else:
            show()
