import requests

if __name__ == "__main__":
    base_addr = "http://127.0.0.1:5000/"
    # base_addr = input("Enter base address of the running API: ")
    if not(base_addr.startswith("http://") or base_addr.startswith("https://")):
        base_addr = "http://" + base_addr

    if not base_addr.endswith("/"):
        base_addr = base_addr+"/"

    print("To get add new sensor use POST method on /sensors,\n\
    it returns a message and id of newly created device:")
    print('$ requests.post(base_addr + "sensors", {"address": "Mogilska 43, 31-545 Kraków, Polska", "owner": "Adam Kitel"}).json()')
    print(requests.post(base_addr + "sensors", {"address": "Mogilska 43, 31-545 Kraków, Polska", "owner": "Adam Kitel"}).json())
    print()
    print("Let's add another one:")
    print('$ requests.post(base_addr + "sensors", {"address": "Mogilska 43, 31-545 Kraków, Polska", "owner": "Adam Kitel"}).json()')
    print(requests.post(base_addr + "sensors", {"address": "Kremowa 21, 37-200 Wadowice, Polska", "owner": "Karol Adamczyk"}).json())
    print()


    print("To get all sensors use GET method on /sensors,\n\
    it returns an object of all devices with it's ID's as keys:")
    print('$ requests.get(base_addr + "sensors").json()')
    print(requests.get(base_addr + "sensors").json())

