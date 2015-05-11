# Stochastic Block Modeling with graph-tool

[Download and install graph-tool](https://graph-tool.skewed.de/static/doc/index.html)

If running this on NYU's HPC Mercer cluster, graph-tool has already been installed and one simply needs to load using the following commands:

	module purge
	module load python/intel/2.7.6
	module load graph-tool/gnu/2.2.42

Before proceeding further, please make sure that the nodes.txt and edges.txt files have been generated according to XYZ.

Executing the following commands will load the graph, purge it, generate the stochastic block model, and generate the hierarchy tree in JSON format.

	python loadgraph.py
	python purge.py '5e-5'  # purges the graph at the PageRank 5e-5 threhold.  This can be adjusted, e.g. 1e-5.
	python generateNestedBlockModel.py '5e-5D'  # generates the nested block model using the graph purged at 5e-5 level.

The output of these scripts will be saved to `../graphs`.  Finally, run the following command to generate the hierarchy tree in JSON format.

	python generateTree.py '5e-5D'  # generates the hierarchy tree in JSON format at the 5e-5 level.

The tree output will be found in `../trees`.