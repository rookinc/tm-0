# Experiment 018

## Title

Cycle Product Classifies Switching on One Cycle

## Status

Executable candidate.

## Question

For one connected signed cycle, are two local sign assignments
switching-equivalent exactly when they have the same cycle product?

## Starting Result

Experiment 017 established that local switching preserves the cycle
sign product.

That proved necessity:

    switching-equivalent
        ->
    same cycle product

Experiment 018 tests sufficiency.

## Construction

Given source and target sign assignments of equal length:

1. Compare their cycle products.
2. If the products differ, reject switching equivalence.
3. If the products agree, construct junction switches recursively.
4. Apply the constructed switches to the source assignment.
5. Confirm that the transformed source equals the target.

## Result

Assignments with the same cycle product admit a switching witness.

Assignments with different cycle products do not.

Therefore, for one connected cycle:

    same cycle product
        <->
    switching-equivalent

## Normal Forms

Every positive cycle is switching-equivalent to:

    all PRESERVE

Every negative cycle is switching-equivalent to:

    exactly one INVERT

## Interpretation

The complete local sign pattern contains gauge-like redundancy.

After quotienting by local switching, one connected cycle retains only
one invariant bit:

    +1 = SAME return class

    -1 = POLAR return class

## Boundary

This result applies only to one connected cycle in the tested model.

It does not classify arbitrary graphs with multiple independent
cycles.

It does not derive the local signs, switching rule, character update,
witness, or thalion.

## Keeper

On one closed cycle, the return product is the complete switching
invariant.
