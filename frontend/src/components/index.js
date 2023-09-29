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
                    <NavLink to="/demo_users" activeStyle>
                        User Endpoint Demo (Current)
                    </NavLink>
                    <NavLink to="/demo_forum" activeStyle>
                        Forum Endpoint Demo (Current)
                    </NavLink>
                    <NavLink to="/demo_opp" activeStyle>
                        Opportunities Endpoint Demo (Current)
                    </NavLink>
                    <NavLink to="/chatbox_template" activeStyle>
                        Chatbox Preview
                    </NavLink>
                    <NavLink to="/demo_waitlist" activeStyle>
                        Waitlist Endpoint Demo
                    </NavLink>
                    <NavLink to="/waitlist_count" activeStyle>
                        Waitlist Count
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};

export default Navbar;