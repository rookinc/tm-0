# Receipt 0056: Selected Equivalence Preserves Carrier

## Recorded Result

TM-0 can now represent:

    one fixed finite carrier

    multiple distinct registered equivalence systems

    one selected equivalence system

    preserved unselected alternatives

Selection derives the classes of the active equivalence relation.

Selection does not mutate the carrier.

## Executable Evidence

Implementation:

    src/tm0/selected_equivalence.py

Focused tests:

    tests/test_selected_equivalence.py

Focused result:

    11 tests passed

Full-suite result:

    385 tests passed

## Demonstrated Distinction

Two selections may share:

    the same carrier

    the same equivalence-class size summary

while preserving:

    different selected equivalence systems

Therefore the quotient summary does not determine the selected
identification law.

## Candidate Semantic Structure

The executable candidate binds:

    fixed carrier

to:

    one selected member of a preserved equivalence family

The family preserves lawful alternatives.

The selection identifies the active law.

## G60 Relevance

The candidate has the minimal structural shape required to host:

    one 30-vertex carrier

    three distinct partitions into fifteen pairs

    one selected quotient system

    two preserved alternative quotient systems

The actual G60-related three-system instance has not yet been loaded.

## Classification

This is an executable candidate receipt.

It is stronger than an expressive-gap receipt.

It is not yet a completed G60 correspondence.

It does not yet establish a permanent ontology name.

## Boundary

No symmetry action is represented.

No stabilizer is represented.

No quotient graph is constructed.

No lawfulness criterion for equivalence systems is derived.

No claim is made that selection is:

    context

    viewpoint

    observation

    witness

    character

No claim is made that selection changes execution.

## Keeper

Selection changes the identification law.

It does not change the carrier.
