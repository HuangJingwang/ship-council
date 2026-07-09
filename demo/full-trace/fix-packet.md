# Fix Packet

## Finding

Filtering was proposed after pagination in the initial plan.

## Required Change

Move organization filtering into the query predicate before pagination and sorting.

## Owner

Backend surface developer.

## Acceptance

- Test creates work items across two organizations.
- Requesting organization A returns only organization A items.
- Pagination total matches organization A only.
