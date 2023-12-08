// server.js

const express = require('express');
const dotenv = require('dotenv');
const path = require('path');
const cors = require("cors");

// Load environment variables from .env file
dotenv.config();

const app = express();

// get env vars
const PORT = process.env.PORT || 3000;
// const TRUSTED_BACKEND = process.env.BACKEND_API_URL || "";

const whitelist = [ "http://localhost:80"]
const corsOptions = {
  origin: function (origin, callback) {
    if (!origin || whitelist.indexOf(origin) !== -1) {
      callback(null, true)
    } else {
      callback(new Error("Not allowed by CORS"))
    }
  },
  credentials: true,
}
app.use(cors(corsOptions))

// app.get("/", (req, res) => {
//   res.send({ message: "Hello World!" })
// })

// Set EJS as the view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

// Health endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'OK' });
});

// Serve the HTML file using EJS
app.get('/', (req, res) => {
    const apiUrl = process.env.BACKEND_API_URL;
    console.log(apiUrl)
    res.render('index', { apiUrl });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
