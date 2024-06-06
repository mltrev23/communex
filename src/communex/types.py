"""
Common types for the communex module.
"""

from typing import NewType, TypedDict

Ss58Address = NewType("Ss58Address", str)
"""Substrate SS58 address.

The `SS58 encoded address format`_ is based on the Bitcoin Base58Check format,
but with a few modification specifically designed to suite Substrate-based
chains.

.. _SS58 encoded address format:
    https://docs.substrate.io/reference/address-formats/
"""


# TODO: replace with dataclasses

# == Burn related
MinBurn = NewType("MinBurn", int)
MaxBurn = NewType("MaxBurn", int)
BurnConfig = NewType("BurnConfig", dict[MinBurn, MaxBurn])


class NetworkParams(TypedDict):
    max_allowed_modules: int
    max_registrations_per_block: int
    unit_emission: int
    max_name_length: int
    min_name_length: int
    burn_config: BurnConfig
    min_weight_stake: int
    max_allowed_subnets: int
    adjustment_alpha: int
    curator: Ss58Address
    proposal_cost: int
    proposal_expiration: int
    max_proposal_reward_treasury_allocation: int
    proposal_reward_interval: int
    subnet_stake_threshold: int


class SubnetParamsMaps(TypedDict):
    netuid_to_founder: dict[int, Ss58Address]
    netuid_to_founder_share: dict[int, int]
    netuid_to_immunity_period: dict[int, int]
    netuid_to_incentive_ratio: dict[int, int]
    netuid_to_max_allowed_uids: dict[int, int]
    netuid_to_max_allowed_weights: dict[int, int]
    netuid_to_min_allowed_weights: dict[int, int]
    netuid_to_max_weight_age: dict[int, int]
    netuid_to_min_stake: dict[int, int]
    netuid_to_name: dict[int, str]
    netuid_to_tempo: dict[int, int]
    netuid_to_trust_ratio: dict[int, int]
    netuid_to_bonds_ma: dict[int, int]
    netuid_to_maximum_set_weight_calls_per_epoch: dict[int, int]
    netuid_to_target_registrations_per_interval: dict[int, int]
    netuid_to_target_registrations_interval: dict[int, int]
    netuid_to_emission: dict[int, int]
    netuid_to_max_registrations_per_interval: dict[int, int]

class SubnetParams(TypedDict):
    founder: Ss58Address
    founder_share: int
    immunity_period: int
    incentive_ratio: int
    max_allowed_uids: int
    max_allowed_weights: int
    min_allowed_weights: int
    max_weight_age: int
    min_stake: int
    name: str
    tempo: int
    trust_ratio: int
    bonds_ma: int | None
    maximum_set_weight_calls_per_epoch: int | None
    target_registrations_per_interval: int
    target_registrations_interval: int
    max_registrations_per_interval: int


# redundant "TypedDict" inheritance because of pdoc warns.
# see https://github.com/mitmproxy/pdoc/blob/26d40827ddbe1658e8ac46cd092f17a44cf0287b/pdoc/doc.py#L691-L692
class SubnetParamsWithEmission(SubnetParams, TypedDict):
    """SubnetParams with emission field."""

    emission: int
    """Subnet emission percentage (0-100).
    """


class ModuleInfo(TypedDict):
    uid: int
    key: Ss58Address
    name: str
    address: str  # "<ip>:<port>"
    emission: int
    incentive: int
    dividends: int
    stake_from: list[tuple[str, int]]  # TODO: type key with Ss58Address
    regblock: int  # block number
    last_update: int  # block number
    stake: int
    delegation_fee: int
    metadata: str


class ModuleInfoWithBalance(ModuleInfo):
    balance: int


class ModuleInfoWithOptionalBalance(ModuleInfo):
    balance: int | None
