FROM node:latest as build-stage

RUN mkdir usr/src/app

COPY . /usr/src/app

ENV PATH /usr/src/app/node_modules/ .bin:$PATH

RUN yarn 

CMD ["npm", "start"]


# FROM node:latest as build-stage
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY ./ .
# RUN npm run build

# FROM nginx:latest as production-stage
# RUN mkdir /app
# COPY --from=build-stage /app/dist /app
# COPY nginx.conf /etc/nginx/nginx.conf