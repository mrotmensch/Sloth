
CURRENTDIR="$PWD"

#EXAMPLEDIR=/project/louvain_example
EXAMPLEDIR=$CURRENTDIR

cd ~/Sotera-distributed-graph-analytics-b3f67d4/dga-giraph/build/dist
#cd /home/hadoop/Sotera-distributed-graph-analytics-b3f67d4/dga-giraph/build/dist


rm -rf $EXAMPLEDIR/output4
./bin/dga-yarn-giraph louvain $EXAMPLEDIR/input4/ $EXAMPLEDIR/output4/ -ca minimum.progress=4 -ca progress.tries=4 -w 1 -ca io.edge.reverse.duplicator=true -ca giraph.SplitMasterWorker=false


cd $CURRENTDIR
