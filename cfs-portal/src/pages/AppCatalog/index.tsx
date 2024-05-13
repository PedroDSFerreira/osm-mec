import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { Button, Typography } from '@mui/material';
import { Skeleton } from '@mui/material';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import { ToastContainer } from 'react-toastify';
import ConfirmationDialog from '../../components/ConfirmationDialog';
import FormDialog from '../../components/FormDialog';
import DropdownButton from '../../components/DropdownButton';

import { useAppCatalog } from '../../hooks/useAppCatalog';
import { ActionType, Item, DropdownOption, FormDialogField, InstanceData } from '../../types/Component';

const AppCatalog = () => {
    const {
        appData,
        vimData,
        rowId,
        loading,
        isDialogOpen,
        isFormDialogOpen,
        setRowId,
        handleFileUpload,
        openDialog,
        closeDialog,
        handleDelete,
        openFormDialog,
        closeFormDialog,
        handleInstantiate,
    } = useAppCatalog();

    const fields: FormDialogField[] = [
        {
            id: 'name',
            label: 'Name',
            type: 'text',
            required: true,
        },
        {
            id: 'description',
            label: 'Description',
            type: 'text',
            required: true,
        },
        {
            id: 'vim_id',
            label: 'VIM',
            type: 'select',
            options: vimData.map((vim_id) => vim_id.name),
            required: true,
        },
    ];

    const columns: GridColDef[] = [
        { field: 'info-name', headerName: 'Name', width: 500 },
        { field: 'description', headerName: 'Description', flex: 1, },
        { field: 'provider', headerName: 'Provider', width: 100 },
        { field: 'version', headerName: 'Version', width: 100 },
        {
            field: 'actions',
            headerName: '',
            width: 150,
            sortable: false,
            align: 'center',
            renderCell: (params) => (
                <DropdownButton
                    title='Actions'
                    options={
                        [
                            {
                                label: 'Instantiate',
                                handleClick: () => {
                                    setRowId(params.row.id);
                                    openFormDialog();
                                }
                            },
                            {
                                label: 'Delete',
                                handleClick: () => openDialog(params.row.id),
                            },
                        ] as DropdownOption[]
                    }
                />
            ),
        },
    ];

    return (
        <>
            <Box display="flex" justifyContent="space-between" alignItems="center" mb='20px'>
                <Typography fontWeight='400' variant="h4">
                    App Catalog
                </Typography>

                <Button
                    component='label'
                    role='undefined'
                    variant='contained'
                    color='primary'
                    tabIndex={-1}
                    startIcon={<AddCircleIcon />}
                    disableRipple
                >
                    Create new app
                    <input type="file" accept='.zip,.gz' hidden onChange={(e) => {
                        const file = e.target.files?.[0];
                        if (file) handleFileUpload(file);
                    }} />
                </Button>
            </Box>
            <Box>
                {loading ? (
                    <>
                        <Skeleton variant="rectangular" height='50px' width="100%" animation="pulse" />
                        <p></p>
                        <Skeleton variant="rectangular" height='50px' width="100%" animation="pulse" />
                        <p></p>
                        <Skeleton variant="rectangular" height='50px' width="100%" animation="pulse" />
                    </>
                ) : (
                    <DataGrid
                        getRowId={(row) => row.id}
                        rows={appData}
                        columns={columns}
                        initialState={{
                            pagination: {
                                paginationModel: {
                                    pageSize: 10,
                                },
                            },
                        }}
                        pageSizeOptions={[5, 10, 20, 50, 100]}
                        disableRowSelectionOnClick
                        sx={{ display: 'grid' }}
                    />
                )}
            </Box>
            <ConfirmationDialog
                item={Item.APP}
                action={ActionType.DELETE}
                onConfirm={handleDelete}
                onClose={closeDialog}
                open={isDialogOpen}
            />
            <FormDialog
                open={isFormDialogOpen}
                onClose={closeFormDialog}
                onSubmit={(formData) => handleInstantiate(rowId, formData)}
                title='Create New Instance'
                fields={fields}
            />
            <ToastContainer />
        </>
    );
};

export default AppCatalog;