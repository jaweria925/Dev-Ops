From node:18.16.0

# set the working directory
WORKDIR /app

#copy the package.json and package-lock.json files and install dependencies

COPY package*.json ./
RUN npm install

#copy the rest of the application code
COPY . .

#Expose the port the app runs on
EXPOSE 3000

#start the application
CMD ["npm", "start"]

