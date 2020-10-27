import { Component } from 'react';
import { Card, Col } from 'antd';
import { 
  EditOutlined,
  EyeOutlined 
} from '@ant-design/icons';
import { Link } from 'react-router-dom';

const { Meta } = Card;

class ProductFrame extends Component {
  componentDidUpdate() {
    console.log('product frame', this.props.product)
  }

  render() {
    return (
      <Col className="gutter-row" span={6}>
        <Card
          style={{ width: 300 }}
          cover={
            <img
              alt="example"
              src={this.props.product.logo}
            />
          }
          actions={[
            <Link to={`/products/${this.props.product.id}/edit`}><EditOutlined key="setting" /></Link>,
            <Link to={`/products/${this.props.product.id}`}><EyeOutlined key="edit" /></Link>,
          ]}
        >
          <Meta
            title={this.props.product.name}
            description={this.props.product.description? this.props.product.description: "-"}
          />
        </Card>
      </Col>
    )
  }
}

export default ProductFrame;
