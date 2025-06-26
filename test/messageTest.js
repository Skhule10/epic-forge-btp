const cds = require('@sap/cds');
const { expect } = require('chai');

describe('Message Entity Tests', () => {
  let srv;

  before(async () => {
    srv = await cds.connect.to('ChatService');
  });

  it('should have a Messages entity', async () => {
    expect(srv.entities.Messages).to.exist;
  });

  it('should be able to create a Message', async () => {
    const result = await srv.run(INSERT.into(srv.entities.Messages).entries({
      ID: '12345',
      content: 'Hello World',
      timestamp: new Date(),
      sender: 'John Doe'
    }));
    expect(result).to.exist;
    expect(result.content).to.equal('Hello World');
  });
});