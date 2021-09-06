import React, {Component} from "react";
import {Button, Grid, TextField} from "@material-ui/core";


export default class ParticipantSignIn extends Component {
    constructor(props) {
        super(props);
        this.state = {
            searchText: '',
            participant: null,
        }

        this.handleTextFieldChange = this.handleTextFieldChange.bind(this);
        this.handleSearch = this.handleSearch.bind(this);
    }

    handleSearch(e) {
        console.log(this.state.searchText);
    }

    handleTextFieldChange(e) {
        this.setState({
            searchText: e.target.value
        })
    }

    render() {
        return (
          <Grid container direction={"column"}>
              <Grid item>
                  <Grid container direction={"row"} spacing={2} alignItems={"center"}>
                      <Grid item xs={8}>
                          <TextField label={'Search Participant'} fullWidth margin={"normal"} onChange={this.handleTextFieldChange}>
                          </TextField>
                      </Grid>
                      <Grid item xs>
                          <Button onClick={this.handleSearch}>
                              Search
                          </Button>
                      </Grid>
                      <Grid item xs>
                          <Button>
                              Playing
                          </Button>
                      </Grid>
                  </Grid>
              </Grid>
              <Grid item>
                  {this.state.participant != null ? 'Hello there' : 'Search for a participant first!'}
              </Grid>
          </Grid>
        );
    }
}