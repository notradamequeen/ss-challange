import axios from 'axios';

export const fetchProducts = () => {
  axios.get(`http://127.0.0.1:5000/products/`, {
    params: {},
  })
  // .then((response) => {
  //   console.log(response)
  //   return {
  //       meta: {
  //           status: 'success'
  //       },
  //       data: response.data
  //   }
  // })
}
