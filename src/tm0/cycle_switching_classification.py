"""Switching classification for one signed cycle.

Two sign assignments on the same cycle are switching-equivalent when a
junction switch transforms one assignment into the other.

For one connected cycle, equal cycle products should be necessary and
sufficient for switching equivalence.
"""

from typing import Optional
from typing import Tuple

from .cycle_switching import cycle_sign_product
from .cycle_switching import switch_cycle_signs
from .local_sign_product import LocalSign


def switching_witness(
    source: Tuple[LocalSign, ...],
    target: Tuple[LocalSign, ...],
) -> Optional[Tuple[LocalSign, ...]]:
    if not source:
        raise ValueError("a signed cycle requires at least one relation")

    if len(source) != len(target):
        raise ValueError("sign assignments must have equal length")

    if cycle_sign_product(source) != cycle_sign_product(target):
        return None

    switches = [LocalSign.PRESERVE]

    for index in range(len(source) - 1):
        value = (
            int(switches[index])
            * int(source[index])
            * int(target[index])
        )
        switches.append(LocalSign(value))

    witness = tuple(switches)

    if switch_cycle_signs(source, witness) != target:
        raise RuntimeError("constructed switching witness failed")

    return witness


def switching_equivalent(
    source: Tuple[LocalSign, ...],
    target: Tuple[LocalSign, ...],
) -> bool:
    return switching_witness(source, target) is not None
