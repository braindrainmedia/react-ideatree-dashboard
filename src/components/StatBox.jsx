import { Box, Button, Typography, useTheme } from "@mui/material";
import { tokens } from "../theme";
import ProgressCircle from "./ProgressCircle";
import Divider from '@mui/material/Divider';
import TextField from '@mui/material/TextField';
import CachedIcon from '@mui/icons-material/Cached';
import DownloadIcon from '@mui/icons-material/Download';
import AddCircleIcon from '@mui/icons-material/AddCircle';
import IosShareIcon from '@mui/icons-material/IosShare';
import AssistantIcon from '@mui/icons-material/Assistant';
import AutoAwesomeIcon from '@mui/icons-material/AutoAwesome';

const StatBox = ({ title, subtitle, icon, progress, increase }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <Box width="100%" m="30px 30px">
      <Box display="flex" justifyContent="space-between">
        <Box>
          {icon}
          <Typography
            variant="h2"
            fontWeight="bold"
            sx={{ color: colors.grey[100] }}
          >
            Idea:
          </Typography>
        </Box>
        
      </Box>
      <Box display="flex" justifyContent="space-between" mt="2px">
        <Typography variant="h5" sx={{ color: colors.greenAccent[500] }}>
          LyricMate
        </Typography>
        
        
      </Box>
      
      <Divider light sx={{ mb: '15px', mt: '10px' }}/>

      <TextField multiline rows={6} variant="filled" color="secondary" fullWidth label="Type your idea here..." id="UserIdea" />
      
      <Button variant="contained" color="secondary" fullWidth sx={{ mt: '0px', borderRadius: '0px'} }>
        Generate Docs
      </Button>

      <Divider light sx={{ mt: '20px' }}/>

      <Box display="flex" justifyContent="space-between" mt="20px">
        <Typography variant="h6" sx={{ color: colors.grey[200] }}>
        LyricMate is an AI-powered songwriting assistant that uses GPT to provide musicians and songwriters with intelligent suggestions for lyrics, chord progressions, melodies and song structures, enabling them to save time and spark creativity in their songwriting process.

        </Typography>
        
      </Box>
    </Box>
  );
};

export default StatBox;
