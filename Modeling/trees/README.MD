# Trees

This folder contains the hierarchical trees output by models in the `../graph-tool` folder.  Please see [that folder](https://github.com/mrotmensch/Sloth/tree/master/Modeling/graph-tool) in the github repo for an explanation of the content.

All tree outputs are contained in the folders '5e-5D','5e-5U', etc, where 5e-5 refers to the threshold and D/U refer to directed or undirected graph.  The files contain the following conventions:

`pruned_..`    means that any nodes in the tree that contained only one child were collapsed.

`.._cropped`   means that the bottom layer of the tree (i.e. the actual articles) were chopped off.

Please see `example.py` for template on how to load and use trees.




