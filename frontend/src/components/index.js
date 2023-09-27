import React from "react";
import { Nav, NavLink, NavMenu } from "./NavbarElements";
 
const Navbar = () => {
    return (
        <>
            <Nav>
                <NavMenu>
                    <NavLink to="/gen_otp_key" activeStyle>
                        Generate API Key for Local Session
                    </NavLink>
                    <NavLink to="/demo_old" activeStyle>
                        Basic Endpoint Demo (Deprecated)
                    </NavLink>
                    <NavLink to="/demo" activeStyle>
                        Endpoint Demo (Current)
                    </NavLink>
                    <NavLink to="/chatbox_template" activeStyle>
                        Chatbox Preview
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};
 
export default Navbar;