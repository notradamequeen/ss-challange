import { Component } from 'react'
import { connect } from "react-redux";
import { 
  Card,
  Divider,
  Row,
  Space,
} from 'antd';
import ProductFrame from '../../components/ProductFrame'; 
import { getProducts } from '../../actions/products';


const { Meta } = Card;

class Products extends Component {
  constructor(props) {
    super(props);
    this.state = {
      products: []
    };
  }
  componentDidMount() {
    console.log(this.props, 'lis')
    this.props.products().then((data) => {
      this.setState({
        products: data.data
      })
      
    })
  }

  render() {
    return (
      <div>
        <Divider orientation="left">
          Products &nbsp;
          <Space size="midlde">
          </Space>
        </Divider>
        <Row gutter={[16, 24]}>
          {
            this.state.products.map(
              product => 
               <ProductFrame product={product}/>
              )
          }
        </Row>
      </div>
    )
  }
}


const mapStateToProps = state => {
  return {
    ...state
  };
};

const mapDispatchToProps = dispatch => {
  return {
   products: () => dispatch(getProducts())
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(Products);
