import { Router } from 'https://deno.land/x/oak/mod.ts';
import { AlcoholCollection } from './db/collections.ts';

export const router = new Router();

router.get('/api/auth', async ctx => {
  const { request } = ctx;
  const uid = request.url.searchParams.get('uid');
  console.log(uid);

  const data: any = await AlcoholCollection.find().toArray();
  console.log(data);
});

router.post('/api/alcohol', async ctx => {
  const { request, response } = ctx;

  const body = request.body();
  const { uid, alcoholLevel } = await body.value;

  console.log(uid, alcoholLevel);

  response.body = 'Hello World!';
  response.status = 201;
});
