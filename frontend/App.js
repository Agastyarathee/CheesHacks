import React, { useState } from 'react';
import styled from 'styled-components';
import InputForm from './InputForm';
import ResponseDisplay from './ResponseDisplay';

const AppWrapper = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
    color: white;
    font-family: 'Arial', sans-serif;
`;

const Header = styled.h1`
    font-size: 2.5rem;
    margin-bottom: 1rem;
    text-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
`;

function App() {
    const [response, setResponse] = useState('');

    return (
        <AppWrapper>
            <Header>Glossy Prompt Input</Header>
            <InputForm setResponse={setResponse} />
            <ResponseDisplay response={response} />
        </AppWrapper>
    );
}

export default App;
