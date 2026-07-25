# Experiment 067: Aligned G15 Cocycle Character Is Classified

## Question

Can TM-0 ingest and classify the retained aligned G15 Z2 cocycle without
mistaking an imported representative for a native derivation from G60?

## Result

Yes.

TM-0 now ingests the retained aligned G15 cocycle candidate, validates
its directed-edge encoding, reduces it to an undirected signed graph,
verifies its support, computes its switching character, and confirms
that the character survives explicit local switching.

The source remains provenance-bounded.

No native G60 origin is claimed.

## Retained Source

The retained source is:

    sources/g15/
    transport_cocycle_edges.json

Its recorded status is:

    imported_from_aletheos_aligned_cocycle

Its recorded base graph is:

    G15

Its recorded source graph is:

    G15

The source artifact path retained by the record is:

    /Users/scottcave/dev/cori/aletheos.ai/
    theorem/cocycle_data_aligned.json

## Provenance Classification

TM-0 classifies the source as:

    aligned_imported_representative_native_origin_open

This classification preserves the existing source audits:

    aligned support exists
        true

    candidate is executable
        true

    strict native writer found
        false

    native derivation from G60 established
        false

Executable classification does not repair missing provenance.

## Directed Record Ingestion

The retained artifact contains:

    directed edge records
        60

TM-0 verifies that:

    every source edge is loop-free

    every record endpoint agrees with source_edge

    every undirected edge has exactly two directed records

    the two records use opposite orientations

    opposite records carry the same cocycle bit

    opposite records carry the same epsilon value

    cocycle bit and epsilon agree

The directed records reduce to:

    undirected edges
        30

    vertices
        15

## Sign Conversion

The source convention is converted as:

    cocycle bit 0
        epsilon +1
        TM-0 PRESERVE

    cocycle bit 1
        epsilon -1
        TM-0 INVERT

The derived counts are:

    bit 0
        10

    bit 1
        20

    sign +1
        10

    sign -1
        20

The bit counts and sign counts agree exactly.

## Support Certification

The unsigned support graph has:

    vertices
        15

    edges
        30

TM-0 compares this support against its independently constructed line
graph of the Petersen graph.

The result is:

    support isomorphic to L(P)
        true

    explicit support mapping size
        15

The signed source therefore lives on a graph structurally equivalent to
G15.

The isomorphism does not make the imported labeling canonical.

## Switching Character

For a connected graph, the cycle rank is:

    edge count - vertex count + 1

For this candidate:

    30 - 15 + 1
        16

TM-0 computes a spanning-tree switching normal form.

The resulting switching signature has:

    entries
        16

This matches the cycle rank exactly.

The normalized chord-sign profile contains:

    negative chords
        8

    positive chords
        8

The retained candidate therefore has a balanced sixteen-bit
cycle-space character in the selected normal form.

## Explicit Switching Test

TM-0 applies a nontrivial local switching assignment:

    switched vertices
        7

The individual edge signs change under the switch.

The graph-switching signature remains unchanged.

Result:

    switching invariant
        true

This confirms that the executable character belongs to the switching
class rather than to one particular local edge-sign presentation.

## Executable Components

The result uses only existing TM-0 objects:

    finite graph

    local sign assignment

    local vertex switching

    spanning-tree normal form

    switching signature

    graph isomorphism

    source provenance

No broader semantic object was required.

## Exact Distinctions

The aligned G15 cocycle candidate is not:

    a native derivation from G60

    the thirty-vertex Project 42 carrier

    the external G900 half-flip

    the K6 grammar-interface obstruction

    a U(1) deformation

The candidate is:

    one retained Z2 signing on a graph isomorphic to G15

Its switching character is executable.

Its native origin remains unresolved.

## Falsification Results

The ingestion frontier would have failed if:

    directed records did not pair
        did not fail

    opposite orientations disagreed
        did not fail

    bit and epsilon values disagreed
        did not fail

    support was not a thirty-edge simple graph
        did not fail

    support was not isomorphic to L(P)
        did not fail

    signature length differed from cycle rank
        did not fail

    local switching changed the signature
        did not fail

All bounded falsification checks passed.

## Test Results

The ingestion layer passed:

    focused tests
        12

The full suite after ingestion passed:

    tests
        502

The support and switching-character layer passed:

    focused tests
        9

The final full suite passed:

    tests
        511

## Semantic Admission Result

This frontier does not force admission of:

    viewpoint

    observer

    retention

    precedent

    contextual quotient

    native cocycle origin

The existing semantic vocabulary is sufficient:

    graph

    relation sign

    return character

    switching equivalence

    provenance boundary

## Classification

This is an executable signed-source classification result.

Experiment 066 is closed.

TM-0 now reproduces the switching character of the retained aligned G15
candidate.

It does not derive the candidate from native G60 structure.

## Boundary

The result certifies executable consistency and switching character.

It does not certify source authorship or strict upstream generation.

It does not prove that this signing is the unique lawful G15 cocycle.

It does not connect the signing to the three Project 42 quotient systems.

It does not construct a signed thirty-vertex cover.

It does not construct G60.

It does not identify the external half-flip with local G60 motion.

No physical interpretation is claimed.

## Keeper

Executable character can be inherited from a source.

Native origin must still be earned.
