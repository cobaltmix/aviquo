import React, {useContext, useEffect} from 'react';
import './App.css';
import Navbar from './components/index';
import { BrowserRouter as Router, Routes, Route }
    from 'react-router-dom';
import DeprecatedDemo from './pages/deprecated_demo';
import ChatBoxTemplate from './pages/chatbox'
import GenerateAPIKey from './pages/gen_key'
import Demo from './pages/demo'
import { GlobalProvider } from './GlobalContext';


const App = () => {
    

    return (
        <GlobalProvider>
            <Router>
                <Navbar />
                <Routes>
                    {/* <Route exact path='/' element={<DeprecatedDemo />} /> */}
                    <Route exact path='/demo_old' element={<DeprecatedDemo />} />
                    <Route path='/chatbox_template' element={<ChatBoxTemplate />} />
                    <Route path='/gen_otp_key' element={<GenerateAPIKey />} />
                    <Route path='/demo_users' element={<Demo />} />
                </Routes>
            </Router>
        </GlobalProvider>
    );
}

export default App;