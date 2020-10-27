import './App.css';
import styled from 'styled-components';
import { Switch, Route, Link, withRouter } from 'react-router-dom';
import Products  from './containers/Products';
import AddProduct  from './containers/AddProduct';
import 'antd/dist/antd.css';
import { Layout, Menu } from 'antd';
import ProductDetails from './containers/ProductDetails';

const { Header, Content, Footer } = Layout;


const AppWrapper = styled.div`
  max-width: calc(768px + 16px * 2);
  margin: 0 auto;
  display: flex;
  min-height: 100%;
  padding: 0 16px;
  flex-direction: column;
`;

function App() {
  return (
    <Layout>
      <Header style={{ position: 'fixed', zIndex: 1, width: '100%' }}>
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
          <Menu.Item key="1">
            <Link to="/products">Product List</Link>
          </Menu.Item>
          <Menu.Item key="2">
            <Link to="/add-product">
              Add Product
            </Link>
          </Menu.Item>
        </Menu>
      </Header>
      <Content className="site-layout" style={{ padding: '0 50px', marginTop: 64 }}>
        <Switch>
          <Route exact path = "/products" component = {Products} />
          <Route exact path = "/add-product" component = {AddProduct} />
          <Route exact path = "/products/:productId" children = {<ProductDetails/>} />
          
        </Switch>
      </Content>       
    </Layout>
  );
}

export default withRouter(App);
