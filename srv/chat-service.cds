using chat from '../db/schema';

service ChatService {
  entity Messages as projection on chat.Message;
}