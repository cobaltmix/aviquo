import React from 'react';
import axios from 'axios';

const GenerateAPIKeyButton = ({ onApiKeyGenerated }) => {
  const buttonStyle = {
    backgroundColor: 'purple',
    color: 'white',
    padding: '10px 20px',
    borderRadius: '8px',
    border: 'none',
    cursor: 'pointer',
    fontSize: '1.2em',
  };

  const centerDivStyle = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
  };

  const handleGenerateApiKey = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/gen_key/');
      onApiKeyGenerated(response.data.key);
      console.log(response.data.key)
    } catch (error) {
      console.error('Error generating API key:', error);
    }
  };

  return (
    <div style={centerDivStyle}>
      <button style={buttonStyle} onClick={handleGenerateApiKey}>
        Generate API Key
      </button>
    </div>
  );
};

export default GenerateAPIKeyButton;