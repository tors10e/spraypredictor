import asyncio
import logging

from aiohttp import ClientSession

from aioambient import API
from aioambient.errors import AmbientError

_LOGGER = logging.getLogger()

API_KEY = "d258562dd92147d4acef831cc71e3a78f56dea831da34b13b3bcc05116d74787"
APP_KEY = "0432267ea11749afb0d6dad49abdab9c883e9587b12b4000bd184ebf09403212"
terra_station_address = "30:83:98:A6:A6:49"

async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=logging.INFO)
    async with ClientSession() as session:
        try:
            api = API(APP_KEY, API_KEY, session=session)

            devices = await api.get_devices()
            _LOGGER.info("Devices: %s", devices)

            for device in devices:
                details = await api.get_device_details(device["macAddress"])
                _LOGGER.info("Device Details (%s): %s", device["macAddress"], details)

        except AmbientError as err:
            _LOGGER.error("There was an error: %s", err)


asyncio.run(main())