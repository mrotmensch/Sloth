cd ~/
sudo yum install git
wget http://apache.arvixe.com/maven/maven-3/3.3.1/binaries/apache-maven-3.3.1-bin.zip
unzip apache-maven-3.3.1-bin.zip
alias mvn=/home/hadoop/apache-maven-3.3.1/bin/mvn

cd /usr/local/
sudo git clone https://github.com/apache/giraph.git
sudo chown -R hadoop:hadoop giraph
export GIRAPH_HOME=/usr/local/giraph
cd $GIRAPH_HOME
git checkout release-1.1
mvn -Phadoop_2 -fae -DskipTests -Dhadoop=non_secure clean install

cd ~/
wget https://services.gradle.org/distributions/gradle-2.3-all.zip
unzip gradle-2.3*
alias gradle=~/gradle-2.3/bin/gradle

git clone https://github.com/Sotera/distributed-graph-analytics.git
cd Sotera*
gradle clean dist

cd ~/
mkdir project
cd project
wget http://s3.amazonaws.com/jmjnyu/examples.zip
unzip examples.zip

hadoop fs -mkdir /project
hadoop fs -copyFromLocal examples/* /project/

