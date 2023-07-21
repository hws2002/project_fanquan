import React, { Component } from "react";
import CreateEventPage from "./CreateEventPage";
import Event from "./Event";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div>
        <Router>
            <Routes>
            <Route path="/event_hall/" element={<p>This is the home page</p>} />
            <Route path="/event_hall/create" element={<CreateEventPage />} />
            <Route path="/event_hall/event/:event_id" element={ <Event/> } />
            </Routes>
        </Router>
      </div>
    );
  }
}
