# MapReduce calculating articles with most outgoing links

Recall that unlike most_popular_article_outgoing, this program examines links to ALL pages in every available namespace.

Note that the result of this program is:
    page_id , number of outgoing links

to translate these results into actual file titles we then grep the decoder file produced in step 3 (https://s3.amazonaws.com/mayar/decoder_cleaning/DECODER/part-00000). It is possible to run a MapReduce program to perform this matching, but given that the decoder file is faitly small and that we only need 3 page titles, the overhead of performing MapReduce would overshadow any potential benifits. 


## to run locally 
pipe example\_input.txt into mapper_most_outgoing_links.py and then into reducer.py:

    cat example_input.txt | python mapper_most_outgoing_links.py | python reducer.py 

## to run on AWS
1. upload mapper and reducer.
2. use input from: 
    * https://s3.amazonaws.com/mayar/JUSTIN/full\_data/part\-00000


3. use the following custom Jar:

    -D mapreduce.job.reduces=1 -files s3://PATH_TO/mapper_most_outgoing_links.py,s3://PATH_TO/reducer.py -mapper mapper_most_outgoing_links_articles.py -reducer reducer.py -input s3://mayar/JUSTIN/full_data/part-00000 -output s3://PATH_TO_OUTPUT


4. you can examine the output of our run in the file:
    * https://s3.amazonaws.com/mayar/Stats/outgoing_links_output/part-00000