import { Application } from 'https://deno.land/x/oak/mod.ts';
import { router } from './routes.ts';

async function main() {
  const app = new Application();

  // Routes
  app.use(router.routes());
  app.use(router.allowedMethods());

  await app.listen({ port: 4000 });
}

await main();
