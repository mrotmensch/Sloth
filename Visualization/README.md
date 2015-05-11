# Deploying WebDemo on AWS Elastic Beanstalk

## Download AWS Elastic Beanstalk Command Line Tool

The tool can be found here: http://aws.amazon.com/code/6752709412171743. 

```sh
wget https://s3.amazonaws.com/elasticbeanstalk/cli/AWS-ElasticBeanstalk-CLI-2.6.4.zip
```

Once you have the tool make sure your system knows where to find it. For example, you can edit your ~/.bashrc to include the folowing lines: 

```sh
AWS_Path= foo/../AWS-EB-CLI-2.6.4/eb/linux/python2.7
PATH=$PATH:${AWS_Path}
```

## Initialize a new git repo and start a EB instance

Elastic Beanstalk uses git to push changes to your site. Initialize a new repo like normal.

```sh
git init
```

Start Elastic Beanstalk

```sh
eb init
```

Answer all the questions and select your options. When complete, start Elastic Beanstalk.

```sh
eb start
```

## Add Files

Files are added in almost the same way as regular git. Note, the push command is replaced with aws.push. 

```sh
git add .
git commit -m “First Commit”
git aws.push
```
The page should be up and running!


