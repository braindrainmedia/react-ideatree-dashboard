import { Box, Button, IconButton, Typography, useTheme } from "@mui/material";
import { tokens } from "../../theme";
import { mockTransactions } from "../../data/mockData";
import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import EmailIcon from "@mui/icons-material/Email";
import PointOfSaleIcon from "@mui/icons-material/PointOfSale";
import PersonAddIcon from "@mui/icons-material/PersonAdd";
import TrafficIcon from "@mui/icons-material/Traffic";
import TipsAndUpdatesIcon from '@mui/icons-material/TipsAndUpdates';
import CachedIcon from '@mui/icons-material/Cached';
import DownloadIcon from '@mui/icons-material/Download';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import IosShareIcon from '@mui/icons-material/IosShare';
import AssistantIcon from '@mui/icons-material/Assistant';
import Header from "../../components/Header";
import LineChart from "../../components/LineChart";
import GeographyChart from "../../components/GeographyChart";
import BarChart from "../../components/BarChart";
import StatBox from "../../components/StatBox";
import DocBox from "../../components/DocBox";
import ProgressCircle from "../../components/ProgressCircle";

const Dashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <Box m="20px">
      {/* HEADER */}
      <Box display="flex" justifyContent="space-between" alignItems="center">
        <Header title="IdeaMap" subtitle="My Ideas" />

        
      </Box>

      {/* GRID & CHARTS */}
      <Box
        display="grid"
        gridTemplateColumns="repeat(12, 1fr)"
        gridAutoRows="140px"
        gap="20px"
      >
        {/* ROW 1 */}
        <Box
          gridColumn="span 3"
          backgroundColor={colors.primary[400]}
          display="flex"
          minWidth="300px"
          height="fit-content"
          alignItems="left"
          justifyContent="center"
          borderRadius= '3px'
          sx={{ border: 1, borderColor: colors.primary[600], borderWidth: '3px', boxShadow: 3, borderRadius: "6px" }}
          
        >
          <StatBox
            ideaName="LyricMate"
            subtitle="Emails Sent"
            progress="0.75"
            increase="+14%"
            icon={
              <TipsAndUpdatesIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>

        {/* ROW 2 */}
        <Box
          gridColumn="span 3"
          backgroundColor={colors.primary[400]}
          display="flex"
          minWidth="700px"
          height="fit-content"
          alignItems="left"
          justifyContent="center"
          borderRadius= '3px'
          sx={{ border: 1, borderColor: colors.primary[600], borderWidth: '3px', boxShadow: 3, borderRadius: "6px" }}
        >
          <DocBox
            title="12,361"
            subtitle="Emails Sent"
            progress="0.75"
            increase="+14%"
            icon={
              <AssistantIcon
                sx={{ color: colors.blueAccent[600], fontSize: "26px" }}
              />
            }
          />
            
          

        </Box>
        
             

      </Box>
    </Box>
  );
};

export default Dashboard;
