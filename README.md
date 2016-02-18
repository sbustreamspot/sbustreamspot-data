# StreamSpot Data

<img src="http://www3.cs.stonybrook.edu/~emanzoor/streamspot/img/streamspot-logo.jpg" height="150" align="right"/>

[http://www3.cs.stonybrook.edu/~emanzoor/streamspot/](http://www3.cs.stonybrook.edu/~emanzoor/streamspot/)

This repository contains the `ALL` dataset, which includes edges from all the
600 benign and attack scenario graphs. The `YDC` and `GFC` datasets can be derived
from `ALL` by picking graph ID's having scenarios as follows:

   * `YDC`: YouTube, Download, CNN
   * `GFC`: GMail, VGame, CNN 

## Format

Tab-separated file with one edge on each line in the following format:

```
source-id	source-type	destination-id	destination-type	edge-type	graph-id
```

Graph ID's correspond to scenarios as follows:
   
   1. YouTube (graph ID's 0 - 99)
   2. GMail (graph ID's 100 - 199)
   3. VGame (graph ID's 200 - 299)
   4. Drive-by-download attack (graph ID's 300 - 399)
   5. Download (graph ID's 400 - 499)
   6. CNN (graph ID's 500 - 599)

## Construction

The `ALL` dataset was extracted from the raw flow-graph data using `preprocess.py`,
which performs the following:

   1. Each node and edge type is mapped to a single character.
   2. Consecutive edges between the same pair of nodes corresponding to
      block-by-block file reads are collapsed into a single edge.
   3. Node ID's are incremented by 1 (so ID's of `-1` become 0).
   4. The timestamp field is removed (raw edges are sorted by timestamp).

`preprocess.py` is run as: `python preprocess.py <raw edges file>`

## Credits

The raw flow-graph data for StreamSpot was provided by
[Venkat N. Venkatakrishnan][1], [Sadegh Momeni][2] and team at the
University of Illinois - Chicago.

## Contact

   * emanzoor@cs.stonybrook.edu
   * leman@cs.stonybrook.edu

[1]: https://www.cs.uic.edu/~venkat/
[2]: http://smomen2.people.uic.edu/
