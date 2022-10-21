/**
 * Backward-compatible drop-in replacement for the deprecated
 * ComposeAttachment.getFile() function. Instead of calling
 * attachment.getFile(), call getFile(attachment).
 */
function getFile(attachment) {
    let file = "getAttachmentFile" in browser.compose
        ? messenger.compose.getAttachmentFile(attachment.id)
        : attachment.getFile();
    return file;
}
