"""Act on a registered equivalence-system family.

The action permutes equivalence-system names while preserving:

    the fixed carrier

    the complete registered family

    the selected-equivalence structure

This scaffold acts only on the family index.

It does not yet act on carrier elements, construct quotient graphs, or
represent the full automorphism group.
"""

from dataclasses import dataclass
from typing import Tuple

from .selected_equivalence import SelectedEquivalence


SystemName = str
FamilyPermutation = Tuple[int, ...]


@dataclass(frozen=True)
class EquivalenceFamilyAction:
    names: Tuple[SystemName, ...]
    permutation: FamilyPermutation

    def __post_init__(self) -> None:
        if not self.names:
            raise ValueError(
                "equivalence family must not be empty"
            )

        if len(self.names) != len(set(self.names)):
            raise ValueError(
                "equivalence family names must be unique"
            )

        expected = tuple(range(len(self.names)))

        if tuple(sorted(self.permutation)) != expected:
            raise ValueError(
                "family action must be a permutation"
            )

    def image_name(
        self,
        name: SystemName,
    ) -> SystemName:
        if name not in self.names:
            raise ValueError(
                "system name is not in the action domain"
            )

        source_index = self.names.index(name)
        target_index = self.permutation[source_index]

        return self.names[target_index]

    def fixed_names(self) -> Tuple[SystemName, ...]:
        return tuple(
            name
            for index, name in enumerate(self.names)
            if self.permutation[index] == index
        )


def act_on_selection(
    selection: SelectedEquivalence,
    action: EquivalenceFamilyAction,
) -> SelectedEquivalence:
    """Move the selected system while preserving carrier and family."""
    selection_names = tuple(
        system.name
        for system in selection.systems
    )

    if set(selection_names) != set(action.names):
        raise ValueError(
            "action domain must match registered systems"
        )

    moved_name = action.image_name(
        selection.selected_name
    )

    return SelectedEquivalence(
        carrier=selection.carrier,
        systems=selection.systems,
        selected_name=moved_name,
    )
