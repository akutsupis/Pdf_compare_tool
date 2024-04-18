// FileUpload.js
import React, { useState } from 'react';
import axios from 'axios';
import './FileUpload.css';
import PrefillButton from './PrefillButton';

const FileUpload = () => {
  const [rfp, setRfp] = useState(null);
  const [proposal, setProposal] = useState(null);
  const [system, setSystem] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  // An array of predefined text prompts
const prefillTexts = [
  'Please analyze the attached proposal in response to the RFP and assess its overall quality. Consider the adherence to the RFP\'s requirements, the thoroughness of the proposed solution, and the professionalism of the presentation. Provide a summary of strengths and areas for improvement.',
  'Review the provided proposal in the context of the RFP and determine the degree of alignment between the proposal\'s offerings and the RFP\'s stipulations. Highlight key areas of compliance and any significant deviations. Suggest specific adjustments the proposer could make to enhance conformity with the RFP requirements.',
  'Examine the submitted proposal relative to the RFP and identify elements that could be refined to increase the proposal\'s effectiveness and likelihood of acceptance. Propose modifications to the scope of work, project timelines, budget details, or any other sections you find would benefit from revisions.'
];

const passcode = process.env.REACT_APP_PASSCODE;

  const handlePrefill = (text) => {
    setSystem(text); // Update the system state with the prefill text
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    const formData = new FormData();
    formData.append('rfp', rfp);
    formData.append('proposal', proposal);
    formData.append('system', system);
    formData.append('passcode', passcode);


    try {
      const res = await axios.post('https://pdf-compare-tool-r48a.onrender.com/uploadfiles/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResponse(res.data.response);
    } catch (error) {
      console.error('There was an error uploading the files', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="FileUpload">
      <h1>Upload Your Documents</h1>
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
          <textarea
            id="system"
            name="system"
            value={system}
            onChange={(event) => setSystem(event.target.value)}
            rows="2" // Adjust the number of rows as needed
            cols="30" // Adjust the number of columns as needed
          />
        </div>
        <div className="PrefillButtons">
          {prefillTexts.map((text, index) => (
            <PrefillButton key={index} text={text} onClick={handlePrefill} />
          ))}
        </div>
        <button type="submit" disabled={loading}>{loading ? 'Loading...' : 'Submit'}</button>
      </form>

      {response && (
        <div className="ResponseDetails">
          <h2>Response Details</h2>
          <div>
            <strong>Message Content:</strong>
            <pre>{response.choices && response.choices[0].message.content}</pre>
          </div>
          <div>
            <strong>Model Used:</strong>
            <pre>{response.model}</pre>
          </div>
          <div>
            <strong>Total Tokens:</strong>
            <pre>{response.usage && response.usage.total_tokens}</pre>
          </div>
        </div>
      )}
    </div>
  );
};

export default FileUpload;