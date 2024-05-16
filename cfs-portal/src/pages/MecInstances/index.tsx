import { useEffect, useState } from "react";

import Box from "@mui/material/Box";
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import Typography from "@mui/material/Typography";
import Skeleton from "@mui/material/Skeleton";
import DropdownButton from "../../components/DropdownButton";
import { getAppI, terminateAppI } from "../../api/appI";
import { DropdownOption, InstanceData } from "../../types/Component";
import toast from "../../utils/toast";

const columns: GridColDef[] = [
    { field: 'name', headerName: 'Name', width: 300 },
    { field: 'description', headerName: 'Description', flex: 1 },
    { field: 'details', headerName: 'Details', flex: 1 },
    {
        field: 'created-at',
        headerName: 'Created At',
        width: 200,
        type: 'date',
        valueFormatter: ({ value }) => (value as Date).toLocaleString()
    },
    { field: 'operational-status', headerName: 'Operational Status', width: 100 },
    { field: 'config-status', headerName: 'Config Status', width: 100 },
    {
        field: 'actions',
        headerName: '',
        width: 150,
        sortable: false,
        renderCell: (params) => (
            <DropdownButton
                title='Actions'
                options={
                    [
                        {
                            label: 'Terminate',
                            handleClick: async () => {
                                try {
                                    await terminateAppI(params.row.id);
                                    toast.success('Instance termination initiated successfully');
                                } catch (error) {
                                    toast.error('Error terminating instance');
                                }
                            },
                        },
                    ] as DropdownOption[]
                }
            />
        ),
    },
];

const MecInstances = () => {
    const [instanceData, setInstanceData] = useState<InstanceData[]>([]);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        getInstanceData();
    }, []);

    const getInstanceData = async () => {
        try {
            const data = await getAppI();
            const formattedData = data.map((d: any) => ({
                ...d,
                'created-at': new Date(d['created-at'] * 1000)
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
                    MEC Instances
                </Typography>
            </Box>
            <Box>
                {loading ? (
                    <>
                        <Skeleton variant="rectangular" height='50px' width="100%" animation="wave" />
                        <p></p>
                        <Skeleton variant="rectangular" height='50px' width="100%" animation="wave" />
                        <p></p>
                        <Skeleton variant="rectangular" height='50px' width="100%" animation="wave" />
                    </>
                ) : (
                    <DataGrid
                        getRowId={(row) => row.id}
                        rows={instanceData}
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
        </>
    );
};

export default MecInstances;