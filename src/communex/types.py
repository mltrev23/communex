"""
Common types for the communex module.
"""

from enum import Enum
from typing import NewType, TypedDict

from pydantic import BaseModel

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


class VoteMode(Enum):
    authority = "Authority"
    vote = "Vote"


class subnetDecryptionInfo(BaseModel):
    node_id: Ss58Address
    node_public_key: bytes
    block_assigned: int


class DisplayGovernanceConfiguration(TypedDict):
    proposal_cost: float
    proposal_expiration: float
    vote_mode: VoteMode
    proposal_reward_treasury_allocation: float
    max_proposal_reward_treasury_allocation: float
    proposal_reward_interval: int


class GovernanceConfiguration(TypedDict):
    proposal_cost: int
    proposal_expiration: int
    vote_mode: int  # 0: Authority, 1: Vote
    proposal_reward_treasury_allocation: float
    max_proposal_reward_treasury_allocation: int
    proposal_reward_interval: int


class DisplayBurnConfiguration(TypedDict):
    min_burn: float
    max_burn: float
    adjustment_alpha: int
    target_registrations_interval: int
    target_registrations_per_interval: int
    max_registrations_per_interval: int


class BurnConfiguration(TypedDict):
    min_burn: int
    max_burn: int
    adjustment_alpha: int
    target_registrations_interval: int
    target_registrations_per_interval: int
    max_registrations_per_interval: int


class NetworkParams(TypedDict):
    # max
    max_name_length: int
    min_name_length: int  # dont change the position
    max_allowed_subnets: int
    max_allowed_modules: int
    max_registrations_per_block: int
    max_allowed_weights: int

    # mins
    floor_delegation_fee: int
    floor_founder_share: int
    min_weight_stake: int

    # S0 governance
    curator: Ss58Address
    general_subnet_application_cost: int

    # Other
    subnet_immunity_period: int
    governance_config: GovernanceConfiguration

    kappa: int
    rho: int

    subnet_registration_cost: int


class SubnetParamsMaps(TypedDict):
    netuid_to_founder: dict[int, Ss58Address]
    netuid_to_founder_share: dict[int, int]
    netuid_to_incentive_ratio: dict[int, int]
    netuid_to_max_allowed_uids: dict[int, int]
    netuid_to_max_allowed_weights: dict[int, int]
    netuid_to_min_allowed_weights: dict[int, int]
    netuid_to_max_weight_age: dict[int, int]
    netuid_to_name: dict[int, str]
    netuid_to_tempo: dict[int, int]
    netuid_to_bonds_ma: dict[int, int]
    netuid_to_maximum_set_weight_calls_per_epoch: dict[int, int]
    netuid_to_emission: dict[int, int]
    netuid_to_immunity_period: dict[int, int]
    netuid_to_governance_configuration: dict[int, GovernanceConfiguration]
    netuid_to_min_validator_stake: dict[int, int]
    netuid_to_max_allowed_validators: dict[int, int]
    netuid_to_module_burn_config: dict[int, BurnConfiguration]
    netuid_to_subnet_metadata: dict[int, str]
    netuid_to_max_encryption_period: dict[int, int]
    netuid_to_copier_margin: dict[int, int]
    netuid_to_use_weights_encryption: dict[int, int]


# WIP
class UpdatableSubnetParams(TypedDict):
    tempo: int


class SubnetParams(UpdatableSubnetParams, TypedDict):
    name: str
    min_allowed_weights: int
    max_allowed_weights: int
    max_allowed_uids: int
    max_weight_age: int
    founder_share: int
    incentive_ratio: int
    founder: Ss58Address
    maximum_set_weight_calls_per_epoch: int | None
    bonds_ma: int | None
    immunity_period: int
    governance_config: GovernanceConfiguration
    min_validator_stake: int | None
    max_allowed_validators: int | None
    module_burn_config: BurnConfiguration
    subnet_metadata: str | None
    max_encryption_period: int
    copier_margin: int
    use_weights_encryption: int


class DisplaySubnetParams(TypedDict):
    name: str
    tempo: int
    min_allowed_weights: int
    max_allowed_weights: int
    max_allowed_uids: int
    max_weight_age: int
    trust_ratio: int
    founder_share: int
    incentive_ratio: int
    founder: Ss58Address
    maximum_set_weight_calls_per_epoch: int | None
    bonds_ma: int
    immunity_period: int
    governance_config: DisplayGovernanceConfiguration
    min_validator_stake: float
    max_allowed_validators: int | None
    module_burn_config: DisplayBurnConfiguration
    subnet_metadata: str | None
    emission: float
    max_encryption_period: int
    copier_margin: int
    use_weights_encryption: int


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
    stake_from: list[tuple[Ss58Address, int]]
    regblock: int  # block number
    last_update: int  # block number
    stake: int
    stake_delegation_fee: int
    validator_weight_fee: int
    metadata: str | None


class ModuleInfoWithBalance(ModuleInfo):
    balance: int


class ModuleInfoWithOptionalBalance(ModuleInfo):
    balance: int | None
