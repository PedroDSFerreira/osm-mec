import { useState, useEffect } from 'react';

import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { Card, CardActionArea, CardContent, CardHeader, Grid, Typography } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { getAppPkg } from '../../api/appPkg';
import { getAppI } from '../../api/appI';
import toast from '../../utils/toast';

const appColumns: GridColDef[] = [
    { field: 'product-name', headerName: 'Name', flex: 1 },
    { field: '_id', headerName: 'ID', flex: 1 },
    { field: 'provider', headerName: 'Provider', flex: 1 },
    { field: 'version', headerName: 'Version', flex: 1 },
];

const instanceColumns: GridColDef[] = [
    { field: 'id', headerName: 'ID', flex: 1 },
    { field: 'vnfd-ref', headerName: 'VNFD', flex: 1 },
    { field: 'member-vnf-index-ref', headerName: 'Member Index', flex: 1 },
    { field: 'nsr-id-ref', headerName: 'NS', flex: 1 },
    {
        field: 'created-time',
        headerName: 'Created At',
        flex: 1,
        type: 'date',
        valueFormatter: ({ value }) => (value as Date).toLocaleString()
    },
];

type AppData = {
    _id: string;
    'product-name': string;
    provider: string;
    version: number;
}

type InstanceData = {
    id: string;
    'vnfd-ref': string;
    'member-vnf-index-ref': string;
    'nsr-id-ref': string;
    'created-time': Date;
}

const Dashboard = () => {
    const navigate = useNavigate();
    const navigateToAppCatalog = () => { navigate('/app-catalog'); }
    const navigateToMecInstances = () => { navigate('/mec-instances'); }

    const [appData, setAppData] = useState<AppData[]>([]);
    const [instanceData, setInstanceData] = useState<InstanceData[]>([]);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        getAppData();
        getInstanceData();
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

    const getInstanceData = async () => {
        try {
            const data = await getAppI();
            const formattedData = data.map((d: any) => ({
                ...d,
                'created-time': new Date(d['created-time'] * 1000)
            }));
            setInstanceData(formattedData);
        } catch (error) {
            setInstanceData([]);
            toast.error('Error fetching instance data');
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <Box display="flex" justifyContent="space-between" alignItems="center" mb='20px'>
                <Typography fontWeight='400' variant="h4">
                    Dashboard
                </Typography>
            </Box>
            <Box>
                <Grid container spacing={2}>
                    <Grid item xs={6}>
                        <Card sx={{ borderRadius: '6px', boxShadow: '6' }}>
                            <CardActionArea onClick={navigateToAppCatalog} >
                                <CardHeader
                                    title={
                                        <Box display="flex" justifyContent="space-between" alignItems="center">
                                            <Typography variant="h5">
                                                App Catalog
                                            </Typography>
                                            <Typography variant="h5" sx={{ marginLeft: 'auto' }}>
                                                {`${appData.length}`}
                                            </Typography>
                                        </Box>
                                    }
                                />
                                <CardContent>
                                    <DataGrid
                                        rows={appData}
                                        columns={appColumns}
                                        disableRowSelectionOnClick
                                        disableColumnMenu
                                        hideFooter
                                        sx={{
                                            '& .MuiDataGrid-columnHeader:focus, .MuiDataGrid-cell:focus': {
                                                outline: 'none',
                                            },
                                        }}
                                    />
                                </CardContent>
                            </CardActionArea>
                        </Card>
                    </Grid>
                    <Grid item xs={6}>
                        <Card sx={{ borderRadius: '6px', boxShadow: '6' }}>
                            <CardActionArea onClick={navigateToMecInstances}>
                                <CardHeader
                                    title={
                                        <Box display="flex" justifyContent="space-between" alignItems="center">
                                            <Typography variant="h5">
                                                MEC Instances
                                            </Typography>
                                            <Typography variant="h5" sx={{ marginLeft: 'auto' }}>
                                                {`${instanceData.length}`}
                                            </Typography>
                                        </Box>
                                    }
                                />
                                <CardContent>
                                    <DataGrid
                                        rows={instanceData}
                                        columns={instanceColumns}
                                        disableRowSelectionOnClick
                                        disableColumnMenu
                                        hideFooter
                                        sx={{
                                            '& .MuiDataGrid-columnHeader:focus, .MuiDataGrid-cell:focus': {
                                                outline: 'none',
                                            },
                                        }}
                                    />
                                </CardContent>
                            </CardActionArea>
                        </Card>
                    </Grid>
                </Grid>
            </Box >
        </>
    );
}

export default Dashboard;