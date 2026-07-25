"""Finite carrier-action group with an induced family action.

This scaffold represents a finite group of permutations acting on:

    one fixed carrier
    one finite family of named equivalence systems

It derives selected-system stabilizers by filtering actions whose
induced family permutation fixes the selected system.

The scaffold does not require or assume any target group order.
"""

from dataclasses import dataclass
from typing import Iterable
from typing import Tuple


CarrierPermutation = Tuple[int, ...]
FamilyPermutation = Tuple[int, ...]


def compose_permutations(
    left: Tuple[int, ...],
    right: Tuple[int, ...],
) -> Tuple[int, ...]:
    """Return left after right."""
    if len(left) != len(right):
        raise ValueError(
            "permutation domains must have equal size"
        )

    expected = tuple(range(len(left)))

    if tuple(sorted(left)) != expected:
        raise ValueError(
            "left action must be a permutation"
        )

    if tuple(sorted(right)) != expected:
        raise ValueError(
            "right action must be a permutation"
        )

    return tuple(
        left[right[index]]
        for index in range(len(left))
    )


def inverse_permutation(
    permutation: Tuple[int, ...],
) -> Tuple[int, ...]:
    """Return the inverse of one finite permutation."""
    expected = tuple(range(len(permutation)))

    if tuple(sorted(permutation)) != expected:
        raise ValueError(
            "action must be a permutation"
        )

    inverse = [0] * len(permutation)

    for source, target in enumerate(permutation):
        inverse[target] = source

    return tuple(inverse)


@dataclass(frozen=True)
class CarrierFamilyAction:
    name: str
    carrier_permutation: CarrierPermutation
    family_permutation: FamilyPermutation

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError(
                "action name must not be empty"
            )

        carrier_expected = tuple(
            range(len(self.carrier_permutation))
        )

        if (
            tuple(sorted(self.carrier_permutation))
            != carrier_expected
        ):
            raise ValueError(
                "carrier action must be a permutation"
            )

        family_expected = tuple(
            range(len(self.family_permutation))
        )

        if (
            tuple(sorted(self.family_permutation))
            != family_expected
        ):
            raise ValueError(
                "family action must be a permutation"
            )

    def compose(
        self,
        other: "CarrierFamilyAction",
        name: str,
    ) -> "CarrierFamilyAction":
        """Return this action after the other action."""
        return CarrierFamilyAction(
            name=name,
            carrier_permutation=compose_permutations(
                self.carrier_permutation,
                other.carrier_permutation,
            ),
            family_permutation=compose_permutations(
                self.family_permutation,
                other.family_permutation,
            ),
        )

    def inverse(
        self,
        name: str,
    ) -> "CarrierFamilyAction":
        """Return the inverse carrier and family action."""
        return CarrierFamilyAction(
            name=name,
            carrier_permutation=inverse_permutation(
                self.carrier_permutation
            ),
            family_permutation=inverse_permutation(
                self.family_permutation
            ),
        )

    def fixes_system(
        self,
        system_index: int,
    ) -> bool:
        if not 0 <= system_index < len(
            self.family_permutation
        ):
            raise ValueError(
                "system index is outside the family"
            )

        return (
            self.family_permutation[system_index]
            == system_index
        )


@dataclass(frozen=True)
class FiniteCarrierActionGroup:
    actions: Tuple[CarrierFamilyAction, ...]

    def __post_init__(self) -> None:
        if not self.actions:
            raise ValueError(
                "action group must not be empty"
            )

        names = tuple(
            action.name
            for action in self.actions
        )

        if len(names) != len(set(names)):
            raise ValueError(
                "action names must be unique"
            )

        carrier_sizes = {
            len(action.carrier_permutation)
            for action in self.actions
        }

        if len(carrier_sizes) != 1:
            raise ValueError(
                "carrier action domains must match"
            )

        family_sizes = {
            len(action.family_permutation)
            for action in self.actions
        }

        if len(family_sizes) != 1:
            raise ValueError(
                "family action domains must match"
            )

        action_pairs = {
            (
                action.carrier_permutation,
                action.family_permutation,
            )
            for action in self.actions
        }

        if len(action_pairs) != len(self.actions):
            raise ValueError(
                "registered actions must be distinct"
            )

    @property
    def carrier_size(self) -> int:
        return len(
            self.actions[0].carrier_permutation
        )

    @property
    def family_size(self) -> int:
        return len(
            self.actions[0].family_permutation
        )

    @property
    def identity(self) -> CarrierFamilyAction:
        carrier_identity = tuple(
            range(self.carrier_size)
        )
        family_identity = tuple(
            range(self.family_size)
        )

        matches = tuple(
            action
            for action in self.actions
            if (
                action.carrier_permutation
                == carrier_identity
                and action.family_permutation
                == family_identity
            )
        )

        if len(matches) != 1:
            raise ValueError(
                "group must contain exactly one identity"
            )

        return matches[0]

    def find_action(
        self,
        carrier_permutation: CarrierPermutation,
        family_permutation: FamilyPermutation,
    ) -> CarrierFamilyAction:
        matches = tuple(
            action
            for action in self.actions
            if (
                action.carrier_permutation
                == carrier_permutation
                and action.family_permutation
                == family_permutation
            )
        )

        if len(matches) != 1:
            raise ValueError(
                "composed action is not uniquely registered"
            )

        return matches[0]

    def compose(
        self,
        left: CarrierFamilyAction,
        right: CarrierFamilyAction,
    ) -> CarrierFamilyAction:
        carrier = compose_permutations(
            left.carrier_permutation,
            right.carrier_permutation,
        )
        family = compose_permutations(
            left.family_permutation,
            right.family_permutation,
        )

        return self.find_action(
            carrier,
            family,
        )

    def inverse(
        self,
        action: CarrierFamilyAction,
    ) -> CarrierFamilyAction:
        return self.find_action(
            inverse_permutation(
                action.carrier_permutation
            ),
            inverse_permutation(
                action.family_permutation
            ),
        )

    def stabilizer(
        self,
        system_index: int,
    ) -> Tuple[CarrierFamilyAction, ...]:
        return tuple(
            action
            for action in self.actions
            if action.fixes_system(system_index)
        )


def finite_carrier_action_group(
    actions: Iterable[CarrierFamilyAction],
) -> FiniteCarrierActionGroup:
    """Register one finite carrier-action group candidate."""
    return FiniteCarrierActionGroup(
        actions=tuple(actions)
    )
