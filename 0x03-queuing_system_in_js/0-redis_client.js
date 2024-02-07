import redis from 'redis';

// new redis client
const client = redis.createClient(); 

// listen -> redis server connection(default -> 127.0.0.1 and port 6379)
client.on('connect', () => console.log('Redis client connected to the server'));

// listen -> failure
client.on('error', (err) => console.error(`Redis client not connected to the server: ${err.message}`));
