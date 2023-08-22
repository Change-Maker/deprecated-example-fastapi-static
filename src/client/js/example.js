const uploadTxtFile = function uploadTxtFile(self) {
  console.log('Triggered onclick event on element:', self);
  const files = document.getElementById('select-txt-file').files;
  if (files.length) {
    console.log('upload this file:', files[0]);
    const formData = new FormData();
    formData.append('txtFile', files[0], files[0].name);
    const url = '/example/txt-file';
    axios
      .post(
        url,
        formData,
        {
          headers: { 'Content-Type': 'multipart/form-data' },
        },
      )
      .then((resp) => {
        console.log(`POST ${url}: response:`, resp);
      })
      .catch((err) => {
        console.error(`Failed to POST ${url}:`, err);
      });

    return;
  }
  console.warn('Please select a txt file first.');
}

window.onload = function () {
  console.log('This is Example page.');

  // Setup buttons.
  document.getElementById('post-user').onclick = function () {
    const url = '/example/user';
    const user = { name: 'alfa', age: 18, isVerified: true };
    axios
      .post(url, user)
      .then((resp) => {
        console.log(`POST ${url}: response:`, resp);
      })
      .catch((err) => {
        console.error(`Failed to POST ${url}:`, err);
      });
  };

  document.getElementById('get-users').onclick = function () {
    const url = '/example/users';
    axios
      .get(url)
      .then((resp) => {
        console.log(`GET ${url}: response:`, resp);
      })
      .catch((err) => {
        console.error(`Failed to GET ${url}:`, err);
      });
  };
};
