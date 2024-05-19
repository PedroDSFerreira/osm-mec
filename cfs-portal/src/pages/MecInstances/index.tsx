import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import InstanceGrid from "../../components/InstanceGrid";

const MecInstances = () => {
    return (
        <>
            <Box display="flex" justifyContent="space-between" alignItems="center" mb='20px'>
                <Typography fontWeight='400' variant="h4">
                    MEC Instances
                </Typography>
            </Box>
            <Box>
                <InstanceGrid />
            </Box>
        </>
    );
};

export default MecInstances;