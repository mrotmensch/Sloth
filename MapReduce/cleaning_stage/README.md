
# MapReduce for cleaning Wikipedia data

Programs in this folder are the first step in the MapReduce pipeline for dataprocessing.

To clean the data of links between articles use mapper\_pagelinks.py as the mapper and reducer.py as the reducer.
To clean the data on each invididual pages use the mapper\_pages.py as the mapper and reducer.py as the reducer.


## For Mappers:

###To run files locally:

1. Use mapper\_pagelinks.py with example\_input\_pagelinks.txt
2. Use mapper\_pages.py with example\_input\_pages.txt

To examine preprocessed results look at:

1. for file corresponding to mapper\_pagelinks.py inspect results\_example\_mapper\_pagelinks.txt
2. for file corresponding to mapper\_pages.py inspect results\_example\_mapper\_pages.txt

## For Reducer:
For both files use reducer.py as the reducer. This is an identity reducer.

### To run files locally:

To examine preprocessed results look at:

1. for file corresponding to mapper\_pagelinks.py+reducer.py inspect results\_example\_reducer\_pagelink.txt
2. for file corresponding to mapper\_pages.py+reducer.py inspect results\_example\_reducer\_pages.txt

## AWS
### To run this program on AWS use the preloaded, publicly available data :

### Upload mappers and reducers to your S3 library

### choose number of reducers you wish to have
For the Pagelinks mapper it is best to choose mutiple shards as output. For the pages program we suggest that you use a single reducer.

### run the costum Jar:

For Pages file:

-D mapreduce.job.reduces=1 -files s3://INDIVIDUAL_PATH/mapper_pages.py,
s3://INDIVIDUAL_PATH/reducer.py
 -mapper mapper_pages.py 
 -reducer reducer.py 
 -input s3://mayar/Wiki_actual_input/enwiki-20150304-page.sql
 -output s3://CHOOSE_OUTPUT_DIRECTORY

