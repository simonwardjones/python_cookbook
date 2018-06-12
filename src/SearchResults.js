import React from 'react';
import './SearchResults.css';
import RecipeResults from './RecipeResults';
import SearchInput from './SearchInput';
import { Container, Row, Col } from 'reactstrap';
import { Card, CardBody } from 'reactstrap';

class searchResults extends React.Component {

  render() {
    const sectioned_results = Object.keys(this.props.filteredRecipes).map(function(key) {
      // console.log('simon',this.props.filteredRecipes[key])
      return <RecipeResults key={key}
                section={key}
                recipeData={this.props.filteredRecipes[key]}
      />
    },this)


    return (
      <Container>
      <Row>
        <Col>
        <SearchInput
          textChange={this.props.onFilterTextChange}
        />
        </Col>
      </Row>
      
      <Row>
        <Col>
          {sectioned_results}
        </Col>
      </Row>
      <Row  className="footer"></Row>
      </Container>
    );
  }
}

export default searchResults;