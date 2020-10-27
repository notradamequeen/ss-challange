import { fetchProducts } from '../api/handler';
import { 
  GET_PRODUCTS_SUCCESS,
  GET_PRODUCTS_LOADING,
  GET_PRODUCT_LOADING,
  GET_PRODUCT_SUCCESS
} from '../constants';
import axios from 'axios';

export const getProducts = () =>  {
  return dispatch => {
    dispatch({
      type: GET_PRODUCTS_LOADING,
      payload: []
    })
    return axios.get(`http://127.0.0.1:5000/products/`, {
      params: {},
    }).then((response) => {
      dispatch({
        type: GET_PRODUCTS_SUCCESS,
        payload: response.data
      })
      return response
    })
  }
}

export const getProduct = (productId) =>  {
  return dispatch => {
    dispatch({
      type: GET_PRODUCT_LOADING,
      payload: []
    })
    return axios.get(`http://127.0.0.1:5000/products/${productId}/`, {
      params: {},
    }).then((response) => {
      dispatch({
        type: GET_PRODUCT_SUCCESS,
        payload: response.data
      })
      return response
    })
  }
}
