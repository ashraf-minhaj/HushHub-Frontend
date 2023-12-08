// server.js

const express = require('express');
const dotenv = require('dotenv');
const path = require('path');

// Load environment variables from .env file
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

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
