import React from "react";
import { Button, Menu, MenuItem } from "@mui/material";
import { DropdownButtonProps } from "../../types/Component";
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';

const DropdownButton = ({ title, options }: DropdownButtonProps) => {
    const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
    const open = Boolean(anchorEl);

    const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    return (
        <>
            <Button
                variant='contained'
                color='primary'
                size='small'
                onClick={handleClick}
                endIcon={<KeyboardArrowDownIcon />}
            >
                {title}
            </Button>
            <Menu
                anchorEl={anchorEl}
                open={open && Boolean(anchorEl)}
                onClose={handleClose}
            >
                {options.map((option, index) => (
                    <MenuItem key={index} onClick={() => { handleClose(); option.handleClick(); }}>
                        {option.label}
                    </MenuItem>
                ))}
            </Menu>
        </>
    );
}

export default DropdownButton;