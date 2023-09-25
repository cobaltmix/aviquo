import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <>
    <React.StrictMode>
    <App url='/api/users/' title='Users'/>
  </React.StrictMode>
  <React.StrictMode>
    <App url='/api/ECS/' title='Extracurricular'/>
  </React.StrictMode>
  <React.StrictMode>
   <App url='/api/AWS/' title='Awards'/>
  </React.StrictMode>
  <React.StrictMode>
   <App url='/api/SC/' title='Scholarships'/>
  </React.StrictMode>
    </>

);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
