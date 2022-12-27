FROM node:19-alpine as build-stage
WORKDIR /frontend
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:stable-alpine as production-stage
RUN rm /etc/nginx/conf.d/default.conf
COPY --from=build-stage /frontend/dist /usr/share/nginx/html
COPY ./proxy/nginx.conf /etc/nginx

RUN mkdir -p /vol/static && \
    chmod 755 /vol/static

VOLUME /vol/static

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]