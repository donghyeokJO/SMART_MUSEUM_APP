import asyncio
import uuid
import winrt.windows.devices.bluetooth.advertisement as winBLE
from winrt.windows.storage.streams import DataReader



class BLEGetter:
    def __init__(self):
        self.uuid = ''

    async def discover(self):
        def process_ibeacon(data, beacon_type="iBeacon"):
            beacon_uuid = uuid.UUID(bytes=bytes(data[2:18]))
            major = int.from_bytes(bytearray(data[18:20]), "big", signed=False)

            self.uuid = str(beacon_uuid) + str(major)

        def on_advert(sender, evt):
            for m_data_buf in evt.advertisement.manufacturer_data:
                if m_data_buf.company_id == 0x004C:
                    data_reader = DataReader.from_buffer(m_data_buf.data)
                    m_data = data_reader.read_bytes(m_data_buf.data.length)
                    if m_data[0] == 0x02:
                        uuid = process_ibeacon(m_data)
                        return uuid

        watcher = winBLE.BluetoothLEAdvertisementWatcher()
        watcher.add_received(on_advert)

        watcher.start()
        await asyncio.sleep(3)
        watcher.stop()
