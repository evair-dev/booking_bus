def show_available_buses(buses):
    print("We have the following buses")

    for bus in buses:
        print(f"{bus['id']}. {bus['name_bus']} ")


def list_id_buses(data, bus_id):
    return [raw for raw in data if raw["id"] == bus_id]


def close_program(option):
    if option == "0" or option.lower() == "exit":
        print("Goodbye buddy")
        exit()
    else:
        return option


def choose_the_bus_to_take(buses):
    bus = close_program(input("Select your bus, write the number: "))
    available_bus = list_id_buses(buses, bus)
    if not available_bus:
        print("Choose the a correct bus.")
        return choose_the_bus_to_take(buses)
    else:
        print(f"You have selected >> {available_bus[0]['name_bus']}")
        return bus
