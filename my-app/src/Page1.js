import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid'; // Import UUID function

// Styled Components
const FormWrapper = styled.div`
  display: flex;
  flex-direction: column;
  max-width: 500px;
  margin: auto;
  padding: 20px;
  background: #ffffff;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
  font-family: Arial, sans-serif;
`;

const FormHeader = styled.h2`
  text-align: center;
  color: #2575fc;
`;

const FormField = styled.div`
  margin-bottom: 20px;
`;

const Label = styled.label`
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
`;

const RadioGroup = styled.div`
  display: flex;
  gap: 20px;
`;

const Input = styled.input`
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
`;

const Button = styled.button`
  padding: 10px;
  font-size: 1rem;
  background-color: #2575fc;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #0056d6;
  }
`;

const Feedback = styled.p`
  text-align: center;
  color: green;
  font-weight: bold;
`;

const Page1 = () => {
  // Define the questions
  const questions = [
    {
      id: "teamwork",
      label:
        "I actively contribute to team discussions and ensure that my efforts align with the group’s goals.",
      type: "boolean",
    },
    {
      id: "community_service",
      label:
        "I believe it is important to give back to the community and have participated in at least one activity that benefits others.",
      type: "boolean",
    },
    {
      id: "leadership",
      label:
        "When faced with a group task, I am comfortable taking the lead and guiding others toward a successful outcome.",
      type: "boolean",
    },
    {
      id: "eagerness_to_learn",
      label:
        "I am always curious to learn new things, even if they are outside my current area of expertise.",
      type: "boolean",
    },
    {
      id: "critical_thinking",
      label:
        "I regularly evaluate problems by considering different perspectives and analyzing all available information before making a decision.",
      type: "boolean",
    },
  ];

  // Additional questions
  const additionalQuestions = [
    { id: "hobbies", label: "What are your hobbies?", type: "string" },
    {
      id: "club_preferences",
      label: "What do you want in a club?",
      type: "string",
    },
  ];

  // Form state
  const [formData, setFormData] = useState({});
  const [feedback, setFeedback] = useState("");
  const [userId, setUserId] = useState("");

  // Generate a unique ID for the user when the form loads
  useEffect(() => {
    setUserId(uuidv4()); // Generate and set the UUID
  }, []);

  // Handle input changes
  const handleChange = (e) => {
    const { name, value, type } = e.target;

    setFormData((prevData) => ({
      ...prevData,
      [name]: type === "radio" ? value === "true" : value,
    }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Attach the userId to the formData
      const dataToSend = { id: userId, ...formData };

      const response = await axios.post("http://127.0.0.1:5000/submit", dataToSend, {
        headers: { "Content-Type": "application/json" },
      });
      setFeedback("Form submitted successfully!");
    } catch (error) {
      console.error("Error submitting form:", error);
      setFeedback("There was an error submitting your form.");
    }
  };

  return (
    <FormWrapper>
      <FormHeader>Club Interest Form</FormHeader>
      <form onSubmit={handleSubmit}>
        {questions.map((q) => (
          <FormField key={q.id}>
            <Label>{q.label}</Label>
            <RadioGroup>
              <label>
                <input
                  type="radio"
                  name={q.id}
                  value="true"
                  onChange={handleChange}
                />{" "}
                True
              </label>
              <label>
                <input
                  type="radio"
                  name={q.id}
                  value="false"
                  onChange={handleChange}
                />{" "}
                False
              </label>
            </RadioGroup>
          </FormField>
        ))}
        {additionalQuestions.map((q) => (
          <FormField key={q.id}>
            <Label>{q.label}</Label>
            <Input
              type="text"
              name={q.id}
              placeholder={`Enter your ${q.id.replace("_", " ")}`}
              onChange={handleChange}
            />
          </FormField>
        ))}
        <Button type="submit">Submit</Button>
      </form>
      {feedback && <Feedback>{feedback}</Feedback>}
    </FormWrapper>
  );
};

export default Page1;

