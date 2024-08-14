## Spark Context vs Session

Context

1. low level api
2. example - RDD
3. version 1 introduced
4. spark core
5. for different context we need to create different objects such sqlcontext, hive contex

Session

1. high level api
2. example - dataframe
3. later on
4. spark sql
5. all contexts inbuilt

## Repartition vs Coalesce

Repartition

1. Increase or descrease partition.
2. Output partition of equal size.
3. Full shuffling.
4. Creates new partitions.

Coalesce

1. Decrease partition.
2. Output partitions are of unequal size.
3. 0 to minimum shuffling.
4. Uses existing partition and hence les shuffling.

## Design Pattern

1. Builder - Used to create spark session (objects)
2. Singleton - one objects in its lifetime.
3. ELT - Extract - Load - Transform.
4. ETL - Extract - Transform - Load (Transformation is bottleneck alternative ELT).
5. ETLT - Extract - Transform - Load - Transform.
6. Decorator - adding the functionality to the exisiting.

## Dataframe vs Dataset

Dataframe
1. Supported by python
2. Untyped
3. Identifies error run time.
4. Lazy - late

Dataset
1. Supported by scala, python
2. Typed
3. Identifies error compiles time.
4. Eager - early

## Cache vs Persistant

A lot more options with Persistant storage as compared to cache.


## Broadcast Join

1. When we join the small table with large table, driver code will copy the entire small table on each worker nodes
and since the data is available with each node there will be no need to perform reshuffle.

2. driver should have enough memory to persist the copy for small table for each worker nodes.
3. table with less than 10 MB is generally considered as small table and it is configurable and max up (8GB).
4. Small table example - Lookup Table and Dimension Table.
5. Broadcast Variable - to configure the global properties which can be broadcast similar to Broadcast Join.
6. autoJoinThreshold is need to configure to handle the max size of table. (-1) to disable the Broadcast Join.