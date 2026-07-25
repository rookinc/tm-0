# Experiment 056: Selected Equivalence Preserves Carrier and Alternatives

## Question

Can TM-0 represent the selection of one lawful equivalence relation
without mutating the carrier or erasing the unselected alternatives?

## Implementation

The executable scaffold is:

    src/tm0/selected_equivalence.py

It defines:

    EquivalenceSystem

    SelectedEquivalence

    canonical_partition

    select_equivalence

## Executable Result

One finite carrier may support multiple distinct registered equivalence
systems.

Exactly one registered system may be selected.

Selection preserves:

    the original carrier

    the selected partition

    the unselected registered alternatives

Different selections may produce:

    equal class-size summaries

while preserving:

    distinct selected equivalence systems

## Focused Evidence

The focused suite verifies:

    partitions are canonicalized

    partition classes are disjoint

    partitions cover the fixed carrier

    at least two systems are required

    registered systems are distinct

    the selected system is registered

    alternatives remain available

    selected classes are derived

    different selections leave the carrier unchanged

    matching quotient summaries do not erase selection

Focused result:

    11 tests passed

Full-suite result:

    385 tests passed

## Interpretation

A selected equivalence is not a mutation of the carrier.

It is a binding between:

    one fixed carrier

and:

    one member of a preserved lawful equivalence family

The quotient summary alone does not recover that binding.

## Candidate Admission

The executable distinction is now real:

    lawful equivalence family

    selected equivalence

The permanent ontology name remains provisional.

This experiment demonstrates the capability.

It does not yet prove that `SelectedEquivalence` is the final or smallest
semantic name.

## G60 Correspondence

The scaffold can host the required shape:

    one carrier

    three distinct pair partitions

    one selected partition

    two preserved alternatives

It has not yet been instantiated with the actual 30-vertex graph and
its three fifteen-pair quotient systems.

That G60-backed instantiation remains required.

## Boundary

No symmetry group is represented.

No action on the family is represented.

No selected-system stabilizer is computed.

No quotient graph is constructed.

No claim is made that every registered equivalence relation is lawful.

No claim is made that selection changes execution.

No claim is made that selection is context, observation, or viewpoint.

## Classification

This is an executable candidate result.

It is stronger than a scaffold.

It is not yet a completed G60 correspondence.

## Keeper

Selection changes the identification law.

It does not change the carrier.
