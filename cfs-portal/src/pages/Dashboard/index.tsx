import { useState, useEffect } from 'react';

import Box from '@mui/material/Box';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { Card, CardActionArea, CardContent, CardHeader, Grid, Typography } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { getAppPkg, getAppI } from '../../api/api';
import { AppData, InstanceData } from '../../types/Component';
import toast from '../../utils/toast';
import InstanceGrid from '../../components/InstanceGrid';

const appColumns: GridColDef[] = [
    { field: 'info-name', headerName: 'Name', flex: 1 },
    { field: 'provider', headerName: 'Provider', flex: 1 },
    { field: 'version', headerName: 'Version', flex: 1 },
];

const Dashboard = () => {
    const navigate = useNavigate();
    const navigateToAppCatalog = () => { navigate('/app-catalog'); }
    const navigateToMecInstances = () => { navigate('/mec-instances'); }

    const [appData, setAppData] = useState<AppData[]>([]);
    const [instanceData, setInstanceData] = useState<InstanceData[]>([]);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        getAppData()
        getInstanceData()
    }, []);

    const getAppData = async () => {
        try {
            const { data } = await getAppPkg();
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
            const { data } = await getAppI();
            setInstanceData(data);
        } catch (error) {
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
                                            "& .MuiDataGrid-columnHeader:focus, .MuiDataGrid-cell:focus": {
                                                outline: 'none',
                                            },
                                            "&.MuiDataGrid-root .MuiDataGrid-cell:focus-within": {
                                                outline: "none !important",
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
                                    <InstanceGrid minimalConfig />
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