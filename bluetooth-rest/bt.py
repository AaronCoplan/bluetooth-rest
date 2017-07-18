import bluetooth

def simple_scan():
    return bluetooth.discover_devices()

def is_device_present(btaddr, timeout):
    if(not bluetooth.is_valid_address(btaddr)):
        return False

    name = bluetooth.lookup_name(btaddr, timeout)
    if(name is None):
        return False
    else:
        return True
