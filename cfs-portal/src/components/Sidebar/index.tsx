import { NavLink, useLocation } from 'react-router-dom';

import { useSidebar } from '../../contexts/sidebarContext';

import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from '@mui/material/ListItemIcon';
import DashboardRoundedIcon from '@mui/icons-material/DashboardRounded';
import ViewListRoundedIcon from '@mui/icons-material/ViewListRounded';
import AccountTreeRoundedIcon from '@mui/icons-material/AccountTreeRounded';

import { useTheme } from '@mui/material';
import { buttonSx, Drawer } from './sidebarStyles';

const listItems = [
    { name: 'Dashboard', icon: <DashboardRoundedIcon />, path: '/dashboard' },
    { name: 'App Catalog', icon: <ViewListRoundedIcon />, path: '/app-catalog' },
    { name: 'MEC Instances', icon: <AccountTreeRoundedIcon />, path: '/mec-instances' }
];

export const Sidebar = () => {
    const location = useLocation();
    const theme = useTheme();
    const { sidebarOpen } = useSidebar();

    return (
        <Drawer
            variant="permanent"
            open={sidebarOpen}
        >
            <Toolbar />
            <Box sx={{ overflow: 'hidden' }}>
                <List>
                    {listItems.map((listItem, index) => (
                        <NavLink
                            to={listItem.path}
                            style={{ textDecoration: 'none', color: theme.palette.text.primary }}
                            key={index}
                        >
                            <ListItem sx={{ padding: '6px' }}>
                                <ListItemButton
                                    selected={location.pathname === listItem.path}
                                    sx={
                                        buttonSx(theme, sidebarOpen)
                                    }
                                    disableGutters
                                >
                                    <ListItemIcon
                                        sx={{
                                            minWidth: 0,
                                            mr: sidebarOpen ? 3 : 'auto',
                                            justifyContent: 'center',
                                        }}
                                    >
                                        {listItem.icon}
                                    </ListItemIcon>
                                    {sidebarOpen && <ListItemText primary={listItem.name} />}
                                </ListItemButton>
                            </ListItem>
                        </NavLink>
                    ))}
                </List>
            </Box>
        </Drawer>
    );
}