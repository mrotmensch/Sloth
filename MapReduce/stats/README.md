# MapReduce for Wikipedia namespace statistics


1.  Mapper is mapper\_full.py
2.  Reducer is reducer.py
3.  Mapper and reducer can be run locally with sample file input\_sample.txt
3.  Results obtained on AWS are saved locally as 'results' and on S3 here: https://s3.amazonaws.com/mayar/Stats/namepace\_hist\_output/part-00000
4. namespace\_helper.txt is a decoder for namespace from id to name.
5. visual.py is a script that should be run locally to visualize the histogram of pages per namespace.
6. The results of visual.py are saved in "Histogram of pages per namespace (logged).png"


On AWS you can find the mapper and reducer here: 
mapper: https://s3.amazonaws.com/mayar/Stats/namespace\_hist/map\_full.py
reducer: https://s3.amazonaws.com/mayar/Stats/namespace\_hist/reducer.py