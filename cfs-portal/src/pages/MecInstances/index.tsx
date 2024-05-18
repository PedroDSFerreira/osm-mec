import { useEffect, useState } from "react";

import Box from "@mui/material/Box";
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import Typography from "@mui/material/Typography";
import Skeleton from "@mui/material/Skeleton";
import DropdownButton from "../../components/DropdownButton";
import DetailsDialog from "../../components/DetailsDialog";
import ConfirmationDialog from "../../components/ConfirmationDialog";
import { IconButton } from "@mui/material";
import { getAppI, terminateAppI } from "../../api/appI";
import { DropdownOption, InstanceData, OperationalStatus, ConfigStatus, ActionType, Item } from "../../types/Component";

import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import CancelIcon from '@mui/icons-material/Cancel';
import AccessTimeFilledIcon from '@mui/icons-material/AccessTimeFilled';
import StopCircleIcon from '@mui/icons-material/StopCircle';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';

import toast from "../../utils/toast";

const renderOperationalStatus = (status: OperationalStatus) => {
    switch (status) {
        case OperationalStatus.INIT:
            return <AccessTimeFilledIcon color='warning' />
        case OperationalStatus.RUNNING:
            return <CheckCircleIcon color='success' />
        case OperationalStatus.FAILED:
            return <CancelIcon color='error' />
        default:
            return <StopCircleIcon sx={{ color: '#aaa' }} />;
    }
}

const renderConfigStatus = (status: ConfigStatus) => {
    switch (status) {
        case ConfigStatus.INIT:
            return <AccessTimeFilledIcon color='warning' />
        case ConfigStatus.CONFIGURED:
            return <CheckCircleIcon color='success' />
        case ConfigStatus.FAILED:
            return <CancelIcon color='error' />
        default:
            return <StopCircleIcon sx={{ color: '#aaa' }} />;
    }
}

const terminateInstance = async (id: string) => {
    try {
        await terminateAppI(id);
        toast.success('Instance terminated successfully');
    } catch (error) {
        toast.error('Error terminating instance');
    }
}

const MecInstances = () => {
    const [instanceData, setInstanceData] = useState<InstanceData[]>([]);
    const [loading, setLoading] = useState(true);
    const [detailsDialogOpen, setDetailsDialogOpen] = useState(false);
    const [detailsData, setDetailsData] = useState('');
    const [confirmationDialogOpen, setConfirmationDialogOpen] = useState(false);
    const [id, setId] = useState('');
    useEffect(() => {
        getInstanceData();
        const interval = setInterval(() => {
            getInstanceData();
        }
            , 5000);
        return () => clearInterval(interval);
    }, []);

    const columns: GridColDef[] = [
        { field: 'name', headerName: 'Name', width: 300 },
        { field: 'description', headerName: 'Description', flex: 1 },
        {
            field: 'details',
            headerName: 'Details',
            flex: 1,
            renderCell: (params) => (
                <>
                    <Box display='flex'>
                        <IconButton onClick={() => {
                            setDetailsDialogOpen(true);
                            setDetailsData(params.row.details);
                        }}>
                            <MoreHorizIcon />
                        </IconButton>
                    </Box>
                    <Box display='flex'>
                        <Typography variant='body2'>
                            {params.row.details}
                        </Typography>
                    </Box>
                </>
            )
        },
        {
            field: 'created-at',
            headerName: 'Created At',
            width: 200,
            type: 'date',
            valueFormatter: ({ value }) => (value as Date).toLocaleString()
        },
        {
            field: 'operational-status',
            headerName: 'Operational Status',
            width: 100,
            align: 'center',
            renderCell: (params) => renderOperationalStatus(params.row['operational-status'] as OperationalStatus)
        },
        {
            field: 'config-status',
            headerName: 'Config Status',
            width: 100,
            align: 'center',
            renderCell: (params) => renderConfigStatus(params.row['config-status'] as ConfigStatus)
        },
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
                                handleClick: () => {
                                    setConfirmationDialogOpen(true);
                                    setId(params.row.id as string);
                                }
                            },
                        ] as DropdownOption[]
                    }
                />
            ),
        },
    ];

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
                        sx={{
                            "&.MuiDataGrid-root .MuiDataGrid-cell:focus-within": {
                                outline: "none !important",
                            },
                            display: 'grid'
                        }}
                    />
                )}
            </Box>
            <DetailsDialog
                open={detailsDialogOpen}
                onClose={() => setDetailsDialogOpen(false)}
                title='Instance Details'
                data={detailsData}
            />
            <ConfirmationDialog
                open={confirmationDialogOpen}
                onClose={() => setConfirmationDialogOpen(false)}
                onConfirm={() => {
                    terminateInstance(id);
                    setConfirmationDialogOpen(false);
                }}
                action={ActionType.TERMINATE}
                item={Item.INSTANCE}
            />
        </>
    );
};

export default MecInstances;