from threading import Thread
from gattlib import BeaconService

data = None

def start(beacondata):
    try:
        global data
        
        service = BeaconService(beacondata['device_id'])

        thread = Thread(target = service.start_advertising, args = (beacondata['uuid'], beacondata['major'], beacondata['minor'], beacondata['tx_power'], beacondata['interval']))
        thread.start()

        data = {
            "service": service,
            "thread": thread
        }        

        return True
    except Exception as e:
        print(e)
        return False

def stop(devicename):
    if data is not None:
        data['service'].stop_advertising()
        data['thread'].join(timeout=6)

        return not(data['thread'].is_alive())

    else:
        # look to make sure it's not already running

        try:
            service = BeaconService(devicename)
            service.stop_advertising()
        except:
            pass
            
        return True
    
def is_running():
    return data is not None
