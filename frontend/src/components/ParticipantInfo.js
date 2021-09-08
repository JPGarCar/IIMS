import React, {Component} from "react";
import {Grid} from "@material-ui/core";


export default class ParticipantInfo extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
          <Grid container direction={"row"} spacing={2}>
              <Grid item xs={6}>
                  <Grid container spacing={2}>
                      <Grid item>
                          <b>Name:</b> {this.props.participant.first_name} {this.props.participant.last_name}
                      </Grid>
                      <Grid item>
                          <b>Signed Waiver:</b> {this.props.participant.signed_waiver ? 'Yes' : 'No'}
                      </Grid>
                      <Grid item>
                          <b>Status:</b> {this.props.participant.status}
                      </Grid>
                      <Grid item>
                          <b>Team:</b> {this.props.team.name}
                      </Grid>
                  </Grid>
              </Grid>
              <Grid item xs={6}>
                  <Grid container spacing={2}>
                      <Grid item>
                          <b>Match:</b> {this.props.match.__str__}
                      </Grid>
                      <Grid item>
                          <b>Match Time:</b> {this.props.match.time}
                      </Grid>
                      <Grid item>
                          <b>Location:</b> {this.props.match.day.location.name}
                      </Grid>
                  </Grid>
              </Grid>
          </Grid>
        );
    }
}