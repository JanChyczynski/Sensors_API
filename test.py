import requests

if __name__ == "__main__":
    # BASE = "http://127.0.0.1:5000/"
    base_addr = input("Enter base address of the running API: ")
    if not(base_addr.startswith("http://") or base_addr.startswith("https://")):
        base_addr = "http://" + base_addr

    if not base_addr.endswith("/"):
        base_addr = base_addr+"/"

    print("To get all sensors use GET method on /sensors:")
    print('$ requests.get(base_addr + "sensors").json()')
    print(requests.get(base_addr + "sensors").json())

