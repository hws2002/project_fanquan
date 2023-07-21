import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export default function Event() {
    const [state, setState] = useState({
        event_name: "",
        is_host : false,
        host: "",
        category: "",
        event_description: "",
        created_at: "",
        capacity: 7,
        joined: 1,
    });

    const { event_id } = useParams();

    useEffect(() => {
        getEventDetails();
    }, []);

    
    const getEventDetails = () => {
        // fetch event details and update state
        fetch(`/event_hall/get-event`+`?event_id=`+`${event_id}`)
        .then((response) => response.json())
        .then((data) => {
            console.log("Event fetched:", data)
            setState({ 
                event_name: data.event_name, 
                is_host : data.is_host,
                host: data.host,
                category: data.category,
                event_description: data.event_description,
                created_at: data.created_at,
                capacity: data.capacity,
                joined: data.joined,
            })
        });
    };

    return (
        <div>
            <h3>{event_id}</h3>
            <h1>Event {state.event_name}</h1>
            <p1>is host : {state.is_host}</p1>
            <p1>Host : {state.host}</p1>
            <p1>Category : {state.category}</p1>
            <p1>Event Description : {state.event_description} </p1>
            <p1>Created at : {state.created_at}</p1>
            <p1>Capacity : {state.capacity}</p1>
            <p1>Current number of members: {state.joined}</p1>
        </div>
    );
}
