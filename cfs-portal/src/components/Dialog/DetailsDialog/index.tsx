import {
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    Button,
} from '@mui/material';
import { DetailsDialogProps } from '../../../types/Component';

const DetailsDialog = ({ open, onClose, title, data }: DetailsDialogProps) => {
    return (
        <Dialog open={open || false} onClose={onClose}>
            <DialogTitle> {title} </DialogTitle>
            <DialogContent> {data} </DialogContent>
            <DialogActions>
                <Button onClick={onClose} color="primary">
                    Close
                </Button>
            </DialogActions>
        </Dialog>
    );
}

export default DetailsDialog;