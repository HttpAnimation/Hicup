const express = require('express');
const os = require('os');
const app = express();
const path = require('path');

const photosPath = path.join(__dirname, 'photos');
const videosPath = path.join(__dirname, 'videos');

app.use('/photos', express.static(photosPath));
app.use('/videos', express.static(videosPath));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

const getLocalIpAddress = () => {
    const interfaces = os.networkInterfaces();
    for (const interfaceName in interfaces) {
        const addresses = interfaces[interfaceName];
        for (const address of addresses) {
            if (address.family === 'IPv4' && !address.internal) {
                return address.address;
            }
        }
    }
    return 'localhost'; // Default to localhost if no suitable address is found
};

const PORT = 3000;
const HOST = getLocalIpAddress();

const server = app.listen(PORT, HOST, () => {
    console.log(`Server is running on http://${HOST}:${PORT}`);
    console.log(`Access the website from other devices using: http://${HOST}:${PORT}`);
});

// Gracefully handle Ctrl+C
process.on('SIGINT', () => {
    console.log('Stopping server...');
    server.close(() => {
        console.log('Server stopped.');
        process.exit(0);
    });
});
