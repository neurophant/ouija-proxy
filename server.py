import asyncio
import logging

from ouija import Proxy, Telemetry, Tuning

import settings


logging.basicConfig(
    format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG if settings.DEBUG else logging.ERROR,
)


async def main() -> None:
    tuning = Tuning(
        fernet=settings.fernet,
        token=settings.TOKEN,
        serving_timeout=settings.SERVING_TIMEOUT,
        tcp_buffer=settings.TCP_BUFFER,
        tcp_timeout=settings.TCP_TIMEOUT,
        udp_payload=settings.UDP_PAYLOAD,
        udp_timeout=settings.UDP_TIMEOUT,
        udp_retries=settings.UDP_RETRIES,
        udp_capacity=settings.UDP_CAPACITY,
    )
    proxy = Proxy(
        telemetry=Telemetry(),
        tuning=tuning,
        proxy_host=settings.PROXY_HOST,
        proxy_port=settings.PROXY_PORT,
    )

    if settings.MONITOR:
        asyncio.create_task(proxy.debug())

    await proxy.serve()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
