FROM ubuntu:15.04

RUN apt-get update && apt-get install -y iputils-ping apache2


# for example docker run hw2 Hellowwwww there! would pass
# arguments to the entry point so docker run hw2 Hellowwwww there!
# ENTRYPOINT ["echo"]

#ENV var1=Ralph var2=duke

#example using variables with CMD
ENV var1=ping var2=8.8.8.8
CMD $var1 $var2

#ENTRYPOINT ["apache2ctl"]
#docker run -d -p 80:80 web2 -D FOREGROUND would pass the arguments. CMD could be used to indicate defaults
