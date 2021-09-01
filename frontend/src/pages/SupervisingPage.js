import React, { Component } from 'react';
import {render} from "react-dom";
import {Card, CardContent, Grid} from "@material-ui/core";
import ParticipantSignIn from "../components/ParticipantSignIn";

export default class SupervisingPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            pool: this.props.pool,
            week: {},
            day: {},
        }
    }

    render() {
        return (
            <Grid container direction="column" spacing={2} >
                <Grid item>
                    <Grid container direction={"row"} justifyContent={"space-between"}>
                        <Grid item>
                            <h3>Week Dropdown</h3>
                        </Grid>
                        <Grid item>
                            <h2>{this.state.pool.name}</h2>
                        </Grid>
                        <Grid>
                            <h3>Day Dropdown</h3>
                        </Grid>
                    </Grid>
                </Grid>
                <Grid item>
                    <Grid container direction={"row"} spacing={3}>
                        <Grid item xs={4}>
                            <Card>
                                <CardContent>
                                    <pre>{JSON.stringify(this.state.pool)}</pre>
                                </CardContent>
                            </Card>
                        </Grid>
                        <Grid item xs={8}>
                            <Card>
                                <CardContent>
                                    <ParticipantSignIn />
                                </CardContent>
                            </Card>
                        </Grid>
                    </Grid>
                </Grid>
                <Grid item>
                    <Card>
                        <CardContent>
                            This is the day times and matches component!
                        </CardContent>
                    </Card>
                </Grid>
            </Grid>
        );
    }

}

const appDiv = document.getElementById("app");
const poolData = JSON.parse(document.getElementById('pool').textContent);
render(<SupervisingPage pool={poolData} />, appDiv)