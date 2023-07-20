import React, { Component } from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";
import InputLabel from "@material-ui/core/InputLabel";
import { Link } from "react-router-dom";

export default class CreateEventPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      event_name: "",
      event_description: "",
      capacity: 7,
      category_id: "1", // Default category
      categories: [
        { id: '1', name: 'Sports' },
        { id: '2', name: 'Lecture' },
        { id: '3', name: 'Concert' },
        { id: '4', name: 'Hangout' },
        { id: '5', name: 'Study' },
        { id: '6', name: 'School Event' },
        { id: '7', name: 'Others' },
      ], // Add state for list of categories
    //   newCategory: "", // State for new category input
    };
    }

  handleInputChange = (event) => {
    this.setState({
        [event.target.name]: event.target.value,
    });
    };

  handleAddCategory = () => {
    const newCategory = {
      id: (this.state.categories.length + 1).toString(),
      name: this.state.newCategory,
    };
    this.setState(prevState => ({
      categories: [...prevState.categories, newCategory],
      newCategory: "",
    }));
  };

  handleCreateEventButtonPressed = () =>{
    console.log(this.state)
    const requestOptions = {
        method: 'POST',
        headers : {'Content-Type': 'application/json'},
        body: JSON.stringify({
            event_name: this.state.event_name,
            event_description: this.state.event_description,
            category_id: this.state.category_id,
            capacity : this.capacity,
            // category_id: parseInt(this.state.category_id), // Convert to number before sending
          }),
        };
    fetch("/event_hall/new_event", requestOptions)
          .then((response) => response.json())
          .then((data) => console.log(data));
    }

  render() {
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <Typography component="h4" variant="h4">
            Create A Event
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <TextField
              required={true}
              type="text"
              name="event_name"
              variant="outlined"
              value={this.state.event_name}
              onChange={this.handleInputChange}
              placeholder="Event Name"
            />
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <InputLabel id="category-label">Category</InputLabel>
            <Select
              labelId="category-label"
              name="category_id"
              value={this.state.category_id}
              onChange={this.handleInputChange}
            >
              {this.state.categories.map((category) => (
                <MenuItem key={category.id} value={category.id}>
                  {category.name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </Grid>
        {/* <Grid item xs={12} align="center">
          <FormControl>
            <TextField
              type="text"
              name="newCategory"
              variant="outlined"
              value={this.state.newCategory}
              onChange={this.handleInputChange}
              placeholder="Add New Category"
            />
            <Button onClick={this.handleAddCategory} color="primary" variant="contained">
              Add Category
            </Button>
          </FormControl>
        </Grid> */}
        <Grid item xs={12} align="center">
          <FormControl>
            <TextField
              required={true}
              type="text"
              name="event_description"
              variant="outlined"
              value={this.state.event_description}
              onChange={this.handleInputChange}
              placeholder="Event Description"
            />
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <FormControl>
            <TextField
              required={true}
              type="number"
              name="capacity"
              variant="outlined"
              value={this.state.capacity}
              onChange={this.handleInputChange}
              placeholder="Capacity"
            />
          </FormControl>
        </Grid>
        <Grid item xs={12} align="center">
          <Button color="primary" variant="contained" onClick={this.handleCreateEventButtonPressed}>
            Create Event
          </Button>
        </Grid>
        <Grid item xs={12} align="center">
          <Button color="secondary" variant="contained" to="/event_hall/" component={Link}>
            Back
          </Button>
        </Grid>
      </Grid>
    );
  }
}