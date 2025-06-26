
        const cds = require('@sap/cds');
        const { expect } = require('chai');

        describe('CAP Service Tests', () => {
            it('should return list of books', async () => {
                const CatalogService = await cds.connect.to('CatalogService');
                const books = await CatalogService.read('Books');
                expect(books).to.be.an('array');
            });
        });
    