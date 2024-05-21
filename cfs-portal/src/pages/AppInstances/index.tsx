import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import InstanceGrid from "../../components/InstanceGrid";

const AppInstances = () => {
    return (
        <>
            <Box display="flex" justifyContent="space-between" alignItems="center" mb='20px'>
                <Typography fontWeight='400' variant="h4">
                    App Instances
                </Typography>
            </Box>
            <Box>
                <InstanceGrid />
            </Box>
        </>
    );
};

export default AppInstances;