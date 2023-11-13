const express = require('express');
const app = express();
const path = require('path');

const photosPath = path.join(__dirname, 'photos');
const videosPath = path.join(__dirname, 'videos');

app.use('/photos', express.static(photosPath));
app.use('/videos', express.static(videosPath));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

const PORT = 3000;
const server = app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Gracefully handle Ctrl+C
process.on('SIGINT', () => {
    console.log('Stopping server...');
    server.close(() => {
        console.log('Server stopped.');
        process.exit(0);
    });
});
