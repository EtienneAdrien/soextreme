# develop stage
FROM node:16 as develop-stage

WORKDIR /app

COPY package*.json ./

RUN npm install -g @quasar/cli

COPY . .

CMD ["npm", "run", "dev"]