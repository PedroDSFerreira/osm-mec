import React, { useState } from "react";
import { Box, Button, Dialog, DialogActions, DialogContent, DialogTitle, Typography } from "@mui/material";
import { UploadDialogProps } from "../../../types/Component";
import { UploadFile, FolderZipOutlined } from "@mui/icons-material";

const UploadDialog = ({ title, open, onClose, onSubmit }: UploadDialogProps) => {
    const [file, setFile] = useState<File | null>(null);

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (file) {
            setFile(file);
        }
    };

    const handleDragOver = (e: any) => {
        e.preventDefault();
    }

    const handleDrop = (e: any) => {
        e.preventDefault();
        const file = e.dataTransfer.files[0];
        if (file) {
            setFile(file);
        }
    }

    const handleSubmit = () => {
        if (file) {
            onSubmit(file);
            setFile(null);
        }
    };

    const handleCancel = () => {
        onClose();
        setFile(null);
    }

    const handleDropZoneClick = () => {
        document.getElementById('input')?.click();
    }

    return (
        <Dialog open={open} onClose={onClose} fullWidth maxWidth='sm'>
            <DialogTitle> {title} </DialogTitle>
            <DialogContent>
                <input
                    id="input"
                    type='file'
                    accept='.tar.gz'
                    onChange={handleFileChange}
                    hidden
                />
                <Box
                    id="drop-zone"
                    onDrop={handleDrop}
                    onDragOver={handleDragOver}
                    onClick={handleDropZoneClick}
                    sx={{ height: '200px', border: '2px dashed #aaa', backgroundColor: 'rgba(0, 0, 0, 0.04)', borderRadius: '6px', padding: '20px', textAlign: 'center', cursor: 'pointer', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}
                >
                    <label style={{ cursor: 'pointer' }}>
                        <UploadFile color="disabled" fontSize="large" />
                        <Typography
                            variant='h6'
                            color='GrayText'
                            fontWeight='bold'
                            sx={{ marginTop: '10px' }}
                        >
                            Drag and drop your file here
                        </Typography>
                        <Typography
                            variant='body1'
                            color='GrayText'
                            fontWeight='bold'
                            sx={{ marginTop: '10px', textDecoration: 'underline' }}
                        >
                            or click to browse
                        </Typography>
                    </label>
                    {file &&
                        <Button
                            disabled
                            sx={{ marginTop: '10px', textTransform: 'none' }}
                            startIcon={<FolderZipOutlined color="disabled" fontSize="small" />}
                        >
                            {file.name}
                        </Button>}
                </Box>
            </DialogContent>
            <DialogActions>
                <Button onClick={handleCancel}>Cancel</Button>
                <Button variant="contained" onClick={handleSubmit}>Upload</Button>
            </DialogActions>
        </Dialog >
    );
}

export default UploadDialog;