/**
 * Returns the trash folder of the account a given message belongs to. The
 * accountsRead permission is required.
 */
async function getTrashFolderForMessage(msgId) {
    let msg = await messenger.messages.get(msgId);
    let account = await messenger.accounts.get(msg.folder.accountId);
    return account.folders.find(folder => folder.type == "trash");
}
