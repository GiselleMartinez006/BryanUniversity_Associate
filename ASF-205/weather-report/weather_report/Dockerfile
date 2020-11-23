FROM node:12.2.0-alpine as react_build 
#also say 
WORKDIR /app
#copy the react app to the container
COPY . /app/ 
# #prepare the contiainer for building react 
RUN npm install --silent
RUN npm install react-scripts@3.0.1 -g --silent 
RUN npm run build 

#prepare nginx
FROM nginx:1.16.0-alpine
COPY --from=react_build /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY /nginx.conf /etc/nginx/conf.d

#fire up nginx
EXPOSE 80 
CMD ["nginx","-g","daemon off;"]

# FROM node:latest as build-deps
# WORKDIR /urs/src/app
# COPY package*.json ./
# RUN npm install
# COPY ./ .
# RUN npm build

# FROM nginx:latest as production-stage
# RUN mkdir /app
# COPY --from=build-deps /usr/src/app/build /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]


# # Stage 1 - the build process
# FROM node:7.10 as build-deps
# WORKDIR /usr/src/app
# COPY package.json yarn.lock ./
# RUN yarn
# COPY . ./
# RUN yarn build

# # Stage 2 - the production environment
# FROM nginx:1.12-alpine
# COPY --from=build-deps /usr/src/app/build /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]

