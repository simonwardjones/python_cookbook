import React from 'react';
import PropTypes from 'prop-types';
import { ListGroup, CardTitle } from 'reactstrap';
import RecipeResult from './RecipeResult';
import './RecipeResults.css';

class RecipeResults extends React.Component {
  render() {
    const listItems = this.props.recipeData.map((recipeData) =>
    <RecipeResult  key={recipeData.title}
          recipeData={recipeData}
    />
    );
    return (
      <div>
    <CardTitle>
      {this.props.section}
    </CardTitle>
    <ListGroup>
      {listItems}
    </ListGroup>
    </div>
  );
  }
}

RecipeResults.propTypes = {
  recipeData: PropTypes.array,
};
export default RecipeResults;