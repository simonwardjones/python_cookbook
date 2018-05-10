import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';
import { BrowserRouter } from 'react-router-dom'
import registerServiceWorker from './registerServiceWorker';
// import axios from 'axios'

// axios.get('./data.json')
//   .then(function (response) {
//     console.log('resp',response);
//   })

ReactDOM.render((
	  <BrowserRouter>
      <App />
      </BrowserRouter>
  ), document.getElementById('root'));

registerServiceWorker();
