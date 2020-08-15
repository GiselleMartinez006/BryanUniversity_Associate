# FROM nginx
# COPY . /usr/share/nginx/html

FROM node:12.16.3

WORKDIR /clientdata

ENV PORT 3000

# COPY package.json  /clientdata/package.json

RUN npx create-react-app .

COPY src/. /clientdata/src/

CMD ["npm","start"] 