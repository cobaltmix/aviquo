import GenerateAPIKeyButton from '../components/GenerateAPIKeyButton';
import React, { useContext } from 'react';
import { GlobalContext } from '../GlobalContext';


const GenerateAPIKey = ({ funct }) => {
    const { updateGlobalState } = useContext(GlobalContext);

    const updateApiKey = (key) => {
        updateGlobalState({
            api_key: key,
        });
        alert('Key Generated!')
    };

    return (
        <>
            <GenerateAPIKeyButton onApiKeyGenerated={updateApiKey} />
        </>
    );
};

export default GenerateAPIKey;