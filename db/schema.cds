namespace chat;

entity Message {
  key ID : UUID;
  content : String;
  timestamp : DateTime;
  sender : String;
}