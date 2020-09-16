# FROM nginx
# COPY . /usr/share/nginx/html

FROM node:12.16.3

WORKDIR /serverdata

ENV PORT 80

COPY package.json  /serverdata/package.json

RUN npm install

RUN npm install vim

COPY . /serverdata

CMD ["node","server.js"] 