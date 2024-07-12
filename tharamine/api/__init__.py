# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: api/api.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    AsyncIterator,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from .. import (
    Trade as _Trade__,
    TradeAggregation as _TradeAggregation__,
    TradeSideAgnosticAggregation as _TradeSideAgnosticAggregation__,
)


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class PointType(betterproto.Enum):
    """Enum representing different types of data points"""

    UNKNOWN_TYPE = 0
    """Default unknown type"""

    TRADE = 1
    """Raw trade data"""

    TRADE_AGG = 9
    """Aggregated trade data"""

    TRADE_SIDE_AGNOSTIC_AGG = 107
    """Aggregated trade data, but without grouping by side"""


class PointSide(betterproto.Enum):
    """Enum representing trade sides"""

    UNKNOWN_SIDE = 0
    """Default unknown side"""

    SELL = 1
    """Sell side"""

    BUY = 2
    """Buy side"""


class PointExchange(betterproto.Enum):
    """Enum representing different exchanges"""

    UNKNOWN_EXCHANGE = 0
    BITMEX = 1
    DERIBIT = 2
    BINANCE_FUTURES = 3
    BINANCE_DELIVERY = 4
    BINANCE = 6
    FTX = 7
    OKEX_FUTURES = 8
    OKEX_OPTIONS = 9
    OKEX_SWAP = 10
    OKEX = 11
    BITFINEX_DERIVATIVES = 16
    BITFINEX = 17
    COINBASE = 18
    CRYPTOFACILITIES = 19
    KRAKEN = 20
    BITSTAMP = 21
    GEMINI = 22
    BYBIT = 24
    BYBIT_SPOT = 60
    NYSE_AMERICAN = 61
    NASDAQ_BX = 62
    NYSE_NATIONAL = 63
    FINRA = 64
    CBOE_EDGA = 67
    CBOE_EDGX = 68
    NYSE_CHICAGO = 69
    NYSE = 70
    NYSE_ARCA = 71
    NASDAQ = 72
    LTSE = 74
    IEX = 75
    NASDAQ_PHILADELPHIA = 77
    CBOE_BYX = 78
    CBOE_BZX = 79
    MIAX_PEARL = 80
    MEMBERS_EXCHANGE = 81
    OTC_EQUITY_SECURITY = 82


class PointCategory(betterproto.Enum):
    """Enum representing different categories of financial instruments"""

    UNKNOWN_CATEGORY = 0
    """Default unknown category"""

    SPOT = 1
    """Spot trading"""

    PERPETUAL = 2
    """Perpetual contracts"""

    FUTURE = 3
    """Future contracts"""

    OPTION = 4
    """Option contracts"""

    COMBO = 5
    """Combination of multiple instrument types"""


class PointAggregationInterval(betterproto.Enum):
    UNKNOWN_AGGREGATION_INTERVAL = 0
    """Default unknown interval"""

    MINUTE = 2
    """One-minute interval"""

    FIVE_MINUTES = 3
    """Five-minute interval"""

    FIFTEEN_MINUTES = 4
    """Fifteen-minute interval"""

    HOUR = 5
    """One-hour interval"""

    FOUR_HOURS = 6
    """Four-hour interval"""

    DAY = 7
    """One-day interval"""

    WEEK = 8
    """One-week interval"""


@dataclass(eq=False, repr=False)
class PointMetaRequest(betterproto.Message):
    type: List["PointType"] = betterproto.enum_field(1)
    """List of data types to filter by"""

    exchange: List["PointExchange"] = betterproto.enum_field(2)
    """List of exchanges to filter by"""

    category: List["PointCategory"] = betterproto.enum_field(3)
    """List of categories to filter by (not applicable to all data types)"""

    coin: List[str] = betterproto.string_field(4)
    """List of coins to filter by"""

    raw_symbol: List[str] = betterproto.string_field(5)
    """List of raw symbols to filter by"""

    from_: int = betterproto.int64_field(6)
    """Start timestamp for data retrieval"""

    to: int = betterproto.int64_field(7)
    """End timestamp for data retrieval"""


@dataclass(eq=False, repr=False)
class PointResponse(betterproto.Message):
    """Response containing series of data points"""

    series: List["PointSeries"] = betterproto.message_field(1)
    """List of point series matching the request criteria"""


