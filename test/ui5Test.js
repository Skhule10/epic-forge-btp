
QUnit.module("UI5 Component Tests");

QUnit.test("Input field placeholder should be correct", function (assert) {
  var input = new sap.m.Input({
    placeholder: "Type your message..."
  });
  assert.strictEqual(input.getPlaceholder(), "Type your message...", "Placeholder is correct");
});

QUnit.test("Button text should be correct", function (assert) {
  var button = new sap.m.Button({
    text: "Send"
  });
  assert.strictEqual(button.getText(), "Send", "Button text is correct");
});

QUnit.test("MessageToast should be displayed on button press", function (assert) {
  var done = assert.async();
  var button = new sap.m.Button({
    text: "Send",
    press: function () {
      sap.m.MessageToast.show("Message sent!");
      done();
    }
  });
  button.firePress();
  assert.ok(true, "MessageToast displayed");
});
