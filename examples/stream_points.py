import asyncio
import kiyotaka
import kiyotaka.api
import time
import os

from grpclib.client import Channel

async def main():
    metadata = {
        'x-kiyotaka-key': os.getenv('KIYOTAKA_KEY', 'YOUR API KEY'),
    }

    channel = Channel(
        host="grpc.api.kiyotaka.ai",
        port=443,
        ssl=True,
    )
    service = kiyotaka.api.ApiStub(channel)

    from_ = int(time.time()) - 60*60

    data_request = kiyotaka.api.PointRequest(
        type=[kiyotaka.api.PointType.TRADE_AGG],
        exchange=[kiyotaka.api.PointExchange.BINANCE],
        coin=["BTC"],
        interval=kiyotaka.api.PointAggregationInterval.MINUTE,
        from_=from_,
    )

    stream = service.stream_points(data_request, timeout=3600, metadata=metadata)
    async for response in stream:
        print(response.to_json())

    channel.close()

if __name__ == "__main__":
    asyncio.run(main())
