import React, { createContext, useState } from 'react';

const GlobalContext = createContext();

const GlobalProvider = ({ children }) => {
  const [globalState, setGlobalState] = useState({
    api_key: null,
  });

  const updateGlobalState = (updatedValues) => {
    setGlobalState((prev) => ({
      ...prev,
      ...updatedValues,
    }));
  };

  return (
    <GlobalContext.Provider value={{ globalState, updateGlobalState }}>
      {children}
    </GlobalContext.Provider>
  );
};

export { GlobalContext, GlobalProvider };
