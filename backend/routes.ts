import { Router } from 'https://deno.land/x/oak/mod.ts';
import { v4 as uuidV4 } from 'https://deno.land/std@0.82.0/uuid/mod.ts';
import './db/connection.ts';
import { findPerson } from './db/person.ts';
import { insertTest } from './db/test.ts';

const NOT_FOUND = 404;
const BAD_REQUEST = 400;
const CREATED = 201;

export const router = new Router();

router.get('/api/auth', async ctx => {
  const { request, response } = ctx;
  const uid = request.url.searchParams.get('uid') as string;

  // validate uuid format
  if (!uuidV4.validate(uid)) {
    return uuidNotValidResponse(response);
  }

  // Get person
  const person = await findPerson(uid);
  if (!person) {
    return personNotFoundResponse(response);
  }

  // Send successful response
  response.body = person;
  return response;
});

router.post('/api/alcohol', async ctx => {
  const { request, response } = ctx;

  const body = request.body();
  const { uid, alcoholLevel } = await body.value;

  // Verify person
  const person = await findPerson(uid);
  if (!person) {
    return personNotFoundResponse(response);
  }

  // Insert test
  const isInserted = await insertTest(uid, alcoholLevel);

  if (!isInserted) {
    return testWasNotInserted(response);
  }

  // Send successful response
  response.status = CREATED;
  return response;
});

function uuidNotValidResponse(response: any) {
  response.status = BAD_REQUEST;
  response.body = { message: 'Identifies is not valid (use UUID format)' };
  return response;
}

function personNotFoundResponse(response: any) {
  response.status = NOT_FOUND;
  response.body = { message: 'Person not found' };
  return response;
}

function testWasNotInserted(response: any) {
  response.status = BAD_REQUEST;
  response.body = { message: 'Test was not inserted' };
  return response;
}
