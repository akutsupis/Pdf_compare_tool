import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
  const [rfp, setRfp] = useState(null);
  const [proposal, setProposal] = useState(null);
  const [system, setSystem] = useState('');
  const [response, setResponse] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append('rfp', rfp);
    formData.append('proposal', proposal);
    formData.append('system', system);

    try {
      const res = await axios.post('http://127.0.0.1:8000/uploadfiles/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setResponse(res.data.response);
    } catch (error) {
      console.error('There was an error uploading the files', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="rfp">RFP (PDF):</label>
          <input
            type="file"
            id="rfp"
            name="rfp"
            accept=".pdf"
            onChange={(event) => setRfp(event.target.files[0])}
          />
        </div>
        <div>
          <label htmlFor="proposal">Proposal (PDF):</label>
          <input
            type="file"
            id="proposal"
            name="proposal"
            accept=".pdf"
            onChange={(event) => setProposal(event.target.files[0])}
          />
        </div>
        <div>
          <label htmlFor="system">System:</label>
          <input
            type="text"
            id="system"
            name="system"
            value={system}
            onChange={(event) => setSystem(event.target.value)}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
      {response && (
        <div>
          <h3>Response Details</h3>
          <div>
            <strong>Message Content:</strong>
            {/* Access the content within the first choice */}
            <pre>{response.choices && response.choices[0].message.content}</pre>
          </div>
          <div>
            <strong>Model Used:</strong>
            {/* Directly printing the model used */}
            <pre>{response.model}</pre>
          </div>
          <div>
            <strong>Total Tokens:</strong>
            {/* Access the total tokens */}
            <pre>{response.usage && response.usage.total_tokens}</pre>
          </div>
        </div>
        )}
    </div>
  );
};

export default FileUpload;