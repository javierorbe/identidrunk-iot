import { client } from './connection.ts';

/**
 * Insert a row of alcohol test.
 * @param id Person id
 * @returns
 */
export async function insertTest(personId: string, alcoholLevel: string) {
  const query = `INSERT INTO "test" (person_id, alcohol_level) VALUES ('${personId}', ${alcoholLevel})`;
  try {
    await client.queryObject(query);
    return true;
  } catch (e) {
    console.error(e);
    return false;
  }
}
