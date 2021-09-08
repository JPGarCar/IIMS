import React, {Component} from "react";
import {Button, Grid, TextField} from "@material-ui/core";
import ParticipantInfo from "./ParticipantInfo";


export default class ParticipantSignIn extends Component {
    constructor(props) {
        super(props);
        this.state = {
            searchText: '',
            number: null,
            participant: null,
            match: null,
            team: null,
        }

        this.handleTextFieldChange = this.handleTextFieldChange.bind(this);
        this.handleSearch = this.handleSearch.bind(this);
        this.handleSignIn = this.handleSignIn.bind(this);
        this.handleNumberTextFieldChange = this.handleNumberTextFieldChange.bind(this);
    }

    handleSignIn(e) {
        const requestOpts = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                'participant_pk': this.state.participant.id,
                'participant_number': this.state.number,
            })
        }

        const teamGame = this.state.match.home_team.team.id === this.state.team.id ? this.state.match.home_team : this.state.match.away_team;

        fetch(
            'http://localhost:8000/match/api/team_games/' + teamGame.id + '/sign_in/', requestOpts
        ).then((response) => response.json()).then((data) => console.log(data))
    }

    handleSearch(e) {
        const requestOptions = {
            method: 'GET',
            headers: {'Content-Type': 'application/json'},
        };
        fetch(
            'http://localhost:8000/league/api/days/' + this.props.day.id + '/participant/'+ this.state.searchText + '/',
            requestOptions)
            .then((response) => {
                console.log(response.statusText);
                response.json().then((data) => {
                    this.setState({
                        participant: data.participant,
                        match: data.match,
                        team: data.team,
                    })
                })
            }).catch(console.log)
    }

    handleTextFieldChange(e) {
        this.setState({
            searchText: e.target.value
        })
    }

    handleNumberTextFieldChange(e) {
        this.setState({
            number: e.target.value
        })
    }

    render() {
        return (
          <Grid container direction={"column"}>
              <Grid item>
                  <Grid container direction={"row"} spacing={4} alignItems={"center"}>
                      <Grid item xs={7}>
                          <Grid container direction={"row"} spacing={1} alignItems={"center"}>
                              <Grid item xs={8}>
                                  <TextField label={'Search Participant'} fullWidth margin={"normal"} onChange={this.handleTextFieldChange}>
                                  </TextField>
                              </Grid>
                              <Grid item xs style={{textAlign: "center"}}>
                                  <Button onClick={this.handleSearch}>
                                      Search
                                  </Button>
                              </Grid>
                          </Grid>
                      </Grid>
                      <Grid item xs>
                          <Grid container direction={"row"} spacing={1} alignItems={"center"}>
                              <Grid item xs>
                                  <TextField label={'Number'} fullWidth margin={"normal"} onChange={this.handleNumberTextFieldChange}>
                                  </TextField>
                              </Grid>
                              <Grid item xs style={{textAlign: 'center'}}>
                                  <Button onClick={this.handleSignIn}>
                                      Sign In
                                  </Button>
                              </Grid>
                          </Grid>
                      </Grid>
                  </Grid>
              </Grid>
              <Grid item>
                  {this.state.participant != null ? <ParticipantInfo participant={this.state.participant} match={this.state.match} team={this.state.team} /> : 'Search for a participant first!'}
              </Grid>
          </Grid>
        );
    }
}