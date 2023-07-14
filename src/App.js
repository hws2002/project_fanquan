import React, {Component} from "react";
import {render} from "react-dom";
import Navbar from './Navbar';

const App = (props) => (
    <Navbar />
);

export default App;

const mainDiv = document.getElementById("main");
render(<App />, mainDiv);