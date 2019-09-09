FROM python:3.6-slim
MAINTAINER Chris Ostrouchov

ARG VERSION=v1.1.0
ARG USERNAME=costrouc
ARG PROJECT=python-package-template

# Download package, install package, no cache
RUN pip install --no-cache-dir https://gitlab.com/$USERNAME/$PROJECT/repository/$VERSION/archive.tar.gz

ENTRYPOINT ["helloworld"]
CMD ["fizzbuzz", "-n", "10"]
