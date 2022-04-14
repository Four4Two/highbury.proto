# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/auth/v1beta1/auth.proto, cosmos/auth/v1beta1/genesis.proto, cosmos/auth/v1beta1/query.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class BaseAccount(betterproto.Message):
    """
    BaseAccount defines a base account type. It contains all the necessary
    fields for basic account functionality. Any custom account type should
    extend this type for additional functionality (e.g. vesting).
    """

    address: str = betterproto.string_field(1)
    pub_key: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)
    account_number: int = betterproto.uint64_field(3)
    sequence: int = betterproto.uint64_field(4)


@dataclass(eq=False, repr=False)
class ModuleAccount(betterproto.Message):
    """
    ModuleAccount defines an account for modules that holds coins on a pool.
    """

    base_account: "BaseAccount" = betterproto.message_field(1)
    name: str = betterproto.string_field(2)
    permissions: List[str] = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the parameters for the auth module."""

    max_memo_characters: int = betterproto.uint64_field(1)
    tx_sig_limit: int = betterproto.uint64_field(2)
    tx_size_cost_per_byte: int = betterproto.uint64_field(3)
    sig_verify_cost_ed25519: int = betterproto.uint64_field(4)
    sig_verify_cost_secp256_k1: int = betterproto.uint64_field(5)


@dataclass(eq=False, repr=False)
class QueryAccountsRequest(betterproto.Message):
    """
    QueryAccountsRequest is the request type for the Query/Accounts RPC method.
    """

    # pagination defines an optional pagination for the request.
    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryAccountsResponse(betterproto.Message):
    """
    QueryAccountsResponse is the response type for the Query/Accounts RPC
    method.
    """

    # accounts are the existing accounts
    accounts: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(1)
    # pagination defines the pagination in the response.
    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class QueryAccountRequest(betterproto.Message):
    """
    QueryAccountRequest is the request type for the Query/Account RPC method.
    """

    # address defines the address to query for.
    address: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryAccountResponse(betterproto.Message):
    """
    QueryAccountResponse is the response type for the Query/Account RPC method.
    """

    # account defines the account of the corresponding address.
    account: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest is the request type for the Query/Params RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is the response type for the Query/Params RPC method.
    """

    # params defines the parameters of the module.
    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the auth module's genesis state."""

    # params defines all the paramaters of the module.
    params: "Params" = betterproto.message_field(1)
    # accounts are the accounts present at genesis.
    accounts: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(2)


class QueryStub(betterproto.ServiceStub):
    async def accounts(
        self, *, pagination: "__base_query_v1_beta1__.PageRequest" = None
    ) -> "QueryAccountsResponse":

        request = QueryAccountsRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/Accounts", request, QueryAccountsResponse
        )

    async def account(self, *, address: str = "") -> "QueryAccountResponse":

        request = QueryAccountRequest()
        request.address = address

        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/Account", request, QueryAccountResponse
        )

    async def params(self) -> "QueryParamsResponse":

        request = QueryParamsRequest()

        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/Params", request, QueryParamsResponse
        )


class QueryBase(ServiceBase):
    async def accounts(
        self, pagination: "__base_query_v1_beta1__.PageRequest"
    ) -> "QueryAccountsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def account(self, address: str) -> "QueryAccountResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(self) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_accounts(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "pagination": request.pagination,
        }

        response = await self.accounts(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_account(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "address": request.address,
        }

        response = await self.account(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_params(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.params(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.auth.v1beta1.Query/Accounts": grpclib.const.Handler(
                self.__rpc_accounts,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAccountsRequest,
                QueryAccountsResponse,
            ),
            "/cosmos.auth.v1beta1.Query/Account": grpclib.const.Handler(
                self.__rpc_account,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAccountRequest,
                QueryAccountResponse,
            ),
            "/cosmos.auth.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
        }


from ...base.query import v1beta1 as __base_query_v1_beta1__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
