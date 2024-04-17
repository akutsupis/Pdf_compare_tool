import React from 'react';
import { Analytics } from "@vercel/analytics/react"
import FileUpload from './FileUpload';
import './App.css';

function App() {
  return (
    <div className="App">
      <div className="card">
        <h1>BidAssessor AI</h1>
      </div>
      <FileUpload />
    </div>
  );
}

export default App;