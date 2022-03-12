import { ModelInit, MutableModel, PersistentModelConstructor } from "@aws-amplify/datastore";





type SimpleMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

type TrailAssignmentMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

type KennelMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

type UserMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

type EventMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

type TrailMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

type KennelUserMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

type KennelEventMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

type UserEventMetaData = {
  readOnlyFields: 'createdAt' | 'updatedAt';
}

export declare class Simple {
  readonly id: string;
  readonly name: string;
  readonly createdAt?: string;
  readonly updatedAt?: string;
  constructor(init: ModelInit<Simple, SimpleMetaData>);
  static copyOf(source: Simple, mutator: (draft: MutableModel<Simple, SimpleMetaData>) => MutableModel<Simple, SimpleMetaData> | void): Simple;
}

export declare class TrailAssignment {
  readonly id: string;
  readonly trailID: string;
  readonly userID: string;
  readonly createdAt?: string;
  readonly updatedAt?: string;
  constructor(init: ModelInit<TrailAssignment, TrailAssignmentMetaData>);
  static copyOf(source: TrailAssignment, mutator: (draft: MutableModel<TrailAssignment, TrailAssignmentMetaData>) => MutableModel<TrailAssignment, TrailAssignmentMetaData> | void): TrailAssignment;
}

export declare class Kennel {
  readonly id: string;
  readonly geolocation: string;
  readonly description: string;
  readonly start?: number;
  readonly created_by?: string;
  readonly updated_by?: string;
  readonly created_at?: number;
  readonly updated_at?: number;
  readonly Users?: (KennelUser | null)[];
  readonly logo?: string;
  readonly banner_image?: string;
  readonly Events?: (KennelEvent | null)[];
  readonly createdAt?: string;
  readonly updatedAt?: string;
  constructor(init: ModelInit<Kennel, KennelMetaData>);
  static copyOf(source: Kennel, mutator: (draft: MutableModel<Kennel, KennelMetaData>) => MutableModel<Kennel, KennelMetaData> | void): Kennel;
}

export declare class User {
  readonly id: string;
  readonly names: string;
  readonly created_by: string;
  readonly created_at: number;
  readonly updated_at: number;
  readonly updated_by: string;
  readonly email: string;
  readonly EventRegistration?: (UserEvent | null)[];
  readonly kennels?: (KennelUser | null)[];
  readonly avatar?: string;
  readonly images?: (string | null)[];
  readonly TrailAssignments?: (TrailAssignment | null)[];
  readonly createdAt?: string;
  readonly updatedAt?: string;
  constructor(init: ModelInit<User, UserMetaData>);
  static copyOf(source: User, mutator: (draft: MutableModel<User, UserMetaData>) => MutableModel<User, UserMetaData> | void): User;
}

export declare class Event {
  readonly id: string;
  readonly start: number;
  readonly end?: number;
  readonly location: string;
  readonly latitude: number;
  readonly longitude: number;
  readonly name: string;
  readonly description: string;
  readonly created_by: string;
  readonly updated_by: string;
  readonly created_at: number;
  readonly updated_at: number;
  readonly Trails?: (Trail | null)[];
  readonly users?: (UserEvent | null)[];
  readonly images?: (string | null)[];
  readonly kennels?: (KennelEvent | null)[];
  readonly createdAt?: string;
  readonly updatedAt?: string;
  constructor(init: ModelInit<Event, EventMetaData>);
  static copyOf(source: Event, mutator: (draft: MutableModel<Event, EventMetaData>) => MutableModel<Event, EventMetaData> | void): Event;
}

export declare class Trail {
  readonly id: string;
  readonly details: string;
  readonly description: string;
  readonly start: number;
  readonly latitude: number;
  readonly longitude: number;
  readonly created_by: string;
  readonly updated_by: string;
  readonly created_at: number;
  readonly updated_at: number;
  readonly eventID?: string;
  readonly images?: (string | null)[];
  readonly features?: (string | null)[];
  readonly TrailAssignments?: (TrailAssignment | null)[];
  readonly createdAt?: string;
  readonly updatedAt?: string;
  constructor(init: ModelInit<Trail, TrailMetaData>);
  static copyOf(source: Trail, mutator: (draft: MutableModel<Trail, TrailMetaData>) => MutableModel<Trail, TrailMetaData> | void): Trail;
}

export declare class KennelUser {
  readonly id: string;
  readonly kennel: Kennel;
  readonly user: User;
  readonly createdAt?: string;
  readonly updatedAt?: string;
  constructor(init: ModelInit<KennelUser, KennelUserMetaData>);
  static copyOf(source: KennelUser, mutator: (draft: MutableModel<KennelUser, KennelUserMetaData>) => MutableModel<KennelUser, KennelUserMetaData> | void): KennelUser;
}

export declare class KennelEvent {
  readonly id: string;
  readonly kennel: Kennel;
  readonly event: Event;
  readonly createdAt?: string;
  readonly updatedAt?: string;
  constructor(init: ModelInit<KennelEvent, KennelEventMetaData>);
  static copyOf(source: KennelEvent, mutator: (draft: MutableModel<KennelEvent, KennelEventMetaData>) => MutableModel<KennelEvent, KennelEventMetaData> | void): KennelEvent;
}

export declare class UserEvent {
  readonly id: string;
  readonly user: User;
  readonly event: Event;
  readonly createdAt?: string;
  readonly updatedAt?: string;
  constructor(init: ModelInit<UserEvent, UserEventMetaData>);
  static copyOf(source: UserEvent, mutator: (draft: MutableModel<UserEvent, UserEventMetaData>) => MutableModel<UserEvent, UserEventMetaData> | void): UserEvent;
}