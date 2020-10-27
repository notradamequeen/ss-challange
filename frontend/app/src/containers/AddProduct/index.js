import { useState, Component } from 'react'
import {
  Card,
  Form,
  Input,
  Button,
  Radio,
  Select,
  Divider,
  Cascader,
  DatePicker,
  InputNumber,
  TreeSelect,
  Switch,
  Upload,
} from 'antd';
import { UploadOutlined } from '@ant-design/icons';

const { TextArea } = Input;


// const [form] = Form.useForm();
//   const [formLayout, setFormLayout] = useState('horizontal');

  // const onFormLayoutChange = ({ layout }) => {
  //   setFormLayout(layout);
  // };

// const formItemLayout =
//   formLayout === 'horizontal'
//     ? {
//         labelCol: {
//           span: 4,
//         },
//         wrapperCol: {
//           span: 14,
//         },
//       }
//     : null;
// const buttonItemLayout =
//   formLayout === 'horizontal'
//     ? {
//         wrapperCol: {
//           span: 14,
//           offset: 4,
//         },
//       }
//     : null;


class AddProduct extends Component {
  render() {
    return(
      <>
        <Divider orientation="left">Add new product</Divider>
        <Form
          labelCol={{
            span: 4,
          }}
          wrapperCol={{
            span: 14,
          }}
          layout="horizontal"
          initialValues={{
            size: 'default',
          }}
          // onValuesChange={onFormLayoutChange}
          size={'default'}
        >
          <Form.Item label="name">
            <Input />
          </Form.Item>
          <Form.Item label="description">
            <TextArea autoSize={{ minRows: 3, maxRows: 5 }}/>
          </Form.Item>
          <Form.Item label="Logo">
            <Upload>
              <Button icon={<UploadOutlined />}>Click to Upload</Button>
            </Upload>
          </Form.Item>
          <Form.Item label="Images">
            <Upload>
              <Button icon={<UploadOutlined />}>Click to Upload</Button>
            </Upload>
          </Form.Item>
          <Form.Item wrapperCol={{
              xs: { span: 24, offset: 0 },
              sm: { span: 16, offset: 8 },
            }}>
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Form.Item>
        </Form>
      </>
    )
  }
}

export default AddProduct;
