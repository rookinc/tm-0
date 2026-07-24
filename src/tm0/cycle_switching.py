"""Local switching of signed relation cycles for TM-0.

Each relation in a closed cycle carries a local sign.

Each junction may also be re-read by a local switch:

    +1 = preserve the local reading
    -1 = reverse the local reading

For edge i from junction i to junction i+1:

    sign_prime(i) = switch(i) * sign(i) * switch(i+1)

The individual relation signs may change.

The product of all relation signs around the closed cycle should remain
unchanged because every junction switch appears exactly twice.
"""

from math import prod
from typing import Tuple

from .local_sign_product import LocalSign


def cycle_sign_product(
    signs: Tuple[LocalSign, ...],
) -> int:
    if not signs:
        raise ValueError("a signed cycle requires at least one relation")

    return prod(int(sign) for sign in signs)


def switch_cycle_signs(
    signs: Tuple[LocalSign, ...],
    switches: Tuple[LocalSign, ...],
) -> Tuple[LocalSign, ...]:
    if not signs:
        raise ValueError("a signed cycle requires at least one relation")

    if len(signs) != len(switches):
        raise ValueError("one local switch is required per junction")

    transformed = []

    for index, sign in enumerate(signs):
        left = switches[index]
        right = switches[(index + 1) % len(switches)]
        value = int(left) * int(sign) * int(right)
        transformed.append(LocalSign(value))

    return tuple(transformed)


def switching_preserves_cycle_product(
    signs: Tuple[LocalSign, ...],
    switches: Tuple[LocalSign, ...],
) -> bool:
    transformed = switch_cycle_signs(signs, switches)

    return cycle_sign_product(signs) == cycle_sign_product(transformed)
