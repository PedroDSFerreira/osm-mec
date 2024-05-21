import { NavLink, useLocation } from 'react-router-dom';

import { useSidebar } from '../../contexts/sidebarContext';
import { SidebarProps } from '../../types/Component';

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

import { useTheme, styled } from '@mui/material';
import { buttonSx, Drawer } from './sidebarStyles';

const listItems = [
    { name: 'Dashboard', icon: <DashboardRoundedIcon />, path: '/dashboard' },
    { name: 'App Catalog', icon: <ViewListRoundedIcon />, path: '/app-catalog' },
    { name: 'App Instances', icon: <AccountTreeRoundedIcon />, path: '/app-instances' }
];


const StyledNavLink = styled(NavLink)(({ theme }) => ({
    textDecoration: 'none',
    color: theme.palette.text.primary
}));

const SidebarItem = ({ item, isOpen, isSelected }: SidebarProps) => {
    const theme = useTheme();
    return (
        <StyledNavLink to={item.path} aria-label={item.name}>
            <ListItem sx={{ padding: '6px' }} >
                <ListItemButton
                    selected={isSelected}
                    sx={buttonSx(theme, isOpen)}
                    disableGutters
                    aria-selected={isSelected}
                >
                    <ListItemIcon
                        sx={{
                            minWidth: 0,
                            mr: isOpen ? 3 : 'auto',
                            justifyContent: 'center',
                        }}
                    >
                        {item.icon}
                    </ListItemIcon>
                    {isOpen && <ListItemText primary={item.name} />}
                </ListItemButton>
            </ListItem>
        </StyledNavLink>
    )
};

export const Sidebar = () => {
    const location = useLocation();
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
                        <SidebarItem
                            key={index}
                            item={listItem}
                            isOpen={sidebarOpen}
                            isSelected={location.pathname === listItem.path}
                        />
                    ))}
                </List>
            </Box>
        </Drawer>
    );
}