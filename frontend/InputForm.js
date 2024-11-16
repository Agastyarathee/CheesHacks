import React, { useState } from 'react';
import styled from 'styled-components';

const FormWrapper = styled.div`
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
  width: 90%;
  max-width: 500px;
`;

const Input = styled.input`
  width: 100%;
  padding: 0.75rem;
  margin-bottom: 1rem;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
`;

const Button = styled.button`
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  background: linear-gradient(135deg, #ff7eb3 0%, #ff758c 100%);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
  &:hover {
    background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%);
  }
`;

function InputForm({ setResponse }) {
  const [prompt, setPrompt] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:5000/api/prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });
      const data = await res.json();
      setResponse(data.result || 'No response received');
    } catch (error) {
      setResponse('Error connecting to server');
    }
  };

  return (
    <FormWrapper>
      <form onSubmit={handleSubmit}>
        <Input
          type="text"
          value={prompt}
          placeholder="Enter your prompt..."
          onChange={(e) => setPrompt(e.target.value)}
        />
        <Button type="submit">Submit Prompt</Button>
      </form>
    </FormWrapper>
  );
}

export default InputForm;
