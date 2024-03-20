import { ChangeEvent, useEffect, useState } from 'react';

import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { Button, Typography } from '@mui/material';
import { Skeleton } from '@mui/material';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import { getAppPkg, newAppPkg } from '../../api/appPkg';

import toast from '../../utils/toast';
import { ToastContainer } from 'react-toastify';

const columns: GridColDef[] = [
    { field: 'product-name', headerName: 'Name', flex: 1 },
    { field: '_id', headerName: 'ID', flex: 1 },
    { field: 'provider', headerName: 'Provider', flex: 1 },
    { field: 'version', headerName: 'Version', flex: 1 },
];

type AppData = {
    _id: string;
    'product-name': string;
    provider: string;
    version: number;
}

const AppCatalog = () => {
    const [appData, setAppData] = useState<AppData[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getAppData();
    }, []);

    const getAppData = async () => {
        try {
            const data = await getAppPkg();
            setAppData(data);
        } catch (error) {
            setAppData([]);
            toast.error('Error fetching app data');
        } finally {
            setLoading(false);
        }
    };

    const handleFileUpload = (e: ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (!file) {
            toast.error('No file selected');
            return;
        } else {
            const formData = new FormData();
            formData.append('file', file);
            try {
                newAppPkg(formData);
                toast.success('New app created successfully');
            } catch (error) {
                toast.error('Error creating new app');
            }
        }
    }

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
                        //getRowId={(row) => row._id}
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
            <ToastContainer />
        </>
    );
}

export default AppCatalog;