@dataclass(eq=False, repr=False)
class PointMetaResponse(betterproto.Message):
    types: List["PointType"] = betterproto.enum_field(1)
    """List of available data types"""

    exchanges: List["PointExchange"] = betterproto.enum_field(2)
    """List of available exchanges"""

    categories: List["PointCategory"] = betterproto.enum_field(3)
    """List of available categories"""

    coins: List[str] = betterproto.string_field(4)
    """List of available coins"""

    raw_symbols: List[str] = betterproto.string_field(6)
    """List of available raw symbols"""


@dataclass(eq=False, repr=False)
class PointRequest(betterproto.Message):
    type: List["PointType"] = betterproto.enum_field(1)
    """List of data types to retrieve"""

    exchange: List["PointExchange"] = betterproto.enum_field(2)
    """List of exchanges to retrieve data from"""

    normalized_symbol: List[str] = betterproto.string_field(3)
    """List of normalized symbols to retrieve"""

    coin: List[str] = betterproto.string_field(4)
    """List of coins to retrieve data for"""

    category: List["PointCategory"] = betterproto.enum_field(5)
    """List of categories to retrieve"""

    raw_symbol: List[str] = betterproto.string_field(6)
    """List of raw symbols to retrieve"""

    side: "PointSide" = betterproto.enum_field(8)
    """Trade side to filter by"""

    interval: "PointAggregationInterval" = betterproto.enum_field(12)
    """Aggregation interval for the data points"""

    from_: int = betterproto.int64_field(14)
    """Start timestamp for data retrieval"""

    period: int = betterproto.int64_field(15)
    """Duration in seconds for data retrieval"""


@dataclass(eq=False, repr=False)
class PointSeriesIdentifier(betterproto.Message):
    type: "PointType" = betterproto.enum_field(2)
    """Type of data point"""

    raw_symbol: str = betterproto.string_field(3)
    """Raw symbol identifier"""

    exchange: "PointExchange" = betterproto.enum_field(4)
    """Exchange where the data originates"""

    normalized_symbol: str = betterproto.string_field(6)
    """Normalized symbol identifier"""

    category: "PointCategory" = betterproto.enum_field(7)
    """Category of the data point"""

    interval: "PointAggregationInterval" = betterproto.enum_field(8)
    """Aggregation interval of the data series"""

    side: "PointSide" = betterproto.enum_field(11)
    """Trade side (buy/sell)"""

    coin: str = betterproto.string_field(20)
    """Coin identifier"""


@dataclass(eq=False, repr=False)
class Point(betterproto.Message):
    """Represents a single data point"""

    id: Optional["PointSeriesIdentifier"] = betterproto.message_field(
        1, optional=True, group="_id"
    )
    """Identifier for the point series"""

    trade: "_Trade__" = betterproto.message_field(7, group="point")
    """Raw trade data"""

    trade_aggregation: "_TradeAggregation__" = betterproto.message_field(
        15, group="point"
    )
    """Aggregated trade data"""

    trade_side_agnostic_aggregation: "_TradeSideAgnosticAggregation__" = (
        betterproto.message_field(108, group="point")
    )
    """Aggregated trade data, but without grouping by side"""


@dataclass(eq=False, repr=False)
class PointSeries(betterproto.Message):
    """Represents a series of data points"""

    id: "PointSeriesIdentifier" = betterproto.message_field(2)
    """Identifier for the point series"""

    points: List["Point"] = betterproto.message_field(3)
    """List of data points in the series"""


