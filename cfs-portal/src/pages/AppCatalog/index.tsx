import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { Button, Typography } from '@mui/material';
import { Skeleton } from '@mui/material';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import { ToastContainer } from 'react-toastify';
import ConfirmationDialog from '../../components/ConfirmationDialog';
import { useAppCatalog } from '../../hooks/useAppCatalog';

const AppCatalog = () => {
    const {
        appData,
        loading,
        isDialogOpen,
        handleFileUpload,
        openDialog,
        closeDialog,
        handleDelete,
    } = useAppCatalog();

    const columns: GridColDef[] = [
        { field: 'product-name', headerName: 'Name', flex: 1 },
        { field: '_id', headerName: 'ID', flex: 1 },
        { field: 'provider', headerName: 'Provider', flex: 1 },
        { field: 'version', headerName: 'Version', flex: 1 },
        {
            field: 'actions',
            headerName: 'Actions',
            flex: 1,
            sortable: false,
            renderCell: (params) => (
                <Button
                    variant='contained'
                    color='primary'
                    size='small'
                    onClick={() => openDialog(params.row._id as string)}
                >
                    Delete
                </Button>
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
                    <input type="file" accept='.zip,.gz' hidden onChange={handleFileUpload} />
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
                        getRowId={(row) => row._id}
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
                title='Delete App'
                content='Are you sure you want to delete this app?'
                onConfirm={handleDelete}
                onClose={closeDialog}
                open={isDialogOpen}
            />
            <ToastContainer />
        </>
    );
};

export default AppCatalog;