import React, {useContext, useEffect} from 'react';
import './App.css';
import Navbar from './components/index';
import { BrowserRouter as Router, Routes, Route }
    from 'react-router-dom';
import DeprecatedDemo from './pages/deprecated_demo';
import ChatBoxTemplate from './pages/chatbox'
import GenerateAPIKey from './pages/gen_key'
import Demo from './pages/demo'
import DemoO from './pages/demo_opp'
import DemoF from './pages/demo_forum'
import DemoW from './pages/demo_waitlist'
import DemoC from './pages/waitlist_count'
import { GlobalProvider, GlobalContext } from './GlobalContext';



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
                    <Route path='/demo_forum' element={<DemoF />} />
                    <Route path='/demo_opp' element={<DemoO />} />
                    <Route path='/demo_waitlist' element={<DemoW />} />
                    <Route path='/waitlist_count' element={<DemoC />} />
                </Routes>
            </Router>
        </GlobalProvider>
    );
}

export default App;