import React from 'react';
import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button,
    TextField,
    SelectChangeEvent,
    MenuItem,
} from '@mui/material';
import { FormDialogProps } from '../../../types/Component';

const FormDialog = ({ open, onClose, onSubmit, title, fields }: FormDialogProps) => {
    const [formData, setFormData] = React.useState<FormData>(new FormData());

    const handleChange = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement> | SelectChangeEvent) => {
        var { name, value } = event.target;
        setFormData(prevFormData => ({ ...prevFormData, [name]: value }));
    }

    const handleSubmit = () => {
        onSubmit(formData);
        onClose();
    }

    return (
        <Dialog open={open || false} onClose={onClose} fullWidth maxWidth='sm'>
            <DialogTitle> {title} </DialogTitle>
            <DialogContent>
                {fields.map((field) => (
                    <React.Fragment key={field.id}>
                        {field.type === 'text' ? (
                            <TextField
                                key={field.id}
                                margin='dense'
                                name={field.id}
                                label={field.label}
                                type='text'
                                fullWidth
                                required={field.required}
                                onChange={handleChange}
                            />
                        ) : (
                            <TextField
                                select
                                key={field.id}
                                margin='dense'
                                name={field.id}
                                label={field.label}
                                fullWidth
                                required={field.required}
                                onChange={handleChange}
                            >
                                {field.options?.map((option, index) => (
                                    <MenuItem key={index} value={option}>{option}</MenuItem>
                                ))}
                            </TextField>
                        )}
                    </React.Fragment>
                ))}
            </DialogContent>
            <DialogActions>
                <Button onClick={onClose} color="primary">
                    Cancel
                </Button>
                <Button onClick={handleSubmit} color="primary" autoFocus>
                    Submit
                </Button>
            </DialogActions>
        </Dialog>
    );
};

export default FormDialog;
