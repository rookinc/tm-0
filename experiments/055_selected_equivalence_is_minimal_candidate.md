# Experiment 055: Selected Equivalence Is the Minimal Candidate

## Question

What is the smallest graph-independent abstraction capable of
expressing the quotient-system selection gap recorded by Experiment 054?

## Existing Primitive

TM-0 already contains:

    EndpointEquivalence

This represents a finite equivalence relation over relation-local ports.

It can determine:

    equivalence

    composition

    closure

The equivalence relation itself is therefore not missing.

## Demonstrated Missing Capability

Experiment 054 established that TM-0 cannot currently represent:

    one fixed body

    several lawful equivalence relations over that body

    selection of one equivalence relation

    preservation of the unselected alternatives

    symmetry acting on the family

    a stabilizer preserving the selected member

## Candidate Reduction

The smallest candidate does not require a new quotient value.

It requires two existing or minimal structures:

    lawful equivalence family

    selected member

The candidate relation is:

    fixed carrier
    +
    family of lawful equivalence relations
    +
    selected equivalence relation

The selected relation determines which carrier elements are identified.

The carrier itself is not modified.

## Candidate Name

The provisional candidate name is:

    SelectedEquivalence

This name describes the required distinction without importing:

    viewpoint

    observer

    context

    memory

    projection

    precedent

No permanent name is admitted by this experiment.

## Why One Equivalence Relation Is Insufficient

A single `EndpointEquivalence` can describe one identification law.

It cannot establish that:

    alternatives exist

    the alternatives are equally lawful

    a symmetry relates the alternatives

    one member is currently selected

Without the family, selection has no domain.

Without selection, the family has no active member.

## Why Quotient Value Is Insufficient

A quotient value records the state after identification.

It does not uniquely determine the identification relation.

Different lawful equivalence relations may produce matching quotient
values.

Therefore:

    quotient value

does not replace:

    selected equivalence relation

## Why Context Is Not Yet Required

Structural context may later include or reference a selected
equivalence.

That does not show that selection is itself context.

The missing primitive can be expressed more narrowly as a relation
between:

    carrier

    lawful equivalence family

    selected member

No broader context object is required for the first executable test.

## Why Witness Is Not Sufficient

A Witness may report which equivalence relation was selected.

A report cannot create the selected relation.

The executable distinction must exist before it can be witnessed.

## Why Character Is Not Sufficient

Character may change under a selected quotient interpretation.

The current gap exists even when quotient-state character values agree.

Character therefore does not uniquely identify the selected relation.

## Minimal Executable Requirements

A focused implementation must be able to:

1. register one finite carrier set

2. register at least two distinct equivalence relations over that same
   carrier

3. reject an equivalence relation defined over a different carrier

4. select exactly one registered equivalence relation

5. preserve the unselected registered alternatives

6. derive equivalence classes under the selected relation

7. distinguish two selections that produce matching quotient-value
   summaries

8. leave the carrier unchanged after selection

## G60 Correspondence Requirement

A later G60-backed test must instantiate:

    one 30-vertex carrier

    three partitions into fifteen disjoint pairs

    three selected two-fold quotient systems

It must verify that:

    the carrier is identical across selections

    the selected pair partition differs

    all three systems remain registered

The full automorphism action and stabilizer action may be added only
after the minimal selection object passes.

## Falsification

The candidate is unnecessary if the existing TM-0 ontology can already
represent all eight minimal executable requirements without extending
an existing interface.

The candidate is too large if any field can be removed while all eight
requirements still pass.

The candidate is inadequate if it cannot later host the three G60
pair-partition systems.

## Result Classification

This is a minimal-candidate audit.

It does not admit `SelectedEquivalence` as permanent ontology.

It narrows the next executable test.

## Boundary

No symmetry group is required in the first implementation.

No stabilizer computation is required in the first implementation.

No quotient graph construction is required in the first implementation.

No claim is made that every equivalence relation is lawful.

No claim is made that selection changes execution.

No claim is made that selection is observation-dependent.

## Keeper Candidate

The family preserves lawful alternatives.

Selection binds one identification law.
