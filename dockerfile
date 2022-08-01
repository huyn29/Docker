
FROM ubuntu:latest
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install openjdk-8-jdk
WORKDIR /usr/local/tomcat
ADD https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.63/bin/apache-tomcat-9.0.63.tar.gz .
RUN tar xvfz apache-tomcat-9.0.63.tar.gz
RUN mv apache-tomcat-9.0.63/* /usr/local/tomcat/
COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml 
COPY context.xml /usr/local/tomcat/webapps/manager/META-INF/context.xml 
EXPOSE 8080
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]