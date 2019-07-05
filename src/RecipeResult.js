import React from 'react';
import PropTypes from 'prop-types';
import './RecipeResult.css';
import { ListGroupItem , ListGroupItemHeading, ListGroupItemText} from 'reactstrap';
import { Badge, Collapse, Button, CardBody, Card, Col, Row } from 'reactstrap';
import Clipboard from 'clipboard';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { okaidia } from 'react-syntax-highlighter/dist/esm/styles/prism';


class RecipeResult extends React.Component {
  componentDidMount() {
    this.clipboard = new Clipboard('.copy-to-clipboard');
  }

  componentWillUnmount() {
    this.clipboard.destroy();
  }

  constructor(props) {
    super(props);
    this.toggle = this.toggle.bind(this);
    this.state = { collapse: false };
  }

  toggle() {
    this.setState({ collapse: !this.state.collapse });
  }

  render() {
    const tags = this.props.recipeData.tags.map((tag) => 
            <Badge key={tag} className="float-md-right tag" color="secondary" pill>{tag}</Badge>
      )
    const toggle_name = this.state.collapse ? "Hide Code Snippet" : "Show Code snippet" 
    return (
        <ListGroupItem>
        <ListGroupItemHeading>
          {this.props.recipeData.title} 
        </ListGroupItemHeading>
        <Row>
        <Col sm="6">
        <small className="text-muted">Author -  {this.props.recipeData.author} </small>
        </Col>
        <Col sm="6">
        {tags}
        </Col>
        </Row>
        <ListGroupItemText className="title">
          {this.props.recipeData.description} 
        </ListGroupItemText>
        <Button className="btn-sm" color="secondary" onClick={this.toggle} >{toggle_name}</Button>
        <Collapse isOpen={this.state.collapse}>
          <div className="relative">
          <Button className="btn-copy copy-to-clipboard" data-clipboard-text={this.props.recipeData.snippet}>
          {/*<button type="button" id="copy-button" data-clipboard-target="#code-copy" classNa="btn btn-default btn-copy" title="Copy to clipboard">*/}
          <svg className="icon" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 24 24">
          <path d="M17,9H7V7H17M17,13H7V11H17M14,17H7V15H14M12,3A1,1 0 0,1 13,4A1,1 0 0,1 12,5A1,1 0 0,1 11,4A1,1 0 0,1 12,3M19,3H14.82C14.4,1.84 13.3,1 12,1C10.7,1 9.6,1.84 9.18,3H5A2,2 0 0,0 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5A2,2 0 0,0 19,3Z" />
          </svg>
          </Button>
          <SyntaxHighlighter language="python" style={okaidia}>
          {this.props.recipeData.snippet}
          </SyntaxHighlighter> 
          </div>
        </Collapse>
      </ListGroupItem>
    );
  }
}
RecipeResult.propTypes = {
  title: PropTypes.string,
  description: PropTypes.string,
};
export default RecipeResult;