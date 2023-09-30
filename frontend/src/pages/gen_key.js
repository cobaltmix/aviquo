import GenerateAPIKeyButton from '../components/GenerateAPIKeyButton';
import React, { useContext, useEffect } from 'react';
import { GlobalContext } from '../GlobalContext';


const GenerateAPIKey = ({ funct }) => {
    const { updateGlobalState } = useContext(GlobalContext);

    const getApiKeyFromLocalStorage = () => {
        const apiKey = localStorage.getItem('api_key');
        if (apiKey) {
            updateGlobalState({
                api_key: apiKey,
            });
        }
    };

    // Call the function to check for the API key when the component mounts
    useEffect(() => {
        getApiKeyFromLocalStorage();
    }, []);


    const updateApiKey = (key) => {
        updateGlobalState({
            api_key: key,
        });
        localStorage.setItem('api_key', key);

        alert('Key Generated!')
    };

    return (
        <>
            <GenerateAPIKeyButton onApiKeyGenerated={updateApiKey} />
        </>
    );
};

export default GenerateAPIKey;