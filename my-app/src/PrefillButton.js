import React from 'react';

const PrefillButton = ({ text, onClick }) => {
  return (
    <button className="PrefillButton" onClick={() => onClick(text)}>
      {text}
    </button>
  );
};

export default PrefillButton;