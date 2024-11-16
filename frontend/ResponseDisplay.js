import React from 'react';
import styled from 'styled-components';

const ResponseWrapper = styled.div`
  margin-top: 1rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 8px;
  color: #333;
  box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
  width: 90%;
  max-width: 500px;
`;

function ResponseDisplay({ response }) {
  return (
    <ResponseWrapper>
      <h3>Server Response:</h3>
      <p>{response}</p>
    </ResponseWrapper>
  );
}

export default ResponseDisplay;
