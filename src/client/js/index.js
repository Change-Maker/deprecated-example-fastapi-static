window.onload = function () {
  console.log('This is Home page.');
  const url = '/hello';
  axios
    .get(url)
    .then((resp) => {
      console.log(`GET ${url} with response:`, resp);
      console.log('Data:', resp?.data);
    })
    .catch((err) => {
      console.error(`GET ${url} with error:`, err);
    });
};
