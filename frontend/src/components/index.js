import React from "react";
import { Nav, NavLink, NavMenu } from "./NavbarElements";

const Navbar = () => {
    return (
        <>
            <Nav>
                <NavMenu>
                    <NavLink to="/gen_otp_key">
                        Generate API Key for Local Session
                    </NavLink>
                    <NavLink to="/demo_old">
                        Basic Endpoint Demo (Deprecated)
                    </NavLink>
                    <NavLink to="/demo_users">
                        User Endpoint Demo (Current)
                    </NavLink>
                    <NavLink to="/chatbox_template">
                        Chatbox Preview
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;