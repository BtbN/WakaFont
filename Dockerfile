FROM python:alpine3.17

RUN apk add --no-cache bash git build-base ruby-bundler ruby-dev woff2 zlib-dev musl-dev linux-headers fontforge
RUN git clone https://github.com/bramstein/sfnt2woff-zopfli.git w && cd w && make -j$(nproc) && mv sfnt2woff-zopfli /usr/local/bin/sfnt2woff && cd .. && rm -rf w
RUN git clone https://github.com/panorama-ed/fontcustom.git w && cd w && gem build fontcustom.gemspec && gem install --no-document fontcustom*.gem
