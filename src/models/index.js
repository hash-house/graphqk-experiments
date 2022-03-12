// @ts-check
import { initSchema } from '@aws-amplify/datastore';
import { schema } from './schema';



const { Simple, TrailAssignment, Kennel, User, Event, Trail, KennelUser, KennelEvent, UserEvent } = initSchema(schema);

export {
  Simple,
  TrailAssignment,
  Kennel,
  User,
  Event,
  Trail,
  KennelUser,
  KennelEvent,
  UserEvent
};