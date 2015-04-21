
/*
`page_id` int(8) unsigned NOT NULL AUTO_INCREMENT,
  `page_namespace` int(11) NOT NULL DEFAULT '0',
  `page_title` varbinary(255) NOT NULL DEFAULT '',
  `page_restrictions` tinyblob NOT NULL,
  `page_counter` bigint(20) unsigned NOT NULL DEFAULT '0',
  `page_is_redirect` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `page_is_new` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `page_random` double unsigned NOT NULL DEFAULT '0',
  `page_touched` varbinary(14) NOT NULL DEFAULT '',
  `page_links_updated` varbinary(14) DEFAULT NULL,
  `page_latest` int(8) unsigned NOT NULL DEFAULT '0',
  `page_len` int(8) unsigned NOT NULL DEFAULT '0',
  `page_content_model` varbinary(32) DEFAULT NULL,*/

/*Get rid of unnecesary files*/
Pages_rel = FOREACH Pages GENERATE page_id,page_namespace,page_title;

Wiki = LOAD 'WIKI/part-00000' USING PigStorage(',') AS (from:int,namespace:int,title:chararray,from_namespace:int);

/*
`pl_from` int(8) unsigned NOT NULL DEFAULT '0',
  `pl_namespace` int(11) NOT NULL DEFAULT '0',
  `pl_title` varbinary(255) NOT NULL DEFAULT '',
  `pl_from_namespace` int(11) NOT NULL DEFAULT '0' */


/* Merge on title so we have id to id*/
B = JOIN Wiki by title, Pages_rel by page_title;

C = FOREACH B GENERATE Wiki::from, Pages_rel::page_id ;


store C into 'csvoutput' using PigStorage('\t','-schema');

/* only want links from articles to articles */

