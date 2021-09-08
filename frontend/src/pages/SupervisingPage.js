import React, { Component } from 'react';
import {render} from "react-dom";
import {Card, CardContent, Grid} from "@material-ui/core";
import ParticipantSignIn from "../components/ParticipantSignIn";

export default class SupervisingPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            pool: this.props.pool,
            week: this.props.week,
            day: this.props.day,
        }
    }

    render() {
        return (
            <Grid container direction="column" spacing={2} alignItems={"center"}>
                <Grid item>
                    <h2>{this.state.pool.__str__}</h2>
                </Grid>
                <Grid item>
                    <Grid container direction={"row"} spacing={3}>
                        <Grid item xs={4}>
                            <Card>
                                <CardContent>
                                    <Grid container spacing={1} justifyContent={"space-evenly"} alignItems={"center"}>
                                        <Grid item>
                                            <b>Activity:</b> {this.state.pool.activity.name}
                                        </Grid>
                                        <Grid item>
                                            <b>Game Duration:</b> {this.state.pool.game_duration}
                                        </Grid>
                                        <Grid>
                                            <b>Gender:</b> {this.state.pool.gender.name}
                                        </Grid>
                                        <Grid item>
                                            <b>Tier:</b> {this.state.pool.tier.name}
                                        </Grid>
                                        <Grid item>
                                            <b>Week:</b> {this.state.week.__str__}
                                        </Grid>
                                        <Grid item>
                                            <b>Day:</b> {this.state.day.__str__}
                                        </Grid>
                                    </Grid>
                                </CardContent>
                            </Card>
                        </Grid>
                        <Grid item xs={8}>
                            <Card>
                                <CardContent>
                                    <ParticipantSignIn day={this.state.day} />
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
const weekData = JSON.parse(document.getElementById('week').textContent);
const dayData = JSON.parse(document.getElementById('day').textContent);
console.log(poolData);
console.log(weekData);
console.log(dayData);
render(<SupervisingPage pool={poolData} day={dayData} week={weekData} />, appDiv)