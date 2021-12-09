import { config } from 'https://deno.land/x/dotenv/mod.ts';
import { Client } from 'https://deno.land/x/postgres/mod.ts';

const {
  POSTGRES_HOSTNAME,
  POSTGRES_DATABASE,
  POSTGRES_USERNAME,
  POSTGRES_PASSWORD,
} = config();

// You can use the connection interface to set the connection properties
const postgresConfig = {
  applicationName: 'my_custom_app',
  connection: {
    attempts: 1,
  },
  database: POSTGRES_DATABASE,
  hostname: POSTGRES_HOSTNAME,
  password: POSTGRES_PASSWORD,
  port: 5432,
  user: POSTGRES_USERNAME,
  tls: {
    enforce: false,
  },
};

console.log(config());

const client = new Client(postgresConfig);
await client.connect();
await client.end();

export { client };
