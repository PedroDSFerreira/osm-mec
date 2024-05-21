import { useEffect, useState } from "react";

import Box from "@mui/material/Box";
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import Typography from "@mui/material/Typography";
import Skeleton from "@mui/material/Skeleton";
import DropdownButton from "../../components/DropdownButton";
import DetailsDialog from "../Dialog/DetailsDialog";
import ConfirmationDialog from "../Dialog/ConfirmationDialog";
import { IconButton, Tooltip, LinearProgress } from "@mui/material";
import { getAppI, terminateAppI } from "../../api/api";
import { DropdownOption, InstanceData, OperationalStatus, ConfigStatus, ActionType, Item, InstanceGridProps, Metrics } from "../../types/Component";

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

const InstanceGrid = ({ minimalConfig = false, instanceCount }: InstanceGridProps) => {
    const [instanceData, setInstanceData] = useState<InstanceData[]>([]);
    const [loading, setLoading] = useState(true);
    const [detailsDialogOpen, setDetailsDialogOpen] = useState(false);
    const [detailsData, setDetailsData] = useState('');
    const [confirmationDialogOpen, setConfirmationDialogOpen] = useState(false);
    const [id, setId] = useState('');
    const [socket, setSocket] = useState<WebSocket | null>(null);
    const [metrics, setMetrics] = useState<Metrics | null>(null);

    useEffect(() => {
        getInstanceData();
        const interval = setInterval(() => {
            getInstanceData();
        }
            , 5000);
        return () => clearInterval(interval);
    }, []);

    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8001');
        setSocket(ws);
    }, []);

    useEffect(() => {
        if (socket) {
            socket.onopen = () => {
                console.log('Connected to WebSocket');
            };
            socket.onmessage = (event) => {
                const data = JSON.parse(event.data);
                setMetrics((prevMetrics) => {
                    if (prevMetrics && data.appi_id in prevMetrics) {
                        return {
                            ...prevMetrics,
                            [data.appi_id]: {
                                ...prevMetrics[data.appi_id],
                                memLoad: data.mem_load,
                                cpuLoad: data.cpu_load
                            }
                        };
                    } else {
                        return {
                            ...prevMetrics,
                            [data.appi_id]: {
                                memLoad: data.mem_load,
                                cpuLoad: data.cpu_load
                            }
                        };
                    }
                });
            };
            socket.onclose = () => {
                console.log('Disconnected from WebSocket');
            };
        }
    }, [socket]);

    const getLoadColor = (load: number) => {
        if (load < 40) {
            return 'success';
        } else if (load < 75) {
            return 'warning';
        } else {
            return 'error';
        }
    }

    const columns: GridColDef[] = [
        { field: 'name', headerName: 'Name', width: 300 },
        ...minimalConfig ? [] : [{ field: 'description', headerName: 'Description', flex: 1 }],
        ...minimalConfig ? [] : [{
            field: 'details',
            headerName: 'Details',
            flex: 1,
            renderCell: (params: any) => (
                <Box display='flex' justifyContent='space-between' alignItems='center' width='100%'>
                    <Typography
                        variant='body2'
                        overflow='hidden'
                        textOverflow='ellipsis'
                        whiteSpace='nowrap'
                        flex='1'
                    >
                        {params.row.details}
                    </Typography>
                    <IconButton onClick={() => {
                        setDetailsDialogOpen(true);
                        setDetailsData(params.row.details);
                    }}>
                        <MoreHorizIcon />
                    </IconButton>
                </Box >
            )
        }],
        {
            field: 'mem-load',
            headerName: 'Mem (%)',
            width: 70,
            type: 'number',
            renderCell: (params: any) => {
                const memLoad = metrics && metrics[params.row.id as string]?.memLoad;

                return (
                    <Box sx={{ position: 'relative', width: '100%' }}>
                        {memLoad != undefined ? (
                            <>
                                <LinearProgress
                                    variant="determinate"
                                    value={memLoad}
                                    sx={{ width: '100%', height: '30px' }}
                                    color={getLoadColor(memLoad)}
                                />
                                <Typography
                                    variant="body2"
                                    fontWeight='bold'
                                    sx={{
                                        position: 'absolute',
                                        top: 0,
                                        left: '50%',
                                        transform: 'translateX(-50%)',
                                        width: '100%',
                                        textAlign: 'center',
                                        lineHeight: '30px'
                                    }}
                                >
                                    {memLoad}
                                </Typography>
                            </>) : (
                            <Typography variant="body2" textAlign='center'>
                                -
                            </Typography>
                        )}
                    </Box>
                )
            }
        },
        {
            field: 'cpu-load',
            headerName: 'CPU (%)',
            width: 70,
            type: 'number',
            renderCell: (params: any) => {
                const cpuLoad = metrics && metrics[params.row.id as string]?.cpuLoad;

                return (
                    <Box sx={{ position: 'relative', width: '100%' }}>
                        {cpuLoad != undefined ? (
                            <>
                                <LinearProgress
                                    variant="determinate"
                                    value={cpuLoad}
                                    sx={{ width: '100%', height: '30px' }}
                                    color={getLoadColor(cpuLoad)}
                                />
                                <Typography
                                    variant="body2"
                                    fontWeight='bold'
                                    sx={{
                                        position: 'absolute',
                                        top: 0,
                                        left: '50%',
                                        transform: 'translateX(-50%)',
                                        width: '100%',
                                        textAlign: 'center',
                                        lineHeight: '30px'
                                    }}
                                >
                                    {cpuLoad}
                                </Typography>
                            </>) : (
                            <Typography variant="body2" textAlign='center'>
                                -
                            </Typography>
                        )}
                    </Box>
                )
            }
        },
        ...minimalConfig ? [] : [{
            field: 'created-at',
            headerName: 'Created At',
            width: 90,
            type: 'date',
            renderCell: (params: any) => (
                <Tooltip title={params.row['created-at'].toLocaleString()}>
                    <Typography variant="body2">
                        {params.row['created-at'].toLocaleDateString()}
                    </Typography>
                </Tooltip>
            )
        }],
        {
            field: 'operational-status',
            headerName: 'Operational Status',
            width: minimalConfig ? undefined : 100,
            headerAlign: 'center',
            flex: minimalConfig ? 1 : undefined,
            align: 'center',
            renderCell: (params) => renderOperationalStatus(params.row['operational-status'] as OperationalStatus)
        },
        ...minimalConfig ? [] : [{
            field: 'config-status',
            headerName: 'Config Status',
            width: 100,
            renderCell: (params: any) => renderConfigStatus(params.row['config-status'] as ConfigStatus)
        }],
        ...minimalConfig ? [] : [{
            field: 'actions',
            headerName: '',
            width: 150,
            sortable: false,
            renderCell: (params: any) => (
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
        }],
    ];

    const getInstanceData = async () => {
        try {
            const { data } = await getAppI();
            const formattedData = data.map((d: any) => ({
                ...d,
                'created-at': new Date(d['created-at'] * 1000)
            }));
            setInstanceData(formattedData);
            if (instanceCount)
                instanceCount(data.length);
        } catch (error) {
            setInstanceData([]);
            toast.error('Error fetching instance data');
            if (instanceCount)
                instanceCount(0);
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <DataGrid
                hideFooter={minimalConfig}
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

export default InstanceGrid;