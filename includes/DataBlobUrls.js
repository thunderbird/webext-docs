const image = await fetch("https://raw.githubusercontent.com/thunderbird/sample-extensions/master/hello-world/images/internet.png")
const imageBlob = await image.blob();

// Retrieve a data: url.
const dataUrl = await new Promise(resolve => {
  var reader = new FileReader();
  reader.onload = (e) => resolve(e.target.result);
  reader.readAsDataURL(imageBlob);
})

// Retrieve a blob: url.
const blobUrl = URL.createObjectURL(imageBlob);