import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Ensure this line exists
import './tailwind.css'; // Add this line to include Tailwind CSS
import App from './App';
import reportWebVitals from './reportWebVitals';
import '@mantine/core/styles.css';
import { MantineProvider } from '@mantine/core';

// other css files are required only if
// you are using components from the corresponding package
// import '@mantine/dates/styles.css';
// import '@mantine/dropzone/styles.css';
// import '@mantine/code-highlight/styles.css';
// ...

ReactDOM.render(
  <React.StrictMode>
    <MantineProvider>
    <App />
    </MantineProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
