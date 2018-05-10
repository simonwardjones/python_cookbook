import React from 'react';
import {Form, FormGroup, Input } from 'reactstrap';
import './SearchInput.css';

class SearchInput extends React.Component {
  handleChange = (event) => {
    this.props.textChange(event);
  }

  render() {
    return (
      <Form className="component-search-input">
        <FormGroup>
          <Input
            onChange={this.handleChange}
            placeholder="Search recipes ..."
          />
        </FormGroup>
      </Form>
    );
  }
}
export default SearchInput;