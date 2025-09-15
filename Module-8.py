# 1.
    # Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out
    # the corresponding airport name and location (town) from the airport database used on this course. The ICAO
    # codes are stored in the ident column of the airport table.


import mysql.connector

def fetch_airport_info(icao_code):
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='airports',
            user='root',
            password='user',
            autocommit=True
        )

        cursor = connection.cursor()
        query = "SELECT name, municipality FROM airport WHERE ident = %s"
        cursor.execute(query, (icao_code,))
        result = cursor.fetchone()

        if result:
            name, municipality = result
            print(f"Airport Name: {name}")
            print(f"Location: {municipality}")
        else:
            print("No airport found with that ICAO code.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    icao_code = input("Enter the ICAO code of the airport: ").strip().upper()
    fetch_airport_info(icao_code)


# 2.
    # Write a program that asks the user to enter the area code (for example FI) and prints out the airports located
    # in that country ordered by airport type.For example, Finland has 65 small airports, 15 helicopter airports and so on.

import mysql.connector

def fetch_airports_by_country(area_code):
    connection = None
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='airports',
            user='root',
            password='user',
            autocommit=True
        )

        cursor = connection.cursor()
        query = """
            SELECT type, COUNT(*)
            FROM airport
            WHERE iso_country = %s
            GROUP BY type
            ORDER BY type
        """
        cursor.execute(query, (area_code,))
        rows = cursor.fetchall()

        if rows:
            print(f"Airports in {area_code}:")
            for airport_type, count in rows:
                print(f"{count} {airport_type}")
        else:
            print("No airports found for that area code.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    area_code = input("Enter the country/area code (e.g., FI): ").strip().upper()
    fetch_airports_by_country(area_code)


# 3.
# Write a program that asks the user to enter the ICAO codes of two airports. The program prints out
# the distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database

import mysql.connector
from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    connection = None
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='airports',  # make sure this is the correct DB
            user='root',
            password='user',
            autocommit=True
        )

        cursor = connection.cursor()
        query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
        cursor.execute(query, (icao_code,))
        result = cursor.fetchone()
        return result  # (latitude, longitude) or None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    icao1 = input("Enter first ICAO code: ").strip().upper()
    icao2 = input("Enter second ICAO code: ").strip().upper()

    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if coords1 and coords2:
        distance_km = geodesic(coords1, coords2).kilometers
        print(f"Distance between {icao1} and {icao2}: {distance_km:.2f} km")
    else:
        print("One or both ICAO codes not found in the database.")








# SORRY BUT DONE THIS MODULE WITH GPT 

























