# GRID_FILES
## Develop an implementation of Grid files for storing and querying 2-dimensional datapoints.

### Dataset:
We would be using synthetic datasets for evaluation. Each data point in the dataset is a triple defined as follows: <id>
<x-coordinate> <y-coordinate>. Here <id> is a unique number between 1 and number-points-in-dataset. Note that the
spatial coordinates of the points in the datasets could be repeated. In other words, two different data-points (i.e., two
different ids) can have the same x and y coordinates.
Dataset A: 30000 points generated in a uniformly random fashion where the x and y coordinates are random integers
between 0 and 400.
### Index structures need to be implemented:
(a) Grid files. Please refer to the class notes on this topic(please find notes pdf uploaded in this repository).
### Simulating Buckets:
Buckets are to be implemented as text files in your code. Bucket size is defined as the number of data points it
can accommodate. For instance, if the bucket-size is defined to be 30, it means that the file simulating the bucket
can store 30 data records. Very Imp: Bucket sizes must be taken as input, should not be hard coded. The value of
bucket-size would be varied in the experiments.
