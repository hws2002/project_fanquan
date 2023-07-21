import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export default function Events() {
    const [state, setState] = useState({
        event_name: "",
        event_description: "",
    });

    const { event_id } = useParams();

    useEffect(() => {
        getEventDetails();
    }, []);

    const getEventDetails = () => {
        // fetch event details and update state
    };

    return (
        <div>
            <h3>{event_id}</h3>
            <h1>Event {state.event_name}</h1>
            <p1>Event Description : {state.event_description} </p1>
        </div>
    );
}
