FROM node:19-alpine as build-stage
WORKDIR /frontend
COPY package*.json ./
RUN npm install
COPY . .

EXPOSE 80
CMD ["npm", "run", "dev", "--", "--host"]