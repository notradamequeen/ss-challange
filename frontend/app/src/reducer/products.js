
import { GET_PRODUCTS_SUCCESS } from '../constants';

const initialState = {
  meta: {
    status: 'LOADING',
  },
  data: []
}

export const products = (state, action) => {
  console.log('action', action)
  switch (action.type) {
    case GET_PRODUCTS_SUCCESS:
      return {
        ...state,
        meta: {
          status: 'SUCCESS'
        },
        data: action.payload
      }
    default:
      return initialState
  }
}
