import React, {Component} from "react";
import {Button, Grid, TextField} from "@material-ui/core";


export default class ParticipantSignIn extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
          <Grid container direction={"column"}>
              <Grid item>
                  <Grid container direction={"row"} spacing={2}>
                      <Grid item xs={8}>
                          <TextField>

                          </TextField>
                      </Grid>
                      <Grid item xs>
                          <Button>
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
                  The player + team + match info!
              </Grid>
          </Grid>
        );
    }
}