import { useEffect, useState } from "react";

import Box from "@mui/material/Box";
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import Typography from "@mui/material/Typography";
import Skeleton from "@mui/material/Skeleton";
import { getAppI } from "../../api/appI";
import toast from "../../utils/toast";

const columns: GridColDef[] = [
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

type InstanceData = {
    id: string;
    'vnfd-ref': string;
    'member-vnf-index-ref': string;
    'nsr-id-ref': string;
    'created-time': Date;
}

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
                        //getRowId={(row) => row._id}
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