class ApiStub(betterproto.ServiceStub):
    async def get_points(
        self,
        point_request: "PointRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "PointResponse":
        return await self._unary_unary(
            "/api.API/GetPoints",
            point_request,
            PointResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def stream_points(
        self,
        point_request: "PointRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["PointSeries"]:
        async for response in self._unary_stream(
            "/api.API/StreamPoints",
            point_request,
            PointSeries,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def get_types(
        self,
        point_meta_request: "PointMetaRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "PointMetaResponse":
        return await self._unary_unary(
            "/api.API/GetTypes",
            point_meta_request,
            PointMetaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_exchanges(
        self,
        point_meta_request: "PointMetaRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "PointMetaResponse":
        return await self._unary_unary(
            "/api.API/GetExchanges",
            point_meta_request,
            PointMetaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_categories(
        self,
        point_meta_request: "PointMetaRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "PointMetaResponse":
        return await self._unary_unary(
            "/api.API/GetCategories",
            point_meta_request,
            PointMetaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_coins(
        self,
        point_meta_request: "PointMetaRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "PointMetaResponse":
        return await self._unary_unary(
            "/api.API/GetCoins",
            point_meta_request,
            PointMetaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_raw_symbols(
        self,
        point_meta_request: "PointMetaRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "PointMetaResponse":
        return await self._unary_unary(
            "/api.API/GetRawSymbols",
            point_meta_request,
            PointMetaResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class ApiBase(ServiceBase):

    async def get_points(self, point_request: "PointRequest") -> "PointResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def stream_points(
        self, point_request: "PointRequest"
    ) -> AsyncIterator["PointSeries"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)
        yield PointSeries()

    async def get_types(
        self, point_meta_request: "PointMetaRequest"
    ) -> "PointMetaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_exchanges(
        self, point_meta_request: "PointMetaRequest"
    ) -> "PointMetaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_categories(
        self, point_meta_request: "PointMetaRequest"
    ) -> "PointMetaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_coins(
        self, point_meta_request: "PointMetaRequest"
    ) -> "PointMetaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_raw_symbols(
        self, point_meta_request: "PointMetaRequest"
    ) -> "PointMetaResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get_points(
        self, stream: "grpclib.server.Stream[PointRequest, PointResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_points(request)
        await stream.send_message(response)

    async def __rpc_stream_points(
        self, stream: "grpclib.server.Stream[PointRequest, PointSeries]"
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.stream_points,
            stream,
            request,
        )

    async def __rpc_get_types(
        self, stream: "grpclib.server.Stream[PointMetaRequest, PointMetaResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_types(request)
        await stream.send_message(response)

    async def __rpc_get_exchanges(
        self, stream: "grpclib.server.Stream[PointMetaRequest, PointMetaResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_exchanges(request)
        await stream.send_message(response)

    async def __rpc_get_categories(
        self, stream: "grpclib.server.Stream[PointMetaRequest, PointMetaResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_categories(request)
        await stream.send_message(response)

    async def __rpc_get_coins(
        self, stream: "grpclib.server.Stream[PointMetaRequest, PointMetaResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_coins(request)
        await stream.send_message(response)

    async def __rpc_get_raw_symbols(
        self, stream: "grpclib.server.Stream[PointMetaRequest, PointMetaResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_raw_symbols(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/api.API/GetPoints": grpclib.const.Handler(
                self.__rpc_get_points,
                grpclib.const.Cardinality.UNARY_UNARY,
                PointRequest,
                PointResponse,
            ),
            "/api.API/StreamPoints": grpclib.const.Handler(
                self.__rpc_stream_points,
                grpclib.const.Cardinality.UNARY_STREAM,
                PointRequest,
                PointSeries,
            ),
            "/api.API/GetTypes": grpclib.const.Handler(
                self.__rpc_get_types,
                grpclib.const.Cardinality.UNARY_UNARY,
                PointMetaRequest,
                PointMetaResponse,
            ),
            "/api.API/GetExchanges": grpclib.const.Handler(
                self.__rpc_get_exchanges,
                grpclib.const.Cardinality.UNARY_UNARY,
                PointMetaRequest,
                PointMetaResponse,
            ),
            "/api.API/GetCategories": grpclib.const.Handler(
                self.__rpc_get_categories,
                grpclib.const.Cardinality.UNARY_UNARY,
                PointMetaRequest,
                PointMetaResponse,
            ),
            "/api.API/GetCoins": grpclib.const.Handler(
                self.__rpc_get_coins,
                grpclib.const.Cardinality.UNARY_UNARY,
                PointMetaRequest,
                PointMetaResponse,
            ),
            "/api.API/GetRawSymbols": grpclib.const.Handler(
                self.__rpc_get_raw_symbols,
                grpclib.const.Cardinality.UNARY_UNARY,
                PointMetaRequest,
                PointMetaResponse,
            ),
        }
