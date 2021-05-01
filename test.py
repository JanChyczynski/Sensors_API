import requests

if __name__ == "__main__":
    # base_addr = "http://127.0.0.1:5000/"
    base_addr = input("Enter base address of the running API: ")
    if not(base_addr.startswith("http://") or base_addr.startswith("https://")):
        base_addr = "http://" + base_addr

    if not base_addr.endswith("/"):
        base_addr = base_addr+"/"

    print('To get add new sensor use POST method on /sensors,\n\
    it takes the new object as an argument, i.e: {"address": <address>, "owner": <owner>}\n\
    it returns a message and id of newly created device:')
    print('$ requests.post(base_addr + "sensors", {"address": "Mogilska 43, 31-545 Kraków, Polska", "owner": "Adam Kitel"}).json()')
    print(requests.post(base_addr + "sensors", {"address": "Mogilska 43, 31-545 Kraków, Polska", "owner": "Adam Kitel"}).json())
    print()
    print("Let's add another one:")
    print('$ requests.post(base_addr + "sensors", {"address": "Kremowa 21, 37-200 Wadowice, Polska", "owner": "Karol Adamczyk"}).json()')
    print(requests.post(base_addr + "sensors", {"address": "Kremowa 21, 37-200 Wadowice, Polska", "owner": "Karol Adamczyk"}).json())
    print()

    print("To get all sensors use GET method on /sensors,\n\
    it returns an object of all devices with it's ID's as keys:")
    print('$ requests.get(base_addr + "sensors").json()')
    print(requests.get(base_addr + "sensors").json())
    print()

    print("To get the sensor with given ID use GET method on /sensors/<int:ID>,\n\
    it returns an object representing single device:")
    print('$ requests.get(base_addr + "sensor/1").json()')
    print(requests.get(base_addr + "sensor/1").json())
    print()

    print('To uptdate the sensor with given ID use PATCH method on /sensors/<int:ID>\n\
    it takes an object with specified changes as an argument, i.e: {"address": <address>, "owner": <owner>}:\n\
    not every field is required so one property at a time, or both can be updated:')
    print('$ requests.patch(base_addr + "sensor/0", {"address": "Nowa 20, 33-333 Wrocław, Polska"}).json()')
    print(requests.patch(base_addr + "sensor/0", {"address": "Nowa 20, 33-333 Wrocław, Polska"}))
    print('$ requests.patch(base_addr + "sensor/0", {"owner": "Jan Nowacki"})')
    print(requests.patch(base_addr + "sensor/0", {"owner": "Jan Nowacki"}))
    print('$ requests.patch(base_addr + "sensor/1", {"address": "Zmienna 65, 11-123 Ełk, Polska", "owner": "Lech Zmieniony"})')
    print(requests.patch(base_addr + "sensor/1", {"address": "Zmienna 65, 11-123 Ełk, Polska", "owner": "Lech Zmieniony"}))
    print()

    print('We can see all the changes using GET on /sensors')
    print('$ requests.get(base_addr + "sensors").json()')
    print(requests.get(base_addr + "sensors").json())
    print()

    print("To delete sensor with given ID use DELETE method on /sensors/<int:ID>,\n\
        it returns Response [204] if there was an object with given ID:")
    print('$ requests.delete(base_addr + "sensor/1")')
    print(requests.delete(base_addr + "sensor/1"))
    print("\tor it returns a message if there was no object with given ID:")
    print('$ requests.delete(base_addr + "sensor/6").json()')
    print(requests.delete(base_addr + "sensor/6").json())
    print()

    print("We can see the sensor with ID=1 was deleted using GET on /sensors")
    print('$ requests.get(base_addr + "sensors").json()')
    print(requests.get(base_addr + "sensors").json())
    print()

