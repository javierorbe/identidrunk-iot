
// import { config } from 'https://deno.land/x/dotenv/mod.ts';
// app.ts
import "https://deno.land/x/dotenv/load.ts";
import { Client } from 'https://deno.land/x/postgres/mod.ts';

// const { DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD } = config();
const DB_HOST = Deno.env.get('DB_HOST')
const DB_DATABASE = Deno.env.get('DB_DATABASE')
const DB_USER = Deno.env.get('DB_USER')
const DB_PASSWORD = Deno.env.get('DB_PASSWORD')


// You can use the connection interface to set the connection properties
const postgresConfig = {
  applicationName: 'my_custom_app',
  connection: {
    attempts: 1,
  },
  database: DB_DATABASE,
  hostname: DB_HOST,
  password: DB_PASSWORD,
  port: 5432,
  user: DB_USER,
  tls: {
    enforce: false,
  },
};

const client = new Client(postgresConfig);

function tryToConnect(n: number) {
  if (n === 0) {
    console.log('Could not connect to database.');
    return;
  }

  if (client.connected) {
    console.log('Connected to database ✔️');
    return;
  }
  console.log(
    `Trying to connect to database`
  );

  setTimeout(async () => {
    await client.connect();
    tryToConnect(n--);
  }, 3000);
}
const tries = 10;
tryToConnect(tries);

export { client };
