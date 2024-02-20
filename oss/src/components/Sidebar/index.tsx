import { NavLink, useLocation } from 'react-router-dom';

import { useSidebar } from '../../contexts/sidebarContext';

import Box from '@mui/material/Box';
import MuiDrawer from "@mui/material/Drawer";
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from '@mui/material/ListItemIcon';
import DashboardRoundedIcon from '@mui/icons-material/DashboardRounded';
import ViewListRoundedIcon from '@mui/icons-material/ViewListRounded';
import AccountTreeRoundedIcon from '@mui/icons-material/AccountTreeRounded';

import { styled, useTheme, Theme, CSSObject } from '@mui/material';
import './sidebar.css'

const drawerWidth = 240;

const listItems = [
    { name: 'Dashboard', icon: <DashboardRoundedIcon />, path: '/dashboard' },
    { name: 'App Catalog', icon: <ViewListRoundedIcon />, path: '/app-catalog' },
    { name: 'MEC Instances', icon: <AccountTreeRoundedIcon />, path: '/mec-instances' }
];

const openedMixin = (theme: Theme): CSSObject => ({
    width: drawerWidth,
    transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen,
    }),
    overflowX: 'hidden',
});

const closedMixin = (theme: Theme): CSSObject => ({
    transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
    }),
    overflowX: 'hidden',
    width: `calc(${theme.spacing(7)} + 1px)`,
    [theme.breakpoints.up('sm')]: {
        width: `calc(${theme.spacing(8)} + 1px)`,
    },
});

const Drawer = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== 'open' })(
    ({ theme, open }) => ({
        width: drawerWidth,
        flexShrink: 0,
        whiteSpace: 'nowrap',
        boxSizing: 'border-box',
        ...(open && {
            ...openedMixin(theme),
            '& .MuiDrawer-paper': openedMixin(theme),
        }),
        ...(!open && {
            ...closedMixin(theme),
            '& .MuiDrawer-paper': closedMixin(theme),
        }),
    }),
);

export const Sidebar = () => {
    const location = useLocation();
    const theme = useTheme();
    const { sidebarOpen } = useSidebar();

    const buttonSx = {
        '&.Mui-selected': {
            backgroundColor: theme.palette.primary.main,
            color: theme.palette.getContrastText(theme.palette.primary.main),
            '& .MuiListItemIcon-root': {
                color: theme.palette.getContrastText(theme.palette.primary.main),
            },
            '& .MuiTypography-root': {
                color: theme.palette.getContrastText(theme.palette.primary.main),
            },
            '&:hover': {
                backgroundColor: theme.palette.primary.main,
            },
        },
        justifyContent: sidebarOpen ? 'initial' : 'center',
        px: 1.9,
        height: '50px',
        borderRadius: '6px',
    };

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
                                        buttonSx
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