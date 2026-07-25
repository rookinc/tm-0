# Experiment 066: Aligned G15 Cocycle Ingestion Frontier

## Question

Can TM-0 ingest and classify the retained aligned G15 Z2 cocycle without
mistaking an imported representative for a native derivation from G60?

## Current Source Candidate

The candidate source is:

    research/mathematics/thalean-graph-theory/
    05-thalean-stress-testing/artifacts/json/
    transport_cocycle_edges.json

It records:

    base graph
        G15

    undirected edges
        30

    directed edge records
        60

    cocycle values
        bit 0
            epsilon +1
            sheet preserving

        bit 1
            epsilon -1
            sheet flipping

    transition class
        z2_signed_lift

    support validation
        passed

The directed records assign the same Z2 value in both orientations of
each undirected edge.

## Provenance Status

The signing is not currently established as a native derivation from
G60.

Its recorded status is:

    imported_from_aletheos_aligned_cocycle

The source note states that the representative was taken from an
archived cocycle edge table and transported through a graph isomorphism
into the active G15 labeling.

Later provenance audits found:

    transport pipeline reproduced exactly
        false

    structural equality of reproduced artifact
        false

    upstream lawfulness established
        false

    possible aligned generator found
        true

    strict writer for source cocycle data found
        false

Therefore the candidate is executable and support-aligned, but its
strict construction origin remains open.

## Existing TM-0 Capability

TM-0 already represents:

    local signs

    signed cycle traversal

    cycle sign product

    local vertex switching

    switching-invariant cycle product

    spanning-tree switching normal form

    graph switching signature

    switching equivalence

The current gap is not the absence of signed semantics.

The current gap is attaching those semantics to the retained aligned G15
candidate while preserving its provenance boundary.

## Bounded Requirement

A minimal ingestion layer must:

1. retain the source artifact without rewriting its claims

2. validate that the source graph is G15

3. reduce sixty directed records to thirty undirected signed edges

4. verify that opposite directed records agree

5. verify that every undirected support edge has exactly two directed
   records

6. convert cocycle bit 0 to TM-0 PRESERVE

7. convert cocycle bit 1 to TM-0 INVERT

8. verify that epsilon agrees with the cocycle-bit conversion

9. verify that the candidate support matches the independently
   constructed Petersen line graph up to explicit isomorphism

10. compute the candidate graph-switching signature

11. compute the cycle rank and verify that the signature length matches
    it

12. test invariance under explicit local switching

## Required Executable Outputs

The first source-backed result should record:

    source status

    provenance classification

    directed record count

    undirected edge count

    bit count

    sign count

    support-isomorphism map to L(P)

    vertex count

    edge count

    cycle rank

    switching-signature length

    normalized negative chord count

    switching-invariance result

## Exact Distinctions

The aligned cocycle candidate is not:

    a native G60 derivation

    the thirty-vertex Project 42 carrier

    the external G900 half-flip

    the K6 grammar-interface obstruction

    a U(1) deformation

The candidate is:

    one Z2 signing on a graph isomorphic to G15

Its switching character is a property of that signed graph.

Its provenance is a separate property of the source record.

Executable agreement does not repair missing provenance.

## Falsification

The ingestion fails if:

    the directed records do not pair consistently

    the source support is not a thirty-edge simple graph

    the source support is not isomorphic to L(P)

    cocycle bits and epsilon values disagree

    the switching signature length does not equal cycle rank

    local switching changes the switching character

## Semantic Admission Result

No new broad semantic object is currently required.

The candidate can be represented using:

    graph

    local sign assignment

    switching operation

    switching character

    source provenance

The provenance boundary is metadata about the claim.

It is not part of the cocycle value itself.

## Classification

This is a bounded signed-source ingestion frontier.

It is not yet an executable result.

It does not establish native G60 cocycle origin.

It does not establish the signed thirty-vertex or sixty-vertex carrier.

## Boundary

The source candidate is retained as an aligned imported representative.

Its support validation is accepted as source evidence.

Its strict upstream construction remains unresolved.

The external half-flip remains lawful carrier transport and is not
treated as a local G60 automorphism.

The K6 triangle obstruction remains a separate grammar-interface gauge
result.

No physical interpretation is claimed.

## Keeper Candidate

Executable character can be inherited from a source.

Native origin must still be earned.
