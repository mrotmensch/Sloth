"pruned_.."    means that any nodes in the tree that contained only one child were collapsed.

".._cropped"   means that the bottom layer of the tree (i.e. the actual articles) were chopped off.


see example.py for template on how to load and use trees.


| pagerank threshold | nodes | edges   |
| ------------------ |:-----:|:-------:|
| 5e-5               | 408   | 16,499  |
| 1e-5               | 5,106 | 484,857 |
| 5e-6               | 13,676| 1,516,816|
| 1e-6               | 117,153 | 16,322,339|
| 5e-7               | 263,621 | 36,626,586 |
| 1e-7               | 1,506,661 | 197,025,405 |
| Full graph         | 11,567,005  | 358,585,207 |


