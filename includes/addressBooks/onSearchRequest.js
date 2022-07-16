messenger.addressBooks.provider.onSearchRequest.addListener(async (node, searchString, query) => {
    let response = await fetch("https://people.acme.com/?query=" + searchString);
    let json = await response.json();
    return {
        isCompleteResult: true,
        // Return an array of ContactProperties as results.
        results: json.map(contact => ({
            DisplayName: contact.name,
            PrimaryEmail: contact.email
        }))
    };
    
}, {
    addressBookName: "ACME employees",
    isSecure: true,
});
