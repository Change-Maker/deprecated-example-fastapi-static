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
