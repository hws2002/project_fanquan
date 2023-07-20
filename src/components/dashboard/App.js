import React, {Component} from "react";
import {render} from "react-dom";
import Navbar from '../../Navbar';

const App = (props) => (
    // <Navbar />
    <div>
        <h1>App</h1>
    </div>
);

export default App;

const mainDiv = document.getElementById("main");
render(<App />, mainDiv);