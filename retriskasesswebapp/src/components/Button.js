// src/components/Button.js
import React from 'react';

export const Button = ({ children, className, onClick, type }) => {
  return (
    <button type={type} className={className} onClick={onClick}>
      {children}
    </button>
  );
};
