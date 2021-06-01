function decodeBinaryString(binaryString, inputEncoding = "utf-8") {
    const buffer = new ArrayBuffer(binaryString.length);
    const bufferView = new Uint8Array(buffer);
    for (let i = 0; i < binaryString.length; i++) {
        bufferView[i] = binaryString.charCodeAt(i);
    }
    let utf8decoder = new TextDecoder(inputEncoding);
    return utf8decoder.decode(buffer);
}