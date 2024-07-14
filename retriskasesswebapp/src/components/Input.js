// src/components/Input.js
import React from 'react';

export const Input = ({ type, className, onChange }) => {
  return (
    <input type={type} className={className} onChange={onChange} />
  );
};
