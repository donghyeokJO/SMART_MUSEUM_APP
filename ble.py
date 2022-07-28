import asyncio
import uuid
import winrt.windows.devices.bluetooth.advertisement as winBLE
from winrt.windows.storage.streams import DataReader


async def discover():
    def process_ibeacon(data, beacon_type="iBeacon"):
        beacon_uuid = uuid.UUID(bytes=bytes(data[2:18]))
        major = int.from_bytes(bytearray(data[18:20]), "big", signed=False)
        minor = int.from_bytes(bytearray(data[20:22]), "big", signed=False)
        tx_pwr = int.from_bytes([data[22]], "big", signed=True)
        print(
            f"\t\t{beacon_type}: {beacon_uuid} - {major} " f"- {minor} \u2197 {tx_pwr}"
        )

    def on_advert(sender, evt):
        for m_data_buf in evt.advertisement.manufacturer_data:
            if m_data_buf.company_id == 0x004C:
                data_reader = DataReader.from_buffer(m_data_buf.data)
                m_data = data_reader.read_bytes(m_data_buf.data.length)
                if m_data[0] == 0x02:
                    process_ibeacon(m_data)
            elif m_data_buf.company_id == 0xFFFF:
                data_reader = DataReader.from_buffer(m_data_buf.data)
                m_data = data_reader.read_bytes(m_data_buf.data.length)
                if m_data[0:2] == [0xBE, 0xAC]:
                    process_ibeacon(m_data, "AltBeacon")

    watcher = winBLE.BluetoothLEAdvertisementWatcher()
    watcher.add_received(on_advert)

    watcher.start()
    await asyncio.sleep(25)
    watcher.stop()


asyncio.run(discover())
