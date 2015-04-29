cd /home/hadoop/Sotera-distributed-graph-analytics-b3f67d4/dga-giraph/build/dist

./bin/dga-yarn-giraph hbse /project/hbse_example/input/ /project/hbse_example/output/ -w 1 -ca io.edge.reverse.duplicator=true -ca giraph.SplitMasterWorker=false

