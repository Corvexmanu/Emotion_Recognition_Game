import React from 'react';
import AppBar from '@material-ui/core/AppBar'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'

const NavBar = () => {
    return(
        <div>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="title" color="inherit">
                        AdFACEry Game - Pull the correct facial expression to earn points!
                    </Typography>
                </Toolbar>
            </AppBar>
        </div>
    )
}
export default NavBar;