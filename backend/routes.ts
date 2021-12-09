import { Router } from 'https://deno.land/x/oak/mod.ts';
import { client } from './db/connection.ts';
import './db/connection.ts';

export const router = new Router();

router.get('/api/auth', async (ctx: any) => {
  const { request } = ctx;
  const uid = request.url.searchParams.get('uid');

  // const array_result = await client.queryArray('SELECT ID, NAME FROM PEOPLE');
  // console.log(array_result.rows); // [[1, 'Carlos'], [2, 'John'], ...]

  console.log(uid);
});

router.post('/api/alcohol', async ctx => {
  const { request, response } = ctx;

  const body = request.body();
  const { uid, alcoholLevel } = await body.value;

  console.log(uid, alcoholLevel);

  response.body = 'Hello World!';
  response.status = 201;
});
