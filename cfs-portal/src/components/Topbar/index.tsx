import { useState } from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import ListItemIcon from '@mui/material/ListItemIcon';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import AccountCircle from '@mui/icons-material/AccountCircle';
import IconButton from '@mui/material/IconButton';
import Logout from '@mui/icons-material/Logout';
import ManageAccountsIcon from '@mui/icons-material/ManageAccounts';
import MenuIcon from '@mui/icons-material/Menu';
import MenuOpenIcon from '@mui/icons-material/MenuOpen';

import { useSidebar } from '../../contexts/sidebarContext';

export const TopBar = () => {
    const { sidebarOpen, toggleSidebar } = useSidebar();
    const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

    const isMenuOpen = Boolean(anchorEl);

    const handleMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
        setAnchorEl(event.currentTarget);
    };

    const handleMenuClose = () => {
        setAnchorEl(null);
    };

    const handleLogout = () => {
        handleMenuClose();
    };

    const renderMenu = (
        <Menu
            id="account-menu"
            anchorEl={anchorEl}
            open={isMenuOpen}
            onClose={handleMenuClose}
            keepMounted
        >
            <MenuItem onClick={handleMenuClose}>
                <ListItemIcon>
                    <ManageAccountsIcon fontSize="small" />
                </ListItemIcon>
                User Settings
            </MenuItem>
            <MenuItem onClick={handleLogout}>
                <ListItemIcon>
                    <Logout fontSize="small" />
                </ListItemIcon>
                Logout
            </MenuItem>
        </Menu>
    );

    return (
        <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }} color='primary' >
            <Toolbar>
                <IconButton
                    color="inherit"
                    aria-label="open/close sidebar"
                    onClick={toggleSidebar}
                    edge="start"
                >
                    {sidebarOpen ? <MenuOpenIcon /> : <MenuIcon />}
                </IconButton>
                <Typography
                    variant="h6"
                    noWrap
                    sx={{ display: { xs: 'none', sm: 'block' } }}
                >
                    MEC Portal
                </Typography>
                <Box sx={{ marginLeft: 'auto' }}>
                    <Button
                        color="inherit"
                        aria-controls="account-menu"
                        aria-haspopup="true"
                        onClick={handleMenuOpen}
                    >
                        <AccountCircle />
                        &nbsp;&nbsp;
                        <Typography
                            variant='h6'
                            textTransform='none'
                            sx={{ display: { xs: 'none', md: 'flex' } }}
                        >
                            Admin
                        </Typography>
                    </Button>
                </Box>
            </Toolbar>
            {renderMenu}
        </AppBar>
    );
};

export default TopBar;