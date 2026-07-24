# Receipt 0017

## Title

Cycle Product Survives Local Switching

## Status

Research receipt.

## Result

Local junction re-readings can change individual relation signs.

Under the switching rule:

    sign_prime(i)
        =
    switch(i) * sign(i) * switch(i+1)

the product of all relation signs around a closed cycle remains
unchanged.

## Interpretation

Individual local signs are not absolute in the tested model.

They depend on the local reading assigned at adjacent junctions.

The closed-cycle product does not depend on those local re-readings.

## Consequence

The return residue is more stable than the individual edge signs.

This supports the distinction:

    local sign assignment
        gauge-like description

    closed-cycle sign product
        invariant receipt

A positive cycle remains positive.

A negative cycle remains negative.

## Limitation

The switching rule remains assumed.

This experiment does not yet prove that switching-equivalent sign
assignments represent the same mechanics.

It does not derive a cocycle law, character accumulation, witness, or
thalion.

## Keeper

The local reading may change.

The closed return keeps its sign.
