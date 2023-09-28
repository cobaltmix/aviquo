import React, { useState } from 'react';
import styled from 'styled-components';

const ContactBox = () => {
  const [query, setQuery] = useState('');

  const handleQuery = () => {
    // Handle the query logic here
    console.log('Query submitted:', query);
  };

  return (
    <Container>
      <Instructions>
        Enter your query in the chat below, and we'll most definitely not get back to you since we're high schoolers tryna rip you off :)
      </Instructions>
      <TextBox
        placeholder="Type your query here"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <SendButton onClick={handleQuery}>Send</SendButton>
    </Container>
  );
};

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-color: #f5f5fa; /* Purple-ish white */
  border-radius: 10px;
  max-width: 400px;
  margin: auto;
  margin-top: 50px;
`;

const Instructions = styled.p`
  margin-bottom: 10px;
  font-size: 14px;
  text-align: center;
`;

const TextBox = styled.textarea`
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
`;

const SendButton = styled.button`
  padding: 10px 20px;
  background-color: #7a506f; /* Purplish */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  &:hover {
    background-color: #6c405c; /* Darker purplish */
  }
`;

export default ContactBox;