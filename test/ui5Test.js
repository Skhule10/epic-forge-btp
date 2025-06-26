
const { expect } = require('chai');
describe('UI5 Button Test', () => {
    it('should alert when button is pressed', () => {
        const button = document.getElementById('myButton');
        button.click();
        expect(window.alert).to.have.been.calledWith('Button Pressed!');
    });
});
