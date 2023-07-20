import React, {Component} from "react";
import {render} from "react-dom";
import Navbar from '../../Navbar';
import HomePage from "./Homepage";
const App = (props) => (
    // <Navbar />
    <div id="event_hall">
        <h1> This is Event hall</h1>
        <HomePage/>
    </div>
);

export default App;

const mainDiv = document.getElementById("main");
render(<App />, mainDiv);