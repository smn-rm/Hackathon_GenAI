# FRONTEND
FROM node:21-alpine3.17
WORKDIR /usr/src/app

# install frontend dependencies
COPY package*.json ./
RUN npm install
# bundle frontend source
COPY . ./

# build frontend
RUN npm run build

# expose port
EXPOSE 8000

# start frontend
CMD ["npm", "run", "start"]