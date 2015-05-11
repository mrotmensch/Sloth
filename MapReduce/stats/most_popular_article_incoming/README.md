# MapReduce calculating most linked-to articles

## to run locally 
pipe example\_input.txt into mapper_most_incoming_links_articles.py and then into reducer.py:

    cat example_input.txt | python mapper_most_incoming_links_articles.py | python reducer.py 

## to run on AWS
1. upload mapper and reducer.
2. use input from: 
    * https://s3.amazonaws.com/mayar/JUSTIN/full\_data/part\-00000


3. use the following custom Jar:

    -D mapreduce.job.reduces=1 -files s3://PATH_TO/mapper_most_incoming_links_articles.py,s3://PATH_TO/reducer.py -mapper mapper_most_incoming_links_articles.py -reducer reducer.py -input s3://mayar/JUSTIN/full_data/part-00000 -output s3://PATH_TO_OUTPUT


4. you can examine the output of our run in the file:
    * https://s3.amazonaws.com/mayar/Stats/incoming_links_articles_output/part-00000