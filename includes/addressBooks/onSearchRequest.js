messenger.addressBooks.provider.onSearchRequest.addListener(async (node, searchString, query) => {
    // Return an array of ContactProperties.
    let results = [];
    fetch("https://people.acme.com/?query=" + searchString)
        .then(response => response.json())
        .then(contacts => {
            for (const contact of contacts) {
                results.push({
                    DisplayName: contact.name, 
                    PrimaryEmail: contact.email
                });
            }
            return { results: results, isCompleteResult: true }
        });
    
}, {
    addressBookName: "ACME employees",
    isSecure: true,
});
