# MapReduce for creating a clean decoder for Wikipedia Page Information


Programs in this folder are the third step in the MapReduce pipeline for dataprocessing.

This program is designed to be run on the cleaned Pages file from step 1. Output of the reducer should be of the form:

    page_id, page_title

## to run locally 
1. use the testing\_input.txt file to run mapper and reducer locally.
Example of local run command:

    cat testing_input.txt | python map_full.py | python reducer.py 

2. view preprocessed sample results in sample\_results.txt

## to run AWS
1. upload mapper and reducer
2. use input from https://s3.amazonaws.com/mayar/JUSTIN/full\_data/decoder.
3. choose choose output folder name (that does not already exist).
4. run the following Jar:

    -D mapreduce.job.reduces=1 -files s3://PATH_TO/map_full.py,s3://PATH_TO/reducer.py -mapper map_full.py -reducer reducer.py -input s3://mayar/JUSTIN/full_data/decoder -output s3://PATH_TO_OUTPUT

# to examine the results of our run see:
    https://s3.amazonaws.com/mayar/decoder_cleaning/DECODER/part-00000    




