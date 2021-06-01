function rawToUtf8(binaryString) {
    const buffer = new ArrayBuffer(binaryString.length);
    const bufferView = new Uint8Array(buffer);
    for (let i = 0; i < binaryString.length; i++) {
        bufferView[i] = binaryString.charCodeAt(i);
    }
    let utf8decoder = new TextDecoder();
    return utf8decoder.decode(buffer);
}