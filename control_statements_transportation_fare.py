# Transport Company Fare Calculation
def calculate_fare(distance):
    if 1 <= distance <= 50:
        fare = distance * 8  # 8 Rs per Km
    elif 51 <= distance <= 100:
        fare = distance * 10  # 10 Rs per Km
    elif distance > 100:
        fare = distance * 12  # 12 Rs per Km
    else:
        print("Invalid distance.")
        return None

    return fare


distance = float(input("Enter the distance (Km): "))
fare = calculate_fare(distance)

if fare is not None:
    print("Total fare: Rs.", fare)
