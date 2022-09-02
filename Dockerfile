FROM python:3.9 as compiler
RUN cd lib \
&& wget "https://sourceforge.net/projects/ta-lib/files/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz" \
&& tar -xvzf ta-lib-0.4.0-src.tar.gz ta-lib/ \
&& rm ta-lib-0.4.0-src.tar.gz
RUN cd /lib/ta-lib \
&& ./configure --build=aarch64-unknown-linux-gnu \
&& make \
&& make install
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
ADD . /marketbot/