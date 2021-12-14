import { Application } from 'https://deno.land/x/oak/mod.ts';
import { organ } from 'https://raw.githubusercontent.com/denjucks/organ/master/mod.ts';
import { router } from './routes.ts';

async function main() {
  const app = new Application();

  // Routes
  app.use(organ());
  app.use(router.routes());
  app.use(router.allowedMethods());

  await app.listen({ port: 4000 });
}

await main();
