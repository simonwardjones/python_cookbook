import React from 'react'
import Header from './Header'
import './App.css'
import SearchResults from './SearchResults'
import createIndex from './createIndex.js'
import filterRecipes from './filterRecipes';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      index: {},
      filteredRecipes: {},
      data: []
    };
  }

  handleSearchChange = (event) => {
    this.setState({
      filteredRecipes: filterRecipes(this.state.index, event.target.value, this.state.data),
    });
  }

  componentDidMount = () => {
    var that = this
    axios.get('./data.json')
      .then(function (response) {
        var data = response.data
        var index = createIndex(data)
        that.setState({
          index: index,
          filteredRecipes: filterRecipes(index,'',data),
          data: data
        })
      }).catch((err) => {
          console.log('can\'t get data')
      })
  }

  hasRecipesToDisplay = () => {
   return !(Object.keys(this.state.data).length === 0
    && this.state.data.constructor === Object)
  }

  render(){
    return (
    <div>
    {

      this.hasRecipesToDisplay() ? (
      <div>
        <Header />
        <SearchResults 
        filteredRecipes={this.state.filteredRecipes}
        onFilterTextChange={this.handleSearchChange}/>
      </div>)
      : (
      // to see this loading screen set class name to temp for a flash of red
      <div>
        <Header />
        <div className=""></div>
      </div>)
    }
    </div>
  )
  }
}

export default App