import { Router } from 'https://deno.land/x/oak/mod.ts';

export const router = new Router();

// GET request to "/api/helloworld"
router.post('/api/alcohol', async ctx => {
  const { request, response } = ctx;

  const body = request.body();
  const { uid, alcoholLevel } = await body.value;

  console.log(uid, alcoholLevel);

  response.body = 'Hello World!';
  response.status = 201;
});
