import React from 'react';
import App from '../deprecated/App';


const DeprecatedDemo = () => {
    return (
        <>
            <App url='/api/users/' title='Users' />
            <App url='/api/Forum/' title='Posts' />
            <App url='/api/Opportunity/' title='Opportunities' />
        </>
    );
};

export default DeprecatedDemo;