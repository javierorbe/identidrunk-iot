import { db } from './connection.ts';
import { AlcoholSchema } from './schemas.ts';

const AlcoholCollection = db.collection<AlcoholSchema>('alcohols');

export { AlcoholCollection };
