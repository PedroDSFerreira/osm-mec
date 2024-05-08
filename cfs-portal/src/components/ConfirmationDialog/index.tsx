import React from 'react';
import PropTypes from 'prop-types';
import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button,
} from '@mui/material';
import { ConfirmationDialogProps } from '../../types/Component';
import capitalize from '../../utils/capitalize';

const ConfirmationDialog = ({ open, onClose, onConfirm, action, item }: ConfirmationDialogProps) => {
    const getTitle = () => {
        return `${capitalize(action.toString())} ${capitalize(item.toString())}`;
    };

    const getContent = () => {
        return `Are you sure you want to ${action} this ${item}?`;
    };

    return (
        <Dialog open={open || false} onClose={onClose}>
            <DialogTitle> {getTitle()} </DialogTitle>
            <DialogContent> {getContent()} </DialogContent>
            <DialogActions>
                <Button onClick={onClose} color="primary">
                    Cancel
                </Button>
                <Button onClick={onConfirm} color="primary" autoFocus>
                    Confirm
                </Button>
            </DialogActions>
        </Dialog>
    );
};

export default ConfirmationDialog;