import React from 'react';
import { Jumbotron } from 'reactstrap';

class Header extends React.Component {

  render() {
    return (
      <div>
        <Jumbotron>
        <div className="container">
          <img src="./favicon.ico" alt="sorry" />
          <h1>Python Cookbook</h1>
          <p>
          A collection of python recipes
          </p>
        </div>
        </Jumbotron>
      </div>
    );
  }
}
export default Header;