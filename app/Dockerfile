#########################################
# author: ashraf minhaj
# email : ashraf_minhaj@yahoo.com
# 
# date: 01-12-23
# the HushHub frontend applicaion
#########################################

FROM node:18 as builder
WORKDIR /app

COPY package*.json ./

RUN npm install

# runner stage
FROM node:18-alpine as runner
WORKDIR /app

# COPY --from=builder /app/node_modules ./node_modules
# COPY --from=builder app/package.json ./
# COPY --from=builder app/package-lock.json ./
COPY --from=builder /app .

# Copy the rest of the application code
COPY server.js ./
COPY views/ ./views

EXPOSE 3000

CMD ["npm", "start"]

# docker build -t front:1 -f Dockerfile.dev .
# docker run -p 3000:3000 --env-file .env front:1
# docker run -v /path/on/host:/usr/src/app/data -p 3000:3000 your-image-name

