import React from "react";
import SearchBar from "../SearchBar/SearchBar";
import './NavBar.css'

const NavBar = (props) => {

    return ( 
        <nav>
            <div className="display">
                <div>
                    <h1>Music<small className="text-muted">Library</small></h1>
                </div>
                <div className="searchbar">
                    <SearchBar/>
                </div>
            </div>
        </nav>
     );
}
 
export default NavBar;