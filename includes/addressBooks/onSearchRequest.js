messenger.addressBooks.onSearchRequest.addListener(async (node, searchString) => {
    // Return an array of ContactProperties.
    let response = await fetch("https://people.acme.com/?query=" + searchString);
    return response.json.map(contact => (
        { 
            DisplayName: contact.name, 
            PrimaryEmail: contact.email
        }
    ));
}, {
    dirName: "ACME employees",
    isSecure: true,
});
