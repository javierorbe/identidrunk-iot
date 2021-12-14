import { client } from './connection.ts';
import { Person } from './entities/person.ts';

export async function findPerson(id: string): Promise<Person | null> {
  const query = `SELECT id, username FROM person WHERE ID = '${id}'`;
  const results = await client.queryObject(query);
  const users = results.rows;
  return users.length == 1 ? (users[0] as Person) : null;
}
