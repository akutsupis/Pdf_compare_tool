import React, { useState } from 'react';

function App() {
  const [uploadedFile1, setUploadedFile1] = useState(null);
  const [uploadedFile2, setUploadedFile2] = useState(null);
  const [userInput, setUserInput] = useState('');
  const [output, setOutput] = useState('');

  const handleFileUpload1 = (event) => {
    setUploadedFile1(event.target.files[0]);
  };

  const handleFileUpload2 = (event) => {
    setUploadedFile2(event.target.files[0]);
  };

  const handleUserInputChange = (event) => {
    setUserInput(event.target.value);
  };

const handlePromptSubmit = () => {
  const formData = new FormData();
  formData.append('rfp', uploadedFile1);
  formData.append('proposal', uploadedFile2);
  formData.append('system', userInput);

  fetch('http://127.0.0.1:8000/uploadfiles/', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
    setOutput(data.response.choices[0].message.content);
  })
  .catch(error => {
    console.error('Error:', error);
  });
};

  return (
    <div>
      <h1>Instructions</h1>
      <p>Upload your files, enter your prompt, and then click 'Submit' to process them.</p>

      <label>
        Upload RFP:
        <input type="file" onChange={handleFileUpload1} />
      </label>

      <label>
        Upload Proposal:
        <input type="file" onChange={handleFileUpload2} />
      </label>

      <label>
        Enter System:
        <textarea value={userInput} onChange={handleUserInputChange} />
      </label>

      <button onClick={handlePromptSubmit}>Submit</button>

      <h2>Output</h2>
      <textarea value={output} readOnly />
    </div>
  );
}

export default App;