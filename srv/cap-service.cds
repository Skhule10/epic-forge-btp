
        namespace myApp;

        entity Books {
            key ID : Integer;
            title : String;
            author : String;
        }

        service CatalogService {
            entity Books as projection on Books;
        }
    