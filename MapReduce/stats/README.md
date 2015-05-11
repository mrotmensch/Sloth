# MapReduce for Wikipedia namespace statistics

The programs in this folder are step 4 of the data processing pipeline. 
The step can re run seperately from the graph analysis.

1. The folder most\_popular\_article\_incoming contains a program that calculated the top 3 most linked-to articles (uses only the articles namespace).
2. The folder most\_popular\_incoming contains a program that calculated the top 3 most linked-to pages (across all namespaces)
3. The folder most\_popular\_article\_outgoing contains a program that calculated the top 3 articles with the most outgoing links(uses only the articles namespace).
4. The folder most\_popular\_outgoing contains a program that calculated the top 3 pages with the most outgoing links (across all namespaces).