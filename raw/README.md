# StreamSpot Data: Raw

The raw flow-graph data for StreamSpot has been provided by
[Venkat N. Venkatakrishnan][1], [Sadegh Momeni][2] and team at the
University of Illinois - Chicago.

Please contact them directly for the data.

## Format

The data contains 600 flow-graphs derived from system-call traces of executions
from the following six scenarios:

   1. YouTube (graph ID's 0 - 99)
   2. GMail (graph ID's 100 - 199)
   3. Flash game (graph ID's 200 - 299)
   4. Drive-by-download attack (graph ID's 300 - 399)
   5. Download (graph ID's 400 - 499)
   6. CNN (graph ID's 500 - 599)

The data is spread across the following files:

### `edges.csv`

Each line corresponds to an edge in some graph, and is of the format:

```
source id, source type, destination id, destination type, edge type, timestamp, graphid
``` 

   * `source id`, `destination id`: Source and destination ID's.
     Further metadata corresponding to each process (file) is contained in
     `process.csv` (`file.csv`).
   * `source type`, `destination type`: One of `process` or `file`. 
   * `edge type`: One of a number of select system calls.
   * `timestamp`: Time of this event in UNIX epoch format.
   * `graph id`: Identifies which graph this edge is from.

### `process.csv`, `file.csv`

Each line contains metadata corresponding to a process or file.

[1]: https://www.cs.uic.edu/~venkat/
[2]: http://smomen2.people.uic.edu/
