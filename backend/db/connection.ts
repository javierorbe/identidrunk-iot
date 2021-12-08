import { MongoClient, Database } from 'https://deno.land/x/mongo/mod.ts';
import { config } from 'https://deno.land/x/dotenv/mod.ts';

const { MONGO_DB_NAME, MONGO_DB_USERNAME, MONGO_DB_PASSWORD } = config();

// Create client
const client = new MongoClient();

// Connect to mongodb
await client.connect('mongodb://localhost:27017');

// Give your database a name
const db = client.database(MONGO_DB_NAME);

export { db };
